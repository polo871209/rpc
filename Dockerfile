# syntax=docker/dockerfile:1

FROM cgr.dev/chainguard/wolfi-base:latest AS builder

RUN apk add --no-cache \
      ca-certificates \
      file \
      git \
      go

WORKDIR /app

COPY go.mod go.sum ./
RUN go mod download && go mod verify

COPY cmd/ ./cmd/
COPY internal/ ./internal/
COPY pkg/ ./pkg/

RUN CGO_ENABLED=0 \
    GOOS=linux \
    GOARCH=amd64 \
    go build \
      -a \
      -installsuffix cgo \
      -ldflags='-w -s -extldflags "-static"' \
      -tags netgo \
      -o server \
      ./cmd/server

RUN file server | grep -q "statically linked"

# Runtime stage
FROM cgr.dev/chainguard/wolfi-base:latest

RUN addgroup -S app && adduser -S app -G app
USER app

WORKDIR /app

COPY --from=builder /app/server /usr/local/bin/server

EXPOSE 50051

HEALTHCHECK --interval=30s \
            --timeout=5s \
            --start-period=10s \
            --retries=3 \
            CMD ["/usr/local/bin/server", "--health-check"]

ENTRYPOINT ["/usr/local/bin/server"]
CMD ["--config", "/etc/server/config.yaml"]

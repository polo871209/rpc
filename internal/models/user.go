package models

import (
	"time"

	pb "grpc-server/pkg/pb"
)

// User represents the domain model for a user
type User struct {
	ID        string
	Name      string
	Email     string
	Age       int32
	CreatedAt time.Time
	UpdatedAt time.Time
}

// ToProto converts domain model to protobuf message
func (u *User) ToProto() *pb.User {
	return &pb.User{
		Id:        u.ID,
		Name:      u.Name,
		Email:     u.Email,
		Age:       u.Age,
		CreatedAt: u.CreatedAt.Unix(),
		UpdatedAt: u.UpdatedAt.Unix(),
	}
}

// FromProto creates domain model from protobuf message
func FromProto(pbUser *pb.User) *User {
	return &User{
		ID:        pbUser.Id,
		Name:      pbUser.Name,
		Email:     pbUser.Email,
		Age:       pbUser.Age,
		CreatedAt: time.Unix(pbUser.CreatedAt, 0),
		UpdatedAt: time.Unix(pbUser.UpdatedAt, 0),
	}
}

// NewUser creates a new user with timestamps
func NewUser(id, name, email string, age int32) *User {
	now := time.Now()
	return &User{
		ID:        id,
		Name:      name,
		Email:     email,
		Age:       age,
		CreatedAt: now,
		UpdatedAt: now,
	}
}

// Update updates user fields and timestamp
func (u *User) Update(name, email string, age int32) {
	if name != "" {
		u.Name = name
	}
	if email != "" {
		u.Email = email
	}
	if age > 0 {
		u.Age = age
	}
	u.UpdatedAt = time.Now()
}

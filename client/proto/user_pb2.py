# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: user.proto
# Protobuf Python Version: 6.31.0
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    6,
    31,
    0,
    '',
    'user.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\nuser.proto\x12\x04user\"d\n\x04User\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\r\n\x05\x65mail\x18\x03 \x01(\t\x12\x0b\n\x03\x61ge\x18\x04 \x01(\x05\x12\x12\n\ncreated_at\x18\x05 \x01(\x03\x12\x12\n\nupdated_at\x18\x06 \x01(\x03\"=\n\x11\x43reateUserRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\r\n\x05\x65mail\x18\x02 \x01(\t\x12\x0b\n\x03\x61ge\x18\x03 \x01(\x05\"?\n\x12\x43reateUserResponse\x12\x18\n\x04user\x18\x01 \x01(\x0b\x32\n.user.User\x12\x0f\n\x07message\x18\x02 \x01(\t\"\x1c\n\x0eGetUserRequest\x12\n\n\x02id\x18\x01 \x01(\t\"<\n\x0fGetUserResponse\x12\x18\n\x04user\x18\x01 \x01(\x0b\x32\n.user.User\x12\x0f\n\x07message\x18\x02 \x01(\t\"I\n\x11UpdateUserRequest\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\r\n\x05\x65mail\x18\x03 \x01(\t\x12\x0b\n\x03\x61ge\x18\x04 \x01(\x05\"?\n\x12UpdateUserResponse\x12\x18\n\x04user\x18\x01 \x01(\x0b\x32\n.user.User\x12\x0f\n\x07message\x18\x02 \x01(\t\"\x1f\n\x11\x44\x65leteUserRequest\x12\n\n\x02id\x18\x01 \x01(\t\"%\n\x12\x44\x65leteUserResponse\x12\x0f\n\x07message\x18\x01 \x01(\t\"/\n\x10ListUsersRequest\x12\x0c\n\x04page\x18\x01 \x01(\x05\x12\r\n\x05limit\x18\x02 \x01(\x05\"N\n\x11ListUsersResponse\x12\x19\n\x05users\x18\x01 \x03(\x0b\x32\n.user.User\x12\r\n\x05total\x18\x02 \x01(\x05\x12\x0f\n\x07message\x18\x03 \x01(\t2\xc6\x02\n\x0bUserService\x12?\n\nCreateUser\x12\x17.user.CreateUserRequest\x1a\x18.user.CreateUserResponse\x12\x36\n\x07GetUser\x12\x14.user.GetUserRequest\x1a\x15.user.GetUserResponse\x12?\n\nUpdateUser\x12\x17.user.UpdateUserRequest\x1a\x18.user.UpdateUserResponse\x12?\n\nDeleteUser\x12\x17.user.DeleteUserRequest\x1a\x18.user.DeleteUserResponse\x12<\n\tListUsers\x12\x16.user.ListUsersRequest\x1a\x17.user.ListUsersResponseB\x06Z\x04./pbb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'user_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'Z\004./pb'
  _globals['_USER']._serialized_start=20
  _globals['_USER']._serialized_end=120
  _globals['_CREATEUSERREQUEST']._serialized_start=122
  _globals['_CREATEUSERREQUEST']._serialized_end=183
  _globals['_CREATEUSERRESPONSE']._serialized_start=185
  _globals['_CREATEUSERRESPONSE']._serialized_end=248
  _globals['_GETUSERREQUEST']._serialized_start=250
  _globals['_GETUSERREQUEST']._serialized_end=278
  _globals['_GETUSERRESPONSE']._serialized_start=280
  _globals['_GETUSERRESPONSE']._serialized_end=340
  _globals['_UPDATEUSERREQUEST']._serialized_start=342
  _globals['_UPDATEUSERREQUEST']._serialized_end=415
  _globals['_UPDATEUSERRESPONSE']._serialized_start=417
  _globals['_UPDATEUSERRESPONSE']._serialized_end=480
  _globals['_DELETEUSERREQUEST']._serialized_start=482
  _globals['_DELETEUSERREQUEST']._serialized_end=513
  _globals['_DELETEUSERRESPONSE']._serialized_start=515
  _globals['_DELETEUSERRESPONSE']._serialized_end=552
  _globals['_LISTUSERSREQUEST']._serialized_start=554
  _globals['_LISTUSERSREQUEST']._serialized_end=601
  _globals['_LISTUSERSRESPONSE']._serialized_start=603
  _globals['_LISTUSERSRESPONSE']._serialized_end=681
  _globals['_USERSERVICE']._serialized_start=684
  _globals['_USERSERVICE']._serialized_end=1010
# @@protoc_insertion_point(module_scope)

# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: foo.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\tfoo.proto\"&\n\x07Request\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\r\n\x05state\x18\x02 \x01(\x08\"\x19\n\x08Response\x12\r\n\x05state\x18\x03 \x01(\x08\x32-\n\nFooService\x12\x1f\n\x08SetState\x12\x08.Request\x1a\t.Responseb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'foo_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _globals['_REQUEST']._serialized_start=13
  _globals['_REQUEST']._serialized_end=51
  _globals['_RESPONSE']._serialized_start=53
  _globals['_RESPONSE']._serialized_end=78
  _globals['_FOOSERVICE']._serialized_start=80
  _globals['_FOOSERVICE']._serialized_end=125
# @@protoc_insertion_point(module_scope)

# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: ring.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\nring.proto\x12\x04ring\"B\n\x08keyValue\x12\x10\n\x03key\x18\x01 \x01(\tH\x00\x88\x01\x01\x12\x12\n\x05value\x18\x02 \x01(\tH\x01\x88\x01\x01\x42\x06\n\x04_keyB\x08\n\x06_value\"g\n\x0breturnValue\x12\x14\n\x07updated\x18\x01 \x01(\tH\x00\x88\x01\x01\x12\x10\n\x03key\x18\x02 \x01(\tH\x01\x88\x01\x01\x12\x12\n\x05value\x18\x03 \x01(\tH\x02\x88\x01\x01\x42\n\n\x08_updatedB\x06\n\x04_keyB\x08\n\x06_value\"\x06\n\x04void2\x8f\x01\n\x05\x41lert\x12-\n\x06\x44\x65lete\x12\x0e.ring.keyValue\x1a\x11.ring.returnValue\"\x00\x12*\n\x03\x41\x64\x64\x12\x0e.ring.keyValue\x1a\x11.ring.returnValue\"\x00\x12+\n\x04Read\x12\x0e.ring.keyValue\x1a\x11.ring.returnValue\"\x00\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'ring_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_KEYVALUE']._serialized_start=20
  _globals['_KEYVALUE']._serialized_end=86
  _globals['_RETURNVALUE']._serialized_start=88
  _globals['_RETURNVALUE']._serialized_end=191
  _globals['_VOID']._serialized_start=193
  _globals['_VOID']._serialized_end=199
  _globals['_ALERT']._serialized_start=202
  _globals['_ALERT']._serialized_end=345
# @@protoc_insertion_point(module_scope)

# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: streamlit/proto/Delta.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from streamlit.proto import Block_pb2 as streamlit_dot_proto_dot_Block__pb2
from streamlit.proto import Element_pb2 as streamlit_dot_proto_dot_Element__pb2
from streamlit.proto import NamedDataSet_pb2 as streamlit_dot_proto_dot_NamedDataSet__pb2
from streamlit.proto import ArrowNamedDataSet_pb2 as streamlit_dot_proto_dot_ArrowNamedDataSet__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1bstreamlit/proto/Delta.proto\x1a\x1bstreamlit/proto/Block.proto\x1a\x1dstreamlit/proto/Element.proto\x1a\"streamlit/proto/NamedDataSet.proto\x1a\'streamlit/proto/ArrowNamedDataSet.proto\"\x9e\x01\n\x05\x44\x65lta\x12\x1f\n\x0bnew_element\x18\x03 \x01(\x0b\x32\x08.ElementH\x00\x12\x1b\n\tadd_block\x18\x06 \x01(\x0b\x32\x06.BlockH\x00\x12!\n\x08\x61\x64\x64_rows\x18\x05 \x01(\x0b\x32\r.NamedDataSetH\x00\x12,\n\x0e\x61rrow_add_rows\x18\x07 \x01(\x0b\x32\x12.ArrowNamedDataSetH\x00\x42\x06\n\x04typeB*\n\x1c\x63om.snowflake.apps.streamlitB\nDeltaProtob\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'streamlit.proto.Delta_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  _globals['DESCRIPTOR']._options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\034com.snowflake.apps.streamlitB\nDeltaProto'
  _globals['_DELTA']._serialized_start=169
  _globals['_DELTA']._serialized_end=327
# @@protoc_insertion_point(module_scope)

# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: chat.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import any_pb2 as google_dot_protobuf_dot_any__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='chat.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\nchat.proto\x1a\x19google/protobuf/any.proto\"H\n\x0bMessageText\x12\n\n\x02id\x18\x01 \x01(\t\x12\n\n\x02ts\x18\x02 \x01(\t\x12\x10\n\x08template\x18\x03 \x01(\t\x12\x0f\n\x07\x63ontent\x18\x04 \x01(\t\"N\n\x0cMessageVoice\x12\n\n\x02id\x18\x01 \x01(\t\x12\n\n\x02ts\x18\x02 \x01(\t\x12\x0b\n\x03url\x18\x03 \x01(\t\x12\x0b\n\x03len\x18\x04 \x01(\t\x12\x0c\n\x04name\x18\x05 \x01(\t\"5\n\x0eMessagePicture\x12\n\n\x02id\x18\x01 \x01(\t\x12\n\n\x02ts\x18\x02 \x01(\t\x12\x0b\n\x03url\x18\x03 \x01(\t\"M\n\x0b\x43hatMessage\x12\x1a\n\x04type\x18\x01 \x01(\x0e\x32\x0c.MessageType\x12\"\n\x04\x62ody\x18\x02 \x01(\x0b\x32\x14.google.protobuf.Any\"H\n\x0f\x43hatOne2One_C2S\x12\n\n\x02\x66r\x18\x01 \x01(\t\x12\n\n\x02to\x18\x02 \x01(\t\x12\x1d\n\x07message\x18\x03 \x01(\x0b\x32\x0c.ChatMessage*/\n\x0bMessageType\x12\x08\n\x04TEXT\x10\x00\x12\t\n\x05VOICE\x10\x01\x12\x0b\n\x07PICTURE\x10\x02\x62\x06proto3'
  ,
  dependencies=[google_dot_protobuf_dot_any__pb2.DESCRIPTOR,])

_MESSAGETYPE = _descriptor.EnumDescriptor(
  name='MessageType',
  full_name='MessageType',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='TEXT', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='VOICE', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='PICTURE', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=403,
  serialized_end=450,
)
_sym_db.RegisterEnumDescriptor(_MESSAGETYPE)

MessageType = enum_type_wrapper.EnumTypeWrapper(_MESSAGETYPE)
TEXT = 0
VOICE = 1
PICTURE = 2



_MESSAGETEXT = _descriptor.Descriptor(
  name='MessageText',
  full_name='MessageText',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='MessageText.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='ts', full_name='MessageText.ts', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='template', full_name='MessageText.template', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='content', full_name='MessageText.content', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=41,
  serialized_end=113,
)


_MESSAGEVOICE = _descriptor.Descriptor(
  name='MessageVoice',
  full_name='MessageVoice',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='MessageVoice.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='ts', full_name='MessageVoice.ts', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='url', full_name='MessageVoice.url', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='len', full_name='MessageVoice.len', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='name', full_name='MessageVoice.name', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=115,
  serialized_end=193,
)


_MESSAGEPICTURE = _descriptor.Descriptor(
  name='MessagePicture',
  full_name='MessagePicture',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='MessagePicture.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='ts', full_name='MessagePicture.ts', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='url', full_name='MessagePicture.url', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=195,
  serialized_end=248,
)


_CHATMESSAGE = _descriptor.Descriptor(
  name='ChatMessage',
  full_name='ChatMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='ChatMessage.type', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='body', full_name='ChatMessage.body', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=250,
  serialized_end=327,
)


_CHATONE2ONE_C2S = _descriptor.Descriptor(
  name='ChatOne2One_C2S',
  full_name='ChatOne2One_C2S',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='fr', full_name='ChatOne2One_C2S.fr', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='to', full_name='ChatOne2One_C2S.to', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='message', full_name='ChatOne2One_C2S.message', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=329,
  serialized_end=401,
)

_CHATMESSAGE.fields_by_name['type'].enum_type = _MESSAGETYPE
_CHATMESSAGE.fields_by_name['body'].message_type = google_dot_protobuf_dot_any__pb2._ANY
_CHATONE2ONE_C2S.fields_by_name['message'].message_type = _CHATMESSAGE
DESCRIPTOR.message_types_by_name['MessageText'] = _MESSAGETEXT
DESCRIPTOR.message_types_by_name['MessageVoice'] = _MESSAGEVOICE
DESCRIPTOR.message_types_by_name['MessagePicture'] = _MESSAGEPICTURE
DESCRIPTOR.message_types_by_name['ChatMessage'] = _CHATMESSAGE
DESCRIPTOR.message_types_by_name['ChatOne2One_C2S'] = _CHATONE2ONE_C2S
DESCRIPTOR.enum_types_by_name['MessageType'] = _MESSAGETYPE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

MessageText = _reflection.GeneratedProtocolMessageType('MessageText', (_message.Message,), {
  'DESCRIPTOR' : _MESSAGETEXT,
  '__module__' : 'chat_pb2'
  # @@protoc_insertion_point(class_scope:MessageText)
  })
_sym_db.RegisterMessage(MessageText)

MessageVoice = _reflection.GeneratedProtocolMessageType('MessageVoice', (_message.Message,), {
  'DESCRIPTOR' : _MESSAGEVOICE,
  '__module__' : 'chat_pb2'
  # @@protoc_insertion_point(class_scope:MessageVoice)
  })
_sym_db.RegisterMessage(MessageVoice)

MessagePicture = _reflection.GeneratedProtocolMessageType('MessagePicture', (_message.Message,), {
  'DESCRIPTOR' : _MESSAGEPICTURE,
  '__module__' : 'chat_pb2'
  # @@protoc_insertion_point(class_scope:MessagePicture)
  })
_sym_db.RegisterMessage(MessagePicture)

ChatMessage = _reflection.GeneratedProtocolMessageType('ChatMessage', (_message.Message,), {
  'DESCRIPTOR' : _CHATMESSAGE,
  '__module__' : 'chat_pb2'
  # @@protoc_insertion_point(class_scope:ChatMessage)
  })
_sym_db.RegisterMessage(ChatMessage)

ChatOne2One_C2S = _reflection.GeneratedProtocolMessageType('ChatOne2One_C2S', (_message.Message,), {
  'DESCRIPTOR' : _CHATONE2ONE_C2S,
  '__module__' : 'chat_pb2'
  # @@protoc_insertion_point(class_scope:ChatOne2One_C2S)
  })
_sym_db.RegisterMessage(ChatOne2One_C2S)


# @@protoc_insertion_point(module_scope)

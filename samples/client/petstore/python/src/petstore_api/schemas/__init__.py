# coding: utf-8

"""
    OpenAPI Petstore
    This spec is mainly for testing Petstore server and contains fake endpoints, models. Please do not use this for any other purpose. Special characters: " \  # noqa: E501
    The version of the OpenAPI document: 1.0.0
    Generated by: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator
"""

import typing

import typing_extensions

from .schema import (
    get_class,
    none_type_,
    classproperty,
    Bool,
    FileIO,
    Schema,
    SingletonMeta,
    AnyTypeSchema,
    UnsetAnyTypeSchema,
    INPUT_TYPES_ALL
)

from .schemas import (
    ListSchema,
    NoneSchema,
    NumberSchema,
    IntSchema,
    Int32Schema,
    Int64Schema,
    Float32Schema,
    Float64Schema,
    StrSchema,
    UUIDSchema,
    DateSchema,
    DateTimeSchema,
    DecimalSchema,
    BytesSchema,
    FileSchema,
    BinarySchema,
    BoolSchema,
    NotAnyTypeSchema,
    OUTPUT_BASE_TYPES,
    DictSchema
)
from .validation import (
    PatternInfo,
    ValidationMetadata,
    immutabledict
)
from .format import (
    as_date,
    as_datetime,
    as_decimal,
    as_uuid
)

def typed_dict_to_instance(t_dict: typing_extensions._TypedDictMeta) -> typing.Mapping: # type: ignore
    res = {}
    for key, val in t_dict.__annotations__.items():
        if isinstance(val, typing._GenericAlias): # type: ignore
            # typing.Type[W] -> W
            val_cls = typing.get_args(val)[0]
            res[key] = val_cls
    return res

X = typing.TypeVar('X', bound=typing.Tuple)

def tuple_to_instance(tup: typing.Type[X]) -> X:
    res = []
    for arg in typing.get_args(tup):
        if isinstance(arg, typing._GenericAlias): # type: ignore
            # typing.Type[Schema] -> Schema
            arg_cls = typing.get_args(arg)[0]
            res.append(arg_cls)
    return tuple(res) # type: ignore


class Unset:
    """
    An instance of this class is set as the default value for object type(dict) properties that are optional
    When a property has an unset value, that property will not be assigned in the dict
    """
    pass

unset: Unset = Unset()

def key_unknown_error_msg(key: str) -> str:
    return (f"Invalid key. The key {key} is not a known key in this payload. "
        "If this key is an additional property, use get_additional_property_"
    )

def raise_if_key_known(
    key: str,
    required_keys: typing.FrozenSet[str],
    optional_keys: typing.FrozenSet[str]
):
    if key in required_keys or key in optional_keys:
        raise ValueError(f"The key {key} is a known property, use get_property to access its value")

__all__ = [
    'get_class',
    'none_type_',
    'classproperty',
    'Bool',
    'FileIO',
    'Schema',
    'SingletonMeta',
    'AnyTypeSchema',
    'UnsetAnyTypeSchema',
    'INPUT_TYPES_ALL',
    'ListSchema',
    'NoneSchema',
    'NumberSchema',
    'IntSchema',
    'Int32Schema',
    'Int64Schema',
    'Float32Schema',
    'Float64Schema',
    'StrSchema',
    'UUIDSchema',
    'DateSchema',
    'DateTimeSchema',
    'DecimalSchema',
    'BytesSchema',
    'FileSchema',
    'BinarySchema',
    'BoolSchema',
    'NotAnyTypeSchema',
    'OUTPUT_BASE_TYPES',
    'DictSchema',
    'PatternInfo',
    'ValidationMetadata',
    'immutabledict',
    'as_date',
    'as_datetime',
    'as_decimal',
    'as_uuid',
    'typed_dict_to_instance',
    'tuple_to_instance',
    'Unset',
    'unset',
    'key_unknown_error_msg',
    'raise_if_key_known'
]
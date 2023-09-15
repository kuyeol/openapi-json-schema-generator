# coding: utf-8

"""
    openapi 3.1.0 sample spec
    sample spec for testing openapi functionality, built from json schema tests for draft2020-12  # noqa: E501
    The version of the OpenAPI document: 0.0.1
    Generated by: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator
"""

from __future__ import annotations
from unit_test_api.shared_imports.schema_imports import *  # pyright: ignore [reportWildcardImportFromLibrary]

Proto: typing_extensions.TypeAlias = schemas.NumberSchema
Length: typing_extensions.TypeAlias = schemas.StrSchema
Properties = typing.TypedDict(
    'Properties',
    {
        "length": typing.Type[Length],
    }
)


class ToStringDict(schemas.immutabledict[str, str]):

    __required_keys__: typing.FrozenSet[str] = frozenset({
    })
    __optional_keys__: typing.FrozenSet[str] = frozenset({
        "length",
    })
    
    def __new__(
        cls,
        *,
        length: typing.Union[
            str,
            schemas.Unset
        ] = schemas.unset,
        configuration_: typing.Optional[schema_configuration.SchemaConfiguration] = None,
        **kwargs: schemas.INPUT_TYPES_ALL,
    ):
        arg_: typing.Dict[str, typing.Any] = {}
        for key, val in (
            ("length", length),
        ):
            if isinstance(val, schemas.Unset):
                continue
            arg_[key] = val
        arg_.update(kwargs)
        used_arg_ = typing.cast(ToStringDictInput, arg_)
        return ToString.validate(used_arg_, configuration=configuration_)
    
    @staticmethod
    def from_dict_(
        arg: typing.Union[
            ToStringDictInput,
            ToStringDict
        ],
        configuration: typing.Optional[schema_configuration.SchemaConfiguration] = None
    ) -> ToStringDict:
        return ToString.validate(arg, configuration=configuration)
    
    @property
    def length(self) -> typing.Union[str, schemas.Unset]:
        val = self.get("length", schemas.unset)
        if isinstance(val, schemas.Unset):
            return val
        return typing.cast(
            str,
            val
        )
    
    def get_additional_property_(self, name: str) -> typing.Union[schemas.OUTPUT_BASE_TYPES, schemas.Unset]:
        schemas.raise_if_key_known(name, self.__required_keys__, self.__optional_keys__)
        return self.get(name, schemas.unset)
ToStringDictInput = typing.Mapping[str, schemas.INPUT_TYPES_ALL]


@dataclasses.dataclass(frozen=True)
class ToString(
    schemas.AnyTypeSchema[ToStringDict, typing.Tuple[schemas.OUTPUT_BASE_TYPES, ...]],
):
    # any type
    properties: Properties = dataclasses.field(default_factory=lambda: schemas.typed_dict_to_instance(Properties)) # type: ignore
    type_to_output_cls: typing.Mapping[
        typing.Type,
        typing.Type
    ] = dataclasses.field(
        default_factory=lambda: {
            schemas.immutabledict: ToStringDict,
        }
    )

Constructor: typing_extensions.TypeAlias = schemas.NumberSchema
Properties2 = typing.TypedDict(
    'Properties2',
    {
        "__proto__": typing.Type[Proto],
        "toString": typing.Type[ToString],
        "constructor": typing.Type[Constructor],
    }
)


class PropertiesWhoseNamesAreJavascriptObjectPropertyNamesDict(schemas.immutabledict[str, typing.Union[int, float]]):

    __required_keys__: typing.FrozenSet[str] = frozenset({
    })
    __optional_keys__: typing.FrozenSet[str] = frozenset({
        "__proto__",
        "toString",
        "constructor",
    })
    
    def __new__(
        cls,
        *,
        __proto__: typing.Union[
            int,
            float,
            schemas.Unset
        ] = schemas.unset,
        toString: typing.Union[
            schemas.INPUT_TYPES_ALL,
            schemas.OUTPUT_BASE_TYPES,
            schemas.Unset
        ] = schemas.unset,
        constructor: typing.Union[
            int,
            float,
            schemas.Unset
        ] = schemas.unset,
        configuration_: typing.Optional[schema_configuration.SchemaConfiguration] = None,
        **kwargs: schemas.INPUT_TYPES_ALL,
    ):
        arg_: typing.Dict[str, typing.Any] = {}
        for key, val in (
            ("__proto__", __proto__),
            ("toString", toString),
            ("constructor", constructor),
        ):
            if isinstance(val, schemas.Unset):
                continue
            arg_[key] = val
        arg_.update(kwargs)
        used_arg_ = typing.cast(PropertiesWhoseNamesAreJavascriptObjectPropertyNamesDictInput, arg_)
        return PropertiesWhoseNamesAreJavascriptObjectPropertyNames.validate(used_arg_, configuration=configuration_)
    
    @staticmethod
    def from_dict_(
        arg: typing.Union[
            PropertiesWhoseNamesAreJavascriptObjectPropertyNamesDictInput,
            PropertiesWhoseNamesAreJavascriptObjectPropertyNamesDict
        ],
        configuration: typing.Optional[schema_configuration.SchemaConfiguration] = None
    ) -> PropertiesWhoseNamesAreJavascriptObjectPropertyNamesDict:
        return PropertiesWhoseNamesAreJavascriptObjectPropertyNames.validate(arg, configuration=configuration)
    
    @property
    def __proto__(self) -> typing.Union[int, float, schemas.Unset]:
        val = self.get("__proto__", schemas.unset)
        if isinstance(val, schemas.Unset):
            return val
        return typing.cast(
            typing.Union[int, float],
            val
        )
    
    @property
    def toString(self) -> typing.Union[schemas.OUTPUT_BASE_TYPES, schemas.Unset]:
        val = self.get("toString", schemas.unset)
        if isinstance(val, schemas.Unset):
            return val
        return typing.cast(
            schemas.OUTPUT_BASE_TYPES,
            val
        )
    
    @property
    def constructor(self) -> typing.Union[int, float, schemas.Unset]:
        val = self.get("constructor", schemas.unset)
        if isinstance(val, schemas.Unset):
            return val
        return typing.cast(
            typing.Union[int, float],
            val
        )
    
    def get_additional_property_(self, name: str) -> typing.Union[schemas.OUTPUT_BASE_TYPES, schemas.Unset]:
        schemas.raise_if_key_known(name, self.__required_keys__, self.__optional_keys__)
        return self.get(name, schemas.unset)
PropertiesWhoseNamesAreJavascriptObjectPropertyNamesDictInput = typing.Mapping[str, schemas.INPUT_TYPES_ALL]


@dataclasses.dataclass(frozen=True)
class PropertiesWhoseNamesAreJavascriptObjectPropertyNames(
    schemas.AnyTypeSchema[PropertiesWhoseNamesAreJavascriptObjectPropertyNamesDict, typing.Tuple[schemas.OUTPUT_BASE_TYPES, ...]],
):
    """NOTE: This class is auto generated by OpenAPI JSON Schema Generator.
    Ref: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator

    Do not edit the class manually.
    """
    # any type
    properties: Properties2 = dataclasses.field(default_factory=lambda: schemas.typed_dict_to_instance(Properties2)) # type: ignore
    type_to_output_cls: typing.Mapping[
        typing.Type,
        typing.Type
    ] = dataclasses.field(
        default_factory=lambda: {
            schemas.immutabledict: PropertiesWhoseNamesAreJavascriptObjectPropertyNamesDict,
        }
    )


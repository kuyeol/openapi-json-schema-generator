# coding: utf-8

"""
    OpenAPI Petstore
    This spec is mainly for testing Petstore server and contains fake endpoints, models. Please do not use this for any other purpose. Special characters: " \  # noqa: E501
    The version of the OpenAPI document: 1.0.0
    Generated by: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator
"""

from __future__ import annotations
from petstore_api.shared_imports.schema_imports import *  # pyright: ignore [reportWildcardImportFromLibrary]

AdditionalProperties: typing_extensions.TypeAlias = schemas.NotAnyTypeSchema

from petstore_api.paths.fake.get.parameters.parameter_0 import schema as schema_2
from petstore_api.paths.fake.get.parameters.parameter_1 import schema
Properties = typing.TypedDict(
    'Properties',
    {
        "enum_header_string": typing.Type[schema.Schema],
        "enum_header_string_array": typing.Type[schema_2.Schema],
    }
)


class HeaderParametersDict(schemas.immutabledict[str, schemas.OUTPUT_BASE_TYPES]):

    __required_keys__: typing.FrozenSet[str] = frozenset({
    })
    __optional_keys__: typing.FrozenSet[str] = frozenset({
        "enum_header_string",
        "enum_header_string_array",
    })
    
    def __new__(
        cls,
        *,
        enum_header_string: typing.Union[
            typing.Literal[
                "_abc",
                "-efg",
                "(xyz)"
            ],
            schemas.Unset
        ] = schemas.unset,
        enum_header_string_array: typing.Union[
            schema_2.SchemaTupleInput,
            schema_2.SchemaTuple,
            schemas.Unset
        ] = schemas.unset,
        configuration_: typing.Optional[schema_configuration.SchemaConfiguration] = None,
    ):
        arg_: typing.Dict[str, typing.Any] = {}
        for key_, val in (
            ("enum_header_string", enum_header_string),
            ("enum_header_string_array", enum_header_string_array),
        ):
            if isinstance(val, schemas.Unset):
                continue
            arg_[key_] = val
        used_arg_ = typing.cast(HeaderParametersDictInput, arg_)
        return HeaderParameters.validate(used_arg_, configuration=configuration_)
    
    @staticmethod
    def from_dict_(
        arg: typing.Union[
            HeaderParametersDictInput,
            HeaderParametersDict
        ],
        configuration: typing.Optional[schema_configuration.SchemaConfiguration] = None
    ) -> HeaderParametersDict:
        return HeaderParameters.validate(arg, configuration=configuration)
    
    @property
    def enum_header_string(self) -> typing.Union[typing.Literal["_abc", "-efg", "(xyz)"], schemas.Unset]:
        val = self.get("enum_header_string", schemas.unset)
        if isinstance(val, schemas.Unset):
            return val
        return typing.cast(
            typing.Literal["_abc", "-efg", "(xyz)"],
            val
        )
    
    @property
    def enum_header_string_array(self) -> typing.Union[schema_2.SchemaTuple, schemas.Unset]:
        val = self.get("enum_header_string_array", schemas.unset)
        if isinstance(val, schemas.Unset):
            return val
        return typing.cast(
            schema_2.SchemaTuple,
            val
        )
HeaderParametersDictInput = typing.TypedDict(
    'HeaderParametersDictInput',
    {
        "enum_header_string": typing.Literal[
            "_abc",
            "-efg",
            "(xyz)"
        ],
        "enum_header_string_array": typing.Union[
            schema_2.SchemaTupleInput,
            schema_2.SchemaTuple
        ],
    },
    total=False
)


@dataclasses.dataclass(frozen=True)
class HeaderParameters(
    schemas.Schema[HeaderParametersDict, tuple]
):
    types: typing.FrozenSet[typing.Type] = frozenset({schemas.immutabledict})
    properties: Properties = dataclasses.field(default_factory=lambda: schemas.typed_dict_to_instance(Properties)) # type: ignore
    additional_properties: typing.Type[AdditionalProperties] = dataclasses.field(default_factory=lambda: AdditionalProperties) # type: ignore
    type_to_output_cls: typing.Mapping[
        typing.Type,
        typing.Type
    ] = dataclasses.field(
        default_factory=lambda: {
            schemas.immutabledict: HeaderParametersDict
        }
    )

    @classmethod
    def validate(
        cls,
        arg: typing.Union[
            HeaderParametersDictInput,
            HeaderParametersDict,
        ],
        configuration: typing.Optional[schema_configuration.SchemaConfiguration] = None
    ) -> HeaderParametersDict:
        return super().validate_base(
            arg,
            configuration=configuration,
        )


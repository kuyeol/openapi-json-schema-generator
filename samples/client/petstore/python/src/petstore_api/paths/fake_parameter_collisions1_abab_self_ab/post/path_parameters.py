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

from petstore_api.paths.fake_parameter_collisions1_abab_self_ab.post.parameters.parameter_10 import schema as schema_2
from petstore_api.paths.fake_parameter_collisions1_abab_self_ab.post.parameters.parameter_11 import schema as schema_3
from petstore_api.paths.fake_parameter_collisions1_abab_self_ab.post.parameters.parameter_12 import schema as schema_5
from petstore_api.paths.fake_parameter_collisions1_abab_self_ab.post.parameters.parameter_13 import schema as schema_4
from petstore_api.paths.fake_parameter_collisions1_abab_self_ab.post.parameters.parameter_9 import schema
Properties = typing.TypedDict(
    'Properties',
    {
        "1": typing.Type[schema.Schema],
        "aB": typing.Type[schema_2.Schema],
        "Ab": typing.Type[schema_3.Schema],
        "A-B": typing.Type[schema_4.Schema],
        "self": typing.Type[schema_5.Schema],
    }
)


class PathParametersDict(schemas.immutabledict[str, schemas.OUTPUT_BASE_TYPES]):

    __required_keys__: typing.FrozenSet[str] = frozenset({
        "1",
        "A-B",
        "Ab",
        "aB",
        "self",
    })
    __optional_keys__: typing.FrozenSet[str] = frozenset({
    })
    
    def __new__(
        cls,
        *,
        Ab: str,
        aB: str,
        configuration_: typing.Optional[schema_configuration.SchemaConfiguration] = None,
    ):
        arg_: typing.Dict[str, typing.Any] = {
            "Ab": Ab,
            "aB": aB,
        }
        used_arg_ = typing.cast(PathParametersDictInput, arg_)
        return PathParameters.validate(used_arg_, configuration=configuration_)
    
    @staticmethod
    def from_dict_(
        arg: typing.Union[
            PathParametersDictInput,
            PathParametersDict
        ],
        configuration: typing.Optional[schema_configuration.SchemaConfiguration] = None
    ) -> PathParametersDict:
        return PathParameters.validate(arg, configuration=configuration)
    
    @property
    def Ab(self) -> str:
        return typing.cast(
            str,
            self.__getitem__("Ab")
        )
    
    @property
    def aB(self) -> str:
        return typing.cast(
            str,
            self.__getitem__("aB")
        )
PathParametersDictInput = typing.TypedDict(
    'PathParametersDictInput',
    {
        "1": str,
        "A-B": str,
        "Ab": str,
        "aB": str,
        "self": str,
    }
)


@dataclasses.dataclass(frozen=True)
class PathParameters(
    schemas.Schema[PathParametersDict, tuple]
):
    types: typing.FrozenSet[typing.Type] = frozenset({schemas.immutabledict})
    required: typing.FrozenSet[str] = frozenset({
        "1",
        "A-B",
        "Ab",
        "aB",
        "self",
    })
    properties: Properties = dataclasses.field(default_factory=lambda: schemas.typed_dict_to_instance(Properties)) # type: ignore
    additional_properties: typing.Type[AdditionalProperties] = dataclasses.field(default_factory=lambda: AdditionalProperties) # type: ignore
    type_to_output_cls: typing.Mapping[
        typing.Type,
        typing.Type
    ] = dataclasses.field(
        default_factory=lambda: {
            schemas.immutabledict: PathParametersDict
        }
    )

    @classmethod
    def validate(
        cls,
        arg: typing.Union[
            PathParametersDictInput,
            PathParametersDict,
        ],
        configuration: typing.Optional[schema_configuration.SchemaConfiguration] = None
    ) -> PathParametersDict:
        return super().validate_base(
            arg,
            configuration=configuration,
        )


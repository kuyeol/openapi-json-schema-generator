# coding: utf-8

"""


    Generated by: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator
"""

import typing
import typing_extensions

from petstore_api import api_client

from . import schema


class Parameter1(api_client.HeaderParameter):
    name = "enum_header_string"
    style = api_client.ParameterStyle.SIMPLE
    schema = schema.Schema

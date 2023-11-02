# coding: utf-8

"""
    OpenAPI Petstore
    This spec is mainly for testing Petstore server and contains fake endpoints, models. Please do not use this for any other purpose. Special characters: \" \\  # noqa: E501
    The version of the OpenAPI document: 1.0.0
    Generated by: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator
"""

import unittest

import petstore_api
from petstore_api.components.schema.json_patch_request_remove import JSONPatchRequestRemove
from petstore_api.configurations import schema_configuration


class TestJSONPatchRequestRemove(unittest.TestCase):
    """JSONPatchRequestRemove unit test stubs"""
    configuration = schema_configuration.SchemaConfiguration(
        disabled_json_schema_keywords={'format'}
    )


if __name__ == '__main__':
    unittest.main()

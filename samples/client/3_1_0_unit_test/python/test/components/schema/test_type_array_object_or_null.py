# coding: utf-8

"""
    openapi 3.1.0 sample spec
    sample spec for testing openapi functionality, built from json schema tests for draft2020-12  # noqa: E501
    The version of the OpenAPI document: 0.0.1
    Generated by: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator
"""

import unittest

import unit_test_api
from unit_test_api.components.schema.type_array_object_or_null import TypeArrayObjectOrNull
from unit_test_api.configurations import schema_configuration


class TestTypeArrayObjectOrNull(unittest.TestCase):
    """TypeArrayObjectOrNull unit test stubs"""
    configuration = schema_configuration.SchemaConfiguration(
        disabled_json_schema_keywords={'format'}
    )

    def test_null_is_valid_passes(self):
        # null is valid
        TypeArrayObjectOrNull.validate(
            None,
            configuration=self.configuration
        )

    def test_string_is_invalid_fails(self):
        # string is invalid
        with self.assertRaises((unit_test_api.ApiValueError, unit_test_api.ApiTypeError)):
            TypeArrayObjectOrNull.validate(
                "foo",
                configuration=self.configuration
            )

    def test_object_is_valid_passes(self):
        # object is valid
        TypeArrayObjectOrNull.validate(
            {
                "foo":
                    123,
            },
            configuration=self.configuration
        )

    def test_number_is_invalid_fails(self):
        # number is invalid
        with self.assertRaises((unit_test_api.ApiValueError, unit_test_api.ApiTypeError)):
            TypeArrayObjectOrNull.validate(
                123,
                configuration=self.configuration
            )

    def test_array_is_valid_passes(self):
        # array is valid
        TypeArrayObjectOrNull.validate(
            [
                1,
                2,
                3,
            ],
            configuration=self.configuration
        )


if __name__ == '__main__':
    unittest.main()

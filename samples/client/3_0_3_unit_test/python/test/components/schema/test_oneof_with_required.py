# coding: utf-8

"""
    openapi 3.0.3 sample spec
    sample spec for testing openapi functionality, built from json schema tests for draft6  # noqa: E501
    The version of the OpenAPI document: 0.0.1
    Generated by: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator
"""

import unittest

import unit_test_api
from unit_test_api.components.schema.oneof_with_required import OneofWithRequired
from unit_test_api.configurations import schema_configuration


class TestOneofWithRequired(unittest.TestCase):
    """OneofWithRequired unit test stubs"""
    configuration = schema_configuration.SchemaConfiguration(
        disabled_json_schema_keywords={'format'}
    )

    def test_both_valid_invalid_fails(self):
        # both valid - invalid
        with self.assertRaises((unit_test_api.ApiValueError, unit_test_api.ApiTypeError)):
            OneofWithRequired.validate(
                {
                    "foo":
                        1,
                    "bar":
                        2,
                    "baz":
                        3,
                },
                configuration=self.configuration
            )

    def test_both_invalid_invalid_fails(self):
        # both invalid - invalid
        with self.assertRaises((unit_test_api.ApiValueError, unit_test_api.ApiTypeError)):
            OneofWithRequired.validate(
                {
                    "bar":
                        2,
                },
                configuration=self.configuration
            )

    def test_first_valid_valid_passes(self):
        # first valid - valid
        OneofWithRequired.validate(
            {
                "foo":
                    1,
                "bar":
                    2,
            },
            configuration=self.configuration
        )

    def test_second_valid_valid_passes(self):
        # second valid - valid
        OneofWithRequired.validate(
            {
                "foo":
                    1,
                "baz":
                    3,
            },
            configuration=self.configuration
        )


if __name__ == '__main__':
    unittest.main()

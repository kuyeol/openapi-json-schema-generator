# coding: utf-8

"""
    openapi 3.1.0 sample spec
    sample spec for testing openapi functionality, built from json schema tests for draft2020-12  # noqa: E501
    The version of the OpenAPI document: 0.0.1
    Generated by: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator
"""

import unittest

import unit_test_api
from unit_test_api.components.schema.minitems_validation import MinitemsValidation
from unit_test_api.configurations import schema_configuration


class TestMinitemsValidation(unittest.TestCase):
    """MinitemsValidation unit test stubs"""
    configuration = schema_configuration.SchemaConfiguration(
        disabled_json_schema_keywords={'format'}
    )

    def test_too_short_is_invalid_fails(self):
        # too short is invalid
        with self.assertRaises((unit_test_api.ApiValueError, unit_test_api.ApiTypeError)):
            MinitemsValidation.validate(
                [
                ],
                configuration=self.configuration
            )

    def test_ignores_non_arrays_passes(self):
        # ignores non-arrays
        MinitemsValidation.validate(
            "",
            configuration=self.configuration
        )

    def test_longer_is_valid_passes(self):
        # longer is valid
        MinitemsValidation.validate(
            [
                1,
                2,
            ],
            configuration=self.configuration
        )

    def test_exact_length_is_valid_passes(self):
        # exact length is valid
        MinitemsValidation.validate(
            [
                1,
            ],
            configuration=self.configuration
        )


if __name__ == '__main__':
    unittest.main()

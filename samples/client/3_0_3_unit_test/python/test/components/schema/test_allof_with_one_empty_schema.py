# coding: utf-8

"""
    openapi 3.0.3 sample spec
    sample spec for testing openapi functionality, built from json schema tests for draft6  # noqa: E501
    The version of the OpenAPI document: 0.0.1
    Generated by: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator
"""

import unittest

import unit_test_api
from unit_test_api.components.schema.allof_with_one_empty_schema import AllofWithOneEmptySchema
from unit_test_api.configurations import schema_configuration


class TestAllofWithOneEmptySchema(unittest.TestCase):
    """AllofWithOneEmptySchema unit test stubs"""
    configuration = schema_configuration.SchemaConfiguration(
        disabled_json_schema_keywords={'format'}
    )

    def test_any_data_is_valid_passes(self):
        # any data is valid
        AllofWithOneEmptySchema.validate(
            1,
            configuration=self.configuration
        )


if __name__ == '__main__':
    unittest.main()

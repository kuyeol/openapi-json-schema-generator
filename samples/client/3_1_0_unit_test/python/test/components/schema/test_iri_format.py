# coding: utf-8

"""
    openapi 3.1.0 sample spec
    sample spec for testing openapi functionality, built from json schema tests for draft2020-12  # noqa: E501
    The version of the OpenAPI document: 0.0.1
    Generated by: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator
"""

import unittest

import unit_test_api
from unit_test_api.components.schema.iri_format import IriFormat
from unit_test_api.configurations import schema_configuration


class TestIriFormat(unittest.TestCase):
    """IriFormat unit test stubs"""
    configuration = schema_configuration.SchemaConfiguration(
        disabled_json_schema_keywords={'format'}
    )

    def test_all_string_formats_ignore_objects_passes(self):
        # all string formats ignore objects
        IriFormat.validate(
            {
            },
            configuration=self.configuration
        )

    def test_all_string_formats_ignore_booleans_passes(self):
        # all string formats ignore booleans
        IriFormat.validate(
            False,
            configuration=self.configuration
        )

    def test_all_string_formats_ignore_integers_passes(self):
        # all string formats ignore integers
        IriFormat.validate(
            12,
            configuration=self.configuration
        )

    def test_all_string_formats_ignore_floats_passes(self):
        # all string formats ignore floats
        IriFormat.validate(
            13.7,
            configuration=self.configuration
        )

    def test_all_string_formats_ignore_arrays_passes(self):
        # all string formats ignore arrays
        IriFormat.validate(
            [
            ],
            configuration=self.configuration
        )

    def test_invalid_iri_string_is_only_an_annotation_by_default_passes(self):
        # invalid iri string is only an annotation by default
        IriFormat.validate(
            "http://2001:0db8:85a3:0000:0000:8a2e:0370:7334",
            configuration=self.configuration
        )

    def test_all_string_formats_ignore_nulls_passes(self):
        # all string formats ignore nulls
        IriFormat.validate(
            None,
            configuration=self.configuration
        )


if __name__ == '__main__':
    unittest.main()

# coding: utf-8

"""
    Generated by: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator
"""

import unittest
from unittest.mock import patch

import urllib3
import typing_extensions

import unit_test_api
from unit_test_api.paths.request_body_post_uuid_format_request_body.post import operation as post  # noqa: E501
from unit_test_api import schemas, api_client
from unit_test_api.configurations import api_configuration, schema_configuration

from .. import ApiTestMixin


class TestPost(ApiTestMixin, unittest.TestCase):
    """
    Post unit test stubs
    """
    api_config = api_configuration.ApiConfiguration()
    schema_config = schema_configuration.SchemaConfiguration(
        disabled_json_schema_keywords={'format'}
    )
    used_api_client = api_client.ApiClient(configuration=api_config, schema_configuration=schema_config)
    api = post.ApiForPost(api_client=used_api_client)  # noqa: E501

    response_status = 200
    response_body = ''

    def test_invalid_uuid_string_is_only_an_annotation_by_default_passes(self):
        content_type = 'application/json'
        # invalid uuid string is only an annotation by default
        with patch.object(urllib3.PoolManager, 'request') as mock_request:
            payload = (
                "2eb8aa08-aa98-11ea-b4aa-73b441d1638"
            )
            body = post.request_body.RequestBody.content["application/json"].schema.validate(
                payload,
                configuration=self.schema_config
            )
            mock_request.return_value = self.response(
                self.json_bytes(self.response_body),
                status=self.response_status
            )
            api_response = self.api.post(
                body=body,
            )
            self.assert_pool_manager_request_called_with(
                mock_request,
                self.api_config.get_server_url('servers', None) + "/requestBody/postUuidFormatRequestBody",
                method='post'.upper(),
                body=self.json_bytes(payload),
                content_type=content_type,
            )

            assert isinstance(api_response.response, urllib3.HTTPResponse)
            assert isinstance(api_response.body, schemas.Unset)

    def test_all_string_formats_ignore_objects_passes(self):
        content_type = 'application/json'
        # all string formats ignore objects
        with patch.object(urllib3.PoolManager, 'request') as mock_request:
            payload = (
                {
                }
            )
            body = post.request_body.RequestBody.content["application/json"].schema.validate(
                payload,
                configuration=self.schema_config
            )
            mock_request.return_value = self.response(
                self.json_bytes(self.response_body),
                status=self.response_status
            )
            api_response = self.api.post(
                body=body,
            )
            self.assert_pool_manager_request_called_with(
                mock_request,
                self.api_config.get_server_url('servers', None) + "/requestBody/postUuidFormatRequestBody",
                method='post'.upper(),
                body=self.json_bytes(payload),
                content_type=content_type,
            )

            assert isinstance(api_response.response, urllib3.HTTPResponse)
            assert isinstance(api_response.body, schemas.Unset)

    def test_all_string_formats_ignore_booleans_passes(self):
        content_type = 'application/json'
        # all string formats ignore booleans
        with patch.object(urllib3.PoolManager, 'request') as mock_request:
            payload = (
                False
            )
            body = post.request_body.RequestBody.content["application/json"].schema.validate(
                payload,
                configuration=self.schema_config
            )
            mock_request.return_value = self.response(
                self.json_bytes(self.response_body),
                status=self.response_status
            )
            api_response = self.api.post(
                body=body,
            )
            self.assert_pool_manager_request_called_with(
                mock_request,
                self.api_config.get_server_url('servers', None) + "/requestBody/postUuidFormatRequestBody",
                method='post'.upper(),
                body=self.json_bytes(payload),
                content_type=content_type,
            )

            assert isinstance(api_response.response, urllib3.HTTPResponse)
            assert isinstance(api_response.body, schemas.Unset)

    def test_all_string_formats_ignore_integers_passes(self):
        content_type = 'application/json'
        # all string formats ignore integers
        with patch.object(urllib3.PoolManager, 'request') as mock_request:
            payload = (
                12
            )
            body = post.request_body.RequestBody.content["application/json"].schema.validate(
                payload,
                configuration=self.schema_config
            )
            mock_request.return_value = self.response(
                self.json_bytes(self.response_body),
                status=self.response_status
            )
            api_response = self.api.post(
                body=body,
            )
            self.assert_pool_manager_request_called_with(
                mock_request,
                self.api_config.get_server_url('servers', None) + "/requestBody/postUuidFormatRequestBody",
                method='post'.upper(),
                body=self.json_bytes(payload),
                content_type=content_type,
            )

            assert isinstance(api_response.response, urllib3.HTTPResponse)
            assert isinstance(api_response.body, schemas.Unset)

    def test_all_string_formats_ignore_floats_passes(self):
        content_type = 'application/json'
        # all string formats ignore floats
        with patch.object(urllib3.PoolManager, 'request') as mock_request:
            payload = (
                13.7
            )
            body = post.request_body.RequestBody.content["application/json"].schema.validate(
                payload,
                configuration=self.schema_config
            )
            mock_request.return_value = self.response(
                self.json_bytes(self.response_body),
                status=self.response_status
            )
            api_response = self.api.post(
                body=body,
            )
            self.assert_pool_manager_request_called_with(
                mock_request,
                self.api_config.get_server_url('servers', None) + "/requestBody/postUuidFormatRequestBody",
                method='post'.upper(),
                body=self.json_bytes(payload),
                content_type=content_type,
            )

            assert isinstance(api_response.response, urllib3.HTTPResponse)
            assert isinstance(api_response.body, schemas.Unset)

    def test_all_string_formats_ignore_arrays_passes(self):
        content_type = 'application/json'
        # all string formats ignore arrays
        with patch.object(urllib3.PoolManager, 'request') as mock_request:
            payload = (
                [
                ]
            )
            body = post.request_body.RequestBody.content["application/json"].schema.validate(
                payload,
                configuration=self.schema_config
            )
            mock_request.return_value = self.response(
                self.json_bytes(self.response_body),
                status=self.response_status
            )
            api_response = self.api.post(
                body=body,
            )
            self.assert_pool_manager_request_called_with(
                mock_request,
                self.api_config.get_server_url('servers', None) + "/requestBody/postUuidFormatRequestBody",
                method='post'.upper(),
                body=self.json_bytes(payload),
                content_type=content_type,
            )

            assert isinstance(api_response.response, urllib3.HTTPResponse)
            assert isinstance(api_response.body, schemas.Unset)

    def test_all_string_formats_ignore_nulls_passes(self):
        content_type = 'application/json'
        # all string formats ignore nulls
        with patch.object(urllib3.PoolManager, 'request') as mock_request:
            payload = (
                None
            )
            body = post.request_body.RequestBody.content["application/json"].schema.validate(
                payload,
                configuration=self.schema_config
            )
            mock_request.return_value = self.response(
                self.json_bytes(self.response_body),
                status=self.response_status
            )
            api_response = self.api.post(
                body=body,
            )
            self.assert_pool_manager_request_called_with(
                mock_request,
                self.api_config.get_server_url('servers', None) + "/requestBody/postUuidFormatRequestBody",
                method='post'.upper(),
                body=self.json_bytes(payload),
                content_type=content_type,
            )

            assert isinstance(api_response.response, urllib3.HTTPResponse)
            assert isinstance(api_response.body, schemas.Unset)

if __name__ == '__main__':
    unittest.main()

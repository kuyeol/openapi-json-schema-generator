# coding: utf-8

"""


    Generated by: https://openapi-generator.tech
"""

from dataclasses import dataclass
import typing_extensions
import urllib3
from urllib3._collections import HTTPHeaderDict

from petstore_api import api_client, exceptions
from datetime import date, datetime  # noqa: F401
import decimal  # noqa: F401
import functools  # noqa: F401
import io  # noqa: F401
import re  # noqa: F401
import typing  # noqa: F401
import typing_extensions  # noqa: F401
import uuid  # noqa: F401

import frozendict  # noqa: F401

from petstore_api import schemas  # noqa: F401

from petstore_api.model.pet import Pet

from . import path

# body param
SchemaForRequestBodyApplicationJson = Pet
SchemaForRequestBodyApplicationXml = Pet


request_body_pet = api_client.RequestBody(
    content={
        'application/json': api_client.MediaType(
            schema=SchemaForRequestBodyApplicationJson),
        'application/xml': api_client.MediaType(
            schema=SchemaForRequestBodyApplicationXml),
    },
    required=True,
)
_auth = [
    'http_signature_test',
    'petstore_auth',
]
_servers = (
    {
        'url': "https://petstore.swagger.io/v2",
        'description': "No description provided",
    },
    {
        'url': "https://path-server-test.petstore.local/v2",
        'description': "No description provided",
    },
)


@dataclass
class ApiResponseFor400(api_client.ApiResponse):
    response: urllib3.HTTPResponse
    body: schemas.Unset = schemas.unset
    headers: schemas.Unset = schemas.unset


_response_for_400 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor400,
)


@dataclass
class ApiResponseFor404(api_client.ApiResponse):
    response: urllib3.HTTPResponse
    body: schemas.Unset = schemas.unset
    headers: schemas.Unset = schemas.unset


_response_for_404 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor404,
)


@dataclass
class ApiResponseFor405(api_client.ApiResponse):
    response: urllib3.HTTPResponse
    body: schemas.Unset = schemas.unset
    headers: schemas.Unset = schemas.unset


_response_for_405 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor405,
)
_status_code_to_response = {
    '400': _response_for_400,
    '404': _response_for_404,
    '405': _response_for_405,
}


class BaseApi(api_client.Api):
    @typing.overload
    def _update_pet_oapg(
        self,
        body: typing.Union[SchemaForRequestBodyApplicationJson,SchemaForRequestBodyApplicationXml,],
        content_type: typing_extensions.Literal["application/json"] = "application/json",
        host_index: typing.Optional[int] = None,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: typing_extensions.Literal[False] = ...,
    ) -> api_client.ApiResponseWithoutDeserialization: ...    @typing.overload
    def _update_pet_oapg(
        self,
        body: typing.Union[SchemaForRequestBodyApplicationJson,SchemaForRequestBodyApplicationXml,],
        content_type: typing_extensions.Literal["application/xml"] = "application/xml",
        host_index: typing.Optional[int] = None,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: typing_extensions.Literal[False] = ...,
    ) -> api_client.ApiResponseWithoutDeserialization: ...
    @typing.overload
    def _update_pet_oapg(
        self,
        body: typing.Union[SchemaForRequestBodyApplicationJson,SchemaForRequestBodyApplicationXml,],
        skip_deserialization: typing_extensions.Literal[True],
        content_type: str = ...,
        host_index: typing.Optional[int] = None,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
    ) -> api_client.ApiResponseWithoutDeserialization: ...

    @typing.overload
    def _update_pet_oapg(
        self,
        body: typing.Union[SchemaForRequestBodyApplicationJson,SchemaForRequestBodyApplicationXml,],
        content_type: str = ...,
        host_index: typing.Optional[int] = None,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: bool = ...,
    ) -> typing.Union[
        api_client.ApiResponseWithoutDeserialization,
    ]: ...

    def _update_pet_oapg(
        self,
        body: typing.Union[SchemaForRequestBodyApplicationJson,SchemaForRequestBodyApplicationXml,],
        content_type: str = 'application/json',
        host_index: typing.Optional[int] = None,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: bool = False,
    ):
        """
        Update an existing pet
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        used_path = path.value

        _headers = HTTPHeaderDict()
        # TODO add cookie handling

        if body is schemas.unset:
            raise exceptions.ApiValueError(
                'The required body parameter has an invalid value of: unset. Set a valid value instead')
        _fields = None
        _body = None
        serialized_data = request_body_pet.serialize(body, content_type)
        _headers.add('Content-Type', content_type)
        if 'fields' in serialized_data:
            _fields = serialized_data['fields']
        elif 'body' in serialized_data:
            _body = serialized_data['body']
        host = self._get_host_oapg('update_pet', _servers, host_index)

        response = self.api_client.call_api(
            resource_path=used_path,
            method='put'.upper(),
            headers=_headers,
            fields=_fields,
            body=_body,
            auth_settings=_auth,
            host=host,
            stream=stream,
            timeout=timeout,
        )

        if skip_deserialization:
            api_response = api_client.ApiResponseWithoutDeserialization(response=response)
        else:
            response_for_status = _status_code_to_response.get(str(response.status))
            if response_for_status:
                api_response = response_for_status.deserialize(response, self.api_client.configuration)
            else:
                api_response = api_client.ApiResponseWithoutDeserialization(response=response)

        if not 200 <= response.status <= 299:
            raise exceptions.ApiException(api_response=api_response)

        return api_response


class UpdatePet(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    @typing.overload
    def update_pet(
        self,
        body: typing.Union[SchemaForRequestBodyApplicationJson,SchemaForRequestBodyApplicationXml,],
        content_type: typing_extensions.Literal["application/json"] = "application/json",
        host_index: typing.Optional[int] = None,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: typing_extensions.Literal[False] = ...,
    ) -> api_client.ApiResponseWithoutDeserialization: ...    @typing.overload
    def update_pet(
        self,
        body: typing.Union[SchemaForRequestBodyApplicationJson,SchemaForRequestBodyApplicationXml,],
        content_type: typing_extensions.Literal["application/xml"] = "application/xml",
        host_index: typing.Optional[int] = None,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: typing_extensions.Literal[False] = ...,
    ) -> api_client.ApiResponseWithoutDeserialization: ...
    @typing.overload
    def update_pet(
        self,
        body: typing.Union[SchemaForRequestBodyApplicationJson,SchemaForRequestBodyApplicationXml,],
        skip_deserialization: typing_extensions.Literal[True],
        content_type: str = ...,
        host_index: typing.Optional[int] = None,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
    ) -> api_client.ApiResponseWithoutDeserialization: ...

    @typing.overload
    def update_pet(
        self,
        body: typing.Union[SchemaForRequestBodyApplicationJson,SchemaForRequestBodyApplicationXml,],
        content_type: str = ...,
        host_index: typing.Optional[int] = None,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: bool = ...,
    ) -> typing.Union[
        api_client.ApiResponseWithoutDeserialization,
    ]: ...

    def update_pet(
        self,
        body: typing.Union[SchemaForRequestBodyApplicationJson,SchemaForRequestBodyApplicationXml,],
        content_type: str = 'application/json',
        host_index: typing.Optional[int] = None,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: bool = False,
    ):
        return self._update_pet_oapg(
            body=body,
            content_type=content_type,
            host_index=host_index,
            stream=stream,
            timeout=timeout,
            skip_deserialization=skip_deserialization
        )


class ApiForput(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    @typing.overload
    def put(
        self,
        body: typing.Union[SchemaForRequestBodyApplicationJson,SchemaForRequestBodyApplicationXml,],
        content_type: typing_extensions.Literal["application/json"] = "application/json",
        host_index: typing.Optional[int] = None,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: typing_extensions.Literal[False] = ...,
    ) -> api_client.ApiResponseWithoutDeserialization: ...    @typing.overload
    def put(
        self,
        body: typing.Union[SchemaForRequestBodyApplicationJson,SchemaForRequestBodyApplicationXml,],
        content_type: typing_extensions.Literal["application/xml"] = "application/xml",
        host_index: typing.Optional[int] = None,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: typing_extensions.Literal[False] = ...,
    ) -> api_client.ApiResponseWithoutDeserialization: ...
    @typing.overload
    def put(
        self,
        body: typing.Union[SchemaForRequestBodyApplicationJson,SchemaForRequestBodyApplicationXml,],
        skip_deserialization: typing_extensions.Literal[True],
        content_type: str = ...,
        host_index: typing.Optional[int] = None,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
    ) -> api_client.ApiResponseWithoutDeserialization: ...

    @typing.overload
    def put(
        self,
        body: typing.Union[SchemaForRequestBodyApplicationJson,SchemaForRequestBodyApplicationXml,],
        content_type: str = ...,
        host_index: typing.Optional[int] = None,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: bool = ...,
    ) -> typing.Union[
        api_client.ApiResponseWithoutDeserialization,
    ]: ...

    def put(
        self,
        body: typing.Union[SchemaForRequestBodyApplicationJson,SchemaForRequestBodyApplicationXml,],
        content_type: str = 'application/json',
        host_index: typing.Optional[int] = None,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: bool = False,
    ):
        return self._update_pet_oapg(
            body=body,
            content_type=content_type,
            host_index=host_index,
            stream=stream,
            timeout=timeout,
            skip_deserialization=skip_deserialization
        )



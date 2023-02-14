# -*- coding: utf-8 -*-
import base64

from Tea.exceptions import TeaException
from openapi_util import models as dkms_util_models
from requests import codes
from sdk.models import VerifyRequest

from alibabacloud_kms_kms20160120.handlers.kms_transfer_handler import get_missing_parameter_client_exception, \
    KmsTransferHandler
from alibabacloud_kms_kms20160120.utils import consts


class AsymmetricVerifyTransferHandler(KmsTransferHandler):

    def __init__(self, client, action, kms_config):
        self.client = client
        self.action = action
        self.response_headers = [consts.MIGRATION_KEY_VERSION_ID_KEY]
        self.encoding = 'utf-8'
        if kms_config is not None and kms_config.encoding is not None:
            self.encoding = kms_config.encoding

    def get_client(self):
        return self.client

    def get_action(self):
        return self.action

    def build_kms_request(self, request, runtime_options):
        if not request.query.get('Digest'):
            raise get_missing_parameter_client_exception('Digest')
        if not request.query.get('Value'):
            raise get_missing_parameter_client_exception("Value")
        kms_request = VerifyRequest()
        kms_request.key_id = request.query.get('KeyId')
        kms_request.algorithm = request.query.get('Algorithm')
        kms_request.message_type = consts.DIGEST_MESSAGE_TYPE
        kms_request.message = base64.b64decode(request.query.get('Digest'))
        kms_request.signature = base64.b64decode(request.query.get('Value'))
        return kms_request

    def call_kms(self, request, runtime_options):
        dkms_runtime_options = dkms_util_models.RuntimeOptions().from_map(runtime_options.to_map())
        dkms_runtime_options.verify = runtime_options.ca
        dkms_runtime_options.response_headers = self.response_headers
        return self.client.verify_with_options(request, dkms_runtime_options)

    def transfer_response(self, response, runtime_options):
        response_headers = response.response_headers
        if not response_headers:
            raise TeaException({
                'message': 'Can not found response headers'
            })
        key_version_id = response_headers.get(consts.MIGRATION_KEY_VERSION_ID_KEY)
        body = {
            'KeyId': response.key_id,
            'Value': response.value,
            'RequestId': response.request_id,
            'KeyVersionId': key_version_id
        }
        return {
            'body': body,
            'headers': response_headers,
            'statusCode': codes.ok
        }

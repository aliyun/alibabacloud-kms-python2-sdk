# -*- coding: utf-8 -*-
import base64

from Tea.exceptions import TeaException
from openapi_util import models as dkms_util_models
from requests import codes
from sdk.models import EncryptRequest

from alibabacloud_kms_kms20160120.handlers.kms_transfer_handler import KmsTransferHandler
from alibabacloud_kms_kms20160120.utils import consts, encryption_context_utils


class EncryptTransferHandler(KmsTransferHandler):

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
        kms_request = EncryptRequest()
        kms_request.key_id = request.query.get('KeyId')
        if runtime_options is not None and runtime_options.encoding is not None:
            encoding = runtime_options.encoding
        else:
            encoding = self.encoding
        plaintext = request.query.get('Plaintext')
        if plaintext is not None:
            if isinstance(plaintext, unicode):
                kms_request.plaintext = request.query.get('Plaintext').encode(encoding)
            else:
                kms_request.plaintext = plaintext
        if request.query.get('EncryptionContext'):
            kms_request.aad = encryption_context_utils.sort_and_encode(request.query.get('EncryptionContext'), encoding)
        return kms_request

    def call_kms(self, request, runtime_options):
        dkms_runtime_options = dkms_util_models.RuntimeOptions().from_map(runtime_options.to_map())
        dkms_runtime_options.verify = runtime_options.ca
        dkms_runtime_options.response_headers = self.response_headers
        return self.client.encrypt_with_options(request, dkms_runtime_options)

    def transfer_response(self, response, runtime_options):
        response_headers = response.response_headers
        if not response_headers:
            raise TeaException({
                'message': 'Can not found response headers'
            })
        key_version_id = response_headers.get(consts.MIGRATION_KEY_VERSION_ID_KEY)
        if not key_version_id:
            raise TeaException({
                'message': "Can not found response headers parameter[%s]" % consts.MIGRATION_KEY_VERSION_ID_KEY
            })
        if runtime_options is not None and runtime_options.encoding is not None:
            encoding = runtime_options.encoding
        else:
            encoding = self.encoding
        ciphertext_blob = key_version_id.encode(encoding) + response.iv + response.ciphertext_blob
        body = {
            'KeyId': response.key_id,
            'CiphertextBlob': base64.b64encode(ciphertext_blob).decode(encoding),
            'RequestId': response.request_id,
            'KeyVersionId': key_version_id
        }
        return {
            'body': body,
            'headers': response.response_headers,
            'statusCode': codes.ok
        }

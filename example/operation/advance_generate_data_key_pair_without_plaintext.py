# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import unicode_literals

import sys


from openapi import models as dedicated_kms_openapi_models
from alibabacloud_kms_kms20160120.client import Client as KmsSdkClient
from sdk import models as dedicated_kms_sdk_models
from alibabacloud_tea_util.client import Client as UtilClient

import os

class AdvanceGenerateDataKeyPairWithoutPlaintext(object):
    def __init__(self):
        pass

    @staticmethod
    def create_kms_instance_config(client_key_file, password, endpoint, ca_file_path):
        config = dedicated_kms_openapi_models.Config(
            client_key_file=client_key_file,
            password=password,
            endpoint=endpoint,
            ca_file_path=ca_file_path
        )
        return config

    @staticmethod
    def create_client(kms_instance_config):
        return KmsSdkClient(kms_instance_config=kms_instance_config)

    @staticmethod
    def advance_generate_data_key_pair_without_plaintext(client, key_format, aad, key_id, key_pair_spec):
        request = dedicated_kms_sdk_models.AdvanceGenerateDataKeyPairWithoutPlaintextRequest(
            key_format=key_format,
            aad=aad,
            key_id=key_id,
            key_pair_spec=key_pair_spec
        )
        return client.advance_generate_data_key_pair_without_plaintext(request)

    @staticmethod
    def main(args):
        kms_instance_config = AdvanceGenerateDataKeyPairWithoutPlaintext.create_kms_instance_config(os.getenv('your client key file path env'), os.getenv('your client key password env'), 'your kms instance endpoint', 'your ca file path')
        client = AdvanceGenerateDataKeyPairWithoutPlaintext.create_client(kms_instance_config)
        key_format = 'your keyFormat'
        aad = UtilClient.to_bytes('your aad')
        key_id = 'your keyId'
        key_pair_spec = 'your keyPairSpec'
        AdvanceGenerateDataKeyPairWithoutPlaintext.advance_generate_data_key_pair_without_plaintext(client, key_format, aad, key_id, key_pair_spec)
        


if __name__ == '__main__':
    AdvanceGenerateDataKeyPairWithoutPlaintext.main(sys.argv[1:])

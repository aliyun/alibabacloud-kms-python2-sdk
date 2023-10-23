# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import unicode_literals

import sys


from openapi import models as dedicated_kms_openapi_models
from alibabacloud_kms_kms20160120.client import Client as KmsSdkClient
from sdk import models as dedicated_kms_sdk_models
from alibabacloud_tea_util.client import Client as UtilClient

import os

class AdvanceDecrypt(object):
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
    def advance_decrypt(client, padding_mode, aad, ciphertext_blob, key_id, iv, algorithm):
        request = dedicated_kms_sdk_models.AdvanceDecryptRequest(
            padding_mode=padding_mode,
            aad=aad,
            ciphertext_blob=ciphertext_blob,
            key_id=key_id,
            iv=iv,
            algorithm=algorithm
        )
        return client.advance_decrypt(request)

    @staticmethod
    def main(args):
        kms_instance_config = AdvanceDecrypt.create_kms_instance_config(os.getenv('your client key file path env'), os.getenv('your client key password env'), 'your kms instance endpoint', 'your ca file path')
        client = AdvanceDecrypt.create_client(kms_instance_config)
        padding_mode = 'your paddingMode'
        aad = UtilClient.to_bytes('your aad')
        ciphertext_blob = UtilClient.to_bytes('your ciphertextBlob')
        key_id = 'your keyId'
        iv = UtilClient.to_bytes('your iv')
        algorithm = 'your algorithm'
        AdvanceDecrypt.advance_decrypt(client, padding_mode, aad, ciphertext_blob, key_id, iv, algorithm)
        


if __name__ == '__main__':
    AdvanceDecrypt.main(sys.argv[1:])

# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import unicode_literals

import sys


from openapi import models as dedicated_kms_openapi_models
from alibabacloud_kms_kms20160120.client import Client as KmsSdkClient
from sdk import models as dedicated_kms_sdk_models
from alibabacloud_tea_util.client import Client as UtilClient

import os

class AdvanceEncrypt(object):
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
    def advance_encrypt(client, padding_mode, aad, key_id, plaintext, iv, algorithm):
        request = dedicated_kms_sdk_models.AdvanceEncryptRequest(
            padding_mode=padding_mode,
            aad=aad,
            key_id=key_id,
            plaintext=plaintext,
            iv=iv,
            algorithm=algorithm
        )
        return client.advance_encrypt(request)

    @staticmethod
    def main(args):
        kms_instance_config = AdvanceEncrypt.create_kms_instance_config(os.getenv('your client key file path env'), os.getenv('your client key password env'), 'your kms instance endpoint', 'your ca file path')
        client = AdvanceEncrypt.create_client(kms_instance_config)
        padding_mode = 'your paddingMode'
        aad = UtilClient.to_bytes('your aad')
        key_id = 'your keyId'
        plaintext = UtilClient.to_bytes('your plaintext')
        iv = UtilClient.to_bytes('your iv')
        algorithm = 'your algorithm'
        AdvanceEncrypt.advance_encrypt(client, padding_mode, aad, key_id, plaintext, iv, algorithm)
        


if __name__ == '__main__':
    AdvanceEncrypt.main(sys.argv[1:])

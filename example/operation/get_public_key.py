# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import unicode_literals

import sys


from openapi import models as dedicated_kms_openapi_models
from alibabacloud_kms_kms20160120.client import Client as KmsSdkClient
from sdk import models as dedicated_kms_sdk_models
from alibabacloud_tea_util.client import Client as UtilClient

import os

class GetPublicKey(object):
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
    def get_public_key(client, key_id):
        request = dedicated_kms_sdk_models.GetPublicKeyRequest(
            key_id=key_id
        )
        return client.get_public_key(request)

    @staticmethod
    def main(args):
        kms_instance_config = GetPublicKey.create_kms_instance_config(os.getenv('your client key file path env'), os.getenv('your client key password env'), 'your kms instance endpoint', 'your ca file path')
        client = GetPublicKey.create_client(kms_instance_config)
        key_id = 'your keyId'
        response = GetPublicKey.get_public_key(client, key_id)
        print response


if __name__ == '__main__':
    GetPublicKey.main(sys.argv[1:])

# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import unicode_literals

import sys


from openapi import models as dedicated_kms_openapi_models
from alibabacloud_kms_kms20160120.client import Client as KmsSdkClient
from sdk import models as dedicated_kms_sdk_models
from alibabacloud_tea_util.client import Client as UtilClient

import os

class GetSecretValue(object):
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
    def get_secret_value(client, fetch_extended_config, secret_name, version_id, version_stage):
        request = dedicated_kms_sdk_models.GetSecretValueRequest(
            fetch_extended_config=fetch_extended_config,
            secret_name=secret_name,
            version_id=version_id,
            version_stage=version_stage
        )
        return client.get_secret_value(request)

    @staticmethod
    def main(args):
        kms_instance_config = GetSecretValue.create_kms_instance_config(os.getenv('your client key file path env'), os.getenv('your client key password env'), 'your kms instance endpoint', 'your ca file path')
        client = GetSecretValue.create_client(kms_instance_config)
        fetch_extended_config = False
        secret_name = 'your secretName'
        version_id = 'your versionId'
        version_stage = 'your versionStage'
        GetSecretValue.get_secret_value(client, fetch_extended_config, secret_name, version_id, version_stage)
        


if __name__ == '__main__':
    GetSecretValue.main(sys.argv[1:])

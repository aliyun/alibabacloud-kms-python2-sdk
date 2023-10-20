# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import unicode_literals

import sys


from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_kms_kms20160120.client import Client as KmsSdkClient
from alibabacloud_kms20160120 import models as kms_20160120_models

import os

class CreateSecret(object):
    def __init__(self):
        pass

    @staticmethod
    def create_open_api_config(access_key_id, access_key_secret, region_id):
        config = open_api_models.Config(
            access_key_id=access_key_id,
            access_key_secret=access_key_secret,
            region_id=region_id
        )
        return config

    @staticmethod
    def create_client(open_api_config):
        return KmsSdkClient(open_api_config=open_api_config)

    @staticmethod
    def create_secret(client, enable_automatic_rotation, rotation_interval, encryption_key_id, secret_name, version_id, secret_data_type, secret_type, description, dkmsinstance_id, secret_data, tags):
        request = kms_20160120_models.CreateSecretRequest(
            enable_automatic_rotation=enable_automatic_rotation,
            rotation_interval=rotation_interval,
            encryption_key_id=encryption_key_id,
            secret_name=secret_name,
            version_id=version_id,
            secret_data_type=secret_data_type,
            secret_type=secret_type,
            description=description,
            dkmsinstance_id=dkmsinstance_id,
            secret_data=secret_data,
            tags=tags
        )
        return client.create_secret(request)

    @staticmethod
    def main(args):
        # 请确保代码运行环境设置了环境变量 ALIBABA_CLOUD_ACCESS_KEY_ID 和 ALIBABA_CLOUD_ACCESS_KEY_SECRET。
        # 工程代码泄露可能会导致 AccessKey 泄露，并威胁账号下所有资源的安全性。以下代码示例使用环境变量获取 AccessKey 的方式进行调用，仅供参考，建议使用更安全的 STS 方式，更多鉴权访问方式请参见：https://help.aliyun.com/document_detail/378657.html
        open_api_config = CreateSecret.create_open_api_config(os.getenv('ALIBABA_CLOUD_ACCESS_KEY_ID'), os.getenv('ALIBABA_CLOUD_ACCESS_KEY_SECRET'), 'your region id')
        client = CreateSecret.create_client(open_api_config)
        enable_automatic_rotation = False
        rotation_interval = 'your rotationInterval'
        encryption_key_id = 'your encryptionKeyId'
        secret_name = 'your secretName'
        version_id = 'your versionId'
        secret_data_type = 'your secretDataType'
        secret_type = 'your secretType'
        description = 'your description'
        d_kmsinstance_id = 'your dKMSInstanceId'
        secret_data = 'your secretData'
        tags = 'your tags'
        response = CreateSecret.create_secret(client, enable_automatic_rotation, rotation_interval, encryption_key_id, secret_name, version_id, secret_data_type, secret_type, description, d_kmsinstance_id, secret_data, tags)
        print response


if __name__ == '__main__':
    CreateSecret.main(sys.argv[1:])

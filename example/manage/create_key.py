# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import unicode_literals

import sys


from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_kms_kms20160120.client import Client as KmsSdkClient
from alibabacloud_kms20160120 import models as kms_20160120_models

import os

class CreateKey(object):
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
    def create_key(client, enable_automatic_rotation, rotation_interval, key_usage, origin, description, dkmsinstance_id, protection_level, key_spec):
        request = kms_20160120_models.CreateKeyRequest(
            enable_automatic_rotation=enable_automatic_rotation,
            rotation_interval=rotation_interval,
            key_usage=key_usage,
            origin=origin,
            description=description,
            dkmsinstance_id=dkmsinstance_id,
            protection_level=protection_level,
            key_spec=key_spec
        )
        return client.create_key(request)

    @staticmethod
    def main(args):
        # 请确保代码运行环境设置了环境变量 ALIBABA_CLOUD_ACCESS_KEY_ID 和 ALIBABA_CLOUD_ACCESS_KEY_SECRET。
        # 工程代码泄露可能会导致 AccessKey 泄露，并威胁账号下所有资源的安全性。以下代码示例使用环境变量获取 AccessKey 的方式进行调用，仅供参考，建议使用更安全的 STS 方式，更多鉴权访问方式请参见：https://help.aliyun.com/document_detail/378657.html
        open_api_config = CreateKey.create_open_api_config(os.getenv('ALIBABA_CLOUD_ACCESS_KEY_ID'), os.getenv('ALIBABA_CLOUD_ACCESS_KEY_SECRET'), 'your region id')
        client = CreateKey.create_client(open_api_config)
        enable_automatic_rotation = False
        rotation_interval = 'your rotationInterval'
        key_usage = 'your keyUsage'
        origin = 'your origin'
        description = 'your description'
        d_kmsinstance_id = 'your dKMSInstanceId'
        protection_level = 'your protectionLevel'
        key_spec = 'your keySpec'
        CreateKey.create_key(client, enable_automatic_rotation, rotation_interval, key_usage, origin, description, d_kmsinstance_id, protection_level, key_spec)
        


if __name__ == '__main__':
    CreateKey.main(sys.argv[1:])

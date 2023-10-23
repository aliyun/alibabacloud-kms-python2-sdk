# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import unicode_literals

import sys


from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_kms_kms20160120.client import Client as KmsSdkClient
from alibabacloud_kms20160120 import models as kms_20160120_models

import os

class DescribeSecret(object):
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
    def describe_secret(client, secret_name, fetch_tags):
        request = kms_20160120_models.DescribeSecretRequest(
            secret_name=secret_name,
            fetch_tags=fetch_tags
        )
        return client.describe_secret(request)

    @staticmethod
    def main(args):
        # 请确保代码运行环境设置了环境变量 ALIBABA_CLOUD_ACCESS_KEY_ID 和 ALIBABA_CLOUD_ACCESS_KEY_SECRET。
        # 工程代码泄露可能会导致 AccessKey 泄露，并威胁账号下所有资源的安全性。以下代码示例使用环境变量获取 AccessKey 的方式进行调用，仅供参考，建议使用更安全的 STS 方式，更多鉴权访问方式请参见：https://help.aliyun.com/document_detail/378657.html
        open_api_config = DescribeSecret.create_open_api_config(os.getenv('ALIBABA_CLOUD_ACCESS_KEY_ID'), os.getenv('ALIBABA_CLOUD_ACCESS_KEY_SECRET'), 'your region id')
        client = DescribeSecret.create_client(open_api_config)
        secret_name = 'your secretName'
        fetch_tags = 'your fetchTags'
        DescribeSecret.describe_secret(client, secret_name, fetch_tags)
        


if __name__ == '__main__':
    DescribeSecret.main(sys.argv[1:])

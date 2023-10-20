# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import unicode_literals

import sys


from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_kms_kms20160120.client import Client as KmsSdkClient
from alibabacloud_kms20160120 import models as kms_20160120_models

import os

class GetRandomPassword(object):
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
    def get_random_password(client, exclude_punctuation, exclude_numbers, exclude_characters, exclude_lowercase, exclude_uppercase, password_length, require_each_included_type):
        request = kms_20160120_models.GetRandomPasswordRequest(
            exclude_punctuation=exclude_punctuation,
            exclude_numbers=exclude_numbers,
            exclude_characters=exclude_characters,
            exclude_lowercase=exclude_lowercase,
            exclude_uppercase=exclude_uppercase,
            password_length=password_length,
            require_each_included_type=require_each_included_type
        )
        return client.get_random_password(request)

    @staticmethod
    def main(args):
        # 请确保代码运行环境设置了环境变量 ALIBABA_CLOUD_ACCESS_KEY_ID 和 ALIBABA_CLOUD_ACCESS_KEY_SECRET。
        # 工程代码泄露可能会导致 AccessKey 泄露，并威胁账号下所有资源的安全性。以下代码示例使用环境变量获取 AccessKey 的方式进行调用，仅供参考，建议使用更安全的 STS 方式，更多鉴权访问方式请参见：https://help.aliyun.com/document_detail/378657.html
        open_api_config = GetRandomPassword.create_open_api_config(os.getenv('ALIBABA_CLOUD_ACCESS_KEY_ID'), os.getenv('ALIBABA_CLOUD_ACCESS_KEY_SECRET'), 'your region id')
        client = GetRandomPassword.create_client(open_api_config)
        exclude_punctuation = 'your excludePunctuation'
        exclude_numbers = 'your excludeNumbers'
        exclude_characters = 'your excludeCharacters'
        exclude_lowercase = 'your excludeLowercase'
        exclude_uppercase = 'your excludeUppercase'
        password_length = 'your passwordLength'
        require_each_included_type = 'your requireEachIncludedType'
        response = GetRandomPassword.get_random_password(client, exclude_punctuation, exclude_numbers, exclude_characters, exclude_lowercase, exclude_uppercase, password_length, require_each_included_type)
        print response


if __name__ == '__main__':
    GetRandomPassword.main(sys.argv[1:])

# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import unicode_literals

import sys


from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_kms_kms20160120.client import Client as KmsSdkClient
from alibabacloud_kms20160120 import models as kms_20160120_models
from alibabacloud_tea_util.client import Client as UtilClient

import os

class ImportKeyMaterial(object):
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
    def import_key_material(client, import_token, encrypted_key_material, key_id, key_material_expire_unix):
        request = kms_20160120_models.ImportKeyMaterialRequest(
            import_token=import_token,
            encrypted_key_material=encrypted_key_material,
            key_id=key_id,
            key_material_expire_unix=key_material_expire_unix
        )
        return client.import_key_material(request)

    @staticmethod
    def main(args):
        # 请确保代码运行环境设置了环境变量 ALIBABA_CLOUD_ACCESS_KEY_ID 和 ALIBABA_CLOUD_ACCESS_KEY_SECRET。
        # 工程代码泄露可能会导致 AccessKey 泄露，并威胁账号下所有资源的安全性。以下代码示例使用环境变量获取 AccessKey 的方式进行调用，仅供参考，建议使用更安全的 STS 方式，更多鉴权访问方式请参见：https://help.aliyun.com/document_detail/378657.html
        open_api_config = ImportKeyMaterial.create_open_api_config(os.getenv('ALIBABA_CLOUD_ACCESS_KEY_ID'), os.getenv('ALIBABA_CLOUD_ACCESS_KEY_SECRET'), 'your region id')
        client = ImportKeyMaterial.create_client(open_api_config)
        import_token = 'your importToken'
        encrypted_key_material = 'your encryptedKeyMaterial'
        key_id = 'your keyId'
        key_material_expire_unix = long(UtilClient.assert_as_string('your keyMaterialExpireUnix'))
        ImportKeyMaterial.import_key_material(client, import_token, encrypted_key_material, key_id, key_material_expire_unix)
        


if __name__ == '__main__':
    ImportKeyMaterial.main(sys.argv[1:])

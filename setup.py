# -*- coding: utf-8 -*-

import os
from setuptools import setup, find_packages

"""
setup module for alibabacloud-kms-python2-sdk.

Created on 12/09/2022

@author: Alibaba Cloud SDK
"""

packages = find_packages()
NAME = "alibabacloud-kms-python2-sdk"
DESCRIPTION = "Alibaba Cloud KMS Python2 SDK"
AUTHOR = "Alibaba Cloud SDK"
AUTHOR_EMAIL = "sdk-team@alibabacloud.com"
URL = "https://github.com/aliyun/alibabacloud-kms-python2-sdk"
VERSION = "1.1.0"
REQUIRES = [
    "alibabacloud_tea_openapi_py2>=0.1.6, <1.0.0",
    'alibabacloud-dkms-gcs-python2>=1.0.0',
    'alibabacloud_kms20160120_py2>=1.0.2,<2.0.0',
    "alibabacloud_openapi_util_py2>=0.1.1, <1.0.0",
    "alibabacloud_tea_util_py2>=0.0.9, <1.0.0",
    'requests'
]

LONG_DESCRIPTION = ''
if os.path.exists('./README.rst'):
    with open("./README.rst") as fp:
        LONG_DESCRIPTION = fp.read()

setup(
    name=NAME,
    version=VERSION,
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/x-rst",
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    license="Apache License 2.0",
    url=URL,
    keywords=["alibabacloud", "kms", "python2", "sdk"],
    packages=find_packages(exclude=["example*"]),
    include_package_data=True,
    platforms="any",
    install_requires=REQUIRES,
    classifiers=(
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Topic :: Software Development"
    )
)

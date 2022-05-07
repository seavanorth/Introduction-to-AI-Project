# -*- coding: utf-8 -*-

#!/usr/bin/env python
#coding=utf-8

from aliyunsdkcore.client import AcsClient
from aliyunsdkcore.acs_exception.exceptions import ClientException
from aliyunsdkcore.acs_exception.exceptions import ServerException
from aliyunsdkcore.auth.credentials import AccessKeyCredential
from aliyunsdkcore.auth.credentials import StsTokenCredential
from aliyunsdkimageenhan.request.v20190930.ExtendImageStyleRequest import ExtendImageStyleRequest

credentials = AccessKeyCredential('LTAI5tMRa1KCcmTsqcKaWt4F', 'MfGGQSZWEulEPxcPN9x7mXZjt4Oz5i')
# use STS Token
# credentials = StsTokenCredential('<your-access-key-id>', '<your-access-key-secret>', '<your-sts-token>')
client = AcsClient(region_id='cn-shanghai', credential=credentials)

request = ExtendImageStyleRequest()
request.set_accept_format('json')

response = client.do_action_with_exception(request)
# python2:  print(response) 
print(str(response, encoding='utf-8'))
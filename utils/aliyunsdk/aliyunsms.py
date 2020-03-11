# -*- coding:utf-8 -*-
__author__ = "leo"

import sys
from aliyunsdkdysmsapi.request.v20170525 import SendSmsRequest
from aliyunsdkdysmsapi.request.v20170525 import QuerySendDetailsRequest
from aliyunsdkcore.client import AcsClient
import uuid
from aliyunsdkcore.profile import region_provider
from aliyunsdkcore.http import method_type as MT
from aliyunsdkcore.http import format_type as FT
import json

ACCESS_KEY_ID = "LTAI5U4PiVykexVV"
ACCESS_KEY_SECRET = "7A4WVVaiUwxVKrpWSCwxXdoNiMJoQk"

REGION = "cn-hangzhou"
PRODUCT_NAME = "Dysmsapi"
DOMAIN = "dysmsapi.aliyuncs.com"

acs_client = AcsClient(ACCESS_KEY_ID, ACCESS_KEY_SECRET, REGION)
region_provider.add_endpoint(PRODUCT_NAME, REGION, DOMAIN)


def send_sms(phone_numbers, code):
    business_id = uuid.uuid1()
    sign_name = '小饭桌应用'
    template_code = 'SMS_68465012'
    template_param = json.dumps({"code": code})
    sms_request = SendSmsRequest.SendSmsRequest()
    # 申请的短信模板编码,必填
    sms_request.set_TemplateCode(template_code)
    # 短信模板变量参数
    if template_param is not None:
        sms_request.set_TemplateParam(template_param)
    # 设置业务请求流水号，必填。
    sms_request.set_OutId(business_id)
    # 短信签名
    sms_request.set_SignName(sign_name)
    # 短信发送的号码列表，必填。
    sms_request.set_PhoneNumbers(phone_numbers)
    # 调用短信发送接口，返回json
    sms_request = acs_client.do_action_with_exception(sms_request)
    return sms_request

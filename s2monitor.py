#-*- coding:utf-8 -*-
'''
--Struts2 VulnMonitor--
Created on 2017-9-8
Updated on 2017-11-21
Author: cahi1l1yn
Version:1.2
'''


import urllib2
import time
from aliyunsdkdysmsapi.request.v20170525 import SendSmsRequest
from aliyunsdkcore.client import AcsClient
import uuid
import logging
from fake_useragent import  UserAgent


url = 'https://cwiki.apache.org/confluence/display/WW/Security+Bulletins' #Struts2官方安全通告地址
i = 54 #漏洞编号：S2-0XX,每次手动运行前需修改为最新编号+1
REGION = "cn-hangzhou"
ACCESS_KEY_ID = ""#阿里云短信API_KEY
ACCESS_KEY_SECRET = ""#阿里云短信API_KEY
acs_client = AcsClient(ACCESS_KEY_ID, ACCESS_KEY_SECRET, REGION)


#日志文件配置
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s %(levelname)s %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    filename='monitor.log',
    filemode='a')


def send_sms(business_id, phone_number, sign_name, template_code):
    smsRequest = SendSmsRequest.SendSmsRequest()
    smsRequest.set_TemplateCode(template_code)
    smsRequest.set_OutId(business_id)
    smsRequest.set_SignName(sign_name);
    smsRequest.set_PhoneNumbers(phone_number)
    smsResponse = acs_client.do_action_with_exception(smsRequest)  #Send request
    return smsResponse


def monitor():
    global i
    key = 'S2-0' + str(i)
    ua = UserAgent()
    req = urllib2.Request(url)
    req.add_header('User-Agent',ua.random)
    try:
        response = urllib2.urlopen(req)
        html =response.read()
        r=html.find(key)
    except:
        logging.warning('urllib error,keep trying......')
        monitor()
    if r > -1:
        i +=1
        logging.info(key + ' existed!') 
        __business_id = uuid.uuid1()
        send_sms(__business_id, "phone_number", "TAG", "SMS_XXXXXX")
        time.sleep(7200) #监控频率
        monitor()
    else:
        logging.info(key + ' does not exist yet.')
        time.sleep(7200) #监控频率
        monitor()
      
if __name__ == '__main__':
    monitor()

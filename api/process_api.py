# -*- coding: utf-8 -*-
# @Time     : 2022-06-11 23:05
# Author    : yejq

'''
ETF2.0的流程模板模块
'''
import json

from api.etf_api import EtfApi
from utils.logger import logger


class Process(EtfApi):
    def add_process(self):
        url = self.BASE_URL + "/g/etfim-svr/v/tmplinsert"
        method = "POST"
        # headers = {
        #     "Content-Type": "application/json;charset = UTF-8",
        #     "Cookie": "token=77fbf344-1836-4954-af13-3a85beb4b1582"
        # }#请求头token通过登录接口封装到EtfApi类中了，此处无需定义header变量了。
        payload = {
            "operate_menu": "10",
            "login_operator": "11",
            "pcfProcess_in": [{"pcf_template_name": "1234",
                               "pcf_template_no": 0,
                               "pcf_template_type": "1",
                               "market_no": "1",
                               "process_no": 1,
                               "role_list": "",
                               "pcf_execute_type": "1",
                               "operator_code_list": "",
                               "send_sms_flag": "0",
                               "sms_recipients": "",
                               "sms_content": "",
                               "exec_order": 1},
                              {"pcf_template_name": "1234",
                               "pcf_template_no": 0,
                               "pcf_template_type": "1",
                               "market_no": "1",
                               "process_no": 2,
                               "role_list": "",
                               "pcf_execute_type": "2",
                               "operator_code_list": "",
                               "send_sms_flag": "0",
                               "sms_recipients": "",
                               "sms_content": "",
                               "exec_order": 2},
                              {"pcf_template_name": "1234",
                               "pcf_template_no": 0,
                               "pcf_template_type": "1",
                               "market_no": "1",
                               "process_no": 3,
                               "role_list": "",
                               "pcf_execute_type": "2",
                               "operator_code_list": "",
                               "send_sms_flag": "0",
                               "sms_recipients": "",
                               "sms_content": "",
                               "exec_order": 3},
                              {"pcf_template_name": "1234",
                               "pcf_template_no": 0,
                               "pcf_template_type": "1",
                               "market_no": "1",
                               "process_no": 5,
                               "role_list": "",
                               "pcf_execute_type": "2",
                               "operator_code_list": "",
                               "send_sms_flag": "0",
                               "sms_recipients": "",
                               "sms_content": "",
                               "exec_order": 4},
                              {"pcf_template_name": "1234",
                               "pcf_template_no": 0,
                               "pcf_template_type": "1",
                               "market_no": "1",
                               "process_no": 7,
                               "role_list": "",
                               "pcf_execute_type": "2",
                               "operator_code_list": "",
                               "send_sms_flag": "0",
                               "sms_recipients": "",
                               "sms_content": "",
                               "exec_order": 5},
                              {"pcf_template_name": "1234",
                               "pcf_template_no": 0,
                               "pcf_template_type": "1",
                               "market_no": "1",
                               "process_no": 29,
                               "role_list": "",
                               "pcf_execute_type": "1",
                               "operator_code_list": "",
                               "send_sms_flag": "0",
                               "sms_recipients": "",
                               "sms_content": "",
                               "exec_order": 6},
                              {"pcf_template_name": "1234",
                               "pcf_template_no": 0,
                               "pcf_template_type": "1",
                               "market_no": "1",
                               "process_no": 9,
                               "role_list": "",
                               "pcf_execute_type": "1",
                               "operator_code_list": "",
                               "send_sms_flag": "0",
                               "sms_recipients": "",
                               "sms_content": "",
                               "exec_order": 7}],
            "operator_no": "11"
        }

        r = self.etf_requests(url=url, method=method, json=payload)
        logger.debug(f"新增流程模板成功，响应信息为：{r.json()}")
        return r

    def processquery(self):
        url = f"/g/etfim-svr/v/processquery"
        method = "POST"
        payload = {
   "operate_menu":"10",
   "login_operator":"11",
   "market_no":"1",
   "pcf_template_type":"1",
   "pcf_template_no":74
}
        r = self.send(url=url, method=method, json=payload)
        logger.debug(f"查询流程模板成功，返回信息为：{r.text}")
        return r

    def modify_process(self):
        url = f"/g/etfim-svr/v/tmpl_modify"
        method = "POST"
        payload = {
   "operate_menu":"10",
   "login_operator":"11",
   "pcfProcess_in":[
      {
         "pcf_template_name":"3456",
         "pcf_template_no":74,
         "pcf_template_type":"1",
         "market_no":"1",
         "process_no":1,
         "role_list":"",
         "pcf_execute_type":"1",
         "operator_code_list":"",
         "send_sms_flag":"0",
         "sms_recipients":"",
         "sms_content":"",
         "exec_order":1
      },
      {
         "pcf_template_name":"3456",
         "pcf_template_no":74,
         "pcf_template_type":"1",
         "market_no":"1",
         "process_no":2,
         "role_list":"",
         "pcf_execute_type":"2",
         "operator_code_list":"",
         "send_sms_flag":"0",
         "sms_recipients":"",
         "sms_content":"",
         "exec_order":2
      },
      {
         "pcf_template_name":"3456",
         "pcf_template_no":74,
         "pcf_template_type":"1",
         "market_no":"1",
         "process_no":3,
         "role_list":"",
         "pcf_execute_type":"2",
         "operator_code_list":"",
         "send_sms_flag":"0",
         "sms_recipients":"",
         "sms_content":"",
         "exec_order":3
      },
      {
         "pcf_template_name":"3456",
         "pcf_template_no":74,
         "pcf_template_type":"1",
         "market_no":"1",
         "process_no":5,
         "role_list":"",
         "pcf_execute_type":"2",
         "operator_code_list":"",
         "send_sms_flag":"0",
         "sms_recipients":"",
         "sms_content":"",
         "exec_order":4
      },
      {
         "pcf_template_name":"3456",
         "pcf_template_no":74,
         "pcf_template_type":"1",
         "market_no":"1",
         "process_no":7,
         "role_list":"",
         "pcf_execute_type":"2",
         "operator_code_list":"",
         "send_sms_flag":"0",
         "sms_recipients":"",
         "sms_content":"",
         "exec_order":5
      },
      {
         "pcf_template_name":"3456",
         "pcf_template_no":74,
         "pcf_template_type":"1",
         "market_no":"1",
         "process_no":6,
         "role_list":"",
         "pcf_execute_type":"2",
         "operator_code_list":"",
         "send_sms_flag":"0",
         "sms_recipients":"",
         "sms_content":"",
         "exec_order":6
      },
      {
         "pcf_template_name":"3456",
         "pcf_template_no":74,
         "pcf_template_type":"1",
         "market_no":"1",
         "process_no":29,
         "role_list":"",
         "pcf_execute_type":"1",
         "operator_code_list":"",
         "send_sms_flag":"0",
         "sms_recipients":"",
         "sms_content":"",
         "exec_order":7
      },
      {
         "pcf_template_name":"3456",
         "pcf_template_no":74,
         "pcf_template_type":"1",
         "market_no":"1",
         "process_no":9,
         "role_list":"",
         "pcf_execute_type":"1",
         "operator_code_list":"",
         "send_sms_flag":"0",
         "sms_recipients":"",
         "sms_content":"",
         "exec_order":8
      }
   ],
   "operator_no":"11"
}
        r = self.send(url=url, method=method, json=payload)
        logger.debug(f"修改流程模板成功，返回信息为：{r.text}")
        return r

    def modify_process_nature(self):
        pass

    def tmpl_del(self):
        url = f"/g/etfim-svr/v/tmpl_del"
        method = "POST"
        payload = {
   "operate_menu":"10",
   "login_operator":"11",
   "pcf_template_no":74,
   "operator_no":"11"
}
        r = self.send(url=url, method=method, json=payload)
        logger.debug(f"删除流程模板成功列表，返回信息为：{r.text}")
        return r

    def tmpl_query(self):
        url = f"/g/etfim-svr/v/tmpl_query"
        method = "POST"
        payload = {
   "operate_menu":"10",
   "login_operator":"11",
   "market_no":0,
   "pcf_template_type":"0"
}
        r = self.send(url=url, method=method, json=payload)
        # r = self.etf_requests(url=url, method=method, json=payload)
        logger.debug(f"查询流程模板成功列表，返回信息为：{r.text}")
        return r


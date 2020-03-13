#!/usr/bin/env python
# -*- coding:utf-8 -*-

import requests
from common.Authorization import author

class http_config():
    def __init__(self):
        global timeout
        timeout = 2

        self.headers = {}
        self.cookie = {}
        self.params = {}
        self.data = {}
        self.url = None
        self.files = {}
        self.state = 0

    def set_url(self, url):
        """
        set url
        :param: interface url
        :return:
        """
        # self.url = scheme+url
        # self.url = self.url = scheme + '://' + host + ':' + port + '/' + url
        self.url = url

    def set_headers(self, header):
        """
        set headers
        :param header:
        :return:
        """
        self.headers = header

    def set_params(self, param):
        """
        set params
        :param param:
        :return:
        """
        self.params = param

    def set_data(self, data):
        """
        set data
        :param data:
        :return:
        """
        self.data = data

    def set_files(self, filename):
        """
        set upload files
        :param filename:
        :return:
        """
        if filename != '':
            file_path = 'F:/AppTest/Test/interfaceTest/testFile/img/' + filename
            self.files = {'file': open(file_path, 'rb')}

        if filename == '' or filename is None:
            self.state = 1

    def get(self):
        """
        defined get method
        :return:
        """
        print(self.params)
        try:
            response = requests.get(self.url, headers=self.headers, params=self.params, timeout=float(timeout),
                                    verify=False).text
            return response
        except TimeoutError:
            return None

    def getWithCookie(self):
        """
        defined get method
        :return:
        """

        print(self.params)
        try:
            ssrequest = requests.session()
            #requests.utils.add_dict_to_cookiejar(ssrequest.cookies, BCOOKIES)
            response = ssrequest.get(self.url, headers=self.headers, params=self.params, timeout=float(timeout),
                                     verify=False)
            # response.raise_for_status()
            return response
        except TimeoutError:
            return None

    def put(self):
        """
        defined get method
        :return:
        """
        try:
            response = requests.put(self.url, data=self.data, headers=self.headers, params=self.params,
                                    timeout=float(timeout))
            # response.raise_for_status()
            return response
        except TimeoutError:
            return None

    def patch(self):
        """
        defined get method
        :return:
        """
        try:
            response = requests.patch(self.url, data=self.data, headers=self.headers, params=self.params,
                                      timeout=float(timeout))
            # response.raise_for_status()
            return response
        except TimeoutError:
            return None

    def post(self):
        """
        defined post method
        :return:
        """
        try:
            response = requests.post(self.url, headers=self.headers, data=self.data,
                                     timeout=float(timeout)).text
            return response
        except TimeoutError:
            return None

        # defined http post method
        # include upload file

    def postWithFile(self):
        """
        defined post method
        :return:
        """
        try:
            response = requests.post(self.url, headers=self.headers, data=self.data, files=self.files,
                                     timeout=float(timeout))
            return response
        except TimeoutError:
            return None

    def postWithJson(self):
        """
        defined post method
        :return:
        """
        try:
            response = requests.post(self.url, headers=self.headers, json=self.data, timeout=float(timeout)).text
            return response
        except TimeoutError:
            return None

    def delete(self):
        try:
            response = requests.delete(self.url, timeout=float(timeout))
            return response
        except TimeoutError:
            return None
httpconfig = http_config()

if __name__ == '__main__':
    ht = http_config()
    url = "http://101.37.146.235:8085/v5.01/purchase/calculate/openapi/list"
    # data = {'word': "药"}
    print(author)
    header = {'content-type': "application/x-www-form-urlencoded",'Authorization':author}
    ht.set_url(url)
    ht.set_headers(header)
    # ht.set_params(data)
    print(ht.get())





"""
需要注意：
1.从excel中读取的数据是str，data、header等需要转化为dict
2.预期要酌情修改，目前预期没有写入excel，可自行写入excel。
"""
from common.Com import Common
from common.HttpConf import http_config
import unittest
import json
from ddt import ddt, data
from common.Authorization import get_Author


http_abstract = http_config()
gets_xls = Common()
getRequestInfo_xls = gets_xls.getXls(u"发票接口测试数据.xlsx", "addNew")


@ddt
class QueryInvoice(unittest.TestCase):


    @data(*getRequestInfo_xls)
    def test_query_invioce(self, data):
        self.url = data['url']
        self.data = data['数据']
        self.num = data[u'编号']
        self.method = data[u'方法']  #用来区分post、get、put
        self.expectation = data[u'预期']
        header = {"Content-Type": "application/json", "Authorization": get_Author()}
        http_abstract.set_headers(header)
        # print(type(header))
        http_abstract.set_url(self.url)

        self.data = json.loads(self.data)  # 将字符串转换成字典传参(从excel中读取的数据是str)
        # print("json.loads后的类型：", type(self.data))
        if self.method == 'post':
            http_abstract.set_data(self.data)
            resp = http_abstract.postWithJson()  #如果参数是严格json就需要postWithJson()
            resp_dic = json.loads(resp)  #把返回转化为dict
            gets_xls.writeCell(u"发票接口测试数据.xlsx", "addNew", resp, rowNo=int(self.num) + 1, colsNo=8)
            if self.expectation != '':
                self.assertIn(resp_dic["message"], self.expectation)

        elif self.method == "get":
            http_abstract.set_params(self.data)
            resp = http_abstract.get()
            resp_dic = json.loads(resp)
            gets_xls.writeCell(u"发票接口测试数据.xlsx", "addNew", resp, rowNo=int(self.num) + 1, colsNo=8)
            if self.expectation != '':
                self.assertIn(resp_dic["message"], self.expectation)




if __name__ == '__main__':
    m_sa = QueryInvoice()
    m_sa.test_query_invioce()

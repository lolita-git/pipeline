from common.HttpConf  import http_config
from common.Authorization import get_Author

if __name__ == '__main__':
    ht = http_config()
    url = "http://101.37.146.235:8085/v5.01/purchase/calculate/openapi/list"
    # data = {'word': "药"}
    author=get_Author()
    print(author)
    header = {'content-type': "application/x-www-form-urlencoded", 'Authorization': author}
    ht.set_url(url)
    ht.set_headers(header)
    # ht.set_params(data)
    print(ht.get())
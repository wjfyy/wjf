import requests,pprint,json
s = requests.Session()
host = "http://zhszyfb2020.szsmk.com"

url_path = "/app/coupon/takeByActivity"

url = host+url_path

body = {
    "recId":"2082",
    "smsCode":"000000",
    "thirdIfNeedSmsCode":1,
    "mobile":"13814027560"
}

res = s.post(url,json=body)
print(res.text)

# res =  test_takebyactivity(mobile='13918908452')
#
# assert res.json()["code"] == "000000"
# assert res.json()["message"] == "操作成功"
#
# if __name__ == "__main__":
#     pytest.main('-q takeByActivity.py')
import requests


def main():
    string = input("请输入要翻译的文本： ")
    data = {
        'i': string,
        'from': ' AUTO',
        'to': ' AUTO',
        'smartresult': 'dict',
        'client': 'fanyideskweb',
        'salt': '1543322298228',
        'sign': 'beb31c597e6235bbe0cc3e05f9bdf821',
        'doctype': 'json',
        'version': '2.1',
        'keyfrom': 'fanyi.web',
        'action': 'FY_BY_REALTIME',
        'typoResult': 'false',
    }
    res = requests.post(
        'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule', data)
    '''     res = requests.Response(
        'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule', data) '''
    translates = res.json()["translateResult"][0][0]['tgt']
    # "translateResult": [[{"tgt": "沟通", "src": "communication"}]]
    # "smartResult":{"entries":["","n. 通讯，[通信] 通信；交流；信函\r\n"]
    # words = res.text  # json()#["smartResult"]["entries"][1]
    print(translates)


if __name__ == "__main__":
    main()

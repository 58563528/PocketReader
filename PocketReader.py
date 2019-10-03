#-*- coding:utf-8 -*-
import requests
import json
import time
import sys
reload(sys)
sys.setdefaultencoding( "utf-8" )
if __name__ == "__main__":
    def TencentReader():
        url = "https://kdy.unisyou.net/yunpan/activity/doSign"
        head = {}
        head['User-Agent'] = 'Mozilla/5.0 (iPad; CPU OS 11_0 like Mac OS X) AppleWebKit/604.1.34 (KHTML, like Gecko) Version/11.0 Mobile/15A5341f Safari/604.1'
        head['Accept'] = "application/json, text/javascript, */*; q=0.01"
        head["Content-Type"] = "application/json"
        head["DNT"] = "1"
        head['Origin'] = "https://kdy.unisyou.net"
		#你自己的口袋阅链接（微信扫码得到的地址，https开头）
        head["Referer"] = "https://xxxxxxx"
        head["Sec-Fetch-Mode"] = "cors"
        head["X-Requested-With"] = "XMLHttpRequest"
		#自己的Request payload
        req = requests.post(url, data=json.dumps(
            {'userName': "自己注册的手机号", 'deviceNumber': "设备号", 'activityId': 'id号',
             'mobile': "iOSNaN --iPad"}), headers=head)
        postmsg = req.content.decode("utf-8")
        print(postmsg)
        translate_results = json.loads(postmsg)
        print(translate_results['resultData'])
        return translate_results['resultData']

    def SendWeChat():
        localtime = u"日期：" + time.strftime("%Y-%m-%d", time.localtime()) + u"时间：" + time.strftime("%H:%M:%S", time.localtime())
        print(u"本地时间为 :", localtime)
        #自己的Server酱key
        api = ""
        title = localtime + u"【口袋阅签到提醒】"
        content = u""""""
        data = {
            "text": title,
            "desp": content
        }
        print(data)
        req = requests.post(api, data=data)
    if(TencentReader() is None):
        print(u'已发送签到提醒')
        SendWeChat()

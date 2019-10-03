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
        head['User-Agent'] = 'Mozilla/5.0 (iPhone; CPU iPhone OS 12_1_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/16D57 MicroMessenger/7.0.3(0x17000321) NetType/WIFI Language/zh_CN'
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
             'mobile': "iOS11 --iPhone"}), headers=head)
        postmsg = req.content.decode("utf-8")
        print(postmsg)
        translate_results = json.loads(postmsg)
        print(translate_results['resultData'])
        return translate_results['resultData']

    def SendWeChat():
        Week = ['周日','周一','周二','周三','周四','周五','周六']
        localtime = time.strftime("%m", time.localtime()) + u"月" + time.strftime("%d", time.localtime()) + u"日"\
                    + Week[int(time.strftime("%w", time.localtime()))] + time.strftime("%H", time.localtime()) + u'时' + time.strftime("%M", time.localtime()) + u'分'
        print(u"Debug：\n本地时间为 :", localtime)
        #自己的Server酱key
        api = "SCU2141T2aa93a5d22cd093b32882b6e53beb38c57dd351715323"
        title =  u"口袋阅签到提醒_" + localtime
        content = ""
        payload = {
            'text': title,
            'desp': content
        }
        print(payload)
        url = 'https://sc.ftqq.com/{}.send'.format(api)
        requests.post(url, params=payload)
    if(TencentReader() is None):
        print(u'已发送签到提醒')
        SendWeChat()


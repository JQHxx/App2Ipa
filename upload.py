#coding=utf-8
import os
import requests
from requests_toolbelt import MultipartEncoder, MultipartEncoderMonitor
import requests

def processUpload(ipapath):
    #置换成自己的key,在蒲公英的控制台可以看到
    apikey = '5f451157610773e185c0dad86d8d0009'
    file = {'file': open(ipapath, 'rb')}
    # 安装类型，密码安装
    buildInstallType = '2'
    buildPassword = '123456'
    def my_callback(monitor):
        # Your callback function
        res = "当前进入：%s" % str(monitor.bytes_read / os.path.getsize(ipapath) *100)[:5] + "%"
        print(res)

    e = MultipartEncoder(
        fields={'_api_key': apikey, 'enctype': 'multipart/form-data', 'buildInstallType': buildInstallType, 'buildPassword': buildPassword,'file': ('filename.ipa', open(ipapath, 'rb'), 'text/plain')}
        )
    m = MultipartEncoderMonitor(e, my_callback)

    r = requests.post('https://www.pgyer.com/apiv2/app/upload', data=m,
                      headers={'Content-Type': m.content_type})
    return r

def upload(type):
    ipaDir = r'/Users/ofweek/Desktop/sh/'
    ipapath = ipaDir + 'devOFweekPhone.ipa'
    if type=="dev":
        ipapath = ipaDir + 'devOFweekPhone.ipa'
    elif type == 'yufabu':
        ipapath = ipaDir + 'ydevOFweekPhone.ipa'
    else:
        ipapath = ipaDir + 'disOFweekPhone.ipa'

    res = ''
    if os.path.exists(ipapath):
        print("正在上传中请稍后...")
        
        r = processUpload(ipapath)
        print(r.text)
        if r.status_code==200:
            print("上传成功，二维码地址是：")
            print('https://www.pgyer.com/U6eU')
            res = 'https://www.pgyer.com/U6eU'
        else:
            res = "生成失败"
    else:
        os.system("open .")
        print("文件不存在")
        res = "生成失败"
    return res
if __name__ == "__main__":
    upload('dev')

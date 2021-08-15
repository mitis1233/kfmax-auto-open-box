import requests, json, os
from time import sleep

def Post_Run(LogCount,LogcCookie):
    URL="https://bbs.kfmax.com/kf_fw_ig_mybpdt.php"
    header={
        'referer': 'https://bbs.kfmax.com/kf_fw_ig_mybp.php',
        'origin':'https://bbs.kfmax.com',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36',
        "cookie": ""
        }
    web_data={
        'do': '3',
        'id': '4',
        'safeid': 'cd602ec'
        }
    count=LogCount #次數
    if LogcCookie != "": #是否更新cookie
        header['cookie']=LogcCookie
    i=0
    while i < count:
        try:
            i+=1
            print(f"第{i}次:")
            web_re=requests.post(URL,headers=header,data=web_data) #post data
            print(web_re.text)
            sleep(0.4)
        except Exception as error:
            print('!錯誤: ',error)
            sleep(0.4)

LogCount=int(input('輸入次數: '))
LogcCookie=input('輸入Cookie(沒輸入為不更新): ')
Post_Run(LogCount,LogcCookie)
os.system("pause")
import requests, json, os, re
from time import sleep

def Post_Run(LogCount,LogcCookie):
    header={
        'referer': 'https://bbs.kfmax.com/kf_fw_ig_mybp.php',
        'origin':'https://bbs.kfmax.com',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36',
        "cookie": ""
        }
    web_data={
        'do': '3',
        'id': '4',
        'safeid': ''
        }
    count=LogCount #次數
    if LogcCookie != "": #是否更新cookie
        header['cookie']=LogcCookie
    #get id
    URL="https://bbs.kfmax.com/kf_fw_ig_mybp.php"
    web_re=requests.get(URL,headers=header)
    web_re=re.search(r'safeid=\w+',web_re.text)[0]
    web_data['safeid']=re.sub('safeid=', '', web_re)
    
    #跑開箱
    URL="https://bbs.kfmax.com/kf_fw_ig_mybpdt.php"
    i=0
    while i < count:
        try:
            i+=1
            web_re=requests.post(URL,headers=header,data=web_data) #post data
            web_re=web_re.text
            print(f"第{i}次: {web_re}")
            if web_re=="盒子不足，请刷新查看最新数目。":
                break
            sleep(0.4)
        except Exception as error:
            print('!錯誤: ',error)
            sleep(0.4)



def Buy_Run(LogcCookie):
    header={
        'referer': 'https://bbs.kfmax.com/kf_fw_ig_mybp.php',
        'origin':'https://bbs.kfmax.com',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36',
        "cookie": ""
        }
    count=3 #次數
    if LogcCookie != "": #是否更新cookie
        header['cookie']=LogcCookie
    #get id
    URL="https://bbs.kfmax.com/kf_fw_ig_mybp.php"
    web_re=requests.get(URL,headers=header)
    web_re=re.search(r'safeid=\w+',web_re.text)[0]
    safeid =re.sub('safeid=', '', web_re)
    
    #跑buy
    URL="https://bbs.kfmax.com/kf_fw_ig_halo.php?do=buy&id=2&safeid="+safeid
    i=0
    while i < count:
        try:
            i+=1
            web_re=requests.post(URL,headers=header) #post data
            web_re=web_re.text
            #判斷是否提升數值
            web_re_ans='提升了光环的效果'
            if re.search(r'未超过光环效果',web_re):
                web_re_ans='未超过光环效果'
            elif re.search(r'你还需要等待',web_re):
                print('战力光环冷卻中.. 直接結束\n')
                break
            web_re_number=re.search(r'\[[%\w\.]+\]',web_re)[0] #數值

            print(f"第{i}次: 數值{web_re_number} {web_re_ans}")
            sleep(0.4)
        except Exception as error:
            print('!錯誤: ',error)
            sleep(0.4)

LogCount=int(input('輸入次數: '))
LogcCookie=input('輸入Cookie(沒輸入為不更新): ')
Post_Run(LogCount,LogcCookie)
Buy_Run(LogcCookie)
os.system("pause")

from time import sleep
from selenium.common.exceptions import SessionNotCreatedException
from utils import load_json, login_and_check_in, send_email
from utils.utils import updateChromeDriver
import random

if __name__ == '__main__':
    # 在八点零六分到九点打卡都可以
    sleep(random.uniform(365, 1800))
    # 1. 导入用户信息
    flag = True
    while flag == True:
        try:
            json_path = './userinfo.json'
            param_data = load_json(json_path)
            for i in range(len(param_data['user_account'])):
                username = param_data['user_account'][i]['username']
                password = param_data['user_account'][i]['password']
                # 2. 对用户进行打卡
                login_and_check_in(username, password)

            flag = False
            sleep(random.uniform(180, 900))
        
        except SessionNotCreatedException:
            # 模拟器的谷歌浏览器版本自动下载更新
            # 填写你的chromedriver.exe保存的本地地址，win系统地址记得别写'\'，改成'/'
            extract_path = None
            updateChromeDriver(extract_path)


    # 3. 发送邮件确认打卡成功
    # send_email()

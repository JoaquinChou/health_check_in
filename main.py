from time import sleep
from utils import load_json, login_and_check_in, send_email
import random

if __name__ == '__main__':
    # 在八点零六分到九点打卡都可以
    sleep(random.uniform(365, 1800))
    # 1. 导入用户信息
    json_path = './userinfo.json'
    param_data = load_json(json_path)
    for i in range(len(param_data['user_account'])):
        username = param_data['user_account'][i]['username']
        password = param_data['user_account'][i]['password']
        # 2. 对用户进行打卡
        login_and_check_in(username, password)
    sleep(random.uniform(180, 900))
    # 3. 发送邮件确认打卡成功
    # send_email()

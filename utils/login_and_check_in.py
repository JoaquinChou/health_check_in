from selenium.common.exceptions import NoSuchElementException
from selenium import webdriver
from time import sleep
import random


def login_and_check_in(username, password):
    # 1.打开浏览器窗口
    sleep(random.uniform(2, 3))
    driver = webdriver.Chrome()

    # 休眠3-4s
    sleep(random.uniform(3, 4))
    driver.get('https://ids.xmu.edu.cn/authserver/login?service=https://xmuxg.xmu.edu.cn/login/cas/xmu')

    # 2.清空用户名框和密码框
    now_handle = driver.current_window_handle
    driver.switch_to.window(now_handle)
    sleep(random.uniform(3, 5))
    driver.find_element_by_id("username").clear()
    driver.find_element_by_id("password").clear()

    # 3. 设置用户信息
    sleep(random.uniform(7, 13))
    driver.find_element_by_id("username").send_keys(username)
    driver.find_element_by_id("password").send_keys(password)

    # 4.登陆
    sleep(random.uniform(1, 3))
    # 该处需要结合具体的网页填写css_selector
    driver.find_element_by_css_selector("[type='submit']").click()

    # 5. 登录每日健康打卡
    # print(driver.window_handles)
    flag = True
    while flag == True:
        try:
            # 该处需要结合具体的网页填写x_path
            # element1 = driver.find_element_by_xpath("//*[@id='mainPage-page']/div[1]/div[3]/div[2]/div[2]/div[3]/div/div[3]")
            # driver.execute_script("arguments[0].click();", element1)
            driver.find_element_by_xpath("//*[contains(text(), 'Daily Health Report 健康打卡')]").click()
            # driver.find_element_by_link_text("Daily Health Report 健康打卡").click()
            # print(driver.window_handles)
            flag = False
        except NoSuchElementException:
            driver.refresh()
            sleep(random.uniform(2, 3))

    # selenium执行时并不会自动切换到新开的页签或者窗口上，
    # 还会停留在之前的窗口中，所以两次打印的句柄都一样。
    # 新开窗口后必须通过脚本来进行句柄切换，才能正确操作相应窗口中的元素。

    # 6. 获得当前最新窗口
    # 注意添加休眠时间,否则窗口无法及时获得句柄
    sleep(random.uniform(1, 3))
    # print(driver.window_handles)
    driver.switch_to.window(driver.window_handles[1])

    # 7. 点击"我的表单"
    flag = True
    while flag == True:
        try:
            driver.find_element_by_css_selector("[class='tab']").click()
            flag = False
        except NoSuchElementException:
            driver.refresh()
            sleep(random.uniform(2, 3))
        
     

    # 8. 将进度条拖到底部，10000足够大，代表拖到底部。
    sleep(random.uniform(2, 4))
    js = "var q=document.documentElement.scrollTop=10000"
    driver.execute_script(js)

    # 9. 点击"其他"
    sleep(random.uniform(1, 3))
    # 该处需要结合具体的网页填写x_path
    driver.find_element_by_xpath('//*[@id="select_1582538939790"]/div/div').click()

    # 10. 点击"是"
    sleep(random.uniform(1, 2))
    # print("++++++++4", driver.window_handles)
    # 该处需要结合具体的网页填写css_selector
    driver.find_element_by_css_selector("[class='dropdown-items']").click()

    # 11. 点击保存
    sleep(random.uniform(1, 3))
    # 该处需要结合具体的网页填写css_selector
    driver.find_element_by_css_selector("[class^='form-save']").click()

    # 12. 对浏览器的弹窗进行"确认"处理
    # 新方法，切换alert
    dialog = driver.switch_to.alert
    # a = driver.switch_to_alert()   #  老方法，切换alert
    # 获取弹窗上的文本
    # print(dialog.text)

    # 确认，相当于点击[确定]按钮
    sleep(random.uniform(2, 4))
    dialog.accept()
    # 取消，相当于点击[取消]按钮
    # a.dismiss()

    # 13. 任务完成，关闭所有的浏览器
    sleep(random.uniform(3, 20))
    driver.quit()

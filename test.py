'''
dfrom selenium import webdriver
import time driver  = webdriver.Chrome()
def openDribe():
    driver.get("http://www.baidu.com")
    driver.maximize_window()

==================================================
browser.curren_url : 获取当前加载页面的 URL
browser.close() : 关闭当前窗口, 如果当前窗口是最后一个窗口, 浏览器将关闭
browser.quit() : 关闭所有窗口并停止 ChromeDriver 的执行
browser.add_cookie(cookie_dict) : 为当前会话添加 cookie
browser.get_cookie(name) : 得到执行 cookie
browser.get_cookies() : 得到所有的 cookie

driver.add_cookie({‘name’ : ‘foo’, ‘value’ : ‘bar’}) driver.add_cookie({‘name’ : ‘foo’, ‘value’ : ‘bar’, ‘path’ : ‘/’}) driver.add_cookie({‘name’ : ‘foo’, ‘value’ : ‘bar’, ‘path’ : ‘/’, ‘secure’:True})
browser.delete_all_cookies() : 删除当前会话的所有cookie
browser.delete_cookie(name) : 删除指定 cookie

browser.back() : 相当于浏览器的后退历史记录
browser.forward() : 相当于浏览器的前进历史记录
browser.execute_script(script, *args) : 同步执行 js 脚本
browser.execute_async_script(script, *args) : 异步执行 js 脚本
browser.get(url) : 在当前窗口加载 url
browser.refresh() : 刷新当前页面
browser.current_window_handle : 当前窗口的 handle， 相当于一个指针一样的东西, 用来指向当前窗口
browser.window_handles : 当前浏览器中的已经打开的所有窗口, 是一个 list
browser.switch_to_window(window_handle) : 切换 window_handle 指向的窗口
browser.title : 当前页面的 title
browser.name : 当前浏览器的名字


==================================================
from selenium import webdriver
import os
import time

# set little time stop and big time stop for viewing changes
little_time_stop = 1
big_time_stop = 2
# 默认广告条数
ads_num_require = 8
# 请求连接
req_url = "http://www.haosou.com/s?ie=utf-8&shb=1&src=360sou_newhome&q=%E9%B2%9C%E8%8A%B1"
# 打开浏览器
browser = webdriver.Chrome()
# 开始请求
browser.get(req_url)
# 获取所有的广告

all_ads_li = browser.find_elements_by_css_selector('#e_idea_pp li')
# 当前广告条数
ads_num_current = len(all_ads_li)
print ("Has been got %d ads" %(ads_num_current))
# 如果广告条数与默认不符
if ads_num_current < ads_num_require:
    print ("The number of ads is not enough ( current : %d require: %d)" %(ads_num_current,ads_num_require))
    # exit()
# 获取顶部连接
i = 0
for ads_li in all_ads_li:
    time.sleep(big_time_stop)
    i = i+1
    print ("ads %d :" %i)
    print (type(ads_li))
    try:
        main = ads_li.find_element_by_css_selector('h3 a')
    except:
        print ("\tError: ads %d cann't find" %(i))
    else:
        print ("\tReady: visit ads %d" %(i))
        main.click()
        print ("\tSucess: visit ads %d" %(i))
        time.sleep(little_time_stop)
    try:
        img_link = ads_li.find_element_by_class_name('e_biyi_img')
    except:
        print ("\tError : no img in ads %d " %(i))
    else:
        print ("\tReady : visit img_link %d" %(i))
        img_link.click()
        print ("\tSuccess : visit img_link %d" %(i))
        time.sleep(little_time_stop)
    try:
        child_div = ads_li.find_element_by_class_name('e_biyi_childLink');
    except:
        print ("\tError : no child link in ads %d" %(i))
    else:
        try:
            child_links = child_div.find_elements_by_css_selector('a')
        except:
            print ("\tError : find child_links error")
        else:
            num_links = len(child_links)
            print ("\tSuccess : there are %d child_links" %(num_links))
            j = 0
            for child_a in child_links:
                j = j + 1
                print ("\t\tReady : visit child link %d in ads %d" %(j, i))
                child_a.click()
                print ("\t\tSuccess : visit child link %d in ads %d" %(j, i))
                time.sleep(little_time_stop)
print ("End and thanks for your using!")


html = "http://192.168.1.43:8010/jxrd/system.do?method=login&init=true"

html_req = requests.get(html)

#====网页源码===
html_req_txt = html_req.text

sleep(3)

# 下面代码选择取消注释
# 延时
# time.sleep(5)
# 关闭当前窗口
# browser.close()
# 关闭所有已经打开的窗口
# browser.quit()
#http://192.168.1.43:8010/jxrd/system.do?method=login&init=true

# #=====输入事件======、
# key_input = drive.find_element_by_xpath('//*[@id="kw"]')
# key_input.send_keys("bloom")
    # sleep(2)
# #=====鼠标点击事件======、
# single_click = drive.find_element_by_xpath('//*[@id="su"]')
# single_click.click()
# sleep(2)
# #=====鼠标双击事件======
# double = drive.find_element_by_xpath('//*[@id="kw"]')
# ActionChains(drive).double_click(double).perform()
# sleep(2)
#
# #=====模拟鼠标移动到元素=======
# above = drive.find_element_by_xpath('//*[@id="su"]')
# ActionChains(drive).move_to_element(above).perform()
#
#
# #=========按下========
# left = drive.find_element_by_xpath('//*[@id="su"]')
# ActionChains(drive).click_and_hold(left).perform()
# sleep(4)

# #=======鼠标右击事件=========
# right = drive.find_element_by_xpath('//*[@id="su"]')
# ActionChains(drive).context_click(right).perform()
# # print ("设置浏览器高宽：480,800 ")
# # drive.set_window_size(480,800)
# # sleep(2)

'''
#coding=utf-8
#-*- coding:utf-8 -*-

# from selenium import webdriver
# from time import  sleep
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.common.action_chains import ActionChains
# from selenium.webdriver.common.alert import Alert
# import os
# drive.get("http:/www.baidu.com")
# print ("浏览器最大化")
# drive.maximize_window()
# text = drive.find_element_by_id("kw").is_displayed()
# print (text)
#===== 键盘事件======

#输入内容
# drive.find_element_by_id("kw").send_keys("selenium")
# sleep(3)
#删除多输入的一个m
# drive.find_element_by_id("kw").send_keys(Keys.BACK_SPACE)
# sleep(3)
#输入空格键+"教程"
# drive.find_element_by_id("kw").send_keys(Keys.SPACE)
# drive.find_element_by_id("kw").send_keys("教程")
# sleep(3)
#ctrl+a 全选输入内容
# # drive.find_element_by_id("kw").send_keys(Keys.CONTROL,'a')
# # sleep(3)
# #ctrl+x 剪切输入内容
# drive.find_element_by_id("kw").send_keys(Keys.CONTROL,'x')
# sleep(3)
#获得title
# title = drive.title
# print (title)
# #获取url
# html_url = drive.current_url
# print (html_url)

#=======================
# print ("设置baidu首页")
# first_url = "http://www.baidu.com"
# print ("now access %s" %first_url)
# drive.get(first_url)
# second_url = 'http://news.baidu.com'
# print ("now access %s" %second_url)
# drive.get(second_url)
# sleep(2)
# #后退与前进网页
# print ('back to %s' %first_url)
# drive.back()
# sleep(2)
# print ('forward to %s' %second_url)
# drive.forward()
# sleep(2)
# sleep(10)

# first_url = "http://www.runoob.com/try/try.php?filename=jqueryui-api-droppable"
# drive.get(first_url)
# #=====鼠标拖拽事件=======
# #先切换到目标所在的frame
# drive.switch_to.frame("iframeResult")
# #确定拖拽启点
# soure = drive.find_element_by_id("draggable")
# #确定拖拽终点
# target = drive.find_element_by_id("droppable")
# ActionChains(drive).drag_and_drop(soure,target).perform()
#==================================================
#定位到页面弹窗
# t = drive.switch_to.alert
# print (t.text)
# #关闭弹窗
# t.accept()

#==========勾选浏览器复选框===========
# drive = webdriver.Chrome()
# file_url = 'file:///'+os.path.abspath('checkbox.html')
# drive.get(file_url)
# checkboxes = drive.find_elements_by_css_selector('input[type=checkbox]')
# for checkboxe in checkboxes:
#     checkboxe.click()
#
# print (len(drive.find_elements_by_css_selector('input[type=checkbox]')))
# drive.find_elements_by_css_selector('input[type=checkbox]').pop().click()
#==============================================
# inputs = drive.find_element_by_tag_name('input')
#
# for input in inputs:
#     if input.get_attribute('type') == 'checkbox':
#         input.click()
#
#==============百度登录============================================

# baidu_url = "http://www.baidu.com"
# driver  = webdriver.Chrome()
# driver.get(baidu_url)
# #=============点击登录链接======================
# driver.find_element_by_xpath('//*[@id="u1"]/a[7]').click()
# print (driver.current_url)
#
# sleep(3)

#通过二次定位找到用户名输入框
# driver.find_element_by_class_name("tang-pass-footerBar").find_element_by_id("TANGRAM__PSP_10__footerULoginBtn").click()



# driver.find_element_by_css_selector("#TANGRAM__PSP_10__footerULoginBtn")
# div = driver.find_element_by_class_name("pass-login-pop-form").find_element_by_name("tang-pass-footerBarULogin pass-link")
# div.click()
# sleep(2)
#
# driver.quit()
# div=driver.find_element_by_class_name("tang-content").find_element_by_name("userName")
# div.send_keys("username")
# #输入登录密码
# driver.find_element_by_name("password").send_keys("password")
# #点击登录
# driver.find_element_by_id("TANGRAM__PSP_10__submit").click()
# a=347.91+705.26+176.81
# b=3.19+100+96+68.83+1.99
# c=200
# print (a)
# print(a-b)
import smtplib
from email.mime.text import MIMEText
from email.header import Header
#发送邮箱
sender = 'a'
#接收邮箱
receiver ='b'
#发送邮件主题
subject = 'python email test'
#发送邮箱服务器
smtpserver = 'smtp.126.com'
#发送邮箱用户/密码
username = 'name'
password = 'pwd'
#中文需参数‘utf-8’，单字节字符不需要
msg =MIMEText('hello pytthon','text','uft-8')
msg ['Subject'] = Header(subject,'utf-8')
smtp = smtplib.SMTP()
smtp.connect('smtp.126.com')
smtp.login(username,password)
smtp.sendmail(sender,receiver,msg.as_string())
smtp.quit()

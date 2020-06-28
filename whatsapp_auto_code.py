# Python code for whatsapp automation

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get('https://web.whatsapp.com/')

name = input('Enter the name of user or group : ')
msg = input('Enter your message : ')
count = int(input('Enter the count : '))

input('Enter anything after scanning QR code')

user = driver.find_element_by_xpath('//span[@title = "{}"]'.format(name))
user.click()

msg_box = driver.find_element_by_class_name('_39LWd')
#msg_box.click()
#msg_box.clear()
msg_box.send_keys(Keys.CONTROL, 'a')
msg_box.send_keys('Hi')
button = driver.find_element_by_class_name('_35EW6')
button.click()




###
#for i in range(count):
#    msg_box.send_keys(msg)
#    button = driver.find_element_by_class_name('_35EW6')
#    button.click()

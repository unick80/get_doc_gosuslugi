from selenium import webdriver
from time import sleep
import os

def main():
    login = input("Введите логин: ")
    password = input("Введите пароль: ")
    driver = webdriver.Chrome()
    driver.get("https://gosuslugi.ru")
    sleep(5)
    btn_lk = driver.find_element_by_class_name("lk-enter")
    btn_lk.click()
    sleep(5)
    input_login = driver.find_element_by_id("login")
    input_login.send_keys(login)
    input_pass = driver.find_element_by_id("password")
    input_pass.send_keys(password)
    btn_login = driver.find_element_by_id("loginByPwdButton")
    btn_login.click()
    sleep(5)
    btn_chl = driver.find_elements_by_class_name("role")
    print(len(btn_chl))
    if len(btn_chl) > 0:
        btn_chl[0].click()
    sleep(5)
    btn_avatar = driver.find_element_by_class_name("avatar-n-location-container")
    btn_avatar.click()
    sleep(5)
    icon_doc = driver.find_element_by_class_name("doc")
    icon_doc.click()
    sleep(5)
    doc_class = driver.find_element_by_class_name('content')
    path = "doc"
    if os.path.isdir(path) == False:
        os.mkdir(path)
    doc = open(path+"\doc.txt", "w+")
    doc.write(doc_class.text)
    doc.close()
    print("Файл записан.")



if __name__ == '__main__':
    main()


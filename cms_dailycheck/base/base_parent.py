# -*- coding: utf-8 -*-

from selenium import webdriver
from selenium.webdriver.common.by import By

from cms_dailycheck.utils import basic_utils
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class BaseParent():

    def __init__(self):
        self.basic_utils_obj = basic_utils.BasicUtils()
        # 获取路径
        self.parent_dir = self.basic_utils_obj.get_parent_dir()
        self.iniPath = self.parent_dir + "\\config\\global_config.ini"

        chrome_driver = self.basic_utils_obj.get_config_value(self.iniPath, "global", "driverPath")  # https://blog.csdn.net/qq_26200629/article/details/86141131
        self.driver = webdriver.Chrome(executable_path=chrome_driver)
        self.driver.implicitly_wait(30)
        self.verificationErrors = []
        self.accept_next_alert = True

    # 用例前的准备工作
    def setup(self):
        basic_utils_obj = basic_utils.BasicUtils()
        # 获取路径
        parentDir = basic_utils_obj.get_parent_dir()
        iniPath = parentDir + "\\config\\global_config.ini"

        driver = self.driver
        self.base_url = basic_utils_obj.get_config_value(iniPath,"global", "baseUrl")    # 域名
        driver.get(self.base_url + basic_utils_obj.get_config_value(iniPath,"global", "loginPath"))    #跳转登录页面
        driver.find_element_by_id(basic_utils_obj.get_config_value(iniPath,"login", "usernameId")).clear()
        driver.find_element_by_id(basic_utils_obj.get_config_value(iniPath,"login", "usernameId")).send_keys(basic_utils_obj.get_config_value(iniPath,"login", "usernameValue"))
        driver.find_element_by_id(basic_utils_obj.get_config_value(iniPath,"login", "pwdId")).clear()
        driver.find_element_by_id(basic_utils_obj.get_config_value(iniPath,"login", "pwdId")).send_keys(basic_utils_obj.get_config_value(iniPath,"login", "pwdValue"))
        driver.find_element_by_id(basic_utils_obj.get_config_value(iniPath,"login", "loginbtnId")).click()

    # 用例后的清零工作
    def teardown(self):
        self.driver.quit()  # 退出浏览器

    def get_driver(self):
        return self.driver

    # 封装 find_element_by_id方法
    def find_by_id(self, id):
        return self.driver.find_element_by_id(id)

    # 封装 find_element_by_xpath方法
    def find_by_xpath(self, xpath):
        return self.driver.find_element_by_xpath(xpath)

    # 封装 find_element_by_partial_link_text 方法
    def find_by_partial_text(self, text):
        return self.driver.find_element_by_partial_link_text(text)

    def find_by_tag_name(self, tag_name):
        return self.driver.find_element_by_tag_name(tag_name)

    def get_driver_and_inipath(self, keyword):
        basic_utils_obj = basic_utils.BasicUtils()
        parentDir = basic_utils_obj.get_parent_dir()
        iniPath = parentDir + "\\config\\" + keyword + "_config.ini"
        return self.driver, iniPath

    def wait_until_element_precence(self,driver, location_method, location_value, timeout=10):
        wait = WebDriverWait(driver, timeout)
        if location_method == "id":
            element = wait.until(EC.element_to_be_clickable((By.ID, location_value)))
        elif location_method == "xpath":
            element = wait.until(EC.element_to_be_clickable((By.XPATH, location_value)))
        elif location_method == "css":
            element = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, location_value)))
        return element


# 测试用
if __name__ == '__main__':
    test_obj = BaseParent()
    test_obj.setUp()
    test_obj.tearDown()


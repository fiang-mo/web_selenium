from selenium import webdriver
from pages.students_infos_page import StudentsInfosPage
import pytest
import allure
from setting import basepath
import os
from common.read_yaml import read_yaml_data

# 测试数据
# test_data = [("中文", True),("English", True),("123456", True)]

yamlpath = os.path.join(basepath, "testdatas", "test_cases.yml")
print("读取到yaml文件地址：%s" %yamlpath)
d = read_yaml_data(yamlpath)
test_data = d.get('test_add_params', [])
print("测试数据：%s" %test_data)

@allure.feature("添加文章分类")
class TestStuinfo():
    @allure.testcase("http://49.235.92.12:8080/zentao/testcase-view-6-2.html")
    @pytest.mark.parametrize("test_input, expected", test_data)
    def test_add_studentinfo_1(self, login, test_input, expected):
        driver = login
        add_studentinfo = StudentsInfosPage(driver)
        with allure.step("step1:点击页面左侧的学生表按钮"):
            add_studentinfo.click_xueshengbiao()
        with allure.step("step2:点击添加学生信息按钮"):
            add_studentinfo.click_add_xueshenginfo()
        with allure.step("step3:输入学号"):
            add_studentinfo.input_xuehao(test_input["xuehao"])
        with allure.step("step3:输入姓名"):
            add_studentinfo.input_name(test_input["name"])
        with allure.step("step3:输入年龄"):
            add_studentinfo.input_age(test_input["age"])
        with allure.step("step3:输入分数"):
            add_studentinfo.input_score(test_input["score"])
        with allure.step("step4:点击保存按钮"):
            add_studentinfo.save_button()
        with allure.step("step5:获取实际结果"):
            result = add_studentinfo.is_add_success(expect="添加成功")
        #断言
        assert result == expected, "断言失败，原因："



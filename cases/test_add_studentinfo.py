from selenium import webdriver
from pages.students_infos_page import StudentsInfosPage
import pytest
import allure

@allure.feature("添加文章分类")
class TestAddstu():

    @allure.testcase("http://49.235.92.12:8080/zentao/testcase-view-6-2.html")
    @allure.title("所有入参字段都按规定长度填写，编辑成功")
    def test_add_studentinfo_1(self, login):
        driver = login
        add_studentinfo = StudentsInfosPage(driver)
        with allure.step("step1:点击页面左侧的学生表按钮"):
            add_studentinfo.click_xueshengbiao()
        with allure.step("step2:点击添加学生信息按钮"):
            add_studentinfo.click_add_xueshenginfo()
        with allure.step("step3:输入学号"):
            add_studentinfo.input_xuehao("654565")
        with allure.step("step3:输入姓名"):
            add_studentinfo.input_name("小明")
        with allure.step("step3:输入年龄"):
            add_studentinfo.input_age("19")
        with allure.step("step3:输入分数"):
            add_studentinfo.input_score("55")
        with allure.step("step4:点击保存按钮"):
            add_studentinfo.save_button()
        with allure.step("step5:获取实际结果"):
            result = add_studentinfo.is_add_success(expect="添加成功")
        #断言
        assert result

    @allure.testcase("http://49.235.92.12:8080/zentao/testcase-view-3-1.html")
    @allure.title("只输入学号和姓名，编辑成功")
    def test_add_studentinfo_2(self, login):
        driver = login
        add_studentinfo = StudentsInfosPage(driver)
        with allure.step("step1:点击页面左侧的学生表按钮"):
            add_studentinfo.click_xueshengbiao()
        with allure.step("step2:点击添加学生信息按钮"):
            add_studentinfo.click_add_xueshenginfo()
        with allure.step("step3:输入学号"):
            add_studentinfo.input_xuehao("12345")
        with allure.step("step3:输入姓名"):
            add_studentinfo.input_name("小明")
        with allure.step("step4:点击保存按钮"):
            add_studentinfo.save_button()
        with allure.step("step5:获取实际结果"):
            result = add_studentinfo.is_add_success(expect="添加成功")
        #断言
        assert result

    @allure.testcase("http://49.235.92.12:8080/zentao/testcase-view-3-1.html")
    @allure.title("不输入学号，编辑失败")
    def test_add_studentinfo_3(self, login):
        driver = login
        add_studentinfo = StudentsInfosPage(driver)
        with allure.step("step1:点击页面左侧的学生表按钮"):
            add_studentinfo.click_xueshengbiao()
        with allure.step("step2:点击添加学生信息按钮"):
            add_studentinfo.click_add_xueshenginfo()
        with allure.step("step3:输入学号"):
            add_studentinfo.input_xuehao("12345")
        with allure.step("step3:输入姓名"):
            add_studentinfo.input_name("小明")
        with allure.step("step4:点击保存按钮"):
            add_studentinfo.save_button()
        with allure.step("step5:获取实际结果"):
            result = add_studentinfo.is_add_success(expect="添加成功")
        #断言
        assert not result



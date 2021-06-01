from common.base import Base
import allure

class StudentsInfosPage(Base):
    '''学生信息表页面'''

    # 学生表按钮
    loc_1 = ("xpath",'//a[@href="/xadmin/fiang/student/"]')
    # 添加学生信息
    loc_2 = ("xpath", '//*[@id="content-block"]/div[1]/div[2]/div/a')
    # 输入框，学号
    loc_3 = ("name", "student_id")
    # 输入框，姓名
    loc_4 = ("name", "name")
    # 输入框，年龄
    loc_5 = ("name", "age")
    # 输入框，分数
    loc_6 = ("name", "score")
    # 保存
    loc_7 = ("xpath", '//*[@id="student_form"]/div[2]/button')
    # 获取保存成功的文本信息
    loc_8 = ("xpath", '//*[@id="content-block"]/div[2]')

    @allure.step("点击页面左侧的学生表按钮")
    def click_xueshengbiao(self):
        '''点击左侧文章分类'''
        self.click(self.loc_1)

    @allure.step("点击添加学生信息按钮")
    def click_add_xueshenginfo(self):
        '''点击添加文章分类'''
        self.click(self.loc_2)

    @allure.step("输入学号")
    def input_xuehao(self, text=''):
        '''输入内容'''
        self.send(self.loc_3, text)

    @allure.step("输入姓名")
    def input_name(self, text=''):
        '''输入内容'''
        self.send(self.loc_4, text)

    @allure.step("输入年龄")
    def input_age(self, text=''):
        '''输入内容'''
        self.send(self.loc_5, text)

    @allure.step("输入分数")
    def input_score(self, text=''):
        '''输入内容'''
        self.send(self.loc_6, text)

    @allure.step("点击保存按钮")
    def save_button(self):
        '''点保存按钮'''
        self.click(self.loc_7)

    @allure.step("判断是否添加成功，返回True / False ")
    def is_add_success(self, expect=""):
        '''判断是否添加成功，返回True / False '''
        get_result = self.get_text(self.loc_8)
        print("保存成功后，获取到页面的信息：%s" %get_result)
        return expect in get_result

if __name__ == '__main__':
    from selenium import webdriver
    driver = webdriver.Chrome()
    driver.maximize_window()
    #先登录
    from pages.login_page import LoginPage
    base_url = "http://106.55.55.176:16666"
    web = LoginPage(driver)
    web.login(base_url)

    #添加文章分类
    student_info = StudentsInfosPage(driver)
    student_info.click_xueshengbiao()
    student_info.click_add_xueshenginfo()
    student_info.input_xuehao("78987")
    student_info.input_name("xioaming")
    student_info.input_age("16")
    student_info.input_score("99")
    student_info.save_button()

    #断言
    result = student_info.is_add_success(expect="添加成功")
    driver.quit()
    assert result

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pytest
import allure
from allure_commons.types import AttachmentType
from page_object.Nokariprofile import Nokari
from utilites.Logger import Logging_Genrator
from utilites.Readconfig import ReadConfigProfile

class Test_Nokari_login:
    profile =ReadConfigProfile.EnterProfile()
    log=Logging_Genrator.loggen()



    @allure.title("Nokari Profile")
    @allure.link("https://www.naukri.com/")
    @allure.id("test nokari log1")
    @allure.story("Nokari Profile Auto Update")
    @allure.severity(allure.severity_level.NORMAL)
    # @pytest.mark.parametrize("user,pas,profile",[("tanveeralam7520@gmail.com","Talam@786","I have 3+years of experience as a Quality Assurance Engineer, I have expertise in testing and involved in Manual testing, ETL testing, Automation testing, Database testing, Functional testing.Rest api testing using postman ,Api automation using python pytest"),("tanveeralam5445@gmail.com","Talam@786786","I have 3+years of experience as a Quality Assurance Engineer, I have expertise in testing and involved in Manual testing, ETL testing, Automation testing, Database testing, Functional testing.Rest api testing using postman ,Api automation using python pytest")])
    def test_nokari_log1(self,setup,EnterData):
        self.log.info("start Nokari daily update test case ")
        self.driver = setup
        self.log.info("open webdiver")
        self.np= Nokari(self.driver)
        self.log.info("open URL for Nokari loging ")
        self.np.Url()
        self.log.info("clicking log in button ")
        self.np.Login()
        self.log.info("Entering User Name")
        self.np.Enter_username(EnterData[0])
        self.log.info("Entering Password")
        self.np.Enter_password(EnterData[1])
        self.log.info("Clicking loging sumbit button ")
        self.np.Click_submit()
        self.log.info("Cheking profile view if profle is  visible then click ")
        if self.np.Click_profile()==True :
            self.log.info("scrooling for employee edit button ")
            self.np.Scroll_employ()
            self.log.info("clicking empolyedit button")
            self.np.Click_employedit()
            self.log.info("Scrolling for summit button ")
            self.np.Scroll_summit()
            self.log.info("clicking job profile and clear and send data ")
            self.np.Clier_job_depriction(self.profile)
            self.log.info("submit job profile ")
            self.np.Empoly_submit()
            self.driver.save_screenshot("D:\\programming\\Nokari_profile\\Screenshot\\nokari_t_01.png")
            allure.attach(self.driver.get_screenshot_as_png(),name="Nokari_t_001",attachment_type=AttachmentType.PNG)
            self.log.info("close webdriver")
            self.driver.close()
            assert True

        elif self.np.Click_profile()==False:
            self.log.info("clicking complete profile buttong ")
            self.np.Click_Complete()
            self.log.info("scrooling for employee edit button ")
            self.np.Scroll_employ()
            self.log.info("clicking empolyedit button")
            self.np.Click_employedit()
            self.log.info("Scrolling for summit button ")
            self.np.Scroll_summit()
            self.log.info("clicking job profile and clear and send data ")
            self.np.Clier_job_depriction(self.profile)
            self.log.info("Clicking loging sumbit button ")
            self.np.Empoly_submit()
            self.driver.save_screenshot("D:\\programming\\Nokari_profile\\Screenshot\\nokari_f_01.png")
            allure.attach(self.driver.get_screenshot_as_png(),name="Nokari_f_01",attachment_type=AttachmentType.PNG)
            self.log.info("close webdriver")
            self.driver.close()
            assert True
        else:
            assert False





from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common import NoSuchElementException


class Nokari:


    Login_button=(By.LINK_TEXT, "Login")
    UserName_xpath = (By.XPATH, "//input[@type='text']")
    Password_xpath = (By.XPATH, "//input[@type='password']")
    Submit_Button_xpath = (By.XPATH, "//button[@type='submit']")
    Viewprofile_xpath = (By.XPATH, "//a[normalize-space()='View profile']")
    Complete_xpath = (By.XPATH, "//a[normalize-space()='Complete profile']")
    Scroll_xpath = (By.XPATH, "//span[@class='widgetTitle'][normalize-space()='Key skills']")
    Imployee_edit_xpath = (By.XPATH, "//span[@class='edit icon typ-14Medium']")
    Job_profile_xpath = (By.XPATH, "//textarea[@id='jobDescription']")
    Skil_xpath = (By.XPATH,"//label[@class='required-field']")
    Submit_empole_button = (By.XPATH, "//button[@id='submitEmployment']")

    def __init__(self,driver):
        self.driver = driver
        self.wait= WebDriverWait(self.driver,15)



    def Url(self):
        self.driver.get("https://www.naukri.com/")


    def Login(self):
        self.driver.find_element(*Nokari.Login_button).click()

    def Enter_username(self,name):
        self.wait.until(ec.visibility_of_element_located(self.UserName_xpath))
        self.driver.find_element(*Nokari.UserName_xpath).send_keys(name)
    def Enter_password(self,password):
        self.wait.until(ec.visibility_of_element_located(self.Password_xpath))
        self.driver.find_element(*Nokari.Password_xpath).send_keys(password)
    def Click_submit(self):
        self.wait.until(ec.visibility_of_element_located(self.Submit_Button_xpath))
        self.driver.find_element(*Nokari.Submit_Button_xpath).click()
    def Click_profile(self):
        try:
            self.wait.until(ec.visibility_of_element_located(self.Viewprofile_xpath))
            self.driver.find_element(*Nokari.Viewprofile_xpath).click()
            return True
        except :
            return False
    def Click_Complete(self):
        self.wait.until(ec.visibility_of_element_located(self.Complete_xpath))
        self.driver.find_element(*Nokari.Complete_xpath).click()
    def Scroll_employ(self):
        self.wait.until(ec.visibility_of_element_located(self.Scroll_xpath))
        emp=self.driver.find_element(*Nokari.Scroll_xpath)
        self.driver.execute_script("arguments[0].scrollIntoView()", emp)
    def Click_employedit(self):
        self.wait.until(ec.visibility_of_element_located(self.Imployee_edit_xpath))
        self.driver.find_element(*Nokari.Imployee_edit_xpath).click()
    def Scroll_summit(self):
        self.wait.until(ec.visibility_of_element_located(self.Skil_xpath))
        sub = self.driver.find_element(*Nokari.Skil_xpath)
        self.driver.execute_script("arguments[0].scrollIntoView()", sub)
    def Clier_job_depriction(self,data):
        self.wait.until(ec.visibility_of_element_located(self.Job_profile_xpath))
        self.driver.find_element(*Nokari.Job_profile_xpath).clear()
        self.driver.find_element(*Nokari.Job_profile_xpath).send_keys(data)


    def Empoly_submit(self):
        self.wait.until(ec.visibility_of_element_located(self.Submit_empole_button))
        self.driver.find_element(*Nokari.Submit_empole_button).click()


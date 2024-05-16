from selenium import webdriver
import pytest
@pytest.fixture()
def setup():
    driver = webdriver.Chrome()
    driver.maximize_window()
    return driver



@pytest.fixture(params=[
    ("tanveeralam7520@gmail.com","Talam@786","I have 3+years of experience as a Quality Assurance Engineer, I have expertise in testing and involved in Manual testing, ETL testing, Automation testing, Database testing, Functional testing.Rest api testing using postman ,Api automation using python pytest"),("tanveeralam5445@gmail.com","Talam@786786","I have 3+years of experience as a Quality Assurance Engineer, I have expertise in testing and involved in Manual testing, ETL testing, Automation testing, Database testing, Functional testing.Rest api testing using postman ,Api automation using python pytest")
])
def EnterData(request):
    return request.param

def pytest_metadata(metadata):
    # To add
    metadata["tester"]="Tanveer Alam"
    metadata["update"]="nokari profile"
    metadata["URL"]="https://www.naukri.com/"
    # To remove
    metadata.pop("JAVA_HOME", None)

def pytest_html_report_title(report):
    report.title = "Nokari Profile Update"

def pytest_html_results_summary(prefix, summary, postfix):
    prefix.extend(["daily update"])
    summary.extend(["week update"])
    postfix.extend(["years update"])







import pytest
from selenium import webdriver
from pages.registration_form_page import RegistrationFormPage

@pytest.fixture(scope="module")
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

def test_registration_form(driver):
    form_page = RegistrationFormPage(driver)
    form_page.open()
    form_page.fill_first_name("Alexander")
    form_page.fill_last_name("Kovalev")
    form_page.fill_email("kovalev@example.com")
    form_page.select_gender("Male")
    form_page.fill_mobile("1234567890")
    form_page.fill_date_of_birth("01 Jan 1995")
    form_page.fill_subjects("hello")
    form_page.upload_picture("/Users/admin/Documents/work/Registration_ui_test/image.jpg")
    form_page.fill_current_address("29 st ")
    form_page.select_state("NCR")
    form_page.select_city("Delhi")
    form_page.submit_form()
    
    success_message = form_page.get_success_message()
    assert "Thanks for submitting the form" in success_message



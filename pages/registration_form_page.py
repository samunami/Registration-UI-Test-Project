from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class RegistrationFormPage:
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://demoqa.com/automation-practice-form"
    
    def open(self):
        self.driver.get(self.url)
    
    def fill_first_name(self, first_name):
        self.driver.find_element(By.ID, "firstName").send_keys(first_name)
    
    def fill_last_name(self, last_name):
        self.driver.find_element(By.ID, "lastName").send_keys(last_name)
    
    def fill_email(self, email):
        self.driver.find_element(By.ID, "userEmail").send_keys(email)
    
    def select_gender(self, gender):
        gender_selector = f"//input[@name='gender' and @value='{gender}']"
        gender_element = self.driver.find_element(By.XPATH, gender_selector)
        self.driver.execute_script("arguments[0].click();", gender_element)

    def fill_mobile(self, mobile):
        self.driver.find_element(By.ID, "userNumber").send_keys(mobile)
    
    def fill_date_of_birth(self, date):
        self.driver.find_element(By.ID, "dateOfBirthInput").send_keys(date)
    
    def fill_subjects(self, subject):
        self.driver.find_element(By.ID, "subjectsInput").send_keys(subject)
    
    def upload_picture(self, file_path):
        self.driver.find_element(By.ID, "uploadPicture").send_keys(file_path)
    
    def fill_current_address(self, address):
        self.driver.find_element(By.ID, "currentAddress").send_keys(address)
    
    def select_state(self, state):
        self.driver.find_element(By.ID, "react-select-3-input").send_keys(state + "\n")
    
    def select_city(self, city):
        self.driver.find_element(By.ID, "react-select-4-input").send_keys(city + "\n")
    
    def submit_form(self):
        self.driver.find_element(By.ID, "submit").click()
    
    def get_success_message(self):
        return WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "modal-content"))
        ).text

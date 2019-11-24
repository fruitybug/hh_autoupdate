from selenium import webdriver
import time

driver = webdriver.Firefox(executable_path="/path/geckodriver")

driver.get('https://hh.ru/account/login')

username = driver.find_element_by_name("username")
password = driver.find_element_by_name("password")

username.send_keys("790000000")
password.send_keys("MyPassword")

submit_button = driver.find_element_by_xpath("//input[@type='submit']")
submit_button.click()
time.sleep(2)

driver.execute_script("window.stop();")
driver.get('https://hh.ru/applicant/resumes')
time.sleep(2)
refresh_button = driver.find_elements_by_class_name('applicant-resumes-update-button')[:2]

if refresh_button:
    for refresh_but in refresh_button:
        try:
            refresh_but.click()
            time.sleep(5)
        except Exception as e:
            print(e)


time.sleep(5)

driver.close()


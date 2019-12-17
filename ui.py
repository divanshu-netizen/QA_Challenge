from selenium import webdriver

driver = webdriver.Chrome('/Users/divanshugupta/PycharmProjects/QAChallenge/Driver/chromedriver 4')
driver.get('http://127.0.0.1:5000/users')
element= driver.find_element_by_id("all-users").is_displayed()
print element
driver.implicitly_wait(10)
driver.quit()
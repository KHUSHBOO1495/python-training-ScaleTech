from selenium import webdriver

driver = webdriver.Chrome()

driver.get("https://example.com")

print(driver.title)

driver.quit()



driver = webdriver.Chrome()

driver.get("https://www.google.com")

print("Title:", driver.title)

search_box = driver.find_element("name", "q")
search_box.send_keys("Python web scraping")

search_box.submit()

print("New title:", driver.title)

driver.quit()

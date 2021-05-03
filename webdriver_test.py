from selenium import webdriver

driver=webdriver.Chrome(executable_path=r"/vagrant/chromedriver")
driver.get("google.com")

print (driver.title)
print (diver.current_url) 
driver.quit()

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

def test_tester():
      driver = webdriver.Chrome()
      driver.get("http://162.246.157.120:8000/")
      elem = driver.find_element_by_id("name")
      assert elem != None
    

from selenium import webdriver
from selenium.webdriver.common.keys import Keys



def test_home():
	driverLocation = 'Users/yonaelbekele/Downloads/chromedriver'
	driver = webdriver.Chrome(driverLocation) 
	driver.get("http://162.246.157.120:8000/")
	elem_name = driver.find_element_by_id("name")
	elem_about = driver.find_element_by_id("about")
	elem_education = driver.find_element_by_id("education")
	elem_skills = driver.find_element_by_id("skills")
	elem_work = driver.find_element_by_id("work")
	elem_contact = driver.find_element_by_id("contact")
	assert elem_name != None
	assert elem_about != None
	assert elem_education != None
	assert elem_skills != None
	assert elem_work != None
	assert elem_contact != None
	
test_home()

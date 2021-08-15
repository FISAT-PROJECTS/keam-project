from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from pprint import pprint as pp
import time as t

# number as per the dropdown in the site
district = {
	'All' 					: 0 ,
	'THIRUVANANTHAPURAM'	: 1 ,
	'KOLLAM' 				: 2 ,
	'PATHANAMTHITTA' 		: 3 ,
	'ALAPPUZHA' 			: 4 ,
	'KOTTAYAM' 				: 5 ,
	'IDUKKI' 				: 6 ,
	'ERNAKULAM' 			: 7 ,
	'THRISSUR' 				: 8 ,
	'PALAKKAD' 				: 9 ,
	'MALAPPURAM' 			: 10 ,
	'KOZHIKODE' 			: 11 ,
	'WAYANAD' 				: 12 ,
	'KANNUR' 				: 13 ,
	'KASARAGOD' 			: 14 ,
	'Other' 				: 15 ,
}

year = {
	2021: 0,
	2020: 1,
	2019: 2,
	2018: 3,
	2017: 4,
	2016: 5,
	2015: 6
}

degree = {
	'UG' : 1,
	'PG' : 2,
}

program = {
	'All' 			: 0 ,
	'B.Tech' 		: 1 ,
	'B.Arch' 		: 2 ,
	'Hotel' 		: 3 ,
	'Management' 	: 4 ,
	'and' 			: 5 ,
	'Catering' 		: 6 ,
	'Technology' 	: 7 ,
	'B.Des' 		: 8 ,
}


def select_combobox_x(driver,dropdown_val):
	driver[0].click()
	driver[0].send_keys(Keys.ARROW_DOWN*dropdown_val)
	driver[0].send_keys(Keys.RETURN)
	# t.sleep(5)


def checklist(driver):
	if type(driver) == list:
		print("{")
		for i,j in enumerate(driver[0].text.split()):
			print("\t\'",j,'\':',i,",")
		print("}")


def automated_choose(driver):	
	#1
	select_yr = driver.find_elements(By.XPATH,"/html/body/div[3]/div[1]/div[2]/div/form/div/div[1]/span[1]/select")
	print(' - select complete')
	checklist(select_yr)
	select_combobox_x(select_yr, year[2015])

	#2
	select_dis = driver.find_elements(By.XPATH,"/html/body/div[3]/div[1]/div[2]/div/form/div/div[1]/span[2]/select")
	print(' - select complete')
	checklist(select_dis)
	select_combobox_x(select_dis, district['ERNAKULAM'])

	#3
	select_deg = driver.find_elements(By.XPATH,"/html/body/div[3]/div[1]/div[2]/div/form/div/div[2]/span[1]/select")
	print(' - select complete')
	checklist(select_deg)
	select_combobox_x(select_deg, degree['UG'])

	#4
	select_prog = driver.find_elements(By.XPATH,"/html/body/div[3]/div[1]/div[2]/div/form/div/div[2]/span[2]/select")
	print(' - select complete')
	checklist(select_prog)
	select_combobox_x(select_prog, program['B.Tech'])


def checklist_x(driver):
	if type(driver) == list:
		for i in driver:
			if type(i) != list:
				print(i.text.split('\n'))
			print()
			

def get_affiliated_links(driver):

	# 1
	select_yr = driver.find_elements(By.XPATH,"/html/body/div[3]/div[1]/div[2]/div/form/div/div[1]/span[1]/select")
	print(' - select complete')
	checklist(select_yr)
	select_combobox_x(select_yr, year[2020])

	a = driver.find_elements(By.XPATH,"/html/body/div[3]/div[1]/div[2]/div/table/tbody/tr/td[1]/span/a")
	print(' - select complete')
	affiliated_links =[]
	if type(a) == list:
		for i in a:
			affiliated_links.append(i.get_attribute("href"))

	with open('affiliated_links.py','w') as f:
		f.write("affiliated_links=['")
		f.write("',\n'".join(affiliated_links))
		f.write("']")


def ktu_site():
	driver =  webdriver.Edge("msedgedriver.exe")
	driver.get('https://ktu.edu.in/eu/afn/affiliationInstitutes.htm')
	
	# automated_choose(driver)

	get_affiliated_links(driver)	

	# from affiliated_links import affiliated_links
	# print(affiliated_links)
	
	driver.implicitly_wait(5)

	driver.close()

ktu_site()


	# for i in institution_name:
	# 	print(i,type(i))
	# 	if type(i)==list:
	# 		for j in i:
	# 			print(j,type(j))
	# 	else:
	# 		print(i.text)
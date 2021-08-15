from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from pprint import pprint as pp
import time as t
from affiliated_links import affiliated_links


def checklist(driver):
	if type(driver) == list:
		print("{")
		for i,j in enumerate(driver[0].text.split()):
			print("\t\'",j,'\':',i,",")
		print("}")


def checklist_x(driver):
	if type(driver) == list:
		for i in driver:
			if type(i) != list:
				print(i.text)
			print()
			

def get_table(driver):
	headings, table_rowdata, rows, row = [], [], [], []

	#2
	# table_heading = driver.find_elements(By.XPATH,"/html/body/div[3]/div[1]/div[2]/table/tbody/tr[1]/th")
	# print(' - select complete')
	# for i in table_heading:
	# 	if type(i) != list:
	# 		headings.append(i.text)
	# 	print()
	# print(headings)


def clear_csv():
	with open('data.csv','w') as f:
		f.write('')


def write_to_csv(data):
	with open('data.csv','a') as f:
		for i in data:
			f.write(",".join(i))
			f.write("\n")


def automated_choose(driver):	
	table_rowdata, rows, row = [], [], []

	#1
	collage_name = driver.find_elements(By.XPATH,"/html/body/div[3]/div[1]/div[2]/div/table/tbody/tr/td/span[1]/h4")[0].text
	print(' - select complete')

	#3
	table_data = driver.find_elements(By.XPATH,"/html/body/div[3]/div[1]/div[2]/table/tbody/tr/td")
	print(' - select complete')
	for i in table_data:
		if type(i) != list:
			table_rowdata.append(i.text)
	for i,r in enumerate(table_rowdata):
		row.append(r)
		if i%8==7:
			row.append(collage_name)
			rows.append(row)
			row=[]
	# pp(rows)
	write_to_csv(rows)


def ktu_site():
	try:
		driver =  webdriver.Edge("msedgedriver.exe")

		#2
		headings = ['Program Category', 'Program Name', 'Degree', 'Program Type', 'Sanctioned Intake', 'Actual Intake', 'NRI', 'PIO', 'clg_name']
		with open('data.csv','w') as f:
			f.write(",".join(headings))
			f.write("\n")
			
		for i in affiliated_links:
			driver.get(i)
		
			automated_choose(driver)

		driver.implicitly_wait(5)

	except Exception as e:
		print("\n\terr: \n",e)

	# finally:
	# 	driver.close()

ktu_site()
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
import openpyxl

path = Service("C:/Users/User/Desktop/chromedriver_win32/chromedriver.exe")
driver = webdriver.Chrome(service=path)

driver.get("https://www.fiercepharma.com/")
time.sleep(1)
alists = driver.find_elements(By.XPATH, '//*[contains(text(),"COVID")]')

worbook = openpyxl.Workbook()
sheet = worbook.worksheets[0]
count = 1
for list in alists:
    if list.text:
        print(list.text+"\n")
        sheet["A"+str(count)] = list.text
        count = count+1
        worbook.save("test.xlsx")
    else:
        print("i am empty")

driver.close()
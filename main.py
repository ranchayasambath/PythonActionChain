from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
import time 

PATH = 'C:\chromedriver.exe'

driver = webdriver.Chrome(PATH)

driver.get("http://essemble.co.uk/escript/drag_drop_engine/dragdrop1.html")
time.sleep(4)

for i in range(1,9):
    print(i)

    source_element = driver.find_element(By.ID,f"drag{i}")

    target_element = driver.find_element(By.ID,f"drop{i}")

    action = ActionChains(driver)

    action.drag_and_drop(source_element,target_element)

    action.pause(1)

    action.perform()

    btn_confirm = driver.find_element(By.ID,"btn")
    
    btn_confirm.click()




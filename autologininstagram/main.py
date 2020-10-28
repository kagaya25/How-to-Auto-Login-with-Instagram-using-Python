from selenium import webdriver 
from time import sleep 
from webdriver_manager.chrome import ChromeDriverManager 
from selenium.webdriver.chrome.options import Options  
  
usr=input('Enter Email Id:')  
pwd=input('Enter Password:')  
  
driver = webdriver.Chrome(ChromeDriverManager().install()) 
driver.get('https://www.instagram.com/') 
print ("Opened instagram") 
sleep(1) 
  
username_box = driver.find_element_by_name('username')
username_box.send_keys(usr) 
print ("Email Id entered") 
sleep(1) 
  
password_box = driver.find_element_by_name('password')
password_box.send_keys(pwd) 
print ("Password entered") 
login_box = driver.find_element_by_css_selector("#loginForm > div > div:nth-child(3) > button > div") 
login_box.click() 
  
print ("Done") 
input('Press anything to quit') 
driver.quit() 
print("Finished") 
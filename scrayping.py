from selenium import webdriver
import time
import pandas as pd 

#GoogleChromeを起動
browser = webdriver.Chrome(executable_path = 'C:\\Users\\user\\anaconda3\\chromedriver.exe')
browser.implicitly_wait(3)

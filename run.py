from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import urllib.request
import time

def Remove(duplicate): 
    final_list = [] 
    for num in duplicate: 
        if num not in final_list: 
            final_list.append(num) 
    return final_list 
driver = webdriver.Chrome(ChromeDriverManager().install())
url=input('Enter the webseries url: ')
driver.get(str(url))
time.sleep(5)
driver.maximize_window()
time.sleep(5)
driver.find_element_by_class_name('show-all').click()
temp = driver.find_element_by_class_name('all-episode')
links=[]
for i in temp.get_attribute('innerHTML').split('a href="')[1:]:
    links.append('https://www3.dramacool.movie'+i.split('"')[0])
download_link=[]
for link in links:
    driver.get('https://www.tubeoffline.com/download-DramaCool-videos.php')
    temp = driver.find_element_by_class_name('videoLink')
    temp.clear()
    temp.send_keys(link)
    driver.find_element_by_id('submitbutton').click()
    time.sleep(3)
    temp = driver.find_element_by_css_selector('#videoDownload > table > tbody')
    temp = temp.get_attribute('innerHTML').split('a href="')[1].split('"')[0]
    print(temp)
    download_link.append(temp)
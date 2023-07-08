import requests
from requests.auth import HTTPBasicAuth



#res = requests.get(url)
#print(res.text)

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

url = "https://quip-amazon.com/1wCGApl0oVdB/Bot-Account-Credentials"


r = requests.get(url, auth=HTTPBasicAuth("ramadhma@amazon.com", "0618Ramsteyn8$"))
print(r.text)
#options: Options = Options()
#options.add_experimental_option('detach', True)
#ser_obj = Service("Documents\\chromedriver.exe")
#driver = webdriver.Chrome(service=ser_obj, options=options)
#driver.implicitly_wait(5)
#driver.get(url)
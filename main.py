import os
import requests
from dotenv import load_dotenv
from dotenv import dotenv_values
from pathlib import Path
from selenium import webdriver
import service
import scraper
import json

profile_url = input("Enter profile URL: ")

driver = webdriver.Chrome()
config = dotenv_values()
user = config.get('USER')
password = config.get('PASSWORD')


service.login(driver, user, password)
json_data = json.dumps(scraper.extractData(driver, profile_url))
json_file = open("./result.json", "w")
json_file.write(json_data)






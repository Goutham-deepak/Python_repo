from selenium import webdriver
from time import sleep

class facebook:
  def __init__(self):
      self.driver = webdriver.Firefox()
      self.driver.get("https://www.facebook.com/")
      
      
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# Specify the path to ChromeDriver if not in PATH
service = Service("C:\\Tools\\chromedriver\\chromedriver.exe")

# Initialize the browser
driver = webdriver.Chrome(service=service)

# Open a website
driver.get("https://www.google.com")

# Print the title of the page
print("Page title is:", driver.title)

# Close the browser
driver.quit()

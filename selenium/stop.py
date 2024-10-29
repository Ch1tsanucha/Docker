from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
from time import sleep

chrome_options = webdriver.ChromeOptions()
# chrome_options.add_argument('--headless')  # Run in headless mode
# chrome_options.add_argument('--no-sandbox')  # Bypass OS security model
# chrome_options.add_argument('--disable-dev-shm-usage')  # Overcome limited resource problems

driver = webdriver.Remote(
    command_executor='http://localhost:4444/wd/hub',
    options=chrome_options
)


driver.quit()

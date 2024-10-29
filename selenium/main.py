from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import pandas as pd
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')  # Run in headless mode
chrome_options.add_argument('--no-sandbox')  # Bypass OS security model
chrome_options.add_argument('--disable-dev-shm-usage')  # Overcome limited resource problems

# Create a Remote WebDriver instance
driver = webdriver.Remote(
    command_executor='http://localhost:4444/wd/hub',
    options=chrome_options
)


try:
    all_price=[]
    all_name=[]
    all_space=[]
    all_floor=[]
    all_bedroom=[]
    all_toilet=[]
    for i in range(1,1100):
            driver.get(f"https://www.livinginsider.com/searchword/Condo/Rent/1/%E0%B8%A3%E0%B8%A7%E0%B8%A1%E0%B8%9B%E0%B8%A3%E0%B8%B0%E0%B8%81%E0%B8%B2%E0%B8%A8-%E0%B9%80%E0%B8%8A%E0%B9%88%E0%B8%B2-%E0%B8%84%E0%B8%AD%E0%B8%99%E0%B9%82%E0%B8%94.html")
            # Parse the page source
            soup = BeautifulSoup(driver.page_source, 'html.parser')
            
            # # Example: Extract and print the page title
            # title = soup.title.string
            # print(f'The title of the page is: {title}')

            # # Example: Find and print price elements
            price_elements = soup.find_all("div", class_="listing-cost")
            Box_of_all = soup.find_all("div", class_="item-desc")
            for Box in Box_of_all:
                 In_box = Box.find_all("div", class_="row")
                 all_name.append(In_box[0].find("div").find("a").find("p").text.strip())
                 Inside = In_box[4].find("div").find_all("div")
                 all_space.append(Inside[0].text.strip())  # Strip whitespace
                 all_floor.append(Inside[1].text.strip())  # Strip whitespace
                 all_bedroom.append(Inside[2].text.strip())  # Strip whitespace
                 all_toilet.append(Inside[3].text.strip())  # Strip whitespace
                    
            for price in price_elements:
                real_price = price.find("div", class_="t-16")
                all_price.append(real_price.text)

            

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    # Clean up
    driver.quit()

# for i in range(len(all_price)):
#      print(all_price[i])
#      print(all_name[i])
#      print(all_space[i])
#      print(all_floor[i])
#      print(all_bedroom[i])
#      print(all_toilet[i])
#      print("")


print(f"len is {len(all_price)}")

data = {
    "Price": all_price,
    "Name": all_name,
    "Space": all_space,
    "Floor": all_floor,
    "Bedroom": all_bedroom,
    "Toilet": all_toilet
}

df = pd.DataFrame(data)

df.to_csv('condo_listings.csv', index=False)

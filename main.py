from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import csv
import pandas as pd


service = Service(executable_path='chromedriver.exe')
driver = webdriver.Chrome(service=service)


#cars shown first on page
def tier_one():
    return driver.find_elements(By.CLASS_NAME, "tm-motors-tier-one-search-card__listing-details-container")

#cars shown second on page
def tier_two():
    return driver.find_elements(By.CLASS_NAME, "tm-motors-tier-two-search-card__listing-details-container")

#cars shown third on page
def tier_three():
    return driver.find_elements(By.CLASS_NAME, "tm-motors-tier-three-search-card__listing-details-container-no-franchise")

#links to cars
def link():
    links_list = []
    links = driver.find_elements(By.CSS_SELECTOR, "a.tm-tiered-search-card__link.o-card")
    for link in links:
        links_list.append(link.get_attribute("href"))
    
    return links_list


#get all cars and return list
def grab_cars():
    # Combine all tiers into a single list
    cars = tier_one() + tier_two() + tier_three()
    
    car_data = []
    
    for car in cars:
        text = car.text.strip()
        
            
        car_data.append((text))
    
    return car_data



#gets info on all cars by removing unwanted text
def grab_details(car_text):
    name =""
    location = ""
    kms = ""
    engine = ""
    transmission = ""
    price = ""
    count = 0
    lines = car_text.splitlines()
    lines = [line for line in lines if "Listed within the last 7 days" not in line]
    while lines:
        line = lines.pop(0)
        if count ==0:
            name = line
            count += 1
        if count ==1 and "," in line:
            location = line
            count += 1
        if "km" in line:
            kms = line
        if "Automatic"  in line:
            transmission = line
        if "Manual" in line:
            transmission = line
            
        if "cc" in line:
            engine = line
        if "$" in line:
            price = line
    
    return {
        "Name": name,
        "Location": location,
        "KMs": kms,
        "Engine Size": engine,
        "Transmission": transmission,
        "Price": price
    }

   

#get cars off website
def see_cars():
    all_cars = []
    car_type = "mx5"   #change this for specific car
    max_price = 20000  #change this for max price
    listing_type = "private"  #remove for both private and dealer
    page_number = 1 # Start at page 1

    while page_number < 3:  # You can adjust this to go through more pages
        print(f"Scraping page {page_number}...")
        url = f"https://www.trademe.co.nz/a/motors/cars/search?search_string={car_type}&price_max={max_price}&listing_type={listing_type}&page={page_number}"
        driver.get(url)
        # Wait until elements are present
        # WebDriverWait(driver, 10).until(
        #     EC.presence_of_all_elements_located((By.CLASS_NAME, "tm-motors-tier-one-search-card__listing-details-container"))
        # )

        cars = grab_cars()
        all_cars.extend(cars)
        page_number += 1
    
    return all_cars


car_list = see_cars()
links = link()
driver.quit()


# Write to CSV
print(f"Total cars found: {len(car_list)}")
print(f"Total links found: {len(links)}")
final_df = pd.DataFrame()
with open("cars.csv", "w", newline="", encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["ID","Name", "Location", "KMs", "Engine Size", "Transmission", "Price", "Link"])  # Include "Link" header
    car_number = 1
    #for car_text, car_link in zip(car_list, links):  # Ensure you're iterating over both lists in sync
    for car_text in (car_list):
        details = grab_details(car_text)
        details["ID"] = car_number  # Add a car number
        df = pd.DataFrame([details])
        final_df = pd.concat([final_df, df], ignore_index=True)  # Append each df to final_df
        car_number += 1

# Write final_df to CSV
final_df.to_csv("cars.csv", index=False)
print("Data written to cars.csv successfully.")


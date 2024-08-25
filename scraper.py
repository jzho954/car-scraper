from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from car import Car

class WebScraper:

    #set up the webdriver
    def __init__(self, driver_path, car_type="mx5", max_price=20000, listing_type="private"):
        self.service = Service(executable_path=driver_path)
        self.driver = webdriver.Chrome(service=self.service)
        self.car_type = car_type
        self.max_price = max_price
        self.listing_type = listing_type

    # get the cars on the top of the page 
    def tier_one(self):
        return self.driver.find_elements(By.CLASS_NAME, "tm-motors-tier-one-search-card__listing-details-container")
    #get the cars in the middle of the page
    def tier_two(self):
        return self.driver.find_elements(By.CLASS_NAME, "tm-motors-tier-two-search-card__listing-details-container")
    #get the cars at the bottom of the page
    def tier_three(self):
        return self.driver.find_elements(By.CLASS_NAME, "tm-motors-tier-three-search-card__listing-details-container-no-franchise")
    #get links of all cars
    def get_links(self):
        links_list = []
        links = self.driver.find_elements(By.CSS_SELECTOR, "a.tm-tiered-search-card__link.o-card")
        for link in links:
            links_list.append(link.get_attribute("href"))
        return links_list

    def get_cars(self):
        cars = self.tier_one() + self.tier_two() + self.tier_three()
        car_data = []
        for car in cars:
            text = car.text.strip()
            car_data.append(text)
        return car_data
    #scrape the cars
    def scrape(self, pages=2):
        all_cars = []
        for page_number in range(1, pages + 1):
            print(f"Scraping page {page_number}...")
            url = f"https://www.trademe.co.nz/a/motors/cars/search?search_string={self.car_type}&price_max={self.max_price}&listing_type={self.listing_type}&page={page_number}"
            self.driver.get(url)
            
            cars = self.get_cars()
            all_cars.extend(cars)
        return all_cars

    def quit(self):
        self.driver.quit()

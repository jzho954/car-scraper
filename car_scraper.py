from scraper import WebScraper
from car import Car
from utils import write_to_csv

# Set up the WebScraper   ***change car_type, max_price for your own search***  ***remove listing_type if you want dealers included in search as well***
scraper = WebScraper(driver_path='chromedriver.exe', car_type="mx5", max_price=20000, listing_type="private")  

# Scrape the cars
car_texts = scraper.scrape(pages=3)
links = scraper.get_links()

# Create Car objects
car_list = []
for i, car_text in enumerate(car_texts, start=1):
    car = Car().from_text(car_text)
    car.car_id = i  # Assign a car ID
    car_list.append(car)

scraper.quit()

# Write the data to CSV
write_to_csv(car_list)

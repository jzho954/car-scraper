# Car Scraper

This project is a Python based web scraper designed to take information about cars from trademe. The data is then stored in a CSV file for easy analysis and record keeping. The scraper is built using Selenium for web automation and pandas for data handling.

## Features

- **Customizable Search:** Modify the `car_type`, `max_price`, and `listing_type` parameters to tailor the search to your specific needs.
- **Private Listings:** By default, the scraper only includes private listings. Remove the `listing_type` parameter to include dealer listings as well.
- **Car Object Creation:** The scraped data is used to create `Car` objects, which are then stored in a list for easy manipulation.
- **CSV Export:** The extracted data is written to a CSV file using pandas, making it easy to analyze or share.

## How to Use

### Prerequisites

- Python 3.x
- [Selenium](https://www.selenium.dev/)
- [pandas](https://pandas.pydata.org/)

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/jzho954/car-scraper.git
   cd car-scraper


2. Install Pandas
``` 
 pip install selenium 
 pip install pandas
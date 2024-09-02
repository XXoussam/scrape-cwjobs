from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
from selenium.webdriver.support import expected_conditions as EC
import time

# Setup Chrome options
chrome_options = Options()
chrome_options.add_argument("--user-data-dir=C:\\Users\\saoud\\Downloads\\chromedriver-win64\\chrome-profile")  # Use custom profile directory
chrome_options.add_argument("--no-first-run")  # Prevents the first run tasks
chrome_options.add_argument("--disable-default-apps")  # Disable the default apps installed in the browser
chrome_options.add_argument("--start-maximized")  # Start the browser maximized
chrome_options.add_argument("--disable-popup-blocking")  # Disable popup blocking
chrome_options.add_argument("--disable-extensions")  # Disable extensions
chrome_options.add_argument("--disable-infobars")  # Disable infobars
chrome_options.add_argument("--disable-blink-features=AutomationControlled") 

# Specify the path to your ChromeDriver
service = Service(r'C:\Users\saoud\Downloads\chromedriver-win64\chromedriver-win64\chromedriver.exe')

# Initialize the Chrome driver
driver = webdriver.Chrome(service=service, options=chrome_options)
# URL you want to open

jobs = [
    "Data Engineer",
    "Power Bi",
    "Data Science",
    "Data",
    "Business Analyst",
    "NHS",
    "DevOps Engineer",
    "Remote",
    "IT Support",
    "Business Intelligence Analyst"
]


# Base URL for job searches
base_url = 'https://www.cwjobs.co.uk/jobs/'

jobs = [
    "Data Engineer",
    "Power Bi",
    "Data Science",
    "Data",
    "Business Analyst",
    "NHS",
    "DevOps Engineer",
    "Remote",
    "IT Support",
    "Business Intelligence Analyst"
]



for job in jobs:
# Format job title for URL (replace spaces with hyphens, lower case)
    job_url_suffix = job.replace(" ", "-").lower()
    full_url = base_url + job_url_suffix
    
    driver.get(full_url)
    time.sleep(10)  # Give time for the page to load

    # Get page source and create a Beautiful Soup object
    soup = BeautifulSoup(driver.page_source, 'html.parser')

    # Find all article elements
    articles = soup.find_all('article', class_='res-1f9va2m')
    
    # Loop through each article and extract information
    for article in articles:
        job_title = article.find('div', class_='res-nehv70').get_text(strip=True) if article.find('div', class_='res-nehv70') else 'No Title Found'
        company_name = article.find('span', attrs={'data-at': 'job-item-company-name'}).get_text(strip=True) if article.find('span', attrs={'data-at': 'job-item-company-name'}) else 'No Company Found'
        location = article.find('span', attrs={'data-at': 'job-item-location'}).get_text(strip=True) if article.find('span', attrs={'data-at': 'job-item-location'}) else 'No Location Found'
        # Find the element containing the job description
        job_description_div = soup.find('div', {'data-at': 'jobcard-content'})
        job_description_text = job_description_div.get_text(strip=True)
        # Print extracted information
        print(f'Job Title: {job_title}')
        print(f'Company: {company_name}')
        print(f'Location: {location}')
        print(f'Job Description: {job_description_text}')
        print('---' * 20)  # Separator for readability


# Close the WebDriver
driver.quit()
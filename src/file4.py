import requests
from bs4 import BeautifulSoup
import json


# beam start job
def process_file4():
    # URL of the careers page
    url = "https://www.dice.com/jobs/q-Full+Stack+Developer-jobs"
    
    # Headers to mimic browser request
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }
    
    # Send GET request
    response = requests.get(url, headers=headers)
    
    # Create BeautifulSoup object
    soup = BeautifulSoup(response.content, 'html.parser')
# Save soup content to a text file
    with open('job page data.txt', 'w', encoding='utf-8') as file:
        file.write(soup.prettify())

    
    job_listings = []

    # Find job cards using the correct class
    job_elements = soup.find_all('dhi-job-search-job-card')
    
    for job in job_elements:
        # Find title and link using the specific structure
        title_element = job.find('h2', class_='job-title')
        if title_element:
            title_link = title_element.find('a', class_='job-title-link')
            if title_link:
                title = title_link.get_text().split('Job Title -')[0].strip()
                link = title_link.get('href')
                
                # Create dictionary for each job
                job_data = {
                    'title': title,
                    'link': link,
                }
                
                job_listings.append(job_data)
    with open('4.json', 'w', encoding='utf-8') as json_file:
        json.dump(job_listings, json_file, indent=4)
    print(f"🚀 Successfully scraped {len(job_listings)} dice fullstack jobs and saved to 4.json")

    return job_listings

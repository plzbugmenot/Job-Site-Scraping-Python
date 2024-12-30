import requests
from bs4 import BeautifulSoup
import json


# paradigm job srap
def process_file2():
    # URL of the careers page
    url = "https://www.paradigm.xyz/careers"
    
    # Headers to mimic browser request
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }
    
    # Send GET request
    response = requests.get(url,  headers=headers)
    
    # Create BeautifulSoup object
    soup = BeautifulSoup(response.content, 'html.parser')
# Save soup content to a text file
    # with open('paradigm_careers.txt', 'w', encoding='utf-8') as file:
    #     file.write(soup.prettify())

    
    # Find all job listings
    job_listings = []

    # Find job sections
    job_elements = soup.find_all('a', class_='link-cover link-underline-hover-large')
    for job in job_elements:
        link = job['href']
        title = job.text.strip()
        
        # Create dictionary for each job
        job_data = {
            'title': title,
            'link': link
        }
        
        # Add job data to listings
        job_listings.append(job_data)
        


    with open('2.json', 'w', encoding='utf-8') as json_file:
        json.dump(job_listings, json_file, indent=4)
    print(f"🚀 Successfully scraped {len(job_listings)} paradigm jobs and saved to 2.json")
    return job_listings

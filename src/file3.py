
import requests
from bs4 import BeautifulSoup
import json

# sui job scrap
def process_file3():
    # URL of the careers page
    url = "https://jobs.sui.io/jobs"
    
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

    
    # Find all job listings
    job_listings = []

    # Find job sections
    job_elements = soup.find_all('div', class_='sc-beqWaB gupdsY job-card')
    for job in job_elements:
        # Find title element
        title_element = job.find('div', {'itemprop': 'title'})
        title = title_element.text.strip() if title_element else ''
        
        # Find link element
        link_element = job.find('a', {'data-testid': 'read-more'})
        link = link_element['href'] if link_element else ''
        
        # Create dictionary for each job
        job_data = {
            'title': title,
            'link': "https://jobs.sui.io/" + link
        }
        
        # Add job data to listings
        job_listings.append(job_data)
        
    with open('3.json', 'w', encoding='utf-8') as json_file:
        json.dump(job_listings, json_file, indent=4)
    print(f"🚀 Successfully scraped {len(job_listings)} sui jobs and saved to 3.json")


    return job_listings



import requests
from bs4 import BeautifulSoup
import json


# beam start job
def process_file1():
    # URL of the careers page
    url = "https://beamstart.com/jobs"
    
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

    # Find job sections - using tr elements
    job_elements = soup.find_all('tr')
    for job in job_elements:
        # Find title and link from h2 > a tag
        title_link = job.find('h2').find('a') if job.find('h2') else None
        
        if title_link:
            title = title_link.text.strip()
            link = title_link['href']
            
            # Create dictionary for each job
            job_data = {
                'title': title,
                'link': f"https://beamstart.com/{link}"
            }
            
            job_listings.append(job_data)
    with open('1.json', 'w', encoding='utf-8') as json_file:
        json.dump(job_listings, json_file, indent=4)
    print(f"🚀 Successfully scraped {len(job_listings)} beamstart jobs and saved to 1.json")

    return job_listings

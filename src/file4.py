import requests
from bs4 import BeautifulSoup
import json


# beam start job
def process_file4():
    all_jobs = []
    
    urls = {
        'fullstack': "https://www.dice.com/jobs/q-Full+Stack+Developer-jobs",
        'web': "https://www.dice.com/jobs/q-Web+Developer-jobs",
        'engineer': "https://www.dice.com/jobs/q-Software+Engineer-jobs",
        'software': "https://www.dice.com/jobs/q-Software+Developer-jobs"
    }
    
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }
    
    for job_type, url in urls.items():
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.content, 'html.parser')
              
        job_listings = []
        job_elements = soup.find_all('dhi-job-search-job-card')
        
        for job in job_elements:
            title_element = job.find('h2', class_='job-title')
            if title_element:
                title_link = title_element.find('a', class_='job-title-link')
                if title_link:
                    title = title_link.get_text().split('Job Title -')[0].strip()
                    link = title_link.get('href')
                    
                    job_data = {
                        'title': title,
                        'link': link,
                    }
                    job_listings.append(job_data)
        
        all_jobs.extend(job_listings)
        print(f"🚀 Successfully scraped {len(job_listings)} dice {job_type} developer jobs")
    
    # Save combined results
    with open('4.json', 'w', encoding='utf-8') as json_file:
        json.dump(all_jobs, json_file, indent=4)
    
    return all_jobs

import requests
from bs4 import BeautifulSoup

def scrape_jobs(job_role, location):
    keywords = job_role.replace(' ', '%20') # To replace the spaces with %20 symbol in the url
    loc = location.replace(' ', '%20')
    url = f"https://www.linkedin.com/jobs-guest/jobs/api/seeMoreJobPostings/search?keywords={keywords}&location={loc}"
    headers = {"User-Agent": "Mozilla/5.0"} 
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    jobs = soup.find_all("li")

    results = []
    for job in jobs:
        title_tag = job.find("h3")
        company_tag = job.find("h4")
        link_tag = job.find("a")
        title = title_tag.get_text(strip=True) if title_tag else ""
        company = company_tag.get_text(strip=True) if company_tag else ""
        link = link_tag['href'] if link_tag else ""
        results.append({"title": title, "company": company, "link": link})
    return results

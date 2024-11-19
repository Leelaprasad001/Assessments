from utils.imports import *

def scrape_website(website_url):
    try:
        response = requests.get(website_url)
        response.raise_for_status()
        soup = BeautifulSoup(response.content, 'html.parser')
        text = soup.get_text(separator="\n", strip=True)
        return text
    except requests.exceptions.RequestException as e:
        print(f"Error scraping website: {e}")
        return None

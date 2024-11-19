from modules.scraper import scrape_website
from modules.processor import process_scraped_data
from modules.api_handler import get_chatgpt_response
from utils.logger import log

def run_chatbot():
    log("Starting chatbot...")

    # Step 1: Scrape the website
    website_url = input("Enter Website URL for Web Scraping: ")
    raw_text = scrape_website(website_url)
    if raw_text:
        # Step 2: Process scraped data
        processed_text = process_scraped_data(raw_text)
        if processed_text:
            # Step 3: Handling ChatGPT Api
            prompt = f"Summarize the following content: {processed_text}"
            chatgpt_response = get_chatgpt_response(prompt)
            print(chatgpt_response)
        else:
            log("Failed to process scraped data.")
            return
    else:
        log("Failed to scrape the website.")
        return
   
if __name__ == "__main__":
    run_chatbot()

# example testing url https://relinns.com/
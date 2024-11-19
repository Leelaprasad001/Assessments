from utils.imports import *

def process_scraped_data(text):
    """
    Perform basic preprocessing on the extracted text.
    This can include removing unnecessary characters, multiple spaces, etc.
    """
    text = text.lower()
    text = re.sub(r'[^a-z0-9\s]', '', text)
    text = re.sub(r'\s+', ' ', text).strip()
    return text

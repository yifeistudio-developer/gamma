import requests
from bs4 import BeautifulSoup

def web_scrap(url: str) -> str:
    try:
        headers = {
            'User-Agent': ('Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
                           'AppleWebKit/537.36 (KHTML, like Gecko)'
                           'Chrome/58.0.3029.110 Safari/537.3'),
            'Accept-Language': 'en-US,en;q=0.9',
        }
        response = requests.get(url, headers=headers, timeout=10)
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            return soup.get_text(separator=' ', strip=True)
        else:
            return f"Error: Could not retrieve the webpage: Status Code {response.status_code}"
    except Exception as e:
        return f"Error: An exception occurred while trying to retrieve the webpage: {str(e)}"
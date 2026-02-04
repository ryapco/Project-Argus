import requests
from bs4 import BeautifulSoup

# The Target: Official Python Standard Library Index
URL = "https://docs.python.org/3/library/index.html"

def fetch_page(url):
    print(f"[CODEX] Fetching {url}...")
    
    # 1. Use the 'requests' library to GET the page
    # Hint: response = requests.____(url)
    response = requests.get(url)
    
    # 2. Check the Status Code
    # In HTTP, 200 means "OK". 404 means "Not Found".
    # We only want to proceed if it is 200.
    if response.status_code != 200:
        print(f"[ERROR] Failed to fetch. Status Code: {response.status_code}")
        return None
        
    return response.text

def parse_titles(html_content):
    print("[CODEX] Parsing content...")
    
    # 3. Initialize the Soup (The Parser)
    soup = BeautifulSoup(html_content, "html.parser")
    
    # 4. Extract Data
    # The Python docs use <h2> tags for section headers.
    # Let's find all of them.
    sections = soup.find_all("li", class_="toctree-l1")
    
    print(f"--- FOUND {len(sections)} SECTIONS ---")
    
    for section in sections[:5]:  # Just print the first 5 to keep it clean
        # .get_text() strips the HTML tags (<a>, <b>) leaving just the words.
        print(f" > {section.get_text().strip()}")

def main():
    # Step A: Get the raw HTML
    html = fetch_page(URL)
    
    if html:
        # Step B: Parse it if it arrived safely
        parse_titles(html)

if __name__ == "__main__":
    main()
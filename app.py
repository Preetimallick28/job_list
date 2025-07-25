import requests
from bs4 import BeautifulSoup
import re

# List of websites to check
websites = [
    "https://example.com",
    "https://another-example.com",
    # Add more websites here
]

# Regex pattern to match LinkedIn URLs
linkedin_pattern = re.compile(r'https?://(www\.)?linkedin\.com/in/[^\s"\'<>]+')

# Output file
output_file = "linkedin_links.txt"

# Clear previous content
with open(output_file, "w") as file:
    file.write("")

# Function to get LinkedIn links from a URL
def get_linkedin_links(url):
    try:
        response = requests.get(url, timeout=10)
        soup = BeautifulSoup(response.text, "html.parser")
        links = soup.find_all("a", href=True)
        for link in links:
            href = link["href"]
            match = linkedin_pattern.search(href)
            if match:
                return match.group(0)
    except Exception as e:
        print(f"Error with {url}: {e}")
    return None

# Main logic
for site in websites:
    linkedin_url = get_linkedin_links(site)
    if linkedin_url:
        print(f"✅ Found: {linkedin_url}")
        with open(output_file, "a") as file:
            file.write(linkedin_url + "\n")
    else:
        print(f"❌ No LinkedIn URL found on {site}")

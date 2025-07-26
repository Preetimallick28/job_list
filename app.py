import requests
from bs4 import BeautifulSoup
import re

# Input and Output files
input_file = "input_websites.txt"
output_file = "linkedin_links.txt"

# Read websites from input file
with open(input_file, "r") as file:
    websites = [line.strip() for line in file if line.strip()]

# Clear previous content from output file
with open(output_file, "w") as file:
    file.write("")

# Function to extract LinkedIn links
def get_linkedin_links(url):
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/115 Safari/537.36'
        }
        response = requests.get(url, headers=headers, timeout=10)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            linkedin_links = []

            for a_tag in soup.find_all('a', href=True):
                href = a_tag['href'].strip()
                # Match any LinkedIn domain (www.linkedin.com, in.linkedin.com, etc.)
                if re.match(r'https?://(www\.|in\.)?linkedin\.com/[^\s"\'<>]+', href, re.IGNORECASE):
                    linkedin_links.append(href)

            return list(set(linkedin_links))  # Unique links
        else:
            print(f"🔴 Error fetching {url}: Status code {response.status_code}")
    except Exception as e:
        print(f"🔴 Error with {url}: {e}")
    return []

# Main logic
for site in websites:
    linkedin_urls = get_linkedin_links(site)
    if linkedin_urls:
        print(f"✅ LinkedIn URLs found on {site}:")
        with open(output_file, "a") as file:
            for link in linkedin_urls:
                print(f"   - {link}")
                file.write(f"{link}\n")
    else:
        print(f"❌ No LinkedIn URL found on {site}")

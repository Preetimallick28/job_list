import requests
from bs4 import BeautifulSoup
import re

# List of websites to check
websites = [
    "http://askmeguru.com/",
    "https://www.jnettechnologies.com/",
    "https://www.sparity.com/",
    "https://conquerorstech.net/",
    "http://www.brainovision.in/",
    "https://axassoftware.com/",
    "http://www.magneqservices.in/",
    "https://raybiztech.com/",
    "https://www.encora.com/",
    "https://www.foraysoft.com/",
    "https://www.avineon.com/en/apac/home",
    "http://oracle.com/",
    "http://www.eurekaitsol.com/",
    "http://tstecnoservice.com/",
    "http://www.experienceflow.ai/",
    "https://greemus.com/",
    "https://www.sisfirst.in/",
    "http://www.pronteff.com/",
    "https://www.savantis.com/",
    "http://www.triloksoft.com/",
    "http://www.metanoiasolutions.net/",
    "http://www.shrasits.com/",
    "https://techclouderp.com/",
    "http://hgtechinc.net/",
    "https://danyonittech.in/",
    "https://www.elitecrest.in/",
    "https://www.creativetechmars.com/",
    "https://zenq.com/",
    "https://www.suchirsoftech.com/",
    "https://techweblabs.com/",
    "http://www.tecnics.com/",
    "https://elabsinfotech.com/",
    "https://tekbon.com/",
    "https://www.webappclouds.com/",
    "http://www.zazz.io/",
    "http://scienstechnologies.com/",
    "https://www.iblesoft.com/",
    "https://www.mwebware.com/",
    "http://vagarioussolutions.com/",
    "https://fission.it/",
    "http://www.c2n.in/",
    "http://www.megasoft.com/",
    "http://www.acuvate.com/",
    "http://vortextechnologies.net/",
    "https://camelq.in/",
    "https://www.kexlin.com/",
    "https://www.techbulls.co.in/",
    "http://www.sanoits.com/",
    "http://votigo.com/",
    "https://www.snovasys.com/",
    "https://www.pramati.com/"
]

# Output file
output_file = "linkedin_links.txt"

# Clear previous content
with open(output_file, "w") as file:
    file.write("")

# Function to get all LinkedIn links from the HTML content using BeautifulSoup
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
                # Match any LinkedIn domain including in.linkedin.com, www.linkedin.com, etc.
                if re.match(r'https?://(www\.|in\.)?linkedin\.com/[^\s"\'<>]+', href, re.IGNORECASE):
                    linkedin_links.append(href)

            return list(set(linkedin_links))  # Unique list
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
        for link in linkedin_urls:
            # print(f"   - {link}")
            with open(output_file, "a") as file:
                file.write(f"{link}\n")
    else:
        print(f"❌ No LinkedIn URL found on {site}")

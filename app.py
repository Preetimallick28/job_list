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


# Regex pattern to match LinkedIn URLs
linkedin_pattern = re.compile(r'https?://([a-z]+\.)?linkedin\.com/(in|company)/[^\s"\'<>]+')

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

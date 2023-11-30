import requests
from bs4 import BeautifulSoup

url = "https://www.1mg.com/all-diseases"
response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, "html.parser")

    # Now, you can navigate the HTML structure to find and extract data.
    # For example, let's extract all the links on the page:
    links = soup.find_all("a")
    for link in links:
        print(link.get("href"))

    # You might need to inspect the HTML structure of the page you're scraping
    # and adjust the code accordingly.

else:
    print(f"Failed to retrieve the page. Status code: {response.status_code}")

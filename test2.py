def crawl(url):
    import requests
    from bs4 import BeautifulSoup

    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")

        links = soup.find_all("a")
        for link in links:
            print(link.get("href"))

    else:
        print(f"Failed to retrieve the page. Status code: {response.status_code}")

crawl("https://www.1mg.com/all-diseases/?label=a")
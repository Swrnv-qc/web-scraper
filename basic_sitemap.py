import requests
import csv
import xml.etree.ElementTree as ET

def get_sitemap_urls(url):
    response = requests.get(url)

    if response.status_code == 200:
        # Parse the XML content
        root = ET.fromstring(response.content)

        # Extract sitemap URLs
        sitemap_urls = [element.text for element in root.iter("{http://www.sitemaps.org/schemas/sitemap/0.9}loc")]

        return sitemap_urls
    else:
        print(f"Error: Unable to retrieve sitemap from {url}")
        return None

def write_to_csv(file_path, data):
    with open(file_path, 'w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(["Sitemap URLs"])
        csv_writer.writerows([[url] for url in data])

# Example usage
website_url = "https://1mg.com"
sitemap_urls = get_sitemap_urls(f"{website_url}/sitemap.xml")

if sitemap_urls:
    print("Sitemap URLs:")
    for url in sitemap_urls:
        print(url)

    # Write URLs to CSV file
    csv_file_path = "sitemap_urls.csv"
    write_to_csv(csv_file_path, sitemap_urls)
    print(f"\nSitemap URLs written to {csv_file_path}")

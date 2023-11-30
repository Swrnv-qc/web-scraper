import requests

def download_html(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an HTTPError for bad responses

        html_content = response.text
        return html_content
    except requests.exceptions.RequestException as e:
        print(f"Error downloading HTML: {e}")
        return None

def save_to_html_file(html_content, filename="output.html"):
    try:
        with open(filename, "w", encoding="utf-8") as file:
            file.write(html_content)
        print(f"HTML content saved to {filename}")
    except Exception as e:
        print(f"Error saving HTML to file: {e}")

# Example usage:
url = "https://www.1mg.com/diseases/hair-loss-77"
html_content = download_html(url)

if html_content:
    save_to_html_file(html_content)
else:
    print("Failed to download HTML.")
import csv
import requests
from bs4 import BeautifulSoup

# Define the target URL (a public sandbox site for scraping practice)
URL = "http://toscrape.com"


def scrape_quotes(url):
    print(f"Connecting to {url}...")

    # Send an HTTP GET request to the website
    response = requests.get(url)

    # Check if the connection was successful
    if response.status_code != 200:
        print(f"Failed to retrieve data. Status code: {response.status_code}")
        return []

    # Parse the raw HTML content using BeautifulSoup
    soup = BeautifulSoup(response.text, "html.parser")

    # Find all HTML containers holding the quotes
    quote_elements = soup.find_all("div", class_="quote")
    dataset = []

    print(f"Successfully connected! Extracting data...")

    # Loop through each element to extract specific text fields
    for element in quote_elements:
        # Extract the main quote text
        text = element.find("span", class_="text").text.strip()

        # Extract the author's name
        author = element.find("small", class_="author").text.strip()

        # Extract all tags associated with the quote
        tags_meta = element.find("div", class_="tags").find_all(
            "a", class_="tag"
        )
        tags = [tag.text.strip() for tag in tags_meta]
        tags_str = ", ".join(tags)  # Combine tags into a single string

        # Append the extracted row to our dataset list
        dataset.append({"Quote": text, "Author": author, "Tags": tags_str})

    return dataset


def save_to_csv(data, filename="scraped_quotes.csv"):
    if not data:
        print("No data to save.")
        return

    # Define the column headers for the CSV
    headers = ["Quote", "Author", "Tags"]

    # Write the data to a CSV file
    with open(filename, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=headers)
        writer.writeheader()
        writer.writerows(data)

    print(f"Success! Custom dataset created and saved to '{filename}'.")


# --- Main Execution ---
if __name__ == "__main__":
    # 1. Scrape the data
    scraped_data = scrape_quotes(URL)

    # 2. Save to a CSV dataset
    save_to_csv(scraped_data)

# imports
from bs4 import BeautifulSoup
import cloudscraper
import csv
import os

URL = "https://breakingbad.fandom.com/wiki/Category:Breaking_Bad_Characters"
OUTPUT_FILE = "breaking_bad_characters.csv"

# Create one cloudscraper instance to reuse for all requests
scraper = cloudscraper.create_scraper()

def fetch_page(url):
    response = scraper.get(url, timeout=10)
    return response

# Parse the characters from the response
def parse_characters(response):
    soup = BeautifulSoup(response.text, "html.parser")
    characters = []

    # Fandom category pages usually store the actual category entries here
    member_links = soup.find_all("a", class_="category-page__member-link")
    print(f"\nFound {len(member_links)} category member link(s) on the page.")

    for link in member_links:
        name = link.get_text(strip=True)
        href = link.get("href")

        if not name or not href:
            continue

        # Skip obvious non-character pages
        bad_words = [
            "season", "episode", "category", "talk", "template",
            "user", "blog", "help", "file", "list of"
        ]
        lower_name = name.lower()
        lower_href = href.lower()

        if any(word in lower_name for word in bad_words):
            continue
        if any(word in lower_href for word in bad_words):
            continue

        full_link = "https://breakingbad.fandom.com" + href

        characters.append({
            "character_name": name,
            "character_link": full_link
        })

    # Remove duplicates while keeping order
    seen = set()
    unique_characters = []

    for character in characters:
        key = (character["character_name"], character["character_link"])
        if key not in seen:
            seen.add(key)
            unique_characters.append(character)

    print(f"Total characters extracted: {len(unique_characters)}\n")
    return unique_characters

# Save the results to a CSV file
def save_to_csv(characters, filename):
    filepath = os.path.abspath(filename)

    with open(filepath, "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        # header row
        writer.writerow(["character_name", "character_link"])
        for character in characters:
            writer.writerow([character["character_name"], character["character_link"]])

    print(f"Saved to: {filepath}")
    print(f"Total rows: {len(characters)}")

# Preview the results
def preview_results(characters, n=10):
    print(f"Preview: First {n} entries")
    for character in characters[:n]:
        print(f"  {character['character_name']:<30} {character['character_link']}")

def main():
    print("Breaking Bad — Character Scraper")

    response = fetch_page(URL)
    characters = parse_characters(response)
    preview_results(characters)
    save_to_csv(characters, OUTPUT_FILE)

if __name__ == "__main__":
    main()
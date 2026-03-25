# Breaking Bad — Fandom Wiki Character Scraper

## Wiki Chosen
Wiki: Breaking Bad Fandom Wiki  
Page scraped: https://breakingbad.fandom.com/wiki/Category:Breaking_Bad_Characters  
Robots.txt: https://breakingbad.fandom.com/robots.txt  
Content license: CC-BY-SA

## Terms of Service & robots.txt
The robots.txt file at https://breakingbad.fandom.com/robots.txt was reviewed before scraping.

User-agent: * — general crawlers are permitted by default.  
Some specific bots such as SemrushBot and GPTBot are blocked, but those restrictions do not apply to this script.

The page used in this project is located at:
/wiki/Category:Breaking_Bad_Characters

The robots.txt file does not disallow the /wiki/ path or /wiki/Category: pages, meaning this page can be accessed by general crawlers.

Content on Fandom wikis is published under a CC-BY-SA license, which allows reuse with attribution.  
This script follows the guidelines provided in the robots.txt file and accesses only the specified page.

## Why Breaking Bad?
Breaking Bad is one of the most popular modern television dramas and has a large fan community that maintains detailed documentation of characters and storylines through the fandom wiki.

The Breaking Bad fandom wiki organizes characters into structured category pages, which makes it a good example of how fan communities document and structure information about media franchises.

## What is being scraped?
From the Breaking Bad character category page, the script collects:

character_name — the name of the character (e.g. Walter White, Jesse Pinkman)  
character_link — the direct wiki link to that character's page  

These values are extracted using BeautifulSoup and saved into a CSV file.

## Why might this data interest researchers?

Media and television studies  
Researchers studying television narratives could use character lists to analyze the structure of a show’s cast or identify major and minor characters.

Network analysis  
Character datasets can be used to build character relationship networks, where nodes represent characters and edges represent interactions between them.

Fandom documentation practices  
Fan-maintained wikis like this one demonstrate how communities organize and preserve information about popular media franchises.

## Requirements
Python 3.7+

Libraries used:

cloudscraper — used instead of standard requests because Fandom sites are protected by Cloudflare, which can block normal requests  
beautifulsoup4 — used to parse the HTML and extract character information  

Install dependencies with your virtual environment active:

pip install cloudscraper beautifulsoup4

## How to Run

Activate your virtual environment (Mac/Linux):

source .is310-venv/bin/activate

Run the scraper:

python fandom_wiki_scraping.py

The script prints progress in the terminal and saves the CSV file in the same directory.

## Output

The script produces breaking_bad_characters.csv with the following columns:

character_name — the name of the character  
character_link — link to the character's wiki page  

Sample output:

character_name,character_link
Walter White,https://breakingbad.fandom.com/wiki/Walter_White
Jesse Pinkman,https://breakingbad.fandom.com/wiki/Jesse_Pinkman
Skyler White,https://breakingbad.fandom.com/wiki/Skyler_White
Hank Schrader,https://breakingbad.fandom.com/wiki/Hank_Schrader


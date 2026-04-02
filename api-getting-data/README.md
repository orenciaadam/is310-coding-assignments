## APIs Used
- **Data USA**: https://datausa.io/about/api
- **Europeana**: https://pro.europeana.eu/page/apis

## Why Data USA?
Data USA is a free, public API with no authentication required for basic use. It provides access to a wide range of U.S. demographic and economic data from sources like the Census Bureau. I chose it because:
- It requires **no API key**, making it easy to work with right away
- The documentation is clear and well-structured
- It connects naturally to Europeana — U.S. states are real places with rich cultural histories

My script fetches the top 10 U.S. states by population in 2023, then searches the Europeana cultural heritage collection for images related to the most populous state (California).

## How to Run

1. Install dependencies:
pip install requests pyeuropeana python-dotenv Pillow

2. Fix numpy if you run into a binary incompatibility error:
pip uninstall numpy
pip install numpy==1.26.4

3. Create a `.env` file in this folder with your Europeana API key:
EUROPEANA_API_KEY=your-key-here

4. Run:
python getting_culture.py

5. Hide your api key:
Use a .gitignore


## Output
Saves combined results from both APIs to `datausa_europeana_results.json`.

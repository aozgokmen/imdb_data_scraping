
# IMDb Top Movies Scraper

## Overview
This Python script scrapes the IMDb Top Rated Movies page to extract information about the movies, including their titles and ratings. The data is then organized into a DataFrame using Pandas, making it easy to handle and analyze the movie data.

## Features
- Scrapes the IMDb Top Rated Movies page.
- Extracts movie titles and ratings.
- Creates a Pandas DataFrame with the extracted data.
- Handles HTTP requests and parses HTML content.

## Requirements
- Python 3.x
- Libraries: requests, BeautifulSoup4, pandas, re

## Installation
1. Ensure Python 3.x is installed on your system.
2. Install the required Python libraries using pip:
   ```bash
   pip install requests beautifulsoup4 pandas
   ```
3. Clone or download this repository.

## Usage
Run the script with Python:
```bash
python imdb_scraper.py
```
The script will output a DataFrame containing the titles and ratings of the top-rated movies on IMDb.

## Code Structure
- The `requests` library is used to fetch the web page content.
- `BeautifulSoup` from `bs4` is utilized for parsing HTML content.
- The `pandas` library is used for creating and managing the DataFrame.
- Regular expressions (`re` module) are used for text processing.

## Contributing
Contributions to improve the script or extend its functionality are welcome. Please follow these steps to contribute:
1. Fork the repository.
2. Create your feature branch.
3. Commit your changes.
4. Push to the branch.
5. Create a new Pull Request.

import requests
from bs4 import BeautifulSoup

# Send a GET request to the IMDb Top 250 Movies page
url = "https://www.imdb.com/chart/top/"
response = requests.get(url)

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(response.content, "html.parser")

# Find the table containing the movie information
table = soup.find("table", class_="chart")

# Find all the rows in the table (excluding the header row)
rows = table.find_all("tr")[1:]

# Iterate over the rows and extract movie information
for row in rows:
    # Find the movie title within the row
    title_column = row.find("td", class_="titleColumn")
    movie_title = title_column.a.text

    # Find the movie year within the row
    year_column = row.find("span", class_="secondaryInfo")
    movie_year = year_column.text

    # Find the movie rating within the row
    rating_column = row.find("td", class_="ratingColumn imdbRating")
    movie_rating = rating_column.strong.text



    # Print the movie title and rating
    print(f"Title: {movie_title}")
    print(f"Title: {movie_year}")
    print(f"Rating: {movie_rating}")
    print("------------------------")

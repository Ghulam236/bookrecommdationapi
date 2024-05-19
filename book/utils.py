

import requests

GOOGLE_BOOKS_API_URL = "https://www.googleapis.com/books/v1/volumes"
API_KEY = 'AIzaxyB7noKrgFi21BfgHInorZuA34'

def fetch_book_data(query,author=None,category=None):
    params = {'q': query, 'key': API_KEY}
    if author:
        params['q'] += f'+inauthor:{author}'
    if category:
        params['q'] += f'+subject:{category}'
    response = requests.get(GOOGLE_BOOKS_API_URL, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        return {'error': 'Failed to fetch data from Google Books API'}

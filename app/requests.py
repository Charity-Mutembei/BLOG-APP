import requests
from .models import Quote

url = "http://quotes.stormconsultancy.co.uk/random.json"

def quotes():
    '''
    '''
    response = requests.get(url).json()
    random_quotes = Quote (response.get('author'), response.get('quote'))
    return random_quotes
from urllib import response

from flask import request
import requests
import json, urllib
from .models import Quote

base_url = "http://quotes.stormconsultancy.co.uk/random.json"

def get_quote ():
    '''
    Returns the random quotes from the quotes api provided 
    '''


    with urllib.request.urlopen(get_quote) as url:
        get_quote_data = url.read()
        get_quote_response = json.loads(get_quote_data)

        quote_results = None


        if get_quote_response['results']:
            quote_results_list =  get_quote_response['results']
            quote_results = process_results(quote_results_list)

    # response = request.args.get(base_url).json()
    # random_quote = Quote(response.get('author'), response.get('quote'))

    return quote_results


def process_results(quote_list):

    '''
    Function  that processes the quote result and transform them to a list of Objects

    Args:
        quote_list: A list of dictionaries that contain quote details

    Returns :
        quote_results: A list of quote objects
    '''

    quote_results = []
    for quote_item in quote_list:
        id = quote_item.get('id')
        title = quote_item.get('original_title')


    return quote_results
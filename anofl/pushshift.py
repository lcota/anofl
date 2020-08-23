from enum import Enum
import requests


def get_push_shift_data(data_type, **kwargs):
    """Returns results from a pushshift.io query
    """
    # Note: using f"" strings automatically calls format() with named arguments
    # taken from the current namespace
    query_url = f"https://api.pushshift.io/reddit/search/{data_type}/"
    search_args = kwargs
    request = requests.get(query_url, params=search_args)
    return request.json()
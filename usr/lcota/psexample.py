# Examples querying pushshift.io for reddit data
# Tutorial from: https://www.jcchouinard.com/how-to-use-reddit-api-with-python/

# Creating a simple wrapper around Pushshift Reddit API
from enum import Enum
import requests

class DataTypes(Enum):
    COMMENT = 'comment'
    POST = 'submission'


def get_push_shift_data(data_type, **kwargs):
    """Returns results from a pushshift.io query
    """
    # Note: using f"" strings automatically calls format() with named arguments
    # taken from the current namespace
    query_url = f"https://api.pushshift.io/reddit/search/{data_type}/"
    search_args = kwargs
    request = requests.get(query_url, params=search_args)
    return request.json()


# parameters for pushshift.io
# Full list: https://pushshift.io/api-parameters/
data_type = "comment"   # can be "comment" or "submission"
query = "liberals"      # search string
duration = "30d"        # sets a time frame
size = "1000"           # Sets a maximum amount of comments to return
sort_type = "score"     # Options: "score", "num_comments", "created_utc"
sort = "desc"
aggs = "subreddit"       # groupings, options: "author", "link_id", "created_utc", "subreddit"


data = get_push_shift_data(data_type=data_type,
                           q = query,
                           after = duration,
                           sort_type = "score",
                           sort = "desc",
                           size = size)


# Query retrieves sorted list of forums sorted by number of appearances
# of word "liberals" over the past 30 days
aggdata = get_push_shift_data(data_type=data_type,
                            q = query,
                            after = duration,
                            size = size,
                            aggs = aggs)

data = aggdata.get("aggs").get(aggs)
data
import httpx
import json
from rich import print as rprint
from api_keys import go_rest_key

headers = {'Accept': 'application/json',
           'Content-Type': 'application/json',
           'Authorization': f'Bearer {go_rest_key}',
           }

my_url = 'https://gorest.co.in/public/v2/users'

def pull_info(url):
    with httpx.Client() as client:
        response = json.loads(client.get(url, headers=headers).text)
        return response

results = pull_info(my_url)
rprint(results)

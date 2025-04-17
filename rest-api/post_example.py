import json
import httpx
from rich import print as rprint
from api_keys import go_rest_key

headers = {'Accept': 'application/json', 
           'Content-Type': 'application/json', 
           'Authorization': f'Bearer {go_rest_key}',
           }

my_url = 'https://gorest.co.in/public/v2/users'

payload = {"name": "Scott Funke", 
           "gender": "male", 
           "email": "sfunke@email2.com", 
           "status": "active"}

payload_json = json.dumps(payload)

def post_user(headers, url, user_info):
    with httpx.Client() as client:
        response = client.post(url, headers=headers, data=user_info)
        structured_response = json.loads(response.text)
        return response, structured_response
    
response = post_user(headers, my_url, payload_json)

rprint(response)

import requests
import json

class GetRequester:

    def __init__(self, URL):
        URL = 'https://learn-co-curriculum.github.io/json-site-example/endpoints/people.json'
        self.url = URL

    def get_response_body(self,URL):
     response = requests.get(URL)
     return response.content

    def load_json(self):
        pass
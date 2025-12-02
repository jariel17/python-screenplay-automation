import requests

class CallAPI:
    def __init__(self, base_url):
        self.base_url = base_url.rstrip("/")

    def post(self, endpoint, json=None, headers=None):
        return requests.post(
            f"{self.base_url}{endpoint}", 
            json=json,
            headers=headers, 
            timeout=30
            )

    def get(self, endpoint, headers=None):
        return requests.get(
            f"{self.base_url}{endpoint}", 
            headers=headers, 
            timeout=30
            )
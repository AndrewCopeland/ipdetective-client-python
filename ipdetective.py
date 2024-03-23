import requests

class IPDetective:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = "https://api.ipdetective.io/ip"

    def GetIpInfo(self, ip_address):
        headers = {'x-api-key': self.api_key}
        url = f"{self.base_url}/{ip_address}?info=true"
        response = requests.get(url, headers=headers)
        if response.status_code >=500:
            return {"error": "Internal server error occured"}
        return response.json()

    def GetBulkIpInfo(self, ip_addresses):
        headers = {'x-api-key': self.api_key}
        url = f"{self.base_url}?info=true"
        response = requests.post(url, headers=headers, json=ip_addresses)
        if response.status_code >=500:
            return {"error": "Internal server error occured"}
        return response.json()

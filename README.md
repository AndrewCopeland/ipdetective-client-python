# IPDetective Client
IPDetective is an API that focuses on bot and non-human IP detection to quickly identify if an IP address comes from a datacenter, VPN or proxy. You can signup to the free API by simply signing in to access your API key. IPDetective tracks over 1000 ASNs and detects over 250 million IP addresses as non-human users from +100 different origins, ranging from data centers, botnets, proxies and vpns.

## Features
- IP Bot Detection
- IP Geolocation
- IP ASN

## Usage
```python3
import os
from ipdetective import IPDetective

def main():
    api_key = os.getenv('IPDETECTIVE_API_KEY')
    ip_client = IPDetective(api_key)
    ip_address = '8.8.8.8'
    ip_info = ip_client.GetIpInfo(ip_address)
    print(ip_info)

if __name__ == "__main__":
    main()
```
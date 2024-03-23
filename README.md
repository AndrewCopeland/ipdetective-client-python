# IPDetective Client
[IPDetective](https://ipdetective.io) is an API that focuses on bot and non-human IP detection to quickly identify if an IP address comes from a datacenter, VPN or proxy. You can signup to the free API by simply signing in to access your API key. IPDetective tracks over 1000 ASNs and detects over 250 million IP addresses as non-human users from +100 different origins, ranging from data centers, botnets, proxies and vpns.

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
    
    # Get information about a singular IP address
    ip_info = ip_client.GetIpInfo('8.8.8.8')
    print(ip_info)
    # {'ip': '8.8.8.8', 'bot': True, 'type': 'bot', 'asn': 15169, 'asn_description': 'GOOGLE', 'country_code': 'US', 'country_name': 'United States of America'}

    # Get information about build IP addresses
    bulk_ip_info = ip_client.GetBulkIpInfo(['8.8.8.8', '1.1.1.1'])
    print(bulk_ip_info)
    # [{'ip': '1.1.1.1', 'bot': True, 'type': 'bot', 'asn': 13335, 'asn_description': 'CLOUDFLARENET', 'country_code': 'US', 'country_name': 'United States of America'}, {'ip': '8.8.8.8', 'bot': True, 'type': 'bot', 'asn': 15169, 'asn_description': 'GOOGLE', 'country_code': 'US', 'country_name': 'United States of America'}]

if __name__ == "__main__":
    main()
```

[Check out our website](https://ipdetective.io)
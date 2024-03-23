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
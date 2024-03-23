import os
from ipdetective import IPDetective
def main():
    api_key = os.getenv('IPDETECTIVE_API_KEY')
    ip_client = IPDetective(api_key)
    
    # Get information about a singular IP address
    ip_info = ip_client.GetIpInfo('8.8.8.8')
    print(ip_info)

    # Get information about build IP addresses
    bulk_ip_info = ip_client.GetBulkIpInfo(['8.8.8.8', '1.1.1.1'])
    print(bulk_ip_info)

if __name__ == "__main__":
    main()
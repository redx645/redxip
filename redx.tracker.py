import requests


print("""
\033[1;32m
 
██╗██████╗░
██║██╔══██╗
██║██████╔╝
██║██╔═══╝░
██║██║░░░░░
╚═╝╚═╝░░░░░

░█████╗░██████╗░██████╗░██████╗░███████╗░██████╗
██╔══██╗██╔══██╗██╔══██╗██╔══██╗██╔════╝██╔════╝
███████║██║░░██║██║░░██║██████╔╝█████╗░░╚█████╗░
██╔══██║██║░░██║██║░░██║██╔══██╗██╔══╝░░░╚═══██╗
██║░░██║██████╔╝██████╔╝██║░░██║███████╗██████╔╝
╚═╝░░╚═╝╚═════╝░╚═════╝░╚═╝░░╚═╝╚══════╝╚═════╝░
              Created By RedX_64
███████╗██╗███╗░░██╗██████╗░███████╗██████╗░
██╔════╝██║████╗░██║██╔══██╗██╔════╝██╔══██╗
█████╗░░██║██╔██╗██║██║░░██║█████╗░░██████╔╝
██╔══╝░░██║██║╚████║██║░░██║██╔══╝░░██╔══██╗
██║░░░░░██║██║░╚███║██████╔╝███████╗██║░░██║
╚═╝░░░░░╚═╝╚═╝░░╚══╝╚═════╝░╚══════╝╚═╝░░╚═╝
\033[0m
""")

def get_location_details(ip_address):
    """
    Fetch location details for the given IP address.
    
    Args:
    ip_address (str): The IP address to fetch details for.
    
    Returns:
    dict: A dictionary containing the location details.
    """
    url = f"http://ip-api.com/json/{ip_address}"
    response = requests.get(url)
    
    if response.status_code == 200:
        return response.json()
    else:
        return None

def print_location_details(location_details):
    """
    Print location details in a readable format.
    
    Args:
    location_details (dict): A dictionary containing the location details.
    """
    print("\033[1;32m[?] Location Details:")
    print(f"[+] Query: {location_details.get('query', 'Not available')}")
    print(f"[+] Status: {location_details.get('status', 'Not available')}")
    print(f"[+] Continent: {location_details.get('continent', 'Not available')}")
    print(f"[+] Continent Code: {location_details.get('continentCode', 'Not available')}")
    print(f"[+] Country: {location_details.get('country', 'Not available')}")
    print(f"[+] Country Code: {location_details.get('countryCode', 'Not available')}")
    print(f"[+] Region: {location_details.get('region', 'Not available')}")
    print(f"[+] Region Name: {location_details.get('regionName', 'Not available')}")
    print(f"[+] City: {location_details.get('city', 'Not available')}")
    print(f"[+] District: {location_details.get('district', 'Not available')}")
    print(f"[+] Zip: {location_details.get('zip', 'Not available')}")
    print(f"[+] Latitude: {location_details.get('lat', 'Not available')}")
    print(f"[+] Longitude: {location_details.get('lon', 'Not available')}")
    print(f"[+] Timezone: {location_details.get('timezone', 'Not available')}")
    print(f"[+] Offset: {location_details.get('offset', 'Not available')}")
    print(f"[+] Currency: {location_details.get('currency', 'Not available')}")
    print(f"[+] ISP: {location_details.get('isp', 'Not available')}")
    print(f"[+] Organization: {location_details.get('org', 'Not available')}")
    print(f"[+] AS: {location_details.get('as', 'Not available')}")
    print(f"[+] AS Name: {location_details.get('asname', 'Not available')}")
    print(f"[+] Mobile: {location_details.get('mobile', 'Not available')}")
    print(f"[+] Proxy: {location_details.get('proxy', 'Not available')}")
    print(f"[+] Hosting: {location_details.get('hosting', 'Not available')}")
    print("\033[0m")

def main():
    ip_address = input("\033[1;32m[?] Enter IP Address: \033[0m")
    location_details = get_location_details(ip_address)
    
    if location_details:
        print_location_details(location_details)
    else:
        print("\033[1;31m[!] Failed to retrieve location details.\033[0m")

if __name__ == "__main__":
    main()

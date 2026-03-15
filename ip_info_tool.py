import requests

# requesting IP
ip_address = input("Enter IP address: ")

# making a request to ipinfo API
url = f"https://ipinfo.io/{ip_address}/json"
response = requests.get(url)

# if successful
if response.status_code == 200:
    data = response.json()  # get data in JSON format
    # displaying info
    print(f"IP: {data.get('ip', 'Unknown')}")
    print(f"Country: {data.get('country', 'Unknown')}")
    print(f"City: {data.get('city', 'Unknown')}")
    print(f"Provider: {data.get('org', 'Unknown')}")
else:
    print("Unable to retrieve information on this IP.")

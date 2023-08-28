import requests


def get_public_ip():
    site = "https://api.ipify.org/?format=json"  #Get the public IP address of my own laptop.
    response = requests.get(site)  # Send an HTTP GET request to the IP address retrieval API
    if response.status_code == 200:  # Check if the request was successful (HTTP status code 200)
        return response.json()["ip"]  # Extract the "ip" value from the JSON response
    else:
        raise Exception("Could not get public IP address.")  # Raise an exception if the request was not successful


if __name__ == "__main__":
    loc = requests.get('https://ipinfo.io/'+get_public_ip()+'/geo')
    print(loc.json())
import requests

urls = ["https://google.com", "https://github.com", "https://thisisnotarealwebsite123456.com"]

for url in urls:
    try:
        response = requests.get(url, timeout=5)
        if response.status_code == 200:
            print(f"{url} is UP")
        else:
            print(f"{url} is DOWN (status code: {response.status_code})")
    except requests.exceptions.RequestException:
        print(f"{url} is DOWN (no response)")
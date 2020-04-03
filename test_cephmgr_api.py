import requests
result = requests.get(
    'http://192.168.191.135:8003/config/cluster',
    verify=False,
    auth=("api", "a9a555e3-9b46-4feb-8d01-143a90bd8b82")
)

print(result.json())
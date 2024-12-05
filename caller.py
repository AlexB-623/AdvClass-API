import requests

core_url = "http://127.0.0.1:8000/api?w="
query = "abandoned industrial site"
callable_url = core_url + query

response = requests.get(callable_url)
response_dict = response.json()
defined = response_dict["definition"][0]
print(defined)
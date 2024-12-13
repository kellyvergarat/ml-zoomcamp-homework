import requests

url = 'http://localhost:8080/2015-03-31/functions/function/invocations'

data = {'url':'https://habrastorage.org/webt/yf/_d/ok/yf_dokzqy3vcritme8ggnzqlvwa.jpeg'}

result = requests.post(url, json=data).json()
print(result)

# response = requests.post(url, json=data)
# print("Response status code:", response.status_code)
# print("Response text:", response.text)

# try:
#     result = response.json()
#     print("Result:", result)
# except requests.exceptions.JSONDecodeError as e:
#     print("JSON decode error:", e)
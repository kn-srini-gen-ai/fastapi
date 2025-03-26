import requests

headers = {"Content-Type": "application/json"}
url = "http://127.0.0.1:8000/add"
data = {"num1": 15.0, "num2": 3.0}
# added in f4@main

response = requests.post(url, headers=headers, json=data)
print("Add Test Response:", response.json())
print(response.status_code)



headers = {"Content-Type": "application/json"}
url = "http://127.0.0.1:8000/multiply"
data = {"num1": 15.0, "num2": 3.0}

response = requests.post(url, headers=headers, json=data)
print("Multiply Test Response:", response.json())
print(response.status_code)



headers = {"Content-Type": "application/json"}
url = "http://127.0.0.1:8000/add"
data = {"num1": -5.0, "num2": -3.0}

response = requests.post(url, headers=headers, json=data)
print("Add Negative Numbers Test Response:", response.json())
print(response.status_code)





headers = {"Content-Type": "application/json"}
url = "http://127.0.0.1:8000/multiply"
data = {"num1": -5.0, "num2": 3.0}

response = requests.post(url, headers=headers, json=data)
print("Multiply Negative Numbers Test Response:", response.json())
print(response.status_code)



headers = {"Content-Type": "application/json"}
url = "http://127.0.0.1:8000/add"
data = {"num1": 5.5, "num2": 3.2}

response = requests.post(url, headers=headers, json=data)
print("Add Decimal Numbers Test Response:", response.json())
print(response.status_code)
#added f4@min



headers = {"Content-Type": "application/json"}
url = "http://127.0.0.1:8000/multiply"
data = {"num1": 5.5, "num2": 3.2}

response = requests.post(url, headers=headers, json=data)
print("Multiply Decimal Numbers Test Response:", response.json())
print(response.status_code)
# modified in f4@main

# added in f4

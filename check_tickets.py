import requests
username = 'aes.creator'
password = 'A3%s!JbuhNO1'

# ServiceNow API endpoint
url = f"https://dev263138.service-now.com/api/now/table/incident"
headers = {
    "Content-Type": "application/json",
    "Accept": "application/json"
}

# Authenticate with ServiceNow
response = requests.get(url, auth=(username, password), headers=headers)
print(response)
if response.status_code == 200:
    tickets = response.json().get("result", [])
    for ticket in tickets:
        description = ticket.get("short_description", "").lower()
        print(description)
else:
    print("Failed to retrieve tickets:", response.status_code)
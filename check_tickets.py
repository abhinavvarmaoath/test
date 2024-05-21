import requests
username = 'aes.creator'
password = 'A3%s!JbuhNO1'

# ServiceNow API endpoint
url = f"https://dev263138.service-now.com/api/now/table/incident"

# Set up HTTP request headers
headers = {
    "Content-Type": "application/json",
    "Accept": "application/json"
}

# Authenticate with ServiceNow
response = requests.get(url, auth=(username, password), headers=headers)

if response.status_code == 200:
    tickets = response.json().get("result", [])
    for ticket in tickets:
        description = ticket.get("short_description", "").lower()
        if "upgrade vmanage" in description:
            print("Upgrade vmanage script triggered for ticket:", ticket["number"])
            # Write a flag to a file
            with open('trigger_hello_world.txt', 'w') as f:
                f.write('run')
            break
else:
    print("Failed to retrieve tickets:", response.status_code)


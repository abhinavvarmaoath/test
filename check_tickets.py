import requests
import subprocess

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
        if ticket['active'] == 'true' and 'changed state to down' in description:
            inputs = '5\n2\n3\n6\n'
            # Execute the main.py script with the inputs
            process = subprocess.Popen(['python3', 'main.py'], stdin=subprocess.PIPE, text=True)
            process.communicate(inputs)
            break
else:
    print("Failed to retrieve tickets:", response.status_code)

import requests
import subprocess
import json
incident_number=''
username = 'admin'
password = 'LoMdP4gR^+7l'

# ServiceNow API endpoint
url1 = f"https://dev225865.service-now.com/api/now/table/incident"
headers = {
    "Content-Type": "application/json",
    "Accept": "application/json"
}

# Authenticate with ServiceNow
response = requests.get(url1, auth=(username, password), headers=headers)
if response.status_code == 200:
    tickets = response.json().get("result", [])
    for ticket in tickets:
        if incident_number == ticket['number']:
            description = ticket.get("short_description", "")
            close_url = f"https://dev225865.service-now.com/api/now/table/incident/{ticket['sys_id']}"
            close_payload = {
                "caller_id": "admin",
                "short_description": description + ' --jenkins',
            }

            close_response = requests.put(close_url, auth=(username, password), headers=headers, data=json.dumps(close_payload))
            if close_response.status_code == 200:
                print(f"Ticket {incident_number} closed successfully.")
            else:
                print(f"Failed to close ticket {incident_number}: {close_response.status_code} - {close_response.text}")
            break

else:
    print("Failed to retrieve tickets:", response.status_code)
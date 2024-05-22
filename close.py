import requests
import subprocess
import json

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
if response.status_code == 200:
    tickets = response.json().get("result", [])
    for ticket in tickets:
        description = ticket.get("short_description", "").lower()

        if (ticket['state'] != '6' or ticket['state'] != '7') and 'changed state to down' in description:
            print(ticket)
            incident_number = ticket['number']
            close_url = f"https://dev263138.service-now.com/api/now/table/incident/{ticket['sys_id']}"
            close_payload = {
              "state": "7",
              "resolved_by": username,
              "resolved_at": "2024-05-21T12:00:00Z",
              "close_code": "Solved (Work Around)",
              "close_notes": "Issue resolved. Awaiting user confirmation before closing."
            }
            print(incident_number)
            close_response = requests.put(close_url, auth=(username, password), headers=headers, data=json.dumps(close_payload))
            if close_response.status_code == 200:
                print(f"Ticket {incident_number} closed successfully.")
            else:
                print(f"Failed to close ticket {incident_number}: {close_response.status_code} - {close_response.text}")
            # break
else:
    print("Failed to retrieve tickets:", response.status_code)

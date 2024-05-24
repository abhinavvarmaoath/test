import requests
import subprocess
import json

username = 'admin'
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
        if ticket['close_notes'] != "Automatically closed after processing by jenkins" and 'changed state to down' in description and '--jenkins'  in description:
            inputs = '5\n2\n3\n7\n'
            process = subprocess.Popen(['python3', 'main.py'], stdin=subprocess.PIPE, text=True)
            process.communicate(inputs)
            # After the process, close the ticket
            incident_number = ticket['number']
            close_url = f"https://dev263138.service-now.com/api/now/table/incident/{ticket['sys_id']}"
            close_payload = {
                "state": "7",
                "active": "false",
                "close_code": "Closed/Resolved by Caller",
                "close_notes": "Automatically closed after processing by jenkins",
                "incident_state": "7",
                "caller_id": "admin",
            }

            close_response = requests.put(close_url, auth=(username, password), headers=headers, data=json.dumps(close_payload))
            if close_response.status_code == 200:
                print(f"Ticket {incident_number} closed successfully.")
            else:
                print(f"Failed to close ticket {incident_number}: {close_response.status_code} - {close_response.text}")
            break

        if ticket['close_notes'] != "Automatically closed after processing by jenkins" and  'backup' in description:
            inputs = '2\n7\n'
            process = subprocess.Popen(['python3', 'main.py'], stdin=subprocess.PIPE, text=True)
            process.communicate(inputs)
            # After the process, close the ticket
            incident_number = ticket['number']
            close_url = f"https://dev263138.service-now.com/api/now/table/incident/{ticket['sys_id']}"
            close_payload = {
                "state": "7",
                "active": "false",
                "close_code": "Closed/Resolved by Caller",  # Adjust this field as necessary
                "close_notes": "Automatically closed after processing by jenkins",
                "incident_state": "7",
                "caller_id": "admin",
            }

            close_response = requests.put(close_url, auth=(username, password), headers=headers,
                                          data=json.dumps(close_payload))
            if close_response.status_code == 200:
                print(f"Ticket {incident_number} closed successfully.")
            else:
                print(
                    f"Failed to close ticket {incident_number}: {close_response.status_code} - {close_response.text}")
            break

else:
    print("Failed to retrieve tickets:", response.status_code)

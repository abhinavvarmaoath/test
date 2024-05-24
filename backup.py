import requests
import json

username = 'admin'
password = 'A3%s!JbuhNO1'

# ServiceNow API endpoint
base_url = 'https://dev263138.service-now.com/api/now/table/incident'

ticket_data = {
    'short_description': 'Configuration Backup',
    'description': 'Configuration Backup',
    'priority': '1',
    'assignment_group': 'Service Desk',
}
headers = {
    "Content-Type": "application/json",
    "Accept": "application/json"
}

try:
    response = requests.post(base_url, auth=(username, password), json=ticket_data, headers=headers)
    response.raise_for_status()  # Raise an error for bad status codes
    if response.status_code == 201:
        print("Incident created successfully.")
        print("Response:", response.json())
    else:
        print("Failed to create incident.")
        print("Status Code:", response.status_code)
        print("Response:", response.json())
except requests.exceptions.RequestException as e:
    print("An error occurred:", e)

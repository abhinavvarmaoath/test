


def service_now_update_incident(request):
    incident_number = request.POST.get('incident_number')
    short_description = request.POST.get('incident_type')
    try:
        username = 'admin'
        password = 'A3%s!JbuhNO1'
        url = f"https://dev263138.service-now.com/api/now/table/incident/"+incident_number
        print(url)
        ticket_data = {
            "caller_id": "admin",
            "short_description": short_description +' --jenkins'
        }
        try:
            response = requests.put(url, auth=(username, password), headers={"Accept": "application/json"}, data=json.dumps(ticket_data))
            if response.status_code == 200:
                ticket_id = response.json().get('result').get('number')
                return JsonResponse({"msg": "Ticket successfully updated"}, status=200)
            else:
                print("Failed to update ticket")
                print("Response:", response.text)
                return JsonResponse({"msg": "Failed to update ticket"}, status=400)
        except requests.exceptions.RequestException as e:
            print("Error:", e)
            return JsonResponse({"msg": "Failed to update ticket"}, status=400)

    except Exception as error:
        return JsonResponse({"msg": "Failed to update ticket"}, status=400)
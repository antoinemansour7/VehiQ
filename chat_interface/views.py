from django.http import JsonResponse, HttpResponseBadRequest
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
import requests
import json  # Import the json module

@csrf_exempt
@require_POST  # Ensure that only POST requests are accepted
def chat_with_rasa(request):
    try:
        data = json.loads(request.body)  # Parse the JSON from the request body
        user_message = data['message']  # Access the 'message' field
    except (json.JSONDecodeError, KeyError):
        return HttpResponseBadRequest("No message provided")

    rasa_endpoint = 'http://localhost:5005/webhooks/rest/webhook'
    try:
        rasa_response = requests.post(rasa_endpoint, json={"sender": "user", "message": user_message})
        return JsonResponse(rasa_response.json(), safe=False)
    except requests.exceptions.RequestException as e:
        return JsonResponse({'error': str(e)}, status=500)


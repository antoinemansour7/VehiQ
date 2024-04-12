from django.http import JsonResponse, HttpResponseBadRequest
from django.views.decorators.csrf import csrf_exempt
import requests

@csrf_exempt
def chat_with_rasa(request):
    if request.method == 'POST':
        user_message = request.POST.get('message')
        if not user_message:
            return HttpResponseBadRequest("No message provided")

        rasa_endpoint = 'http://localhost:5005/webhooks/rest/webhook'
        try:
            rasa_response = requests.post(rasa_endpoint, json={"sender": "user", "message": user_message})
            return JsonResponse(rasa_response.json(), safe=False)
        except requests.exceptions.RequestException as e:
            return JsonResponse({'error': str(e)}, status=500)
    else:
        return HttpResponseBadRequest("Only POST requests are allowed")


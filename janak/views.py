# janak/views.py
import json
import requests
from django.shortcuts import render
from django.http import JsonResponse
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt

def home(request):
    return render(request, 'janak/index.html')

@csrf_exempt
def generate_email(request):
    if request.method == 'POST':
        prompt = request.POST.get('prompt', '')
        
        if not prompt:
            return JsonResponse({'error': 'Prompt is required'}, status=400)
        
        try:
            # Prepare Grok API request
            headers = {
                "Authorization": f"Bearer {settings.GROK_API_KEY}",
                "Content-Type": "application/json"
            }
            
            payload = {
                "model": "llama-3.1-8b-instant",  # Grok model
                "messages": [
                    {
                        "role": "system",
                        "content": "You are a professional email assistant. Generate a well-structured email based on the user's prompt. Include a relevant subject line, professional greeting, clear body content, and appropriate closing."
                    },
                    {
                        "role": "user",
                        "content": prompt
                    }
                ],
                "temperature": 0.7,
                "max_tokens": 1024,
                "top_p": 1,
                "frequency_penalty": 0,
                "presence_penalty": 0
            }
            
            # Call Grok API
            response = requests.post(
                settings.GROK_API_URL,
                headers=headers,
                data=json.dumps(payload)
            )
            
            # Check for successful response
            if response.status_code == 200:
                response_data = response.json()
                email_content = response_data['choices'][0]['message']['content']
                return JsonResponse({'email': email_content})
            else:
                return JsonResponse({
                    'error': f"Grok API error: {response.status_code}",
                    'details': response.text
                }, status=500)
                
        except Exception as e:
            print("Error in generate_email:", e)
            return JsonResponse({'error': str(e)}, status=500)
    
    return JsonResponse({'error': 'Invalid request method'}, status=400)
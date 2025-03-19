from django.shortcuts import render
from django.http import JsonResponse
import os
import google.generativeai as genai  # Correct import

# Initialize the model directly
genai.configure(api_key='AIzaSyAHU2Zcczml8QhbPddUnRHSrHudM6AVK3s')

# Use the gemini model directly
model = genai.GenerativeModel("gemini-2.0-flash")

def chat_view(request):
    if request.method == 'POST':
        user_input = request.POST.get('question')
        if user_input:
            # Send user input to the model and get the response
            response = model.generate_content(contents=user_input)

            # Check if the response has valid text, otherwise return an error
            if response.text:
                return JsonResponse({'response': response.text})
            else:
                return JsonResponse({'error': 'No valid response from the model'}, status=500)
        else:
            return JsonResponse({'error': 'No question provided'}, status=400)

    # If it's a GET request, render the chat page
    return render(request, 'chat/chat.html')

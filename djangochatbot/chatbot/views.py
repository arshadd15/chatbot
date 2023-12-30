from django.shortcuts import render
from django.http import JsonResponse
import openai


openai_api_key = ''
openai.api_key = openai_api_key

def ask_openai(message):
    response = openai.completions.create(
        model = "text-davinci-003",
        prompt = message,
        n = 1,
        stop = None,
    )
    print(response)
    answer = response.choice[0].text.strip()
    return answer

def chatbot(request):
    if request.method == "POST":
        message = request.POST.get('message')
        response = ask_openai(message)
        return JsonResponse({'message': message, 'response': response})
    return render(request,'chatbot.html')
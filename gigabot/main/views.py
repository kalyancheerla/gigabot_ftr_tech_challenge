from django.shortcuts import render
from django.http import JsonResponse
from .chatbot import get_chatbot_response

# Chatbot function
#def get_chatbot_response(message):
#    return "You are dumb!"

# Create your views here.
def home(request):
    if request.method == "POST":
        message = request.POST.get('message')
        response = get_chatbot_response(message)
        return JsonResponse({'message': response})
    return render(request, "index.html")

def about_us(request):
    developers = [
        {'name': 'Kalyan Cheerla', 'bio': 'Lead Developer', 'image': 'https://avatars.githubusercontent.com/u/32354220'},
        {'name': 'Bhavani Rachakatla', 'bio': 'Developer', 'image': 'https://avatars.githubusercontent.com/u/28670100'},
           ]
    return render(request, "about_us.html", {'developers': developers})

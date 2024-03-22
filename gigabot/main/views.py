from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, "index.html")

def about_us(request):
    developers = [
        {'name': 'Kalyan Cheerla', 'bio': 'Project Manager', 'image': 'https://avatars.githubusercontent.com/u/32354220'},
        {'name': 'Bhavani Rachakatla', 'bio': 'Design and Testing Lead', 'image': 'https://avatars.githubusercontent.com/u/28670100'},
           ]
    return render(request, "about_us.html", {'developers': developers})
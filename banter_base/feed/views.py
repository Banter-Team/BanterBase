from django.shortcuts import render

# Create your views here.
def home(request):
        return render(request, 'feed/home.html')


def new_entry(request):
        return render(request, 'feed/new_entry.html')
from django.shortcuts import render
from .forms import BanterEntry
from django.http import HttpResponseRedirect

# Create your views here.
def home(request):
        return render(request, 'feed/home.html')


def new_entry(request):
           # if this is a POST request we need to process the form data
        if request.method == 'POST':
                # create a form instance and populate it with data from the request:
                form = BanterEntry(request.POST)
                # check whether it's valid:
                if form.is_valid():
                        # process the data in form.cleaned_data as required
                        # ...
                        # redirect to a new URL:
                        return HttpResponseRedirect('/thanks/')

                # if a GET (or any other method) we'll create a blank form
        else:
                form = BanterEntry()
        return render(request, 'feed/new_entry.html', {'form':form})
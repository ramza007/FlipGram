from django.shortcuts import render
from django.http  import HttpResponse

# Create your views here.
def base(request):
    return render(request, 'base.html')


def profile(request):
    '''
    View function to display the profile of the logged in user when they click on the user icon
    '''
    return render(request, 'my-profile.html')

def explore(request):
    '''
    Views the initial profile
    '''
    return render(request, 'explore.html')

def timeline(request):
    '''
    returns timeline html
    '''
    return render(request, 'timeline.html')
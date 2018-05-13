from django.shortcuts import render
from django.http  import HttpResponse
from django.contrib.auth.decorators import login_required

# Create your views here.
def base(request):
    return render(request, 'base.html')


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


@login_required(login_url='/accounts/login')
def index(request):
    current_user = request.user
    title = 'FlipGram'
    grammers = Profile.get_profiles
    following = Follow.get_following(current_user.id)
    images = []
    for followed in following:
        # get profile id for each and use it to find user id
        profiles = Profile.objects.filter(id=followed.profile.id)
        for profile in profiles:
            post = Image.objects.filter(user=profile.user)
            for image in post:
                images.append(image)
    return render(request, 'index.html', {"images": images, "title": title, "following": following, "user": current_user, "grammers": grammers})


@login_required(login_url='/accounts/login')
def profile(request):
    '''
    View function to display the profile of the logged in user when they click on the user icon
    '''
    current_user = request.user  # get the id of the current

    try:

        single_profile = Profile.objects.get(user=current_user.id)

        title = f'{current_user.username}\'s'

        info = Profile.objects.filter(user=current_user)

        pics = Image.objects.filter(user=request.user.id).all()

    except:

        title = f'{current_user.username}\'s'

        pics = Image.objects.filter(user=request.user.id).all()

        info = Profile.objects.filter(user=7)

    return render(request, 'my-profile.html', {"title": title, "current_user": current_user, "info": info, "pics": pics})

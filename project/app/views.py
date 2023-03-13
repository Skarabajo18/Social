from django.shortcuts import (render,
                              redirect)
from django.contrib.auth import (authenticate,
                                 login)
from django.contrib.auth.decorators import login_required

# Create your views here.
from .forms import (SignUpForm)
from .models import (UserAccount,
		             UserRelationship,
			         UserProfile)

def login(request):
    
    return render(request, 'login.html')

@login_required
def home(request):
    x = request
    Users = UserAccount.objects.all()
    UserProfiles = UserProfile.objects.all()
    context = {'Users': Users, 'UserProfiles': UserProfiles}
    return render(request=request, template_name='layout.html', context=context)

def signup(request):

	if request.method == 'POST':

		sign_up_form = SignUpForm(request.POST)

		if sign_up_form.is_valid():

			sign_up_form.cleaned_data['first_name'] = f'''{sign_up_form.cleaned_data['first_name']}'''.upper()
			sign_up_form.cleaned_data['last_name'] = f'''{sign_up_form.cleaned_data['last_name']}'''.upper()

			sign_up_form.save()
			
			return redirect('home')
	else:

		sign_up_form = SignUpForm()

	context = { 'sign_up_form' : sign_up_form }

	return render(request, 'signup.html', context)

@login_required
def user_profile(request):
	User_ = UserAccount.objects.get(username=request.user.username)
	UserProfile_ = UserProfile.objects.get(User_id=request.user.id)
	print(UserProfile_.image.url)
	context = {'User': User_,
               'UserProfile': UserProfile_}
	
	return render(request, 'profile.html', context)

def profile_user(request, username=None):
	User_ = UserAccount.objects.get(username=username)
	UserProfile_ = UserProfile.objects.get(User=User_)
	print(UserProfile_.image.url)
	context = {'User': User_,
               'UserProfile': UserProfile_}
	return render(request, 'profile.html', context)

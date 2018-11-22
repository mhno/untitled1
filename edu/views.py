from django.contrib.auth.models import User
from django.shortcuts import render

from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth import logout
#
# def signup(request):
#     if request.method == 'POST':
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             username = form.cleaned_data.get('username')
#             raw_password = form.cleaned_data.get('password1')
#             user = authenticate(username=username, password=raw_password)
#             login(request, user)
#             return redirect('home')
#     else:
#         form = UserCreationForm()
#     return render(request, 'signup.html', {'form': form})
from forms.user_forms import SignUpForm


def index(request):
    return render(request,"index.html")

# def signup(request):
#     username = request.POST['username']
#     password = request.POST['password']
#     user = authenticate(request, username=username, password=password)
#     if user is not None:
#         login(request, user)
#         # Redirect to a success page.
#         ...
#     else:
#         # Return an 'invalid login' error message.

def sign_up(request):
    comments_list = User.objects.order_by('-created_at')
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        print(form.data)
        if form.is_valid():
            user = form.save()
            user_info = User()
            user_info.user = user
            user_info.is_active = True
            user_info.save()
            user.save()


    else:
        form = SignUpForm()
    print(form.errors)
    return render(request, 'sign_up.html', {'comments': comments_list,'form': form})


def logout_view(request):
    logout(request)
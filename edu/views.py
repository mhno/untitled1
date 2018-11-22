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

from django.contrib.auth.models import User

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
    # if request.method == 'POST':
    #     error = False
        if request.POST:
            name=request.POST.get("name")
            lastname=request.POST.get("last_name")
            username = request.POST.get("username")
            email=request.POST.get("email")
            password1 = request.POST.get("password1")
            password2=request.POST.get("password2")

            user = User.objects.create_user(username,email,password1)

            user.first_name = name
            user.last_name = lastname
            user.save()

        return render(request,"sign_up.html")
           # user = authenticate(request, username=username, password=password)
        #     if user is not None:
        #         if user.is_active:
        #             login(request, user)
        #             return HttpResponseRedirect("/")
        #         else:
        #             error = True
        #     error = True
        # return render(request, "login_form.html", {
        #     "error": error
        # })

    #     form = forms.user_forms.SignUpForm(request.POST)
    #     if form.is_valid():
    #         form.save()
    #         username = form.cleaned_data.get('username')
    #         raw_password = form.cleaned_data.get('password1')
    #
    #         user = authenticate(username=username, password=raw_password)
    #         login(request, user)
    #         return redirect('/')
    # else:
    #     form = SignUpForm()
    # return render(request, 'sign_up.html', {'form': form})

def logout_view(request):
    logout(request)
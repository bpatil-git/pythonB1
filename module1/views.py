from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages, sessions


# Create your views here.

def landing_page(request):
    return render(request, "index.html")

def login_view(request):
    return render(request, "login.html")

def home(request):
    if request.method == 'POST':
        uname = request.POST['uname']
        pas = request.POST['pas']
        user = authenticate(username=uname, password=pas)
        if user is not None:
            print('User%%%%%%%%%', user)
            login(request, user)
            request.session["username"] = user.first_name
            # request.session.set_expiry(600)
            return render(request, "home.html")
            # messages.info(request, f"You are now logged in as {username}")
        else:
            print('User##########', user)  //comment
            messages.error(request, "Invalid username or password...")
            return redirect('module1:login')
    elif request.session.has_key("username"):
        print("Keyyyyyyyyyyyyyyy", request.session.has_key("username"))
        return render(request, "home.html")
    else:
        print("Keyyyyyyyyyyyyyyy", request.session.has_key("username"))
        return redirect('module1:landing_page')

def contact(request):
    return render(request, "contact.html")

def user_logout(request):
   try:
      del request.session['username']
      logout(request)
   except:
      pass
   return render(request, "logout.html")

def travel_oper(request):
    return render(request, "travel_ope_base.html")

def learnings(request):
    return render(request, "learn.html")

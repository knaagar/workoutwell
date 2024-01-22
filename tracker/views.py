import os
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse

from .models import personal_details, goals, exercise_tracker, blog
from dotenv import load_dotenv

load_dotenv()
RapidApiKey = os.getenv('RAPIDAPIKEY')

import datetime
import requests, random

# Retrieve a random quote from an external API
def get_quotes():
    api_url = "https://type.fit/api/quotes"
    response = requests.get(api_url)
    data = response.json()
    rn = random.randint(0, 15)
    return data[rn]

# Get AI response based on a prompt
def get_ai_response(request):
    if request.method == 'GET':
        prompt = request.GET.get('prompt', '')  # Retrieving prompt from GET parameters
        url = "https://chatgpt-gpt4-ai-chatbot.p.rapidapi.com/ask"
        payload = { "query": prompt }
        headers = {
            "content-type": "application/json",
            "X-RapidAPI-Key": RapidApiKey,
            "X-RapidAPI-Host": "chatgpt-gpt4-ai-chatbot.p.rapidapi.com"
        }

        response = requests.post(url, json=payload, headers=headers)
        data = response.json()
        
        return JsonResponse(data)  # Returning JSON response to the browser
    else:
        return JsonResponse({'error': 'Invalid request method'})

# Create your views here.

# Display the home page for users who are logged in
def home_unlogin(request):
    if request.user.is_authenticated:
        pd = personal_details.objects.all().filter(user = request.user).values()
        ed = exercise_tracker.objects.all().filter(user = request.user, created_at = datetime.date.today()).values()
        gd = goals.objects.all().filter(user = request.user).values()
        qd = get_quotes()
        c = {"details": pd, "quotes": qd, "edetails": ed, "gdetails": gd}
        return render(request, "index.html", context = c)
    else:
        return redirect('/signin')

# User login functionality
def signin(request):
    if request.user.is_authenticated:
        return redirect('/')
    else:
        if request.method == "POST":
            username = request.POST["username"]
            password = request.POST["password"]
            user = authenticate(username = username, password = password)
            if user is not None:
                login(request, user)
                return redirect('/')
            else:
                return redirect('/signin')
        else:
            return render(request, "login.html")

# User logout functionality
def signout(request):
    logout(request)
    return redirect('/signin')

# User registration functionality
def signup(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        confpassword = request.POST["confirmpassword"]
        
        if password == confpassword:
            user = User.objects.create_user(username = username, password = password)
            user.save()
            login(request, user)
            return redirect('/')
        else:
            return render(request, "signup.html")
    else:
        return render(request, "signup.html")

# Upload/Update user personal details
def upload_pd(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            fname = request.POST["firstname"]
            lname = request.POST["lastname"]
            dob = request.POST["dob"]
            weight = request.POST["weight"]
            height = request.POST["height"]
            disease = request.POST["disease"]
            details = personal_details(user = request.user, fname = fname, lname = lname, dob = dob, w = weight, h = height, disease = disease)
            details.save()
            return redirect('/home')
        else:
            pd = personal_details.objects.all().filter(user = request.user).values()
            c = {"details": pd}
            return render(request, "update_pd.html", context=c)
    else:
        return redirect('/home')

# Display all user goals
def allgoal(request):
    if request.user.is_authenticated:
        gd = goals.objects.all().filter(user = request.user).values()
        c = {"gdetails": gd}
        return render(request, "goals.html", context = c)
    else:
        return redirect('/signin')

# Create a new goal for the user
def creategoal(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            gname = request.POST["gname"]
            gdesc = request.POST["gdesc"]
            sdate = request.POST["sdate"]
            tdate = request.POST["tdate"]
            gtag = request.POST["gtag"]
            gstatus = request.POST["gstatus"]
            gdetails = goals(user = request.user, gname = gname, gdesc = gdesc, sdate = sdate, tdate = tdate, gtag = gtag, gstatus = gstatus)
            gdetails.save()
            return redirect('/goals')
        else:
            return render(request, "newgoal.html")
    else:
        return redirect('/')

# Display all user exercises
def allexer(request):
    if request.user.is_authenticated:
        ed = exercise_tracker.objects.all().filter(user = request.user).order_by('-priority').values()
        c = {"edetails": ed}
        return render(request, "exercises.html", context = c)
    else:
        return redirect('/signin')

# Create a new exercise for the user
def createexercise(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            ename = request.POST["ename"]
            edesc = request.POST["edesc"]
            etag = request.POST["etag"]
            created_at = request.POST["created_at"]
            priority = request.POST["priority"]
            edetails = exercise_tracker(user = request.user, ename = ename, edesc = edesc, etag = etag, created_at=created_at, priority=priority)
            edetails.save()
            return redirect('/exercises')
        else:
            return render(request, "newexercise.html")
    else:
        return redirect('/')


# Display all user blogs
def allblogs(request):
    if request.user.is_authenticated:
        bd = blog.objects.all()
        c = {"bdetails": bd}
        return render(request, "blogs.html", context = c)
    else:
        return redirect('/signin')

# Display user account details
def get_account(request):
    if request.user.is_authenticated:
        pd = personal_details.objects.all().filter(user = request.user).values()
        bd = blog.objects.all().filter(user = request.user).values()
        c = {"pdetails": pd, "bdetails": bd}
        return render(request, "account.html", context = c)
    else:
        return redirect('/signin')

# User deletion confirmation  
def del_conf(request):
    if request.user.is_authenticated:
        return render(request, "delete_user_confirmation.html")
    else:
        return redirect('/signin')

# Display user tools page
def get_tools(request):
    if request.user.is_authenticated:
        pd = personal_details.objects.all().filter(user = request.user).values()
        c = {"pdetails": pd}
        return render(request, "tools.html", context = c)
    else:
        return redirect('/signin')

# Display recommendations page
def get_recommendations(request):
    if request.user.is_authenticated:
        return render(request, "temp_cb.html")
    else:
        return redirect('/signin')

# Create a new blog
def createblog(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            title = request.POST["title"]
            tag = request.POST["tag"]
            date_published = datetime.date.today()
            intro = request.POST["intro"]
            content = request.POST["content"]
            bdetails = blog(user = request.user, title = title, tag = tag, date_published=date_published, intro=intro, content=content)
            bdetails.save()
            return redirect('/blogs')
        else:
            return render(request, "newblog.html")
    else:
        return redirect('/')

# User deletion
def delete_user(request):
    if request.method == "POST":
        user = request.user
        logout(request) 
        user.delete()
        return redirect('/signin')
    return render(request, 'delete_user_confirmation.html')

# Update a goal
def update_goals(request, goal_id):
    if request.method == "POST":
        new_status = request.POST.get("new_status")
        goal = goals.objects.get(id=goal_id)
        goal.gstatus = new_status
        goal.save()
    return redirect('/goals')

# Delete a goal
def delete_goal(request, goal_id):
    if request.method == "POST":
        goal = goals.objects.get(id=goal_id)
        goal.delete()
    return redirect('/goals')
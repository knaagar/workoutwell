"""
URL configuration for workoutwell project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from tracker.views import *



urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', home_unlogin),
    path('', home_unlogin),
    path('signin/', signin),
    path('signout/', signout),
    path('signup/', signup),
    path('uploadpd/', upload_pd),
    path('goals/', allgoal),
    path('creategoal/', creategoal),
    path('exercises/', allexer),
    path('createexercise/', createexercise),
    path('blogs/', allblogs),
    path('createblog/', createblog),
    path('myaccount/', get_account),
    path('tools/', get_tools),
    path('recommendations/', get_recommendations),
    path('update_goals/<int:goal_id>/', update_goals, name='update_goals'),
    path('delete_goal/<int:goal_id>/', delete_goal, name='delete_goal'),
    path('delete_confirmation/', del_conf),
    path('delete_user/', delete_user, name='delete_user'),
    path('get_ai_response/', get_ai_response, name='get_ai_response'),
]

"""
URL configuration for notenanalyse project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),

    # Landing page and dashboard
    path("", views.index, name="index"),
    path("dashboard", views.dashboard, name="dashboard"),

    # Subjects
    path("subjects", views.subjects, name="subjects"),
    path("subjects/create", views.create_subject, name="create_subject"),
    path("subjects/show", views.show_subject, name="show_subject"),
    path("subjects/delete", views.delete_subjects, name="delete_subject"),

    # Icons
    path("symbols", views.symbols, name="symbols"),
    path("symbols/create", views.create_symbol, name="create_symbol"),
    path("symbols/show", views.create_symbol, name="show_symbol"),
    path("symbols/delete", views.create_symbol, name="delete_symbol"),

    # Account actions
    path('account/', include('account.urls')),
    path('login/', views.login_user, name='login' ),
    path('register/', views.register_user, name='register' ),
    path('logout/', views.logout_user, name='logout' ),
]

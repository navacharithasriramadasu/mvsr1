
from django.contrib.auth import views as auth
from django.urls import path
from .views import *

urlpatterns=[
    path('upload/',upload_excel,name="upload_excel"),
    path("login/",login,name="login"),
    path("profile/", logins, name="logins"),
    path('upload_sub/',upload_sub,name="upload_sub"),
    path('notifications.html/',notification_view,name="notification_view"),
    path('/dashboard',dashboard_view,name="dashboard_view"),
    #path("download_payments/", download_payments_excel, name="download_payments"),
]

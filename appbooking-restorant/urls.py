from django.contrib import admin
from django.urls import path, include
from booking import views as bviews

urlpatterns =[
    path("signup/", bviews.signup, name ='signup'),
    path("admin/", admin.site.urls),
    path("accounts/", include("django.contrib.auth.uls")),
    path("", bviews.home, name ='home'),
    path("search/", bviews.search_place, name ='search_place'),
    path("bookings/", bviews.my_bookings, name ='my_bookings'),
    path("",include("bookings.urls"))
]
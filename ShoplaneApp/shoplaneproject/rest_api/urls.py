from django.urls import path
from django.views.decorators.csrf import csrf_exempt
from .views import userSignupView,allProductsView,LoginView
urlpatterns=[
    path("users/signup",csrf_exempt(userSignupView.as_view()),name="user-signup"),
    path("allproducts/",allProductsView.as_view(),name="all-products"),
    path("users/login",csrf_exempt(LoginView.as_view()),name="user-login"),
]
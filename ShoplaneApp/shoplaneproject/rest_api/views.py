from django.http import Http404,HttpResponseBadRequest,JsonResponse
from .models import UserSignup,Products
from .serializer import UserSignupSerializer
from django.views import View
import json

class userSignupView(View):
    def post(self,request):
        user_data=json.loads(request.body)

        try:
            UserSignup.objects.create(**user_data)
            return JsonResponse(user_data,safe=False,status=200)
        except Exception as e:
            return HttpResponseBadRequest("User Registration Failed!!")
        
class LoginView(View):
    def post(self,request):
        login_data=json.loads(request.body)
        email=login_data["email"]
        password=login_data["password"]
        try:
            logg=UserSignup.objects.filter(email=email,password=password).values()

            for item in list(logg):
                if item["password"]==password:
                    return JsonResponse("Login Successfull!!",safe=False) 
                else:
                    return JsonResponse("Invalid username or password!!",safe=False)
        except Exception as e:
            return HttpResponseBadRequest()

class allProductsView(View):
    def get(self,request):
        products=Products.objects.all().values()
        return JsonResponse(list(products),safe=False,status=200)
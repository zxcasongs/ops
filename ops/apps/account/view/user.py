import jwt
from rest_framework.views import APIView
from django.contrib.auth import authenticate, login
from utils.jwt_token import create_jwt_token,parse_payload
from apps.account.models import User
from rest_framework import status
from utils.http_response import APIResponse
from utils.authorization import MyAuthentication
from utils.permissions import MyPermission
from rest_framework.response import Response
from apps.account.models import Role



class UserLogin(APIView):
    authentication_classes = []
    permission_classes = []
    def post(self,request,*args,**kwargs):
        try:
            data = request.data
            username = data['username']
            password = data['password']
            user = authenticate(username=username,password=password)
            print(user)
            if user and user.is_active:
                login(request,user)
                user_obj = User.objects.filter(username=username).first()
                print(user_obj)
                # permissions_list = Role.objects.filter(user__id=user_obj.id).all().values(
                #     'permissions__method', 'permissions__path'
                # )


                token  =  create_jwt_token({'username': username},1440)
                #token = create_jwt_token({'username': username}, 1)

                data = {"token": token, "name": username}




                return  APIResponse(data=data)
        except Exception as e:
            return  APIResponse(errcode=100,errmsg=e,status=status.HTTP_200_OK)




class Getuser(APIView):
    authentication_classes = [MyAuthentication]
    permission_classes = [MyPermission]
    def get(self,request,*args,**kwargs):
        return Response("123")
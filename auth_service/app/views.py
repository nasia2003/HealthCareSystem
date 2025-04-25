from django.http import HttpResponse
import requests
from rest_framework.views import APIView
from django.views import View
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import render
from .serializers import RegisterSerializer, LoginSerializer
import logging
logger = logging.getLogger()

class RegisterAPI(APIView):
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)

        # Kiểm tra tính hợp lệ của dữ liệu
        if serializer.is_valid():
            # Lấy dữ liệu từ serializer
            user = serializer.save()
            user_data = {
                "email": user.email,
                "username": user.username,
                "fullname": user.fullname,
            }

            return Response({
                "message": "User created successfully",
                "user": user_data
            }, status=status.HTTP_201_CREATED)

        # Nếu dữ liệu không hợp lệ, trả về lỗi
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class RegisterView(View):
    def get(self, request):
        return render(request, 'authentication/register.html')
    
    def post(self, request):
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        if password != confirm_password:
            error = 'Passwords do not match.'
            return render(request, 'authentication/register.html', {'error': error})
    
        data = {
            'username': request.POST.get('username'),
            'fullname': request.POST.get('fullname'),
            'email': request.POST.get('email'),
            'password': password,
        }

        logger.debug(data)

        api_url = "http://host.docker.internal:8000/auth/api/register/"
        try:
            # Gửi yêu cầu POST tới API ngoài
            response = requests.post(api_url, json=data)

            # Kiểm tra phản hồi từ API
            if response.status_code == 201:
                # Nếu thành công, trả về thông báo thành công
                return render(request, 'authentication/register.html', {'message': "Đăng kí thành công rồi!!!"})
            else:
                # Nếu API trả về lỗi, hiển thị thông báo lỗi
                error = f"Failed to register user on external API: {response.text}"
                return render(request, 'authentication/register.html', {'error': error})

        except requests.exceptions.RequestException as e:
            # Xử lý lỗi nếu không thể kết nối với API ngoài
            error = f"Error occurred while connecting to external API: {str(e)}"
            return render(request, 'authentication/register.html', {'error': error})

class LoginAPI(APIView):
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data
            return Response({"message": "Login successful", "username": user.username})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class LoginView(View):
    def get(self, request):
        return render(request, 'authentication/login.html')
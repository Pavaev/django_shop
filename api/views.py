import jwt

from django.contrib.auth import get_user_model, authenticate
from django.http import HttpResponse
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.utils import json
from rest_framework.views import APIView

from authentication.models import User
from products.models import Product
from api.serializers import ProductSerializer, UserSerializer


class WorkWithProductSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = []


class WorkWithUserSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = []


class Login(APIView):
    # permission_classes = (permissions.AllowAny,)
    # serializer_class = UserSerializer
    # authentication_classes = (BasicAuthentication,)

    def post(self, request, *args, **kwargs):
        User = get_user_model()
        if not request.data:
            return Response({'Error': "Please provide email/password"}, status="400")

        email = request.data['email']
        password = request.data['password']
        try:
            user = authenticate(email=email, password=password)
        except User.DoesNotExist:
            return Response({'Error': "Invalid email/password"}, status="400")
        if user:
            payload = {
                'id': user.id,
                'email': user.email,
            }
            jwt_token = {'token': jwt.encode(payload, "SECRET_KEY").decode('utf-8')}

            return HttpResponse(
                json.dumps(jwt_token),
                status=200,
                content_type="application/json"
            )

        else:
            return Response(
                json.dumps({'Error': "Invalid credentials"}),
                status=400,
                content_type="application/json"
            )

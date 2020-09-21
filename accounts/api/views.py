from accounts.api.serializers import UserSerializer
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework import generics
from ..models import User
from rest_framework.permissions import AllowAny
from rest_framework import status
from rest_framework.authtoken import views as auth_views
from rest_framework.compat import coreapi, coreschema
from rest_framework.schemas import ManualSchema

from .serializers import AuthCustomTokenSerializer


class UserCreateAPIView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (AllowAny,)

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        data = {}

        if serializer.is_valid(raise_exception=True):
            user = serializer.save()
            data['response'] = "successfully registered new user"
            data["email"] = user.email
            token = Token.objects.get(user=user).key
            data["token"] = token
            data["status"] = status.HTTP_201_CREATED
            headers = self.get_success_headers(serializer.data)
            data["headers"] = headers

        else:
            data = serializer.errors
        return Response(data)


# class CustomAuthToken(ObtainAuthToken):
#
#     def post(self, request, *args, **kwargs):
#         serializer = self.serializer_class(data=request.data,
#                                            context={'request': request})
#         serializer.is_valid(raise_exception=True)
#         user = serializer.validated_data['user']
#         token, created = Token.objects.get_or_create(user=user)
#         return Response({
#             'token': token.key,
#             # 'user_id': user.pk,
#             # 'email': user.email
#         })

class CustomAuthToken(auth_views.ObtainAuthToken):
    serializer_class = AuthCustomTokenSerializer
    if coreapi is not None and coreschema is not None:
        schema = ManualSchema(
            fields=[
                coreapi.Field(
                    name="email",
                    required=True,
                    location='form',
                    schema=coreschema.String(
                        title="Email",
                        description="Valid email for authentication",
                    ),
                ),
                coreapi.Field(
                    name="password",
                    required=True,
                    location='form',
                    schema=coreschema.String(
                        title="Password",
                        description="Valid password for authentication",
                    ),
                ),
            ],
            encoding="application/json",
        )


obtain_auth_token = CustomAuthToken.as_view()








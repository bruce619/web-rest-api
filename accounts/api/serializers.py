from rest_framework import serializers
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={'input_type': 'password'}, write_only=True)

    def __init__(self, *args, **kwargs):
        # first call parent's constructor
        super(UserSerializer, self).__init__(*args, **kwargs)
        # there's a `fields` property now
        self.fields['username'].required = True

    class Meta:
        model = User
        fields = ['email', 'username', 'password', 'password2']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def save(self):
        account = User(
            username=self.validated_data['username'],
            email=self.validated_data['email'],
        )
        password = self.validated_data['password']
        password2 = self.validated_data['password2']

        if password != password2:
            raise serializers.ValidationError({'password': 'password must match'})
        account.set_password(password)
        account.save()
        return account


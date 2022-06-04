"""""
Serializers for the user API View. Copied form Udemy Advanced Python & Django course
"""""
from django.contrib.auth import get_user_model, authenticate

from rest_framework import serializers
from django.utils.translation import gettext as _


class UdemyUserSerializer(serializers.ModelSerializer):
    """Serializer for the user objects."""

    class Meta:
        model = get_user_model()
        fields = ['email','password','username']
        extra_kwargs = {'password':{'write_only':True, 'min_length':5}}

    def create(self, validated_data):
        """Create and return a user with encrypted password. """
        return get_user_model().objects.create_user(**validated_data)

    
    def update(self, instance, validated_data):
        """Update and return user.  copied from Udemy"""
        password = validated_data.pop('password', None)
        user = super().update(instance, validated_data)

        if password:
            user.set_password(password)
            user.save()

        return user


class UdemyAuthTokenSerializer(serializers.Serializer):
    """Serializer for the user auth token. copied from Udemy """
    email = serializers.EmailField()
    password = serializers.CharField(
        style={'input_type':'password'},
        trim_whitespace=False,
    )

    def validate(self,attrs):
        """Validate and authenticate the user. """
        email = attrs.get('email')
        password = attrs.get('password')
        #print(f"*****{email}")
        #print(f"******{password}")
        user = authenticate(
            request = self.context.get('request'),
            username=email,
            password=password,
        )
        if not user:
            msg = _('Unable to athenticate with provided credentials.')
            raise serializers.ValidationError(msg, code='authorization')

        attrs['user'] = user
        return attrs

from django.contrib.auth import (
    get_user_model, authenticate)
from django.utils.translation import gettext as _
from rest_framework import serializers, status


class UserSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(required=True, write_only=True)

    class Meta:
        model = get_user_model()
        fields = ['email',
                  'full_name',
                  'password',
                  'confirm_password']
        extra_kwargs = {'password': {'write_only': True, 'min_length': 5,
                                     'required': True},
                        'full_name': {'min_length': 2}}

    def create(self, validated_data):
        return get_user_model().objects.create_user(**validated_data)

    def update(self, instance, validated_data):
        password = validated_data.pop('password', None)
        user = super().update(instance, validated_data)

        if password:
            user.set_password(password)
            user.save()
        return user

    def validate(self, attrs):
        confirm_password = attrs.pop('confirm_password')
        password = attrs.get('password')
        if not password == confirm_password:
            raise serializers.ValidationError(
                detail="Passwords does not match",
                code=status.HTTP_400_BAD_REQUEST
            )
        return attrs


class AuthTokenSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(style={'input_type': 'password'},
                                     trim_whitespace=False, )

    def validate(self, attrs):
        email = attrs.get('email')
        password = attrs.get('password')
        user = authenticate(
            request=self.context.get('request'),
            username=email,
            password=password,
        )
        if not user:
            msg = _('Unable to authenticate with provided credentials.')
            raise serializers.ValidationError(msg, code='authorization')

        attrs['user'] = user
        return attrs



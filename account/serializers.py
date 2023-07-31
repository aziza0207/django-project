from django.contrib.auth import get_user_model
from rest_framework import serializers, status


class UserSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(required=True, write_only=True)

    class Meta:
        model = get_user_model()
        fields = ['email',
                  'full_name',
                  'password',
                  'confirm_password']
        extra_kwargs = {'password': {'write_only': True, 'min_length': 5},
                        'full_name': {'min_length': 2}}

    def create(self, validated_data):
        return get_user_model().objects.create_user(**validated_data)

    def validate(self, attrs):
        confirm_password = attrs.pop('confirm_password')
        password = attrs.get('password')
        if not password == confirm_password:
            raise serializers.ValidationError(
                detail="Passwords does not match",
                code=status.HTTP_400_BAD_REQUEST
            )
        return attrs

from rest_framework import serializers
from django.contrib.auth import update_session_auth_hash
from authentication.models import Account


class AccountSerializer(serializers.ModelSerializer):
    password =serializers.CharField(write_only=True, required=False)
    confirm_password = serializers.CharField(write_only=True, required=False)


    class Meta:
        model = Account
        fields = ('id', 'email', 'username', 'updated_at',
                  'first_name', 'last_name', 'university_id', 'password',
                  'confirm_password',)
        read_only_fields = ('created', 'updated_at',)

    def create(self, validated_data):
        return Account.objects.create(**validated_data)


    def update(self, instance, validated_data):
        instance.username = validated_data.get('username', instance.username)
        instance.university_id = validated_data.get('university_id', instance.university_id)
        instance.save()

        password = validated_data.get('password', None)
        confirm_password = validated_data.get('confirm_password', None)

        if password and confirm_password:
            if password == confirm_password:
                instance.set_password(password)
                instance.save()
            else:
                raise serializers.ValidationError({
                    "password":["Passwords don't match."]
                })


        update_session_auth_hash(self.context.get('request'), instance)

        return instance

# from rest_framework import serializers
# from user_app.models import User
# from django.contrib.auth.password_validation import validate_password
# from django.contrib.auth.hashers import make_password
# class SignupSerializer(serializers.ModelSerializer):
#     confirm_password = serializers.CharField(style={'input_style':'password'},write_only=True)
#     class Meta:
#         model= User
#         fields=('first_name','last_name','phone_no','email','password','confirm_password')
#         extra_kwargs = {
#             'password': {'write_only': True},
#         }
#     def create(self,validated_data):
#         if User.objects.filter(email=self.validated_data.get("email")).exists():
#             raise serializers.ValidationError({'error': 'Email already exists'})
#         if validate_password(validated_data['password']) == None:
#                password = make_password(validated_data['password'])
#                account = User.objects.create(last_name=validated_data.get("last_name"),first_name=validated_data.get("first_name"),email=validated_data.get("email"),password=password)
#         return account
#     # def update(self, account,validated_data):
#     #     account.last_name = validated_data.get("last_name", account.last_name)
#     #     account.first_name = validated_data.get("first_name", account.first_name)
#     #     account.email = validated_data.get("email", account.email)
#     #     account.save()
#     #     return account
  
        
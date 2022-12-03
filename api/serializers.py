from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from users.models import UserProfile
from items.models import Categories, SubCategories, Products, Transaction


class RegisterUserSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={'input_type': 'password'}, write_only=True)

    class Meta:
        model = UserProfile
        fields = ['email', 'first_name', 'last_name', 'username', 'password', 'password2']
        extra_kwargs = {
            'password': {'write_only': True},
            'email': {'required': True}
        }

    def create(self, validated_data):
        user = UserProfile(email=self.validated_data['email'],
                           username=self.validated_data['username'], )
        password = self.validated_data['password']
        password2 = self.validated_data['password2']
        first_name = self.validated_data['first_name']
        last_name = self.validated_data['last_name']
        if password != password2:
            raise serializers.ValidationError({'password do not match'})
        user.set_password(password)
        user.save()
        return user


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        exclude = ('is_verified',)
        extra_kwargs = {
            'user_type': {'required': True},
            'contact_number': {'required': True},
            'country': {'required': True},
            'id_photo': {'required': True},
        }

    def create(self, validated_data):
        return UserProfile(**validated_data)


class GeneralTokenObtainSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super(GeneralTokenObtainSerializer, self).validate(attrs)
        data.update({'user': self.user.username})
        data.update({'id': self.user.id})
        data.update({'user_type': self.user.user_type})
        return data


class CategoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categories
        fields = '__all__'

    def create(self, validated_data):
        return Categories(**validated_data)


class SubCategoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubCategories
        fields = '__all__'

    def create(self, validated_data):
        return SubCategories(**validated_data)


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = '__all__'

    def create(self, validated_data):
        return Products(**validated_data)

class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = '__all__'

    def create(self, validated_data):
        transaction = Transaction(
            product_taken=self.validated_data['product_taken'],
            student=self.validated_data['student'],
            lab_incharge=self.validated_data['lab_incharge'])
        transaction.save()

        return transaction

    def validate(self, attrs):
        data = super(TransactionSerializer, self).validate(attrs)

        return data




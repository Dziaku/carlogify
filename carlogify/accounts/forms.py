from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    """
    Specify the user model created while adding a user
    on the admin page.
    """
    class Meta:
        model = CustomUser
        fields = [
            "first_name", 
            "last_name", 
            "email",
            "password", 
            "date_of_birth",
            "is_staff",
            "is_active",
            "groups",
            "user_permissions"
        ]
class CustomUserChangeForm(UserChangeForm):
    """
    Specify the user model edited while editing a user on the
    admin page.
    """
    class Meta:
        model = CustomUser
        fields = [
            "first_name", 
            "last_name", 
            "email", 
            "password",
            "date_of_birth",
            "is_staff",
            "is_active", 
            "groups",
            "user_permissions"
         ]
        
class RegisterForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['email', 'first_name', 'last_name', 'date_of_birth']

"""
This module defines forms for managing user registration in a political party Django application.

It extends Django's built-in `UserCreationForm` to capture additional fields like first name, surname,
email, identification number, and gender, which are necessary for registering new members.
"""

from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class CreateUserForm(UserCreationForm):
    """
    A form for creating a new user as a member of the political party.

    This form inherits from Django's `UserCreationForm` and includes additional
    fields specific to the political party registration.

    Attributes:
        first_name (str): The first name of the user, required.
        surname (str): The surname of the user, required.
        email (str): The email address of the user, required.
        id_number (str): The identification number of the user, required.
        username (str): The username for the user account, required.
        gender (str): The gender of the user, selected from predefined choices ('M', 'F', 'O').
    """

    first_name = forms.CharField(max_length=30, required=True, help_text='Required. 30 characters or fewer.')
    surname = forms.CharField(max_length=30, required=True, help_text='Required. 30 characters or fewer.')
    email = forms.EmailField(required=True, help_text='Required. Enter a valid email address.')
    id_number = forms.CharField(max_length=20, required=True, help_text='Required. 20 characters or fewer.')
    username = forms.CharField(max_length=30, required=True, help_text='Required. 30 characters or fewer.')

    gender_choices = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]
    gender = forms.ChoiceField(choices=gender_choices, required=True)

    class Meta:
        """
        Meta class to define additional properties for the `CreateUserForm`.

        Attributes:
            model (User): The model associated with this form.
            fields (list): List of field names that will be included in the form.
        """
        model = User
        fields = ['first_name', 'surname', 'email', 'id_number', 'gender', 'username', 'password1', 'password2']

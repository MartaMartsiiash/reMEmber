"""
Forms related to user authentication and registration.
"""


from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model


User = get_user_model()


class SignUpForm(UserCreationForm):
    """
    Custom signup form with a single password field and no default help texts.
    """

    password1 = forms.CharField(
        label="Пароль",
        widget=forms.PasswordInput(attrs={'class': 'password-field'}),
    )

    def __init__(self, *args, **kwargs):
        """
        Initialize the signup form.
        """
        super().__init__(*args, **kwargs)
        self.fields.pop("password2", None)
        for field in self.fields.values():
            field.help_text = ""

    def clean(self):
        """
        Perform custom form validation.
        """
        return forms.ModelForm.clean(self)

    class Meta(UserCreationForm.Meta):
        """
        Form metadata.
        """
        model = User
        fields = ("username", "email", "location")

class ProfileForm(forms.ModelForm):
    """
    User profile edit form.
    """

    class Meta:
        """
        Metadata for the Profile form.
        """
        model = User
        fields = ('username', 'location')

from django import forms  # 강의 14.1 - 1. 장고에서 forms가져오면서 시작.
from . import models


class LoginForm(forms.Form):  # - 2. Form 상속한 class만들기

    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        email = self.cleaned_data.get("email")
        password = self.cleaned_data.get("password")
        try:
            user = models.User.objects.get(email=email)
            if user.check_password(password):
                return self.cleaned_data
            else:
                self.add_error("password", forms.ValidationError("Password is wrong "))
        except models.User.DoesNotExist:
            self.add_error("email", forms.ValidationError("User does not exist"))

    # def clean_password(self):
    #     return "lakakakakak"

    # return "lalalaalala"


class SignUpForm(forms.ModelForm):
    class Meta:
        model = models.User
        fields = ("first_name", "last_name", "email")

    password = forms.CharField(widget=forms.PasswordInput)
    password1 = forms.CharField(widget=forms.PasswordInput, label="Confirmed Password")

    # def clean_email(self):
    #     email = self.cleaned_data.get("email")
    #     try:
    #         models.User.objects.get(email=email)
    #         raise forms.ValidationError("User already exists with that email")
    #     except models.User.DoesNotExist:
    #         return email

    def clean_password1(self):
        password = self.cleaned_data.get("password")
        password1 = self.cleaned_data.get("password1")

        if password != password1:
            raise forms.ValidationError("Password confirmation does not match")
        else:
            return password

    # def save(self):
    # first_name = self.cleaned_data.get("first_name")
    # last_name = self.cleaned_data.get("last_name")
    # email = self.cleaned_data.get("email")
    # password = self.cleaned_data.get("password")
    # user = models.User.objects.create_user(email, email, password)
    # user.first_name = first_name
    # user.last_name = last_name
    # user.save()

    def save(self, *args, **kwargs):
        user = super().save(commit=False)
        email = self.cleaned_data.get("email")
        password = self.cleaned_data.get("password")
        user.username = email
        user.set_password(password)
        user.save()

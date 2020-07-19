from django import forms

# class ContactForm(forms.Form):
#     name = forms.CharField(max_length=30)
#     mobile = forms.IntegerField()
#     email = forms.EmailField(max_length=50)
#     location = forms.CharField(max_length=100)
#     course = forms.CharField(max_length=30)

class ContactForm(forms.Form):
    name = forms.CharField(
        label="Enter Your Name",
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'Name'
            }
        )
    )
    mobile = forms.IntegerField(
        label="Enter Your Mobile Number",
        widget=forms.NumberInput(
            attrs={
                'class':'form-control',
                'placeholder':'Mobile Number'
            }
        )
    )
    email = forms.EmailField(
        label="Enter Your Email ID",
        widget=forms.EmailInput(
            attrs={
                'class':'form-control',
                'placeholder':'Email ID'
            }
        )
    )
    location = forms.CharField(
        label="Enter Your Location",
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'Location'
            }
        )
    )
    course = forms.CharField(
        label="Enter Your Course",
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'Course'
            }
        )
    )
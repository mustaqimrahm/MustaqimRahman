from django import forms

class NameForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={"type":"text", "class":"form-control", "placeholder":"Name", "id":"name", "name":"name", "required":True}), label='')
    email = forms.EmailField(widget=forms.TextInput(attrs={"type":"email", "class":"form-control", "placeholder":"Enter Email", "id":"email", "name":"email", "required":True}), label='')
    message = forms.CharField(widget=forms.Textarea(attrs={"class":"form-control", "placeholder":"Message", "id":"message", "name":"message", "required":True}), label='')

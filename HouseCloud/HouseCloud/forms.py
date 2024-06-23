from django import forms


class UploadFileForm(forms.Form):
    file = forms.FileField(label="")
    path = forms.CharField(max_length=512)
    father = forms.CharField(max_length=512)

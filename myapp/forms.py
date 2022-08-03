from django import forms

from .models import Comments, GetInfo


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comments
        fields = ('name', 'comment',)

    def __init__(self, *args, **kwargs):
        super(CommentForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control'})


class GetInfoForm(forms.ModelForm):

    class Meta:
        model = GetInfo
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(GetInfoForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control'})

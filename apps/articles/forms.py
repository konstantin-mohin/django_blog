# -*- coding: utf-8 -*-

from django import forms


class FormCommentNonAuth(forms.Form):
    comname = forms.CharField(max_length=128, required=False)
    comemail = forms.EmailField(max_length=100, required=False)
    comsite = forms.CharField(max_length=128, required=False)
    comment = forms.CharField()


class FormCommentAuth(forms.Form):
    comment = forms.CharField()

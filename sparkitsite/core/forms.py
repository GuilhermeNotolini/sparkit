# -*- coding: utf-8 -*-
from django import forms

class SparkCampForm(forms.Form):
	nome_projeto 	= forms.CharField(max_length=256)
	url_projeto 	= forms.CharField(max_length=256, required=False)
	desc_projeto 	= forms.CharField()
	time 			= forms.CharField()
	email 			= forms.EmailField()
	celular 		= forms.CharField()
# -*- coding: utf-8 -*-
from annoying.decorators import render_to
from templated_emails.utils import send_templated_email
from forms import SparkCampForm

@render_to('index.html')
def index(request):
	if request.POST:
		TO_EMAIL = ['contato@sparkit.com.br']
		nome 	= request.POST['nome']
		sender	= request.POST['sender']
		msg 	= request.POST['msg']
		send_templated_email(TO_EMAIL, 'emails/contato', locals())
		ENVIADO = True


	return locals()

@render_to('core/camp.html')
def spark_camp(request):
	form = SparkCampForm(request.POST or None)
	ENVIADO = False
	if form.is_valid():
		TO_EMAIL = ['contato@sparkit.com.br']

		nome 			= form.cleaned_data['nome_projeto']
		nome_projeto 	= form.cleaned_data['nome_projeto']
		url_projeto 	= form.cleaned_data['url_projeto']
		desc_projeto 	= form.cleaned_data['desc_projeto']
		time 			= form.cleaned_data['time']
		email 			= form.cleaned_data['email']
		celular 		= form.cleaned_data['celular']

		send_templated_email(TO_EMAIL, 'emails/spark-campus', locals())
		ENVIADO = True
	return locals()
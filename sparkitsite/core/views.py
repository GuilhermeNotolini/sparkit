# -*- coding: utf-8 -*-
from annoying.decorators import render_to
from forms import SparkCampForm

@render_to('core/index.html')
def index(request):
    return locals()

@render_to('core/camp.html')
def spark_camp(request):
    form = SparkCampForm(request.POST or None)
    if form.is_valid():
    	pass
    
    return locals()
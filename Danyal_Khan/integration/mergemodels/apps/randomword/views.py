from django.shortcuts import render, redirect
from django.conf.urls import url
import string
import random
from django.core.urlresolvers import reverse


# Create your views here.
def index(request):
	return render (request, 'randomword/index.html')

def generate(request, size=14, chars=string.ascii_uppercase + string.digits):
	
	
		request.session['word']=''.join(random.choice(chars) for _ in range(14))
		
		
		if "counter" in request.session:
			request.session['counter']+=1
		else: 
			request.session['counter']=0
		
		

	
	
		return redirect(reverse('random:my_index'))
	




# 		print "*" *100
# 		print(request.POST)
# 		print "*" *100
# 		print "line two"
# 		print(request.POST['word'])

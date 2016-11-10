from django.shortcuts import render, HttpResponse
import time

# Create your views here.
def index(request):
	context = {
	"date":time.strftime('%b %d, %Y'),
	"time":time.strftime('%l:%M%p')
	
	}
	print time.strftime('%l')
	return render(request, 'timedisplay/index.html', context)




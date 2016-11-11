from django.shortcuts import render,redirect

def index(request):
	return render (request,'index.html')

def show_pic(request,color):
	if color == 'blue':
		return render(request,'blue.html')
	elif color == 'orange':
		return render(request,'orange.html')
	elif color == 'red':
		return render(request,'red.html')
	elif color == 'purple':
		return render(request,'purple.html')
	elif color=='':
		return render(request,'tmnt.html')
	else:
		return render(request,'worng.html')
	
	
	


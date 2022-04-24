from django.shortcuts import render

# Create your views here.

def home(request):
	if request.method == 'POST':
		a = request.POST['bir']
		b = request.POST['ikki']
		c = request.POST
		if '+' in c:
			d = int(a)+int(b)
			return render(request,'kalkul/home.html',{'d':d})
		elif '-' in c:
			d = int(a)-int(b)
			return render(request,'kalkul/home.html',{'d':d})
		elif '*' in c:
			d = int(a)*int(b)
			return render(request,'kalkul/home.html',{'d':d})
		elif '/' in c:
			d = int(a)/int(b)
			return render(request,'kalkul/home.html',{'d':d})
	return render(request,'kalkul/home.html')

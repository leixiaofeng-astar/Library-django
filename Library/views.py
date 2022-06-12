from django.http import HttpResponse

def home(request):
	return HttpResponse("<h1>Welcome Django class, Aoxuan and Yanyang<h1>\n<h2>Class completed<h2>")

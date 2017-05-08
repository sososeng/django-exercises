from django.template.response import TemplateResponse
# Create your views here.

def homepage(request):
	context={
	'page_title': 'Test Home Page'
	}
	return TemplateResponse(request, 'homepage.html',context)

def profile(request):

	return TemplateResponse(request, 'index.html',{})
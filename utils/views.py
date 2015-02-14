from django.shortcuts import render

def view_404(request):
	return render(request, 'utils/404.html')

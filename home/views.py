from django.shortcuts import render

def post_list(request):
    return render(request, 'home/project_list.html', {})

# Create your views here.

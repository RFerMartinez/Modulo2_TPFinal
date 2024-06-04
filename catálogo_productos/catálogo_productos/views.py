from django.shortcuts import render

def home(request):
    template="home.html"
    ctx = {

    }
    return render(request=request, template_name=template, context=ctx)


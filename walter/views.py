from django.shortcuts import render

def walter_home(request):
    return render(request, 'static/index.html', {"foo": "bar"},
        content_type="application/xhtml+xml")


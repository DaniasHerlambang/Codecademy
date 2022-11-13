from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.shortcuts import HttpResponse
from django.views.generic import CreateView
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from .models import Bank_result

def execute(request):
    response_data = {}
    if request.method == 'POST':
        text = request.POST.get('text')
        print(text)
        response_data['text'] = text
        Bank_result.objects.create(
            result = text,
            )
        result = Bank_result.objects.last()
        mydict = {
            'value': result ,
            'result': Bank_result.objects.last()
        }
        return render(request, 'home.html', {'result':mydict})
    else:
        result = Bank_result.objects.last()
        mydict = {
            'value': "for x in range(6):" ,
            'result': Bank_result.objects.last()
        }
        return render(request, 'home.html', {'result': mydict})

from django.shortcuts import render

# Create your views here.
def mpesa(request):
    return render(request,'payments/mpesa.html')
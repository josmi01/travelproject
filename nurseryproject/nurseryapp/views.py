# from django.http import HttpResponse
from django.shortcuts import render

from . models import place

from . models import team
# Create your views here.


# def home(request):
#     return render(request,"home.html")
# def about(request):
#     return HttpResponse("this is nursery application")
# def contact(request):
#     return render(request,"contact.html")
# def details(request):
#     return HttpResponse("this is nursery.it located in vadakkencherry.please visit our nursery")
# def thanks(request):
#     return render(request,"thanks.html")
def demo(request):
  return render (request,"index.html")
# def equations(request):
#     x=int(request.GET['num1'])
#     y=int(request.GET['num2'])
#     add=x+y
#     sub=x-y
#     mul=x*y
#     div=x/y
#     return render(request,"result.html",{'addition':add,'subtraction':sub,'multiplication':mul,'division':div})
def demo(request):
    obj=place.objects.all()
    tem=team.objects.all()
    return render(request,"index.html",{'result':obj,'res':tem})



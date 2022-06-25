from django.http import HttpResponse
from django.shortcuts import render,redirect
import joblib
from django.contrib import messages
from .BC import blockchain,getBlockDetails,generateNextBlock


def homepage(request):
    return render(request, "home.html")


def AddBlock(request):
    lis = []

    lis.append(request.GET["PID"])
    lis.append(request.GET["PQ"])
    lis.append(request.GET["OID"])
    generateNextBlock(lis)
    messages.success(request,"Product added sucessfully")
    # return render(request, "addblock.html", {"lis": lis})
    return redirect('/')

def result(request):
    return render(request, "result.html" , {"ans": getBlockDetails()})


#

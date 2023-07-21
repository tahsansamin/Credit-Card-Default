from django.shortcuts import render
from django.http import HttpResponse
import joblib


# Create your views here.
def home(request):
    return  render(request,'home.html')

def result(request):
    rf = joblib.load('credit.sav')
    lis=[]
    lis.append(request.GET['LIMIT_BAL'])
    lis.append(request.GET['AGE'])
    lis.append(request.GET['PAY_0'])
    lis.append(request.GET['PAY_ATM1'])
    lis.append(request.GET['PAY_ATM2'])
    lis.append(request.GET['PAY_ATM3'])
    
    lis.append(request.GET['PAY_ATM5'])
    lis.append(request.GET['PAY_ATM6'])
    lis.append(request.GET['PAY_2'])
    lis.append(request.GET['BILL_ATM1'])
    lis.append(request.GET['BILL_ATM2'])
    lis.append(request.GET['BILL_ATM3'])
    lis.append(request.GET['BILL_ATM4'])
    lis.append(request.GET['BILL_ATM5'])
    lis.append(request.GET['BILL_ATM6']) 

    ans = rf.predict([lis])
    pred = ""
    if ans == 0:
        pred = "default"
    else:
        pred = "won't default"

    print('the result is',pred)
    
    
    
    return render(request,'result.html',{'pred':pred})

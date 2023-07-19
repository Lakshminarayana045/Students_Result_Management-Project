from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import studentdata
from.models import hscdata
from .models import degreedata
from .models import btechdata
import faker
fake=faker.Faker()
def mainpage(request):
    return render(request,'mainpage.html')
@login_required(login_url='login')
def ssc(request):
    if request.method == 'POST':
        d=request.POST.get('htno')
        return redirect('resultdata',d)
    else:
        return render(request, 'ssc.html')

def resultdata(request,d):
    data = studentdata.objects.get(hallno=d)
    u = studentdata.objects.filter(hallno=d).exists()
    m=(data.marathi+ data.hindi+data.english+data.math+data.science+data.socialsci)
    if u == True:
        p=(m//6)
        if data.marathi >= 35 and data.hindi >= 35 and data.english >= 35 and data.math >= 35 and data.science >= 35 and data.socialsci >= 35:
            if m>=210 and m<308:
                context = {'data': data, 're': 'Pass', 'g':'D','m':m,'p':p}
                return render(request, 'resultdata.html',context)
            if m>=308 and m<406:
                context = {'data': data, 're': 'Pass', 'g':'C','m':m,'p':p}
                return render(request, 'resultdata.html',context)
            if m>=406 and m<504:
                context = {'data': data, 're': 'Pass', 'g':'B','m':m,'p':p}
                return render(request, 'resultdata.html',context)
            if m>=504 and m<600:
                context = {'data': data, 're': 'Pass', 'g':'A','m':m,'p':p}
                return render(request, 'resultdata.html',context)
        else:
            context = {'data': data, 're': 'Fail', 'g': 'E', 'm': m,'p':p}
            return render(request, 'resultdata.html', context)
    else:
        return HttpResponse('Invalid Hallticket No')

@login_required(login_url='login')
def hsc(request):
    if request.method == 'POST':
        d=request.POST.get('htno')
        return redirect('intermidiate',d)
    else:
        return render(request, 'hsc.html')

def intermidiate(request,d):
    data = hscdata.objects.get(hallno=d)
    u =  hscdata.objects.filter(hallno=d).exists()
    m=(data.english+data.marathi+data.math+data.physics+data.chemistry+data.biology)
    if u == True:
        p=(m//6)
        if data.english >= 35 and data.marathi >= 35 and data.math >= 35 and data.physics >= 35 and data.chemistry >= 35 and data.biology >= 35:
            if m>=210 and m<308:
                context = {'data': data, 're': 'Pass', 'g':'D','m':m,'p':p}
                return render(request, 'intermidiate.html',context)
            if m>=308 and m<406:
                context = {'data': data, 're': 'Pass', 'g':'C','m':m,'p':p}
                return render(request, 'intermidiate.html',context)
            if m>=406 and m<504:
                context = {'data': data, 're': 'Pass', 'g':'B','m':m,'p':p}
                return render(request, 'intermidiate.html',context)
            if m>=504 and m<600:
                context = {'data': data, 're': 'Pass', 'g':'A','m':m,'p':p}
                return render(request, 'intermidiate.html',context)
        else:
            context = {'data': data, 're': 'Fail', 'g': 'E', 'm': m,'p':p}
            return render(request, 'intermidiate.html', context)
    else:
        return HttpResponse('Invalid Hallticket No')



@login_required(login_url='login')
def degree(request):
    if request.method == 'POST':
        d=request.POST.get('htno')
        return redirect('degreeData',d)
    else:
        return render(request, 'degree.html')

def degreeData(request,d):
    data = degreedata.objects.get(hallno=d)
    u = degreedata.objects.filter(hallno=d).exists()
    m=(data.bcomunication+ data.pm+data.dbms+data.clanguage+data.bstatistics)
    if u == True:
        p=(m//5)
        if data.bcomunication >= 35 and data.pm >= 35 and data.dbms >= 35 and data.clanguage >= 35 and data.bstatistics >=35:
            if m>=175 and m<256:
                context = {'data': data, 're': 'Pass', 'g':'D','m':m,'p':p}
                return render(request, 'degreeData.html',context)
            if m>=256 and m<337:
                context = {'data': data, 're': 'Pass', 'g':'C','m':m,'p':p}
                return render(request, 'degreeData.html',context)
            if m>=337 and m<418:
                context = {'data': data, 're': 'Pass', 'g':'B','m':m,'p':p}
                return render(request, 'degreeData.html',context)
            if m>=418 and m<500:
                context = {'data': data, 're': 'Pass', 'g':'A','m':m,'p':p}
                return render(request, 'degreeData.html',context)
        else:
            context = {'data': data, 're': 'Fail', 'g': 'E', 'm': m,'p':p}
            return render(request, 'degreeData.html', context)
    else:
        return HttpResponse('Invalid Hallticket No')


@login_required(login_url='login')
def btech(request):
    if request.method == 'POST':
        d=request.POST.get('htno')
        return redirect('btechData',d)
    else:
        return render(request, 'btech.html')

def btechData(request,d):
    data = btechdata.objects.get(hallno=d)
    u = btechdata.objects.filter(hallno=d).exists()
    m=(data.cd+data.se+data.ai+data.dcs+data.aca+data.mad)
    if u == True:
        p=(m//6)
        if data.cd >= 35 and data.se>= 35 and data.ai >= 35 and data.dcs >= 35 and data.aca >=35 and data.mad>=35:
            if m >= 210 and m < 308:
                context = {'data': data, 're': 'Pass', 'g': 'D', 'm': m, 'p': p}
                return render(request, 'btechData.html', context)
            if m >= 308 and m < 406:
                context = {'data': data, 're': 'Pass', 'g': 'C', 'm': m, 'p': p}
                return render(request, 'btechData.html', context)
            if m >= 406 and m < 504:
                context = {'data': data, 're': 'Pass', 'g': 'B', 'm': m, 'p': p}
                return render(request, 'btechData.html', context)
            if m >= 504 and m < 600:
                context = {'data': data, 're': 'Pass', 'g': 'A', 'm': m, 'p': p}
                return render(request, 'btechData.html', context)
        else:
            context = {'data': data, 're': 'Fail', 'g': 'E', 'm': m, 'p': p}
            return render(request, 'btechData.html', context)
    else:
        return HttpResponse('Invalid Hallticket No')

def signup(request):
        if request.method == "POST":
            if request.POST['password1'] == request.POST['password2']:
                try:
                    User.objects.get(username=request.POST['username'])
                    messages.warning(request, 'username are already exist!')
                    return redirect('signup')

                    # return render(request, 'signup.html', {'error': 'Username is already taken!'})
                except User.DoesNotExist:

                    user = User.objects.create_user(request.POST['username'], password=request.POST['password1'])
                    auth.login(request, user)
                    return redirect('login')
            else:
                return render(request, 'signup.html', {'error': 'Password does not match!'})
        else:
            return render(request, 'signup.html')


def login(request):
    if request.method == 'POST':
        user = auth.authenticate(username=request.POST['username'], password=request.POST['password'])
        if user is not None:
            auth.login(request, user)
            return redirect('main')
        else:
            return HttpResponse('Your Pssword Is Incorrct.....')
    else:
        return render(request, 'login.html')


def Logout(request):
    if request.method == 'POST':
        auth.logout(request)
    return redirect('login')

def generatedata(request):
    for i in range(30):
        studentdata(
            firstname=fake.first_name(),
            lastname=fake.last_name(),
            hallno=fake.random_element(elements=range(10001,20000)),
            marathi=fake.random_element(elements=range(36,100)),
            hindi=fake.random_element(elements=range(36,100)),
            english=fake.random_element(elements=range(36,100)),
            math=fake.random_element(elements=range(36,100)),
            science=fake.random_element(elements=range(36,100)),
            socialsci=fake.random_element(elements=range(1,100))
        ).save()
    return redirect('ssc')

def savedata(request):
    for i in range(30):
        hscdata(
            firstname=fake.first_name(),
            lastname=fake.last_name(),
            hallno=fake.random_element(elements=range(20001,30000)),
            english=fake.random_element(elements=range(36,100)),
            marathi=fake.random_element(elements=range(36,100)),
            math=fake.random_element(elements=range(36,100)),
            physics=fake.random_element(elements=range(36,100)),
            chemistry=fake.random_element(elements=range(36,100)),
            biology=fake.random_element(elements=range(1,100))
        ).save()
    return redirect('hsc')

def storeData(request):
    for i in range(30):
        degreedata(
            firstname=fake.first_name(),
            lastname=fake.last_name(),
            hallno=fake.random_element(elements=range(30001,40000)),
            bcomunication=fake.random_element(elements=range(36,100)),
            pm=fake.random_element(elements=range(36,100)),
            dbms=fake.random_element(elements=range(36,100)),
            clanguage=fake.random_element(elements=range(36,100)),
            bstatistics=fake.random_element(elements=range(36,100))
         ).save()
    return redirect('degree')


def savebtech(request):
    for i in range(30):
        btechdata(
            firstname=fake.first_name(),
            lastname=fake.last_name(),
            hallno=fake.random_element(elements=range(40001,50000)),
            cd=fake.random_element(elements=range(36,100)),
            se=fake.random_element(elements=range(36,100)),
            ai=fake.random_element(elements=range(36,100)),
            dcs=fake.random_element(elements=range(36,100)),
            aca=fake.random_element(elements=range(36,100)),
            mad=fake.random_element(elements=range(36,100))

        ).save()
    return redirect('btech')

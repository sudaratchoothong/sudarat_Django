from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import sudarat_tb_model
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.contrib.auth.decorators import login_required, permission_required

# Create your views here.
# def index(request, fname, lname, age, hobby):
#     # return HttpResponse("Hello Django")
#     data ={
#         'fname' : fname,
#         'lname' : lname,
#         'age'   : age,
#         'hobby' : hobby
#     }
#     return render(request, 'myWebsite/index.html', data)

def index(request):
    content = sudarat_tb_model.objects.all().order_by("-id")
    data ={
        'news' : content,

    }
    return render(request, 'sudarat_app/index.html', data)
    

def showName(request, fname,lname):
    return HttpResponse("My name is "+ fname +" "+ lname)

@login_required(login_url='/loginUser')
def addStudent(request):
    return render(request, 'sudarat_app/addNews.html')

def recordNews(request):
    member_studentId = request.POST['member_studentId']
    member_firstname = request.POST['member_firstname']
    member_lastname = request.POST['member_lastname']
    member_detail = request.POST['member_detail']
    member_image = request.FILES['member_image']
    content = sudarat_tb_model(member_studentId=member_studentId, member_firstname=member_firstname,
                               member_lastname=member_lastname, member_detail=member_detail, member_image=member_image)
    content.save()
    return redirect('/contentNews')

@login_required(login_url='/loginUser')
@permission_required('is_saff', login_url='/loginWarning')
def contentNews(request):
    content = sudarat_tb_model.objects.all()
    data ={
        'content' : content
    }
    return render(request, 'sudarat_app/contentNews.html', data)

def contentEdit(request):
    id = request.GET['id']
    result = sudarat_tb_model.objects.filter(pk=id)
    data = {
        'result' : result   
    }
    return render(request, 'sudarat_app/contentEdit.html', data)


def contentUpdate(request):
    member_studentId = request.POST['member_studentId']
    member_firstname = request.POST['member_firstname']
    member_lastname = request.POST['member_lastname']
    member_detail = request.POST['member_detail']
    member_image = request.FILES['member_image']

    id = request.POST['id']
    content = sudarat_tb_model.objects.get(pk=id)
    content.member_studentId = member_studentId
    content.member_firstname = member_firstname
    content.member_lastname = member_lastname
    content.member_detail = member_detail
    content.member_image = member_image
    content.save()
    return redirect('/contentNews')

def contentDelete(request):
    id = request.GET['id']
    content = sudarat_tb_model.objects.get(pk=id)
    content.delete()
    return redirect('/contentNews')

@login_required(login_url='/loginUser')
@permission_required('is_saff', login_url='/loginWarning')
def contentShow(request):
    id = request.GET['id']
    result = sudarat_tb_model.objects.filter(pk=id)
    data = {
        'result' : result,
    }
    return render(request,'sudarat_app/contentShow.html',data)

def registUser(request):
    return render(request,'sudarat_app/registUser.html')

def registData(request):
    fname = request.POST['fname']
    lname = request.POST['lname']
    email = request.POST['email']
    username = request.POST['username']
    password = request.POST['password']
    repassword = request.POST['repassword']
    
    if password == repassword:
        if User.objects.filter(username = username).exists():
            messages.error(request,'Username has been already usend')
            return redirect('/registUser')
        elif User.objects.filter(email = email).exists():
            messages.error(request,'Email has been already used')
            return redirect('/registUser')
        else:
            user = User.objects.create_user(
            first_name = fname,
            last_name = lname,
            username = username,
            password = password,
            email = email
        ) 
        user.save()
        return HttpResponse("Data saved")
    else:
            messages.error(request,'Password is not equal to re-password')
            return redirect('/registUser') 

def loginUser(request):
    if request.user.is_authenticated:
        return redirect('/')
    return render(request, 'sudarat_app/loginUser.html') 

def loginData(request):
    username = request.POST['username']
    password = request.POST['password']
    user = auth.authenticate(username=username, password=password)
    if user is not None:
        auth.login(request, user)
        return redirect('/')
    else:
        messages.error(request, 'Login error')
        return redirect('/loginUser')
    
def logoutUser(request):
    auth.logout(request)
    return redirect('/loginUser')

def loginWarning(request):
    return render(request,'sudarat_app/loginWarning.html')



def handler404(request, exception):
    return render(request,'sudarat_app/404errorPage.html')


# def handler500(request, exception=None):
#     return render(request,'sudarat_app/500errorPage.html')


# def resultPage(request):
#     # topic = request.POST['topic_news']
#     # detail = request.POST['detail_news']
#     topic = request.GET['topic_news']
#     detail = request.GET['detail_news']

#     data ={

#         'topic' : topic,
#         'detail' : detail,
        
#     }

#     return render(request, 'myWebsite/resultPage.html', data) 

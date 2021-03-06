from django.shortcuts import render, get_object_or_404, redirect
from .models import UserInfo,Review,Comment,Item
from django.contrib.auth.models import User
from django.contrib import auth

# Create your views here.
def index(request):
    return render(request, 'index.html')

def search(request):
    search = request.GET['search']
    search1 = Item.objects.filter(name__icontains=search)
    return render(request, 'item.html', {'arr':search1})

def item(request, id):
    item = Item.objects.filter(gender = id)
    return render(request, 'item.html', {'arr':item , 'item1' : id })

def item1(request):
    item1 = Item.objects.filter(gender__in = [1,2,3])
    return render(request, 'item1.html', {'arr': item1})

def item2(request):
    item2 = Item.objects.filter(gender = 3)
    return render(request, 'item2.html', {'arr':item2})

def login(request):
    if request.method == 'POST':
            username = request.POST['user_name']
            password = request.POST['password']
            user = auth.authenticate(request, username=username, password=password)
            if user is not None:
                auth.login(request, user)
                return redirect('/')
            else:
                return render(request, 'login.html', {'error': 'username or password is incorrect.'})
    else:
        return render(request, 'login.html')
    return render(request, 'login.html')

def logout(request):
    #if request.method == 'POST':
        auth.logout(request)
        return redirect('/')
    #return render(request, 'index.html')

def join1(request):
    if request.method == 'POST':
        if request.POST['password1'] == request.POST['password2']:
            user = User.objects.create_user(
                request.POST['user_name'], password=request.POST['password1'], email=request.POST['email'], first_name=request.POST['first_name'])
            auth.login(request, user)
            return redirect('/')
        else:
            return render(request, 'join1.html', {'error': '비밀번호와 비밀번호 확인이 일치하지 않습니다'})
    return render(request, 'join1.html')

def join2(request):
    return render(request, 'join2.html')

def info1(request, userinfo_id):
    userinfo = get_object_or_404(UserInfo, pk=userinfo_id)
    return render(request, 'info1.html',{'userinfo':userinfo})

def info2(request, userinfo_id):
    userinfo = get_object_or_404(UserInfo, pk=userinfo_id)
    return render(request, 'info2.html',{'userinfo':userinfo})

def info3(request, userinfo_id):
    userinfo = get_object_or_404(UserInfo, pk=userinfo_id)
    return render(request, 'info3.html',{'userinfo':userinfo})

def info4(request, userinfo_id):
    userinfo = get_object_or_404(UserInfo, pk=userinfo_id)
    return render(request, 'info4.html',{'userinfo':userinfo})

def info5(request, userinfo_id):
    userinfo = get_object_or_404(UserInfo, pk=userinfo_id)
    return render(request, 'info5.html',{'userinfo':userinfo})

def result1(request):
    return render(request, 'result1.html')

def result2(request, userinfo_id):
    userinfo = get_object_or_404(UserInfo, pk=userinfo_id)
    if request.GET['type'] == "sexy":
         # 남자 솔로
        if userinfo.couple == 1 and userinfo.gender == True:
            item = Item.objects.filter(gender = 1, types = '섹시')
            return render(request, 'result2.html', {'arr':item})
        # 여자 솔로
        if userinfo.couple == 1 and userinfo.gender == False:
            item = Item.objects.filter(gender = 2, types = '섹시')
            return render(request, 'result2.html', {'arr':item})
        # 남자 커플 남남
        if userinfo.couple == 2 and userinfo.gender == True:
            item = Item.objects.filter(gender = 1, types = '섹시')
            return render(request, 'result2.html', {'arr':item})
        # 남자 커플 남녀
        if userinfo.couple == 3 and userinfo.gender == True:
            item = Item.objects.filter(gender = 3, types = '섹시')
            return render(request, 'result2.html', {'arr':item})
        # 여자 커플 여여
        if userinfo.couple == 4 and userinfo.gender == False:
            item = Item.objects.filter(gender = 2, types = '섹시')
            return render(request, 'result2.html', {'arr':item})
        # 여자 커플 남녀
        if userinfo.couple == 3 and userinfo.gender == False:
            item = Item.objects.filter(gender = 3, types = '섹시')
            return render(request, 'result2.html', {'arr':item})

        item = Item.objects.filter(types = '섹시')
        return render(request, 'result2.html', {'arr':item})
    else:
         # 남자 솔로
        if userinfo.couple == 1 and userinfo.gender == True:
            item = Item.objects.filter(gender = 1).exclude(types = '섹시')
            return render(request, 'result2.html', {'arr':item})
        # 여자 솔로
        if userinfo.couple == 1 and userinfo.gender == False:
            item = Item.objects.filter(gender = 2).exclude(types = '섹시')
            return render(request, 'result2.html', {'arr':item})
        # 남자 커플 남남
        if userinfo.couple == 2 and userinfo.gender == True:
            item = Item.objects.filter(gender = 1).exclude(types = '섹시')
            return render(request, 'result2.html', {'arr':item})
        # 남자 커플 남녀
        if userinfo.couple == 3 and userinfo.gender == True:
            item = Item.objects.filter(gender = 3).exclude(types = '섹시')
            return render(request, 'result2.html', {'arr':item})
        # 여자 커플 여여
        if userinfo.couple == 4 and userinfo.gender == False:
            item = Item.objects.filter(gender = 2).exclude(types = '섹시')
            return render(request, 'result2.html', {'arr':item})
        # 여자 커플 남녀
        if userinfo.couple == 3 and userinfo.gender == False:
            item = Item.objects.filter(gender = 3).exclude(types = '섹시')
            return render(request, 'result2.html', {'arr':item})

        item = Item.objects.all().exclude(types = '섹시')
        return render(request, 'result2.html', {'arr':item})
    return render(request, 'result2.html')

def survey(request, userinfo_id):
    userinfo = get_object_or_404(UserInfo, pk=userinfo_id)
    return render(request, 'survey.html',{'userinfo':userinfo})
    
def mypage(request, userinfo_id):
    #userinfo = UserInfo.objects.filter(user_id=User.objects.get(username = request.user.get_username()))
    userinfo = get_object_or_404(UserInfo, pk=userinfo_id)
    return render(request, 'mypage.html',{'userinfo':userinfo})

def goinfo(request, userinfo_id):
    userinfo = get_object_or_404(UserInfo, pk=userinfo_id)
    return redirect('/info1/'+str(userinfo_id))

def order(request):
    return render(request, 'order.html')

def detail(request, id):
    detail = get_object_or_404(Item, pk=id)
    review = Review.objects
    userinfo = UserInfo.objects
    return render(request, 'detail.html',{'detail':detail, 'review':review, 'userinfo':userinfo})

def loading(request):
    return render(request, 'loading.html')

def chanege_order(request):
    return redirect('/order')

def review_create(request):
    cr = Review()
    cr.user_id = User.objects.get(username = request.user.get_username())
    cr.contents = request.GET['contents']
    cr.item_id = request.GET['item_id']
    cr.save()
    return redirect('/detail/'+str(cr.item_id))

# 로그인하고 나서 마이페이지 가는 순간 userinfo 만들기
def infocreate(request):
    userinfo = UserInfo()
    userinfo.user_id = User.objects.get(username = request.user.get_username())
    userinfo.gender = True
    userinfo.couple = 0
    userinfo.save()
    return redirect('/mypage/'+str(userinfo.id))

# info1에서 성별 물어보면 성별만 수정해서 info2로
def infogenderud(request, userinfo_id):
    userinfo = get_object_or_404(UserInfo, pk=userinfo_id)
    userinfo.gender = request.GET['gender']
    #userinfo.couple = 0
    userinfo.save()
    return redirect('/info2/'+str(userinfo_id))

# info2에서 커플인지 아닌지 물어보면 커플인지 수정
def infocoupleud(request, userinfo_id):
    userinfo = get_object_or_404(UserInfo, pk=userinfo_id)
    userinfo.couple = request.GET['couple']
    userinfo.save()
    if request.GET['couple'] == "1":
        return redirect('/info5/'+str(userinfo_id)) #솔로니까 info5로 가게
    else:
        return redirect('/info3/'+str(userinfo_id)) #커플이니까 info3로 가게

# info3에서 커플 타입 물어보고 수정
def infotypeud(request, userinfo_id):
    userinfo = get_object_or_404(UserInfo, pk=userinfo_id)
    userinfo.couple = request.GET['couple']
    userinfo.save()
    return redirect('/info4/'+str(userinfo_id))

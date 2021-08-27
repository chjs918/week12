from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator
from django.utils import timezone
from .models import Drama
from .forms import dramaForm
from django.http import HttpResponse,JsonResponse
import json

# Create your views here.

def home(request):
    blog = Drama.objects.all()
    blogList = Drama.objects.all()
    paginator = Paginator(blogList, 3)
    page = request.GET.get('page')
    posts = paginator.get_page(page) 
    return render(request,'home.html',{'blog' : blog, 'posts' : posts})

def detail(request, blog_id):
    blog_detail = get_object_or_404(Drama, pk = blog_id)
    return render(request, 'detail.html' ,{'blog' : blog_detail})

def new(request):
    if request.method == 'POST': #폼 다채우고 저장버튼 눌렀을 때
        form = dramaForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit = False)
            post.date = timezone.now()
            post.save()
            return redirect('detail', post.id)
        return redirect('home')
    else:  #글을 쓰기위해 들어갔을 때
        form = dramaForm()
        return render(request,'new.html', {'form':form})


def edit(request, blog_id):
    post = get_object_or_404(Drama, pk = blog_id)
    if request.method == 'GET':  #수정하려고 들어갔을 때
        form = dramaForm(instance = post)
        return render(request, 'edit.html', {'form' : form})
    else:   #수정 끝나고 수정 버튼을 눌렀을 때
        form = dramaForm(request.POST, request.FILES, instance = post)
        if form.is_valid():
            post = form.save(commit = False)
            form.date = timezone.now()
            post.save()
            return redirect('/dramaboard/detail/' + str(blog_id))
        return redirect('home')

def delete(request, blog_id):
    blog_delete =  Drama.objects.get(id = blog_id)
    blog_delete.delete()
    return redirect('home')

def post_likes(request): 
  if request.is_ajax(): #ajax 방식일 때 아래 코드 실행
    blog_id = request.GET['blog_id'] #좋아요를 누른 게시물id (blog_id)가지고 오기
    post = Drama.objects.get(id=blog_id) 
    
    user = request.user #request.user : 현재 로그인한 유저
    if post.like.filter(id = user.id).exists(): #이미 좋아요를 누른 유저일 때
      post.like.remove(user) #like field에 현재 유저 추가
      message = "좋아요 취소" #화면에 띄울 메세지
    else: #좋아요를 누르지 않은 유저일 때
      post.like.add(user) #like field에 현재 유저 삭제
      message = "좋아요" #화면에 띄울 메세지
    #post.like.count() : 게시물이 받은 좋아요 수  
  context = {
    'like_count' : post.like.count(),
    "message":message,
  }
  return HttpResponse(json.dumps(context), content_type='application/json')

def dramamap(request):
  return render(request, 'map.html')

def dramamap1(request):
  return render(request, 'map1.html')

def dramamap2(request):
  return render(request, 'map2.html')

def dramamap3(request):
  return render(request, 'map3.html')

def dramamap4(request):
  return render(request, 'map4.html')

def dramamap5(request):
  return render(request, 'map5.html')
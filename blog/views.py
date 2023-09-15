from django.shortcuts import render
#import model
from .models import Post
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# Create your views here.

#create func สำหรับอ่าน post ทั้งหมด
def post_list(request):
    #create ตัวแปรที่เก็บ post ทั้งหมดที่ publish
    posts=Post.published.all()

    #create ตัวแปรกำหนดจำนวน post ต่อ page
    per_page=1
    paginator=Paginator(posts,per_page)
    page=request.GET.get('page')
    try:
        posts=paginator.page(page)
    except PageNotAnInteger:
        posts=paginator.page(1)
    except EmptyPage:
        posts=paginator.page(paginator.num_pages)

    #ส่งค่า post ไปแสดง template 
    return render(request,'blog/post/list.html',{'posts':posts})

#create func to display POST detail
def post_detail(request,id):
    #create ตัวแปร post เก็บ id 
    post=Post.published.get(id=id)
    #ส่งค่า post ไปแสดง template 
    return render(request,'blog/post/detail.html',{'post':post})
from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from craigslist_app.models import Category, Post
from django.http import HttpResponse
from craigslist_app.forms import CategoryForm, PostForm
# Create your views here.
def index(request):
    data = {
        "all_categories": Category.objects.all()
    }
    return render(request, "pages/category/category_list.html", data)
def category_new(request):
    form = CategoryForm(request.POST or None)
    data = {
        "form": form
    }
    if request.method == "POST":
        try:
             form.save()
             return redirect("")
        except:
            return HttpResponse('Error during category creation')
    return render(request, "pages/category/category_new.html", data)
def category_edit(request, category_id):
    form = CategoryForm()
    data = {
        "form": form
    }
    return render(request, "pages/category/category_new.html", data)        

def category_detail(request, category_id):
    try:
        category = Category.objects.get(id=category_id)
    except:
        return HttpResponse(f"category: {category_id} doesnt exist")
    data = {
        "category": category
    }
    return render(request, "pages/category/category_detail.html", data)

def post_list(request, category_id):
     try:
        category = Category.objects.get(id=category_id)
     except:
        return HttpResponse(f"post: {category_id} doesnt exist")

     data = {
         "category": category
     }
     return render(request, "pages/post/post_list.html", data)

def post_detail(request, category_id, post_id):
    try:
        post = Post.objects.get(id=post_id)
    except:
        return HttpResponse(f"post {post_id} doenst exist")
    data = {
        "post": post
    }
    return render(request, "pages/post/post_detail.html", data)


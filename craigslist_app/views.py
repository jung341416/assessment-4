from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from craigslist_app.models import Category, Post
from django.http import HttpResponse
from craigslist_app.forms import CategoryForm, PostForm
# Create your views here.
def index(request):
    data = {
        "all_categories": get_all_categories()
    }
    return render(request, "pages/category/category_list.html", data)

def category_new(request):
    form = CategoryForm(request.POST or None)
    data = {
        "add_or_edit": "Add",
        "form": form
    }
    if request.method == "POST":
        try: 
            form.save()
            return redirect("home")
        except:
            return HttpResponse('Error during category creation')
    return render(request, "pages/category/category_new.html", data)

def category_edit(request, category_id):
  
    category = get_category(category_id)
    form = CategoryForm(request.POST or None, instance=category)
    data = {
        "add_or_edit": 'Edit',
        "form": form
    }
    if request.method == "POST":
        try:
            form.save()
            return redirect("category_detail", category.id)
        except:
            return HttpResponse('Error during category Edit')
    return render(request, "pages/category/category_new.html", data)        

def category_detail(request, category_id):
    try:
        category = get_category(category_id)
    except:
        return HttpResponse(f"category: {category_id} doesnt exist")
    data = {
        "category": category
    }
    return render(request, "pages/category/category_detail.html", data)

def category_delete(request, category_id):
    category = get_category(category_id)
    try:
        category.delete()
    except:
        return HttpResponse(f"category: {category_id} doesnt exist")
    return redirect("home")

def post_new(request, category_id):
     category = get_category(category_id)
     form = PostForm(request.POST or None)
     data = {
         "add_or_edit": 'Add',
         "category": category,
         "form": form
     }
     if request.method == "POST":
        try: 
            form.save()
            return redirect("category_detail", category.id)
        except:
            return HttpResponse('Error during post creation')
     return render(request, "pages/post/post_new.html", data)

def post_list(request, category_id):
    category = get_category(category_id)
    data = {
        "category": category
    }
    return render(request, "pages/post/post_list.html", data)

def post_detail(request, category_id, post_id):
    post = get_post(post_id)
    category = get_category(category_id)
    data = {
        "post": post,
        "category": category
    }
    return render(request, "pages/post/post_detail.html", data)    

def post_edit(request, category_id, post_id):
    category = get_category(category_id)
    post = get_post(post_id)
    form = PostForm(request.POST or None, instance=post)
    data = {
        "add_or_edit": "Edit",
        "post": post,
        "category": category,
        "form": form
    }
    if request.method == "POST":
        try:
            form.save()
            return redirect('post_list', category.id)
        except:
            HttpResponse(f"form doens't exist")
    return render(request, "pages/post/post_new.html", data)

def post_delete(request, category_id, post_id):
    category = get_category(category_id)
    post = get_post(post_id)
    try:
        post.delete()
    except:
        HttpResponse('Failed to Delete Post')
    
    return redirect('post_list', category.id)



def get_category(category_id):
    return Category.objects.get(id=category_id)
def get_post(post_id):
    return Post.objects.get(id=post_id)
def get_all_categories():
    return Category.objects.all()
def get_all_posts():
    return Post.objects.all()
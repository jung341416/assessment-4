from django.forms import ModelForm
from craigslist_app.models import Category, Post

class CategoryForm(ModelForm):
    class Meta:
        model =  Category
        fields = "__all__"

class PostForm(ModelForm):
    class Meta:
        model =  Post
        fields = "__all__"


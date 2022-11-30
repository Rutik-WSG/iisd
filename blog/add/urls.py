from django import views
from django.contrib import admin
from django.db import router
from django.urls import path

# from enroll.views import login
# from enroll import views
from .views import *
from add import views

urlpatterns = [
    path('user/login/',login),
    path("add",Add),
    path("get",Show),
    path("update/<int:pk>",update),
    path('delete/<int:pk>', views.delete_items, name='delete-items'),
    path('add-bookmark',UserAddBookMark.as_view(),name='add-bookmark'),
    path('remove-bookmark/<int:bookmark_id>',UserRemoveBookMark.as_view(),name='remove-bookmark'),
    path('view-bookmark/<int:user_id>',UserViewBookMark.as_view(),name='view-bookmarks'),
    path("view-get",Show1),
    path("view-comments",Show2),
    path('comments', views.Usercomment.as_view(), name='comment'),
    #path('view-comment/<int:id>', Usercomment1.as_view(),name='view-comment'),
    path('add-category',AddCategoryTypeView.as_view(),name="add-category"),
    path('get/category-type',CategoryTypeView.as_view(),name="get/category-type"),
    
]
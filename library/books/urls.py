#! /usr/bin/env python
# coding=utf-8
# author:"""HTJ"""
# time:2020/2/13
# Zen of Python:
"""
做自己的項目
　　１．強健的肌肉
　　２．一切都變得有序，井井有條
"""
from django.urls import path
from .views import BookListView

urlpatterns = [
    path('', BookListView.as_view(), name='home'),


]



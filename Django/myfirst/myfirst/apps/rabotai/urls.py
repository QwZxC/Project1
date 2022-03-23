from django.urls import path
from . import views

app_name = 'rabotai'
urlpatterns = [
    path('',views.index, name = '_index_'),
    path('<int:article_id>/',views.detail, name = 'detail'),
    path('<int:article_id>/leave_comment',views.leave_comment, name = 'leave_comment')
]
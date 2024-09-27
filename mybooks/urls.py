from django.urls import path
from .views import book_list, book1, book2, book3

urlpatterns = [
    path('', book_list),
    path('book1/', book1, name='book1'),
    path('book2/', book2, name='book2'),
    path('book3/', book3, name='book3'),

]

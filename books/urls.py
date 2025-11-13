from django.urls import path

import books
from books.views import BookListApiView, book_list_view, BookDetailApiView, BookDeleteApiView, BookUpdateApiView, BookCreateListApi, BookUpdateDeleteView, BookCreateApiView

urlpatterns=[
    path('',BookListApiView.as_view(),name='books-list'),
    path('books/create/',BookCreateApiView.as_view(),name='books-create'),
    path('books/',book_list_view),
    path('books/<int:pk>/',BookDetailApiView.as_view(),name='books-detail'),
    path('books/<int:pk>/delete/',BookDeleteApiView.as_view(),name='books-delete'),
    path('books/<int:pk>/update/',BookUpdateApiView.as_view(),name='books-update'),
    path('booklistcreate',BookCreateListApi.as_view(),name='books-create'),
    path('books/<int:pk>/updatedelete/',BookUpdateDeleteView.as_view(),name='books-updatedelete'),
]
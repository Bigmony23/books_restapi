from django.urls import path

import books
from books.views import BookListApi, book_list_view, BookDetailApi, BookDeleteApi, BookUpdateApi, BookCreateApi, \
    BookCreateListApi, BookUpdateDeleteView

urlpatterns=[
    path('',BookListApi.as_view(),name='books-list'),
    path('books/create/',BookCreateApi.as_view(),name='books-create'),
    path('books/',book_list_view),
    path('books/<int:pk>/',BookDetailApi.as_view(),name='books-detail'),
    path('books/<int:pk>/delete/',BookDeleteApi.as_view(),name='books-delete'),
    path('books/<int:pk>/update/',BookUpdateApi.as_view(),name='books-update'),
    path('booklistcreate',BookCreateListApi.as_view(),name='books-create'),
    path('books/<int:pk>/updatedelete/',BookUpdateDeleteView.as_view(),name='books-updatedelete'),
]
from django.urls import path
from rest_framework.routers import SimpleRouter

from .views import BookListApiView , BookDetailApiView , \
    BookDeleteApiView , BookUpdateApiView , BookCreateApiView, \
    BookListCreateApiView , BookUpdateDeleteApiView , BookViewSet

router = SimpleRouter()
router.register('books',BookViewSet , basename='books')

urlpatterns = [
    # path('books/' , BookListApiView.as_view(), name='book_list'),
    # path('books/create/' , BookCreateApiView.as_view() , name='book_create'),
    # path('book/list/create/', BookListCreateApiView.as_view() , name='booklist_create'),
    # path('books/<int:pk>/edit/' , BookUpdateDeleteApiView.as_view() , name='book_edit'),
    # path('books/<int:pk>/' ,BookDetailApiView.as_view() , name='book_detail'),
    # path('books/<int:pk>/update/', BookUpdateApiView.as_view() , name='book_update'),
    # path('books/<int:pk>/delete/' , BookDeleteApiView.as_view() , name='book_update'),
    # path('book/list/' ,book_list_view , name='booklist_func'),
]

urlpatterns =urlpatterns + router.urls
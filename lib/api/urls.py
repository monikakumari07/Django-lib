from django.urls import path
from api.views import *
# from api.views.bookViews import *

app_name = 'api'

urlpatterns = [
#USER
    path('signup/', CreateSignupView.as_view()),
    path('login_user/',loginView.as_view()),

#BOOK
    path('create_book/', CreateBookView.as_view()),
    path('update_book/<int:pk>/', UpdateBookView.as_view()),
    path('delete_book/<int:pk>/', DeleteBookView.as_view()),
    path('get_all_book/',GetAllBookView.as_view()),
    
#REGISTER
    path('create_register/', CreateRegisterView.as_view()),
    path('update_register/<int:pk>/', UpdateRegisterView.as_view()),
    path('delete_register/<int:pk>/', DeleteRegisterView.as_view()),
    path('get_all_register_details/',getall_Register.as_view()),
]
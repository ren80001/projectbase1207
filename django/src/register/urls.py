from django.urls import path
from . import views

app_name = 'register'

urlpatterns = [
    path('', views.TopView.as_view(), name='top'),
    path('user_profile/<int:pk>/', views.DetailView.as_view(), name='user_profile'),
    path('login/', views.Login.as_view(), name='login'),
    path('Guest_login/', views.GuestLogin.as_view(), name='Guest_login'),
    path('sign_up/', views.SignUp.as_view(), name='sign_up'),
    path('logout/', views.Logout.as_view(), name='logout'),
    path('user_create/', views.UserCreate.as_view(), name='user_create'),
    path('user_create/done', views.UserCreateDone.as_view(), name='user_create_done'),
    path('user_create/complete/<token>/', views.UserCreateComplete.as_view(), name='user_create_complete'),
    path('user_detail/<int:pk>/', views.UserDetail.as_view(), name='user_detail'),
    path('user_update/<int:pk>/', views.UserUpdate.as_view(), name='user_update'),
    path('search/', views.ListView.as_view(), name='search'),
    path('password_reset/', views.PasswordReset.as_view(), name='password_reset'),
    path('password_reset/done/', views.PasswordResetDone.as_view(), name='password_reset_done'),
    path('password_reset/confirm/<uidb64>/<token>/', views.PasswordResetConfirm.as_view(), name='password_reset_confirm'),
    path('password_reset/complete/', views.PasswordResetComplete.as_view(), name='password_reset_complete'),
    path("<int:pk>/like/", views.like, name="like"),
    path("api/like/<int:pk>/", views.api_like, name="api_like"),
]
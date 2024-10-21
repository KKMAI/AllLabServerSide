from django.urls import path
from snippets import views
from rest_framework.authtoken import views as auth_views


urlpatterns = [
    path('snippets/', views.SnippetList.as_view()),
    path('snippets/<int:pk>/', views.SnippetDetail.as_view()),
    path('categories/', views.category_list),
    path('users/', views.UserList.as_view()),
    path('users/<int:pk>/', views.UserDetail.as_view()),
    path('api-token-auth/', auth_views.obtain_auth_token)
]
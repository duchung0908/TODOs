from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.MyTokenObtainPairView.as_view(), name='get_access_token'), # get access token login 
    path('token/refresh/', views.TokenRefreshView.as_view(), name='token_refresh'), # get refresh token
    path('create/', views.CreateTodoView.as_view(), name='create_Todo_item'), # api create Todo item
    path('list/', views.ListTodoView.as_view(), name="list_Todo_items"), # api get list Todo items
    path('detail/<uuid:todo_id>/', views.DetailTodoView.as_view(), name="detail_Todo_item"), # api get detail Todo item
    path('update/<uuid:todo_id>/', views.UpdateTodoView.as_view(), name="update_Todo_item"), # api update Todo items
    path('delete/<uuid:todo_id>/', views.DeleteTodoView.as_view(), name="delete_Todo_item"), # api delete Todo item
]
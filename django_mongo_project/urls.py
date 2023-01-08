from django.contrib import admin
from django.urls import path, include
from mongo_project import views
### It automatically finds the corrects urls for base & id

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api',views.UserListCBV.as_view()),
    path('subject',views.SubjectListCBV.as_view()),
    path('signup',views.CreateUserList.as_view()),
    path('login',views.LoginUser.as_view()),
    path('show',views.ShowUserList.as_view()),
    path('logout',views.LogoutUser.as_view())
]

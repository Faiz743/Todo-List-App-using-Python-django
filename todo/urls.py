
from django.contrib import admin
from django.urls import path
from todoapp.views import home,add,deleteItem

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
    path('add/', add, name="add"),
    path('delete/<int:todo_id>/', deleteItem, name="delete"),
]

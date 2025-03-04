from django.urls import path
from . import views

app_name = 'expenses' 

urlpatterns = [
    path('', views.ExpenseListView.as_view(), name='expense_list'),
    path('add/', views.ExpenseCreateView.as_view(), name='expense_add'),
    path('<int:pk>/', views.ExpenseDetailView.as_view(), name='expense_detail'),
    path('update/<int:pk>/', views.ExpenseUpdateView.as_view(), name='expense_update'),
    path('delete/<int:pk>/', views.ExpenseDeleteView.as_view(), name='expense_delete'),

    path('categories/', views.CategoryListView.as_view(), name='category_list'),
    path('categories/add/', views.CategoryCreateView.as_view(), name='category_add'),
    path('categories/update/<int:pk>/', views.CategoryUpdateView.as_view(), name='category_update'),
    path('categories/delete/<int:pk>/', views.CategoryDeleteView.as_view(), name='category_delete'),
]
from django.urls import path
from . import views
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path('', views.index, name="expenses"),
    path('add-expense', views.add_expense, name="add-expenses"),
    path('edit-expense/<int:id>', views.edit_expense, name="edit-expense"),
    path('delete-expense/<int:id>', views.delete_expense, name="delete-expense"),
    path('stats', views.stats_view,name="stats"),
    path('export_csv', views.export_csv,name="export-csv"),
    path('import_csv', views.import_csv,name="import-csv"), 
    path('search-expenses', csrf_exempt(views.search_expenses),name="search_expenses") 
]

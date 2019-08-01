from django.urls import path, include

from . import views

app_name = 'olymipic_games'
urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
    path('results/', views.SearchResultsPageView.as_view(), name='results'),
    path('results/<int:year>/<str:discipline>/', views.get_results, name='get_results')
]
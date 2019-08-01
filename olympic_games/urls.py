from django.urls import path, include

from . import views

app_name = 'olympic_games'
urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
    path('results/', views.ResultsPageView.as_view(), name='results')
    path('results/<int:year>/<str:discipline>/', views.detail, name='results_discipline')
]
from dashboard.views import DashboardListView
from django.urls import path


urlpatterns = [
    path('index/', DashboardListView.as_view(), name='dashboard-index'),
]
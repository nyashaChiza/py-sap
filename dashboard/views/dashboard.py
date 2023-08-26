from django.views.generic import ListView

class DashboardListView(ListView):
    template_name = 'dashboard/index.html'  # Replace with your actual template file
    queryset = []
    context_object_name = 'data'
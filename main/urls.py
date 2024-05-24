from django.urls import path
from main.views import report_list

app_name = 'main'

urlpatterns = [
    path('report-list', report_list, name='report_list'),
]


urlpatterns = [
    path('admin/', admin.site.urls),
    path('admin_actions/', include('admin.urls')),
    # other paths...
]

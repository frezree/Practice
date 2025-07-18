
from django.contrib import admin
from django.urls import path
from students.views import my_first_programe
from students.views import walletinfoview
#from practice.settings import ADMIN_URL
#from django.urls import path,include


urlpatterns = [
    path('admin_main', admin.site.urls),
    path('hello/',my_first_programe),
    path("apiv/",walletinfoview.as_view())
    #path('abc/', include("students.url")),
]

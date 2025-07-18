from django.urls import path
from students.views import walletinfoview

urlpatterns = [
    path("apiv/",walletinfoview.as_view())
]
# csvreader/urls.py
from django.conf.urls import url
import views

urlpatterns = [
    url(r'^$', views.HomePageView.as_view()),
    url(r'^about/$', views.AboutPageView.as_view()),
    url(r'^output/$', views.UploadFileForm.as_view(), name="output")
]
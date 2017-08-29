# csvreader/urls.py
from django.conf.urls import url
from csv_validator_content import views

urlpatterns = [
    url(r'^$', views.HomePageView.as_view(), name="home"),
]
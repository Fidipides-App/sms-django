from django.urls import path

from .views import HomeView, SearchResultView, SearchView

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("search/", SearchView.as_view(), name="search"),
    path("search/result/", SearchResultView.as_view(), name="search-result"),
]

from django.urls import path, include


urlpatterns = [
    path("elibrary/", include("src.elibrary.urls"), name="elibrary"),
]

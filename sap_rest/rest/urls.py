from django.urls import path, include

from sap_rest.rest.router import router

app_name = "rest"
urlpatterns = [
    path('', include(router.urls)),
]

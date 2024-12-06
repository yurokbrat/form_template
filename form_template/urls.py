from django.urls import path
from form_template.views import GetFormView

urlpatterns = [
    path("get_form/", GetFormView.as_view(), name="get_form"),
]


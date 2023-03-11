
from django.urls import path, include
from apps.form.views import FormCreateView

urlpatterns = [path('', FormCreateView.as_view(), name='create_form'),
]
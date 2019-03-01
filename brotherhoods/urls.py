from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.schemas import get_schema_view
from brotherhoods import views

schema_view = get_schema_view(title='Brotherhood API')

urlpatterns = [
    path('schema/', schema_view),
    path('brotherhoods/', views.BrotherhoodList.as_view(), name='brotherhood-list'),
    path('brotherhood/', views.BrotherhoodCreate.as_view(), name='brotherhood-create'),
    path('brotherhoods/<int:pk>/', views.BrotherhoodDetail.as_view(), name='brotherhood-detail'),
    path('', views.api_root),
]

urlpatterns = format_suffix_patterns(urlpatterns)

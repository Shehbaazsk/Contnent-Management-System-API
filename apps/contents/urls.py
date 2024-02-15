from django.urls import path
from contents.api.api_views import ContentListCreateAPIView,ContentUpdateDeleteAPIView

app_name = 'contents'

urlpatterns = [
    path("", ContentListCreateAPIView.as_view()),
    path("<int:pk>/", ContentUpdateDeleteAPIView.as_view())   
]

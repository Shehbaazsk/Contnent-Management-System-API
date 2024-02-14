from django.urls import path,include
from accounts.api.urls import urlpatterns

app_name = "accounts"


urlpatterns = [
    path('api/', include('accounts.api.urls'))
]

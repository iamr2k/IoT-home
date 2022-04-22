from django.urls import include, path
from rest_framework import routers
from api import views

# router = routers.DefaultRouter()
# router.register(r'api', views.tempViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    # path('', include(router.urls)),
    path('api/', views.tempViewSet.as_view(), name="Temp"),
    path('temp/', views.tempassistViewSet.as_view(), name="Temp"),
    path('chartapi/', views.chartapi.as_view(), name="Chart"),
    path('fm/', views.fmview.as_view(), name="Broadcast"),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]

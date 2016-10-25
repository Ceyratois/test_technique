from django.conf.urls import url, include
from django.contrib import admin
from rest_framework import routers

from tridim_models import views as models_views
from api import views as api_views

router = routers.DefaultRouter()
router.register(r'users', api_views.UserViewSet)
router.register(r'badges', api_views.BadgeViewSet)
router.register(r'tridim_models', api_views.TridimModelViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^admin/', admin.site.urls),
    url(r'^models/new', models_views.ModelCreationView.as_view(success_url='new')),
    url(r'^accounts/login', models_views.UserCreationView.as_view()),
#    url(r'^', models_views.UserCreationView.as_view())
]

from django.conf.urls import url
from django.contrib import admin

from tridim_models import views as models_views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^models/new', models_views.ModelCreationView.as_view(success_url='new')),
    url(r'^accounts/login', models_views.UserCreationView.as_view()),
#    url(r'^', models_views.UserCreationView.as_view())
]

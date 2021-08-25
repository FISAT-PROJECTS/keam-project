from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from college_predictor import views as predictor_views

urlpatterns = [
    path('admin/nonononononononnonono/', admin.site.urls),

    path('', predictor_views.formInput, name='home'),
]
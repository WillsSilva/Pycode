from django.contrib import admin # type: ignore
from django.urls import path # type: ignore
from django.conf import settings # type: ignore
from django.conf.urls.static import static # type: ignore
from cars.views import CarsListView, NewCarCreateview, CarDetailView
from accounts.views import register_view, login_view, logout_view

urlpatterns = [
    path('admin/', admin.site.urls),
]

urlpatterns = [
    path('admin/',admin.site.urls),
    path('register/', register_view,name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('cars/', CarsListView.as_view(), name='cars_list'),
    path('new_car',NewCarCreateview.as_view(), name='new_car'),
    path('car/<int:pk>/',CarDetailView.as_view(), name='car_detail'),
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
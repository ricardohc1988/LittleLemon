from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router: DefaultRouter = DefaultRouter()
router.register(r'tables', views.BookingViewSet)


urlpatterns = [
    path('menu/', views.MenuItemsView.as_view()),
    path('booking/', include(router.urls)),
]
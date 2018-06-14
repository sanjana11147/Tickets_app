from django.urls import include, path

from . import views

urlpatterns = [
	path('', views.ListTicket.as_view()),
	path('<int:pk>/', views.DetailTicket.as_view()),
	path('rest-auth/', include('rest_auth.urls')),
]

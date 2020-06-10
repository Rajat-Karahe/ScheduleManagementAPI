from django.urls import path, include
from django.views.decorators.csrf import csrf_exempt

import events.views as views
from .views import (
    EventList,
    EventDetail,
    UserList,
    UserDetail,
    UserRegistration
)


urlpatterns = [
    path('', views.api_root, name='api-root'),
    path('users/', UserList.as_view(), name='user-list'),
    path('users/<int:pk>/', UserDetail.as_view(), name='user-detail'),
    path('events', EventList.as_view(), name='event-list'),
    path('events/<int:pk>/', EventDetail.as_view(), name='event-detail'),
    path('users/register/', UserRegistration.as_view(), name='user-registration'),
    path('', include('rest_framework.urls', namespace='rest_framework'))
]
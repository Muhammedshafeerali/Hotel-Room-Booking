from django .urls import path
from . import views


urlpatterns=[ 
    path('',views.hotel_log,name='hotel_log'),
    path('hotel-home/<int:id>/',views.hotel_home,name='hotel_home'),
    path('hotel_logout',views.hotel_logout,name='hotel_logout'),
    path('hotel_rooms/<int:id>/',views.hotel_rooms,name='hotel_rooms'),
    path('add_room/<int:id>/',views.add_room,name='add_room'),
    path('hotel_profile/<int:id>/',views.hotel_profile,name='hotel_profile'),
    path('hotel_update/<int:id>/',views.hotel_update,name='hotel_update'),


]
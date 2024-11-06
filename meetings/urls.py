from . import views
from django.urls import path
from meetings.views import detail, detail_room,delete_meeting,add_meeting

urlpatterns=[
    path('meetings',views.meetings_list_view, name='meetings_list_view') ,
    path('detail/<int:id>/',detail, name='detail') ,       #meeting
    path('rooms',views.rooms_list_view, name='rooms') ,
   path('detail_room/<int:id>/',detail_room, name='detail_room') ,    #meeting detail
   path('delete/<int:id>/', delete_meeting ,name='delete_meeting'),
   path('add',  add_meeting ,name=' add_meeting')
    ]
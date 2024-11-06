from django.shortcuts import render,get_object_or_404,redirect
from meetings.form import MeetingForm
from meetings.models import Meeting , Room  
 from django.http import HttpResponse

# Create your views here.


def meetings_list_view(request):
    meetings = Meeting.objects.all()  # Get all meetings
    return render(request, 'meetings.html', {'meetings': meetings, })

def detail(request, id):
   meeting = Meeting.objects.get(pk=id)
   return render(request, "details.html", {"meeting": meeting})

def rooms_list_view(request):
    rooms = Room.objects.all()  # Get all rooms
    return render(request, 'rooms.html', {'rooms': rooms, })
def detail_room(request, id):
   room = Room.objects.get(pk=id)
   return render(request, "room_details.html", {"room": room})

def delete_meeting(request, id):
 meeting = get_object_or_404(Meeting, id=id) # Get the meeting by
 meeting.delete() # Delete the meeting
 return redirect('meetings_list_view') # Redirect to the
#meetings list view after deletion
 return render(request, 'confirm_delete.html', {'meeting': meeting})
# Render confirmation page

#Vue pour ajouter une nouvelle réunion
def add_meeting(request):
 if request.method == "POST":
        form = MeetingForm(request.POST)
        if form.is_valid():
            form.save() # Sauvegarde le meeting si le formulaire est
            return redirect('meetings_list_view') # Redirige vers une
        else:
         form = MeetingForm()
        return render(request, 'new.html', {'form': form})
from rest_framework.viewsets import ModelViewSet
from .models import Note
from .serializers import NoteSerializer
from rest_framework import permissions
from rest_framework.exceptions import PermissionDenied

class NoteViewSet(ModelViewSet):
    queryset = Note.objects.all()  # Define the queryset
    serializer_class = NoteSerializer 
    
    

# class IsOnwer()
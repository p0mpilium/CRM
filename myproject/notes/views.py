from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Note
from myproject.serializers import NoteSerializer

class NoteList(APIView):
    def get(self, request, format=None):
        notes = Note.objects.all()
        serializer = NoteSerializer(notes, many=True)
        return Response(serializer.data)

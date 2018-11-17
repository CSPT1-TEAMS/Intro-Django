from rest_framework import serializers, viewsets

from .models import PersonalNote


class PersonalNoteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PersonalNote
        fields = ("title", "body")

    def create(self, validated_data):
        note = PersonalNote.objects.create(**validated_data)
        return note


class PersonalNoteViewSet(viewsets.ModelViewSet):
    serializer_class = PersonalNoteSerializer
    queryset = PersonalNote.objects.all()

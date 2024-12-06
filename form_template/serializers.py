from rest_framework import serializers


class FieldSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=255)
    type = serializers.ChoiceField(choices=["email", "phone", "date", "text"])


class FormTemplateSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=255)
    fields = FieldSerializer(many=True)

from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from form_template.mongo_client import templates_collection
from form_template.validators import validate_field_type


class GetFormView(APIView):
    def post(self, request: Request) -> Response:
        data = request.data
        matched_template = None

        for template in templates_collection.find({}, {"_id": 0}):
            template_fields = {field["name"]: field["type"] for field in template["fields"]}
            if all(
                field in data and validate_field_type(data[field]) == field_type
                for field, field_type in template_fields.items()
            ):
                matched_template = template["name"]
                break

        if matched_template:
            return Response({"template_name": matched_template}, status=status.HTTP_200_OK)

        result = {key: validate_field_type(value) for key, value in data.items()}
        return Response(result, status=status.HTTP_400_BAD_REQUEST)

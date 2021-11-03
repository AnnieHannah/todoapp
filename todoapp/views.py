from rest_framework.decorators import APIView
from rest_framework.response import Response
from . import methods


# Todo adding API.
class AddTodo(APIView):
    def post(self, request):
        response = methods.new_todo(request.data)
        return Response(response['Response'], status=response['Status'])

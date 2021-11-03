from rest_framework import status
from .models import TodoModel
from .serializer import TodoSerializer


# Method for adding new todo.
def new_todo(data):
    serializer = TodoSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return {
            'Response': {'response': {'todo': serializer.data['todo']}, 'message': 'Todo has been added', 'success': True},
            'Status': status.HTTP_200_OK
        }
    return {
        'Response': serializer.errors,
        'Status': status.HTTP_400_BAD_REQUEST
    }

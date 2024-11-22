from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from app.managers import EntityManager
from app.repositories.entity_repository import EntityRepository
from app.serializers.entity_serializer import EntitySerializer


class EntityView(APIView):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.entity_manager = EntityManager(repository=EntityRepository())

    def post(self, request):
        serializer = EntitySerializer(data=request.data)
        if serializer.is_valid():
            try:
                entity = self.entity_manager.create_entity(serializer.validated_data)
                return Response(EntitySerializer(entity).data, status=status.HTTP_201_CREATED)
            except ValueError as e:
                return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, name):
        try:
            entity = self.entity_manager.get_entity(name)
            return Response(EntitySerializer(entity).data)
        except ValueError as e:
            return Response({"error": str(e)}, status=status.HTTP_404_NOT_FOUND)

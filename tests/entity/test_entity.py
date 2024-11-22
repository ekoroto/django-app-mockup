from app.managers import EntityManager
from ..test_repositories import InMemoryEntityRepository


def test_create_entity_with_test_service():
    manager = EntityManager(repository=(InMemoryEntityRepository))

    data = {"name": "Test", "schema": {}}
    result = manager.create_entity(data)

    assert result == data

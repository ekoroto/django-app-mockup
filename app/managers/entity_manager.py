from repositories import EntityRepository


class EntityManager:
    def __init__(self, repository=None):
        self.repository = repository or EntityRepository()

    def create_entity(self, data):
        if 'name' not in data:
            raise ValueError("Name is required for Entity")
        return self.repository.create(data)

    def get_entity(self, entity_id):
        entity = self.repository.get_by_id(entity_id)
        if not entity:
            raise ValueError(f"Entity with ID {entity_id} not found")
        return entity

class InMemoryEntityRepository:
    def __init__(self):
        self.entities = {}

    def create(self, data):
        if data["name"] in self.entities:
            raise ValueError(f"Entity with name {data['name']} already exists")
        self.entities[data["name"]] = data
        return data

    def get_by_name(self, name):
        return self.entities.get(name)

    def update(self, entity, data):
        if entity["name"] not in self.entities:
            raise ValueError(f"Entity with name {entity['name']} does not exist")
        self.entities[entity["name"]].update(data)
        return self.entities[entity["name"]]

    def delete(self, entity):
        if entity["name"] in self.entities:
            del self.entities[entity["name"]]

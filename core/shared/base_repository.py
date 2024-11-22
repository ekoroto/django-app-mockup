from abc import ABC

class BaseRepository(ABC):
    def __init__(self, model):
        self.model = model

    def create(self, data):
        return self.model.objects.create(**data)

    def get_by_id(self, obj_id):
        return self.model.objects.filter(id=obj_id).first()

    def update(self, obj, data):
        for field, value in data.items():
            setattr(obj, field, value)
        obj.save()
        return obj

    def delete(self, obj):
        obj.delete()

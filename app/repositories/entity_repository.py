from app.models.entity import Entity
from core.shared import BaseRepository


class EntityRepository(BaseRepository):
    def __init__(self):
        super().__init__(model=Entity)

    #Add some specific methods here

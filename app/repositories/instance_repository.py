from app.models.instance import Instance
from core.shared import BaseRepository


class InstanceRepository(BaseRepository):
    def __init__(self):
        super().__init__(model=Instance)

    #Add some specific methods here

class BaseDAO:
    def get_all(self):
        raise NotImplementedError

    def get_by_id(self, entity_id):
        raise NotImplementedError

    def create(self, entity):
        raise NotImplementedError

    def update(self, entity):
        raise NotImplementedError

    def delete(self, entity_id):
        raise NotImplementedError

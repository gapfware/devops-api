from fastapi.encoders import jsonable_encoder


def crud_factory(model):
    class Crud:
        @classmethod
        def get_all(cls, db):
            return jsonable_encoder(db.query(model).all())

        @classmethod
        def get_by_name(cls, db, name):
            return jsonable_encoder(db.query(model).filter_by(name=name).first())

        @classmethod
        def get_by_id(cls, db, id):
            return jsonable_encoder(db.query(model).get(id))

        @classmethod
        def create(cls, db, data):
            instance = model(**data.model_dump())
            db.add(instance)
            db.commit()
            db.refresh(instance)
            return jsonable_encoder(instance)

        @classmethod
        def update(cls, db, id, data):
            instance = db.query(model).get(id)
            for key, value in data.dict().items():
                setattr(instance, key, value)
            db.commit()
            db.refresh(instance)
            return jsonable_encoder(instance)

        @classmethod
        def delete(cls, db, id):
            instance = db.query(model).get(id)
            db.delete(instance)
            db.commit()
            return jsonable_encoder(instance)

    Crud.model = model
    return Crud

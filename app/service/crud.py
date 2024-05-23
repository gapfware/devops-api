from fastapi.encoders import jsonable_encoder
from psycopg2.errorcodes import UNIQUE_VIOLATION
from psycopg2 import errors


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
            return jsonable_encoder(db.get(model, id))

        @classmethod
        def create(cls, db, data):
            instance = model(**data.model_dump())
            db.add(instance)
            db.commit()
            db.refresh(instance)
            return jsonable_encoder(instance)

        @classmethod
        def update(cls, db, id, data):
            instance = db.get(model, id)
            for key, value in data.model_dump().items():
                setattr(instance, key, value)
            try:
                db.commit()
                db.refresh(instance)
                return jsonable_encoder(instance)
            except errors.lookup(UNIQUE_VIOLATION):
                db.rollback()
                raise Exception("Category name already exists")

        @classmethod
        def delete(cls, db, id):
            instance = db.get(model, id)
            db.delete(instance)
            db.commit()
            return jsonable_encoder(instance)

    Crud.model = model
    return Crud

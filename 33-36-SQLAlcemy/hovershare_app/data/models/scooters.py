import sqlalchemy as sa

from hovershare_app.data.sqlalchemybase import SqlAlchemyBase


class Scooter(SqlAlchemyBase):
    _tablename_ = 'scooters'

    id = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    created_date = sa.Column(sa.DateTime)
    vin = sa.Column(sa.String)
    model = sa.Column(sa.String)
    battery_level = sa.Column(sa.Integer)

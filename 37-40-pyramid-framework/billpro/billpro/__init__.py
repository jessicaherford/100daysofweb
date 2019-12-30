import os

from pyramid.config import Configurator

from billpro.bin import load_base_data
from billpro.data.db_session import DbSession


def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    config = Configurator(settings=settings)
    config.include('pyramid_jinja2')
    config.include('.routes')
    config.scan()

    init_db()

    return config.make_wsgi_app()


def init_db():
    db_file = os.path.join(
        os.path.abspath(os.path.dirname(__file__)),
        'db',
        'bill_tracker.sqlite'
    )
    DbSession.global_init(db_file)
    load_base_data.load_starter_data()

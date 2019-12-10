import flask
from cityscape_api.views import city_api
from cityscape_api.views import home
from cityscape_api.config import settings
import cityscape_api.services.weather_service
import cityscape_api.services.sun_service
import cityscape_api.services.location_service

app = flask.Flask(__name__)
is_debug = True

app.register_blueprint(home.blueprint)
app.register_blueprint(city_api.blueprint)


def configure_app():
    mode = 'dev' if is_debug else 'prod'
    data = settings.load(mode)

    #cityscape_api.services.weather_service.global_init(data.get('weather_key'))
    #services.sun_service.use_cached_data = data.get('use_cached_data')
    cityscape_api.services.location_service.use_cached_data = data.get('use_cached_data')

    print("Using cached data? {}".format(data.get('use_cached_data')))


def run_web_app():
    app.run(debug=is_debug, port=5001)


configure_app()

if __name__ == '__main__':
    run_web_app()

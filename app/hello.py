from pyramid.config import Configurator
from pyramid.response import Response


def hello_world(request):
    return Response('<h1>Hello World!</h1>')


def get_app():
    config = Configurator()
    config.add_route('hello', '/')
    config.add_view(hello_world, route_name='hello')
    app = config.make_wsgi_app()

    return app

application = get_app()

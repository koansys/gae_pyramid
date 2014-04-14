import sys
print sys.path
from wsgiref.simple_server import make_server
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

if __name__ == '__main__':
    app = get_app()
    server = make_server('0.0.0.0', 6543, app)
    server.serve_forever()


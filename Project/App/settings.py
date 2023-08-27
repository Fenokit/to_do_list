# Создана для определения настроек сервера
from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import urlparse
from App.urls import parse_urls


# Определяем класс обработчика запросов
class RequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html; charset=utf-8')
        self.end_headers()

        parsed_url = urlparse(self.path)
        path = parsed_url.path
        html_content = parse_urls(path)
        self.wfile.write(html_content.encode())

# Определяем функцию, которая будет запускать сервер
def run(server_class=HTTPServer, handler_class=RequestHandler, port=8000):
        server_address = ('', port)
        httpd = server_class(server_address, handler_class)
        print(f'Starting server on port {port}...')
        httpd.serve_forever()
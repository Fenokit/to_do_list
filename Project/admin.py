# Создам для запуска и настройки сервера
import http.server
from App.urls import RequestHandler

# Определяем функцию, которая будет запускать сервер
def run(server_class=http.server.HTTPServer, handler_class=RequestHandler, port=8000):
        server_address = ('', port)
        httpd = server_class(server_address, handler_class)
        print(f'Starting server on port {port}...')
        httpd.serve_forever()

# Запускаем сервер
if __name__ == '__main__':
        run()
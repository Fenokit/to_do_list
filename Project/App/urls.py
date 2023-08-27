# Создан для работы с URL – запросами
import http.server


# Определяем класс обработчика запросов
class RequestHandler(http.server.BaseHTTPRequestHandler):
        def do_GET(self):
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(b'Hello, World!')
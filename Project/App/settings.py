# Создана для определения настроек сервера
import datetime
from http.server import HTTPServer, BaseHTTPRequestHandler
from App.templates import ReadTheApp, js_code
from urllib.parse import parse_qs
# Список задач и статусов
tasks = []
time_create_task = []

# Класс обработчика запросов
class RequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html; charset=utf-8')
        self.end_headers()
        PAGE_HTML = ReadTheApp()
        
        # Генерация HTML-кода таблицы
        table_html = ''
        for i, task in enumerate(tasks):
            table_html += f"""
                <tr id="ClassList {i}"> 
                    <td><input type="checkbox" onclick="toggleCheck(this.parentNode.parentNode)" />&nbsp;</td>
                    <td>{task}</td>
                    <td>< class="delete" onclick="toggleDelete(this.parentNode.parentNode)"></button></td> 
                </tr>"""
            
        # Вставка сгенерированной таблицы в HTML-шаблон
        PAGE_HTML = PAGE_HTML.web_app('html').replace('{task_Table}', table_html)
        # Отправка ответа
        self.wfile.write(PAGE_HTML.encode())
    
    # Метод, вызываемый при получении POST-запроса
    def do_POST(self):
        # Получение данных из POST-запроса
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length).decode('utf-8')
       
         # Извлечение значения поля и действия из данных POST-запроса
        parsed_data = parse_qs(post_data)
        print(f'{post_data}- {parsed_data} \n {content_length}' )
        if 'task' in parsed_data:

            # Перебор переменных из HTML
            task = parsed_data['task'][0]
            # action = parsed_data['priority'][0]
            time_create = datetime.datetime.today()

            # Добавление переменных в БД
            tasks.append(task)
            time_create_task.append(time_create.strftime("%d.%m.%Y\n%H:%M:%S"))
        elif 'index' in parsed_data and 'status' in parsed_data:
            index = int(parsed_data['index'][0])
        elif 'index' in parsed_data and 'action' in parsed_data:
            index = int(parsed_data['index'][0])
            action = parsed_data['action'][0]
            print(action)
            if action == 'delete':
                del tasks[index-1]
    
        # Переадресация обратно на главную страницу
        self.send_response(303)
        print(tasks)
        self.send_header('Location', '/')
        self.end_headers()


# Определяем класс сервера
class Server:
    # Список портов
    def __init__(self, host='', list_port=[8000, 8080]):
        self.list_port = list_port
        self.host = host

    # Проверка свободен ли один из портов
    def checking_port(self):
        for port in self.list_port:
            try:
                server_address = (self.host, port)
                httpd = HTTPServer(server_address, RequestHandler)
                print(f'Port {port} is open')
                return port
            except OSError:
                print(f'Port {port} is closed')
        return None
    
    # Функция для запуска сервера
    def run_server(self, server_class=HTTPServer, handler_class=RequestHandler, port=None):
        port = self.checking_port()
        if port is not None:
            server_address = (self.host, port)
            httpd = server_class(server_address, handler_class)
            print(f'Server running at {"http://127.0.0.1" if self.host == "" else self.host}:{port}')
            httpd.serve_forever()
        else:
            print('No available ports to start the server.')
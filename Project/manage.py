# Создам для запуска и настройки сервера
import datetime
from http.server import HTTPServer, BaseHTTPRequestHandler
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
        # Шаблон HTML, CSS, JS
        page_html = '''
        <!DOCTYPE html>
         <html>
         <head>    
            <style>
                #main {
                    text-align: center;
                }

                input[type="text"] {
                    width: 350px;
                    padding: 14px 20px;
                    margin: 8px 0;
                    box-sizing: border-box;
                    background-color: #f1f1f1;
                    border: none;
                    border-radius: 10px 2px 2px 10px; 
                }
                    
                .button {
                    background-color: #4CAF50;
                    padding: 14px 20px;
                    color: white;
                    margin: 8px 0;
                    border: none;
                    cursor: pointer;
                    border-radius: 2px 10px 10px 2px;
                }
                    
                table {
                    text-align: center;
                    margin: 8px 0;
                    border: none;
                    cursor: pointer;
                    border-radius: 10px 10px 0px 0px;
                }
                th {
                    background-color: #4CAF50;
                    color: white;
                }

                .completed {
                    text-align: left;
                    padding: 8px;
                }

                .name_value, value, remake, delete {
                    text-align: center;
                    padding: 8px;
                }

                </style>
                <script>
                function toggleCheck(row) {
                    var checkbox = row.querySelector('.checkbox');
                    alert(checkbox.textContent);
                    }
                function toggleDelete(row) {
                    var button = row.querySelector('.delete');
                    alert(button.textContent);
                    }
                </script>    
         </head>
         <body>
            <div id="main">
                <div>
                    <h1>Добро Пожаловать в To Do List</h1>
                    <p>Работы выполнена в целях обучения<br>Выполнил Муканов Ренат</p>
                </div>
                <div>
                    <form method="post">
                        <input type="text" name="task" placeholder="Введите значение" required>
                        <input type="submit" value="Добавить" class="button">
                    </form>
                </div>
                <div>
                <table>
                    <thead>
                        <tr>
                            <th class="completed"><input type="checkbox" onclick="toggleCheck(this.parentNode.parentNode)" />&nbsp;</th>
                            <th class="name_value">Наименование задачи</th>
                            <th class="remake">Редактировать</th>
                            <th class="delete">Удалить</th>
                        </tr>
                    </thead>
                        <tbody>
                            {task_Table}
                        </tbody>
                    </table>
                </div>
            </div>
         </body>
         </html>'''
        
        # Генерация HTML-кода таблицы
        table_html = ''
        for i, task in enumerate(tasks):
            # Шаблон записи в таблице
            table_html += f"""
                <tr id="ClassList {i}"> 
                    <td class="completed"><input type="checkbox" onclick="toggleCheck(this.parentNode.parentNode)" />&nbsp;</td>
                    <td class="value">{task}</td>
                    <td class="delete"><input type="checkbox" onclick="toggleCheck(this.parentNode.parentNode)" />&nbsp;</td>
                    <td class="remake"><input type="checkbox" onclick="toggleCheck(this.parentNode.parentNode)" />&nbsp;</td> 
                </tr>"""
            
        # Вставка сгенерированной таблицы в HTML-шаблон
        page_html = page_html.replace('{task_Table}', table_html)
        # Отправка ответа
        self.wfile.write(page_html.encode())
    
    # Метод, вызываемый при получении POST-запроса
    def do_POST(self):

        # Получение данных из POST-запроса
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length).decode('utf-8')

        # Извлечение значения поля и действия из данных POST-запроса
        parsed_data = parse_qs(post_data)
        print(f'{post_data}- {parsed_data} \n {content_length}')
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
                HTTPServer(server_address, RequestHandler)
                print(f'Port {port} is open')
                return port
            except OSError:
                print(f'Port {port} is closed')
        return None
    
    # Функция для запуска сервера
    def run_server(self, server_class=HTTPServer, handler_class=RequestHandler):
        port = self.checking_port()
        if port is not None:
            server_address = (self.host, port)
            httpd = server_class(server_address, handler_class)
            print(f'Server running at http://{"127.0.0.1" if self.host == "" else self.host}:{port}')
            httpd.serve_forever()
        else:
            print('No available ports to start the server.')


# Запускаем сервер
if __name__ == '__main__':
    a = Server()
    a.run_server()

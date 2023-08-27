# Создан для работы с шаблонами – HTML, CSS, JS
def read_html_from_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        html_content = f.read()
    return html_content

def general_html_string():
    return read_html_from_file('App/Templates/index.html')

def add_html_string():
    return read_html_from_file('App/Templates/add.html')

def delete_html_string():
    return read_html_from_file('App/Templates/delete.html')
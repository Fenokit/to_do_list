# Создан для работы с шаблонами – HTML, CSS, JS
def general_html_string():
    with open('App/Templates/index.html', 'r', encoding='utf-8') as f:
        html_content = f.read()
        return html_content
def add_html_string():
    with open('App/Templates/add.html', 'r', encoding='utf-8') as f:
        html_content = f.read()
        return html_content
def delete_html_string():
    with open('App/Templates/delete.html', 'r', encoding='utf-8') as f:
        html_content = f.read()
        return html_content
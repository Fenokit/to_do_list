# Создан для работы с URL – запросами
from App.templates import *

def parse_urls(path_urls=''):
    if path_urls == '/add':
        html_content = add_html_string()
    elif path_urls == '/delete':
        html_content = delete_html_string()
    else:
        html_content = general_html_string()
        
    return html_content
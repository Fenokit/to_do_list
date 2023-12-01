# Создан для работы с шаблонами – HTML, CSS, JS
class ReadTheApp:
    def read_app_from_file(self, file_path):
        with open(file_path, 'r', encoding='utf-8') as f:
            html_content = f.read()
        return html_content

    def web_app(self, web):
        match web:
            case 'html':
                return self.read_app_from_file('App/Templates/index.html')
class js_code:           
    def Priority(row):
        priority = row.querySelector('.priority')
        priority.submit
        if priority.textContent == 'high':
            priority.classList.toggle('.purple')
        else:
            if priority.textContent == 'medium':
                priority.classList.toggle('.blue')
            else:
                priority.classList.toggle('.black')

    def toggleCheck(row):
        checkbox = row.querySelector('.checkbox')
        checkbox.classList.toggle('checked')
        task = row.querySelector('.task')
        task.classList.toggle('completed')
        time = row.querySelector('.time')
        time.classList.toggle('completed')
        priority = row.querySelector('.priority')
        priority.classList.toggle('.priority')
        priority.submit

    def toggleDelete(row):
        button = row.querySelector('.delete')
        console.log(button)
        task = row.querySelector('.task')
        console.log(task)
        priority = row.querySelector('.priority')
        console.log(priority)
        if button.textContent == 'удалить':
            button.textContent = 'вернуть'
            row.classList.add('deleted')
        else:
            button.textContent = 'удалить'
            row.classList.remove('deleted')

    def deleteRow(row):
        table = document.getElementById('table_all')
        table.removeChild(row)

    def restoreRow(row):
        button = row.querySelector('.delete')
        task = row.querySelector('.task')
        button.textContent = 'удалить'
        row.classList.remove('deleted')

    def confirmDelete(index):
        if confirm("Вы уверены, что хотите удалить эту запись?"):
            document.getElementById("delete-form-" + index).submit()


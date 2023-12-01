function Priority(row) {
    var priority = row.querySelector('.priority');
    priority.submit;
    if (priority.textContent === 'high'){
      priority.classList.value('.purple');
    } else if (priority.textContent === 'medium') {
      priority.classList.toggle('.blue');
    } else {
      priority.classList.toggle('.black');
      }
  }


  function toggleCheck(row) {
    var checkbox = row.querySelector('.checkbox');
    checkbox.classList.toggle('checked');
    var task = row.querySelector('.task');
    task.classList.toggle('completed');
    var time = row.querySelector('.time');
    time.classList.toggle('completed');
    var priority = row.querySelector('.priority');
    priority.classList.toggle('.priority')
    priority.submit;
  }

  function toggleDelete(row) {
    var button = row.querySelector('.delete')
    alert(button.textContent)
    var task = row.querySelector('.task')
    alert(task.textContent)
    var priority = row.querySelector('.priority')
    alert(priority.textContent)

    if (button.textContent === 'удалить') {
        button.textContent = 'вернуть';
        row.classList.add('deleted');
    } else {
        button.textContent = 'удалить';
        row.classList.remove('deleted');
    }
  }

  function deleteRow(row) {
    var table = document.getElementById('table_all');
    table.removeChild(row);
  }

  function restoreRow(row) {
    var button = row.querySelector('.delete');
    var task = row.querySelector('.task');
    button.textContent = 'удалить';
    row.classList.remove('deleted');
  }

  function confirmDelete(index) {
    if (confirm("Вы уверены, что хотите удалить эту запись?")) {
        document.getElementById("delete-form-" + index).submit();
    }
  }
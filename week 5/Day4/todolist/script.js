const tasks = [];

function addTask(event) {
  event.preventDefault();
  const taskInput = document.getElementById('taskInput');
  const taskText = taskInput.value.trim();

  if (taskText === '') return;

  const taskId = tasks.length;
  const task = {
    task_id: taskId,
    text: taskText,
    done: false,
  };
  tasks.push(task);

  const taskList = document.querySelector('.listTasks');
  const taskElement = createTaskElement(task);
  taskList.appendChild(taskElement);

  taskInput.value = '';
}

function createTaskElement(task) {
  const taskElement = document.createElement('div');
  taskElement.classList.add('task');

  const checkbox = document.createElement('input');
  checkbox.type = 'checkbox';
  checkbox.checked = task.done;
  checkbox.addEventListener('change', () => {
    task.done = checkbox.checked;
    updateTaskStatus(taskElement, task.done);
  });

  const taskLabel = document.createElement('span');
  taskLabel.textContent = task.text;
  if (task.done) {
    taskLabel.classList.add('done');
  }

  const deleteButton = document.createElement('button');
  deleteButton.innerHTML = '<i class="fa fa-times"></i>';
  deleteButton.addEventListener('click', () => {
    deleteTask(task.task_id);
    taskElement.remove();
  });

  taskElement.appendChild(deleteButton);
  taskElement.appendChild(checkbox);
  taskElement.appendChild(taskLabel);

  return taskElement;
}

function updateTaskStatus(taskElement, done) {
  const taskLabel = taskElement.querySelector('span');
  if (done) {
    taskLabel.classList.add('done');
  } else {
    taskLabel.classList.remove('done');
  }
}

function deleteTask(taskId) {
  tasks.splice(taskId, 1);
}

const taskForm = document.getElementById('taskForm');
taskForm.addEventListener('submit', addTask);
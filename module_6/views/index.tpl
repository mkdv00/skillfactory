<html>
    <head>
        <meta charset="utf-8">
        <title>Задачи на день</title>
        <link rel="stylesheet" href="static/styles.css">
    </head>
    <body>
        <div class="container">
            <h1>Текущие задачи</h1>
            <ul id="todo-list">
            % for task in tasks:
                <li>
                    <div class="chekbox-two">
                        <label class="checkbox">
                            % if task.is_completed:
                            <input type="checkbox" class="checkbox_true" data-uid="{{ task.uid }}"
                            disabled='disabled' checked='checked'>
                            <span class="checkbox__icon"></span>
                            % else:
                            <input type="checkbox" class="checkbox_true" data-uid="{{ task.uid }}">
                            <span class="checkbox__icon"></span>
                            % end
                            <span class="task_text">{{ task }}</span>
                        </label>
                        <a href="#" class="remove">X</a>
                        <hr/>
                    </div>
                </li>
            % end
            </ul>
            <br/>
            <form action="/add-task" method="post" id="todo-add">
                <input type="text" name="description" class="form-control"/>
                <button class="add" type="submit">+</button>
            </form>
        </div>

        <script src="http://code.jquery.com/jquery-3.3.1.slim.min.js"></script>
        <script src="static/script.js"></script>
    </body>
</html>

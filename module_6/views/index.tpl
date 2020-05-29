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
                            <input type="checkbox">
                            <span class="checkbox__icon"></span>
                            {{ task }}
                        </label>
                    </div>
                    <a href="#" class="remove">X</a>
                    <hr/>
                </li>
            % end
            </ul>
            <br/>
            <form id="todo-add">
                <input type="text" class="form-control"/>
                <button class="add" type="submit">+</button>
            </form>
        </div>

        <script src="http://code.jquery.com/jquery-3.3.1.slim.min.js"></script>
        <script src="static/script.js"></script>
    </body>
</html>

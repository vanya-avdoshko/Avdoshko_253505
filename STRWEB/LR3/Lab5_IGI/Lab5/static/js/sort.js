document.addEventListener('DOMContentLoaded', function () {
    const employeesPerPage = 3; // Количество сотрудников на странице
    const employeeRows = Array.from(document.querySelectorAll('.employee-item')); // Все сотрудники
    const totalEmployees = employeeRows.length; // Общее количество сотрудников
    const tableBody = document.getElementById('employeeTableBody');
    const tableHeaders = document.querySelectorAll('.sortable');
    
    let currentPage = 1;

    // Функция для сортировки данных
    function sortTable(column, order) {
        // Сортируем все строки
        employeeRows.sort((a, b) => {
            const aValue = a.dataset[column].toLowerCase();
            const bValue = b.dataset[column].toLowerCase();

            if (aValue < bValue) return order === 'asc' ? -1 : 1;
            if (aValue > bValue) return order === 'asc' ? 1 : -1;
            return 0;
        });

        // Перестроим таблицу с отсортированными строками
        tableBody.innerHTML = '';
        employeeRows.forEach(row => tableBody.appendChild(row));

        // Переотображаем сотрудников на текущей странице после сортировки
        showPage(currentPage);
    }

    // Функция для отображения сотрудников на текущей странице
    function showPage(page) {
        employeeRows.forEach((employee, index) => {
            if (index >= (page - 1) * employeesPerPage && index < page * employeesPerPage) {
                employee.style.display = 'table-row'; // Показываем сотрудника на текущей странице
            } else {
                employee.style.display = 'none'; // Прячем остальные сотрудники
            }
        });

        updatePaginationButtons(); // Обновляем кнопки пагинации
        updateArrows(); // Обновляем состояние стрелок
    }

    // Функция для создания кнопок пагинации
    function createPagination() {
        const pageNumbersContainer = document.getElementById('pageNumbers');
        const totalPages = Math.ceil(employeeRows.length / employeesPerPage); // Обновляем количество страниц
        pageNumbersContainer.innerHTML = ''; // Очищаем контейнер кнопок

        for (let page = 1; page <= totalPages; page++) {
            const button = document.createElement('button');
            button.innerText = page;
            button.classList.add('page-button');
            button.addEventListener('click', (e) => {
                e.preventDefault();
                currentPage = page;
                showPage(currentPage);
            });
            pageNumbersContainer.appendChild(button);
        }
    }

    // Обновление активной кнопки пагинации
    function updatePaginationButtons() {
        const buttons = document.querySelectorAll('.page-button');
        buttons.forEach(button => {
            if (parseInt(button.innerText) === currentPage) {
                button.classList.add('active');
            } else {
                button.classList.remove('active');
            }
        });
    }

    // Обновление состояния стрелок (активность кнопок)
    function updateArrows() {
        const prevArrow = document.getElementById('prevPage');
        const nextArrow = document.getElementById('nextPage');
        const totalPages = Math.ceil(employeeRows.length / employeesPerPage);

        prevArrow.classList.toggle('disabled', currentPage === 1);
        nextArrow.classList.toggle('disabled', currentPage === totalPages);
    }

    // Обработчики для стрелок
    document.getElementById('prevPage').addEventListener('click', function (e) {
        e.preventDefault();
        if (currentPage > 1) {
            currentPage--;
            showPage(currentPage);
        }
    });

    document.getElementById('nextPage').addEventListener('click', function (e) {
        e.preventDefault();
        const totalPages = Math.ceil(employeeRows.length / employeesPerPage);
        if (currentPage < totalPages) {
            currentPage++;
            showPage(currentPage);
        }
    });

    // Обработчик клика по заголовкам таблицы
    tableHeaders.forEach(header => {
        header.addEventListener('click', function () {
            const column = this.dataset.sort;
            const isAscending = this.classList.contains('asc');
            const newOrder = isAscending ? 'desc' : 'asc';

            // Удаляем активный класс у всех заголовков
            tableHeaders.forEach(h => h.classList.remove('asc', 'desc', 'active'));

            // Добавляем классы к текущему заголовку
            this.classList.add('active', newOrder);

            // Выполняем сортировку
            sortTable(column, newOrder);
        });
    });

    // Инициализация пагинации
    createPagination();
    showPage(currentPage); // Показываем сотрудников на первой странице
});

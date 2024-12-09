document.addEventListener('DOMContentLoaded', function() {
    const employeesPerPage = 3; // Количество сотрудников на странице
    const employees = document.querySelectorAll('.employee-item'); // Все сотрудники
    const totalEmployees = employees.length; // Общее количество сотрудников

    if (totalEmployees === 0) {
        console.log('Нет сотрудников для отображения');
        return;
    }

    const totalPages = Math.ceil(totalEmployees / employeesPerPage); // Общее количество страниц
    let currentPage = 1;

    // Функция для отображения сотрудников на текущей странице
    function showPage(page) {
        employees.forEach((employee, index) => {
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
        pageNumbersContainer.innerHTML = ''; // Очищаем контейнер кнопок

        for (let page = 1; page <= totalPages; page++) {
            const button = document.createElement('button');
            button.innerText = page;
            button.classList.add('page-button');
            button.addEventListener('click', (e) => {
                e.preventDefault();  // Предотвращаем стандартное поведение
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

        prevArrow.classList.toggle('disabled', currentPage === 1);
        nextArrow.classList.toggle('disabled', currentPage === totalPages);
    }

    // Обработчики для стрелок
    document.getElementById('prevPage').addEventListener('click', function(e) {
        e.preventDefault();  // Предотвращаем стандартное поведение
        if (currentPage > 1) {
            currentPage--;
            showPage(currentPage);
        }
    });

    document.getElementById('nextPage').addEventListener('click', function(e) {
        e.preventDefault();  // Предотвращаем стандартное поведение
        if (currentPage < totalPages) {
            currentPage++;
            showPage(currentPage);
        }
    });

    // Инициализация пагинации
    createPagination();
    showPage(currentPage); // Показываем сотрудников на первой странице
});

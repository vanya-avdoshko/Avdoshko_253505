document.addEventListener('DOMContentLoaded', function() {
    const filterInput = document.getElementById('filterInput');
    const filterButton = document.getElementById('filterButton');
    const tableBody = document.getElementById('employeeTableBody');
    
    // Функция для фильтрации таблицы
    function filterTable() {
        const filterValue = filterInput.value.toLowerCase(); // Получаем текст из поля ввода
        const rows = tableBody.getElementsByClassName('employee-item'); // Получаем все строки таблицы

        Array.from(rows).forEach(row => {
            const cells = row.getElementsByTagName('td'); // Получаем все ячейки строки
            let rowText = ''; // Текст для проверки на совпадение

            // Собираем текст из всех ячеек строки (кроме первого столбца с чекбоксом)
            for (let i = 1; i < cells.length; i++) {
                rowText += cells[i].textContent.toLowerCase();
            }

            // Проверяем, содержит ли строка введенный текст
            if (rowText.indexOf(filterValue) > -1) {
                row.style.display = ''; // Показываем строку
            } else {
                row.style.display = 'none'; // Скрываем строку
            }
        });
    }

    // Слушаем нажатие на кнопку фильтрации
    filterButton.addEventListener('click', function() {
        filterTable(); // Запускаем фильтрацию при нажатии кнопки
    });

    // // Опционально: можно также фильтровать при изменении текста в поле ввода
    // filterInput.addEventListener('input', function() {
    //     filterTable(); // Запускаем фильтрацию при каждом изменении текста
    // });
});

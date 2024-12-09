document.addEventListener('DOMContentLoaded', function () {
    const rewardButton = document.getElementById('rewardButton'); // Кнопка премирования
    const rewardTextBlock = document.getElementById('rewardText'); // Блок для текста премирования
    const rewardMessage = document.getElementById('rewardMessage'); // Элемент для сообщения
    const loader = document.getElementById('loader'); // Прелоадер

    // Обработчик события для кнопки "Премировать"
    rewardButton.addEventListener('click', function () {
        // Находим все отмеченные чекбоксы
        const selectedCheckboxes = document.querySelectorAll('input[name="selected_employees"]:checked');

        if (selectedCheckboxes.length === 0) {
            alert('Выберите хотя бы одного сотрудника для премирования.');
            return;
        }

        // Показать прелоадер
        loader.style.display = 'block';

        // Имитация выполнения операции (например, отправка на сервер)
        setTimeout(function () {
            // Извлекаем фамилии выбранных сотрудников
            const selectedEmployees = [];
            selectedCheckboxes.forEach(checkbox => {
                const employeeRow = document.getElementById(`employee-${checkbox.value}`);
                const employeeName = employeeRow.querySelector('td:nth-child(3)').textContent;
                selectedEmployees.push(employeeName);
            });

            // Формируем текст премирования
            const message = `Следующие сотрудники премированы: ${selectedEmployees.join(', ')}.`; // Объединение элементов массива в строку через запятую
            rewardMessage.textContent = message;

            // Показываем блок с текстом премирования
            rewardTextBlock.style.display = 'block';

            // Скрыть прелоадер
            loader.style.display = 'none';
        }, 2000); // Задержка в 2 секунды для имитации выполнения задачи
    });
});
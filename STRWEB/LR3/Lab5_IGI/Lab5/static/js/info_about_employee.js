document.addEventListener('DOMContentLoaded', function() {
    // Находим все строки сотрудников в таблице
    const employeeRows = document.querySelectorAll('.employeeDetails');
    
    // Элементы для вывода информации
    const detailsBlock = document.getElementById('employeeDetails');
    const detailName = document.getElementById('detailName');
    const detailPosition = document.getElementById('detailPosition');
    const detailPhone = document.getElementById('detailPhone');
    const detailPhoto = document.getElementById('detailPhoto');
    
    // Добавляем обработчик события на каждую строку таблицы
    employeeRows.forEach(function(row) {
        row.addEventListener('click', function() {
            // Извлекаем данные из атрибутов data-* строки
            const name = row.getAttribute('data-name');
            const position = row.getAttribute('data-position');
            const phone = row.getAttribute('data-phone');
            const photo = row.getAttribute('data-photo');
            
            // Заполняем блок с деталями
            detailName.textContent = name;
            detailPosition.textContent = position;
            detailPhone.textContent = phone;
            detailPhoto.src = photo;

            // Показываем блок с деталями
            detailsBlock.style.display = 'block';
        });
    });
});

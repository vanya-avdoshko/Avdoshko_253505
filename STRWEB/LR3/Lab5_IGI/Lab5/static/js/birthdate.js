document.getElementById('birthdate-form').addEventListener('submit', function (event) {  
    event.preventDefault(); // Предотвращаем стандартное поведение формы

    const birthdateInput = document.getElementById('birthdate').value;

    if (!birthdateInput) {
        alert('Пожалуйста, введите дату рождения.');
        return;
    }

    const birthDate = new Date(birthdateInput);
    const today = new Date();
    const age = today.getFullYear() - birthDate.getFullYear();
    const isBeforeBirthday = today < new Date(today.getFullYear(), birthDate.getMonth(), birthDate.getDate()); // Проверяем, был ли рожден в прошлом году

    const finalAge = isBeforeBirthday ? age - 1 : age;  // Если был рожден в прошлом году, уменьшаем возраст

    // День недели
    const daysOfWeek = ['Воскресенье', 'Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота'];
    const dayOfWeek = daysOfWeek[birthDate.getDay()];  // Получаем день недели из даты рождения

    if (finalAge >= 18) {
        alert(`Ваш возраст: ${finalAge}. Вы родились в ${dayOfWeek}.`);
    } else {
        alert(`Ваш возраст: ${finalAge}. Вы несовершеннолетний. Для использования сайта требуется разрешение родителей.`);
    }
});

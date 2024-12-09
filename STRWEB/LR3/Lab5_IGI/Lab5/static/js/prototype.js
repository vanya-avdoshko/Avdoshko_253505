// Базовый класс Person с общими свойствами и методами
function Person(firstName, lastName) {
    this.firstName = firstName; // Имя
    this.lastName = lastName;   // Фамилия
}

// Геттер для имени
Person.prototype.getFirstName = function () {
    return this.firstName;
};

// Сеттер для имени
Person.prototype.setFirstName = function (firstName) {
    this.firstName = firstName;
};

// Геттер для фамилии
Person.prototype.getLastName = function () {
    return this.lastName;
};

// Сеттер для фамилии
Person.prototype.setLastName = function (lastName) {
    this.lastName = lastName;
};

// Класс Student, наследующий Person
function Student(firstName, lastName, className) {
    Person.call(this, firstName, lastName); // Вызов конструктора Person
    this.className = className; // Добавляем класс
}

// Наследование методов Person
Student.prototype = Object.create(Person.prototype);
Student.prototype.constructor = Student;

// Геттер для класса
Student.prototype.getClassName = function () {
    return this.className;
};

// Сеттер для класса
Student.prototype.setClassName = function (className) {
    this.className = className;
};

// Метод для добавления нового студента
Student.addStudent = function () {
    const firstName = document.getElementById('first-name').value.trim();
    const lastName = document.getElementById('last-name').value.trim();
    const className = document.getElementById('class-name').value.trim();

    // Проверка имени и фамилии
    if (!Student.validateName(firstName)) {
        alert('Имя должно содержать только буквы.');
        return null;
    }

    if (!Student.validateName(lastName)) {
        alert('Фамилия должна содержать только буквы.');
        return null;
    }

    // Проверка класса
    if (!Student.validateClassName(className)) {
        alert('Класс должен быть в формате "число до 11 и буква". Например, 10а.');
        return null;
    }

    return new Student(firstName, lastName, className);
};

// Метод для проверки имени/фамилии
Student.validateName = function (name) {
    return /^[а-яА-ЯёЁa-zA-Z]+$/.test(name);
};

// Метод для проверки класса
Student.validateClassName = function (className) {
    return /^([1-9]|1[0-1])[а-яa-z]$/.test(className);
};

// Метод для отображения студентов
Student.displayStudents = function (students) {
    const list = document.getElementById('student-list');
    list.innerHTML = '';

    students.forEach(student => {
        const li = document.createElement('li');
        li.textContent = `${student.getFirstName()} ${student.getLastName()}, ${student.getClassName()}`;
        list.appendChild(li);
    });
};

// Метод для поиска однофамильцев
Student.findSameSurnames = function (students) {
    const sameSurnames = [];
    const surnamesCount = {};

    students.forEach(student => {
        const surname = student.getLastName();
        surnamesCount[surname] = (surnamesCount[surname] || 0) + 1;
    });

    for (let surname in surnamesCount) {
        if (surnamesCount[surname] > 1) {
            sameSurnames.push(surname);
        }
    }

    const list = document.getElementById('same-surnames');
    list.innerHTML = '';

    sameSurnames.forEach(surname => {
        const li = document.createElement('li');
        li.textContent = surname;
        list.appendChild(li);
    });
};

// Массив студентов
const students = [];

// Обработчик формы
document.getElementById('student-form').addEventListener('submit', function (event) {
    event.preventDefault();
    const student = Student.addStudent();

    if (student) {
        students.push(student);
        Student.displayStudents(students);
        Student.findSameSurnames(students);
    }
});

// Базовый класс Person, представляющий человека
class Person {
    constructor(firstName, lastName) {
        this.firstName = firstName;
        this.lastName = lastName;
    }

    // Геттеры и сеттеры для имени
    getFirstName() {
        return this.firstName;
    }

    setFirstName(firstName) {
        this.firstName = firstName;
    }

    // Геттеры и сеттеры для фамилии
    getLastName() {
        return this.lastName;
    }

    setLastName(lastName) {
        this.lastName = lastName;
    }
}

// Класс Student, наследующий от Person
class Student extends Person {
    constructor(firstName, lastName, className) {
        // Вызов конструктора родительского класса
        super(firstName, lastName);
        this.className = className; // Уникальное свойство класса Student
    }

    // Геттеры и сеттеры для класса
    getClassName() {
        return this.className;
    }

    setClassName(className) {
        this.className = className;
    }

    // Метод для добавления ученика
    static addStudent() {
        let firstName = document.getElementById('first-name').value.trim();
        let lastName = document.getElementById('last-name').value.trim();
        let className = document.getElementById('class-name').value.trim();

        if (!/^[А-Яа-яA-Za-z]+$/.test(firstName)) {
            alert("Имя должно содержать только буквы.");
            return null;
        }

        if (!/^[А-Яа-яA-Za-z]+$/.test(lastName)) {
            alert("Фамилия должна содержать только буквы.");
            return null;
        }

        if (!/^(?:[1-9]|1[0-1])[а-яa-z]$/.test(className)) {
            alert("Класс должен быть в формате 'число (1-11) и буква' (например, '10а').");
            return null;
        }

        return new Student(firstName, lastName, className);
    }

    // Метод для отображения списка учеников
    static displayStudents(students) {
        let list = document.getElementById('student-list');
        list.innerHTML = '';

        students.forEach(student => {
            let li = document.createElement('li');
            li.textContent = `${student.getFirstName()} ${student.getLastName()}, ${student.getClassName()}`;
            list.appendChild(li);
        });
    }

    // Метод для поиска однофамильцев
    static findSameSurnames(students) {
        let sameSurnames = [];
        let surnamesCount = {};

        students.forEach(student => {
            let surname = student.getLastName();
            surnamesCount[surname] = (surnamesCount[surname] || 0) + 1;
        });

        for (let surname in surnamesCount) {
            if (surnamesCount[surname] > 1) {
                sameSurnames.push(surname);
            }
        }

        let list = document.getElementById('same-surnames');
        list.innerHTML = '';

        sameSurnames.forEach(surname => {
            let li = document.createElement('li');
            li.textContent = surname;
            list.appendChild(li);
        });
    }
}

// Инициализация массива учеников
let students = [];

// Обработчик события для формы добавления ученика
document.getElementById('student-form').addEventListener('submit', function(event) {
    event.preventDefault();
    let student = Student.addStudent();

    if (student) {
        students.push(student);
        Student.displayStudents(students);
        Student.findSameSurnames(students);
    }
});

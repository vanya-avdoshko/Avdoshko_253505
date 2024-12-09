class BackgroundAnimation {
    // Конструктор класса, принимающий элемент фона
    constructor(backgroundElement) {
        // Если элемент фона не передан, выходим из конструктора
        if (!backgroundElement) {
            return;
        }

        this.background = backgroundElement; // Элемент фона, на котором будут размещаться изображения
        this.itemCount = 50; // Количество элементов (изображений), которые будут добавлены на фон
        this.itemSrc = this.background.getAttribute('data-src'); // Путь к изображению, которое будет использоваться для элементов
        this.items = []; // Массив для хранения созданных элементов

        // Инициализация элементов
        this.init();
    }

    // Метод для инициализации элементов на фоне
    init() {
        // Создаём элементы (изображения) и добавляем их на фон
        for (let i = 0; i < this.itemCount; i++) {
            const item = document.createElement('img'); // Создаём новый элемент <img>
            item.src = this.itemSrc; // Устанавливаем путь к изображению
            item.classList.add('background__item'); // Добавляем класс для стилизации

            // Устанавливаем случайные позиции для элемента на фоне
            item.style.left = `${(i > this.itemCount / 2 - 1) ? (Math.random() * 30) : (70 + Math.random() * 30)}vw`; // Позиция по оси X
            item.style.top = `${Math.random() * 100}vh`; // Позиция по оси Y (случайная)

            // Устанавливаем случайные размеры и повороты для каждого элемента
            const size = Math.random() * 30 + 50; // Случайный размер от 50 до 80 пикселей
            const initialRotate = Math.random() * 360; // Случайный угол поворота от 0 до 360 градусов
            item.style.width = `${size}px`; // Устанавливаем ширину
            item.style.transform = `rotate(${initialRotate}deg)`; // Устанавливаем начальный угол поворота

            // Добавляем элемент в DOM
            this.background.appendChild(item);

            // Добавляем информацию об элементе в массив для дальнейшего использования
            this.items.push({ element: item, rotation: initialRotate });
        }

        // Добавляем обработчик события для анимации при прокрутке страницы
        window.addEventListener('scroll', () => {
            const scrollY = window.scrollY; // Получаем текущее положение прокрутки по оси Y

            // Для каждого элемента на фоне изменяем его позицию и угол поворота
            this.items.forEach((item, i) => {
                // Разная скорость прокрутки для каждого элемента
                const speed = 0.1 + (i % 5) * 0.05; // Увеличиваем скорость для элементов с чётным индексом
                const newTop = parseFloat(item.element.style.top) + scrollY * speed; // Вычисляем новую позицию по оси Y с учётом прокрутки

                // Разная скорость вращения для каждого элемента
                const rotationSpeed = 0.1 + 0.4 * Math.random(); // Случайная скорость вращения
                item.rotation += rotationSpeed; // Обновляем угол поворота элемента

                // Применяем новые значения для элемента (позиция + угол поворота)
                item.element.style.transform = `translateY(${newTop}px) rotate(${item.rotation}deg)`;
            });
        });
    }
}

// Экспортируем класс, если используется модульная система 
export default BackgroundAnimation;

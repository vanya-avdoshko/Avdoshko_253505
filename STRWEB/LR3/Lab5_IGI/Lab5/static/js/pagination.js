document.addEventListener('DOMContentLoaded', function() {
    const productsPerPage = 3; // Количество товаров на страницу
    const products = document.querySelectorAll('.product-item'); // Все товары
    const totalProducts = products.length; // Общее количество товаров

    if (totalProducts === 0) {
        console.log('Нет товаров для отображения');
        return;
    }

    const totalPages = Math.ceil(totalProducts / productsPerPage); // Общее количество страниц

    let currentPage = 1;

    // Функция для отображения товаров на текущей странице
    function showPage(page) {
        products.forEach((product, index) => {
            if (index >= (page - 1) * productsPerPage && index < page * productsPerPage) {
                product.style.display = 'block'; // Показываем товар на текущей странице
            } else {
                product.style.display = 'none'; // Прячем остальные товары
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
            button.addEventListener('click', () => {
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
    document.getElementById('prevPage').addEventListener('click', function() {
        if (currentPage > 1) {
            currentPage--;
            showPage(currentPage);
        }
    });

    document.getElementById('nextPage').addEventListener('click', function() {
        if (currentPage < totalPages) {
            currentPage++;
            showPage(currentPage);
        }
    });

    // Инициализация пагинации
    createPagination();
    showPage(currentPage); // Показываем товары на первой странице
});
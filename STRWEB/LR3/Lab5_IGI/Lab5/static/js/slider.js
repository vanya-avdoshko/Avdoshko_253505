class Slider { 
  constructor(sliderElement, options) { 
      // Сохраняем элемент слайдера 
      this.sliderElement = sliderElement; 
      // Находим контейнер слайдов 
      this.slides = sliderElement.querySelector('#slides'); 
      // Определяем количество слайдов 
      this.totalSlides = this.slides.children.length; 
      // Устанавливаем текущий слайд на 0 
      this.currentSlide = 0; 
      // Сохраняем настройки 
      this.loop = options.loop; 
      this.auto = options.auto; 
      this.delay = options.delay * 1000; // Переводим задержку в миллисекунды 
      this.stopMouseHover = options.stopMouseHover; 
      this.interval = null; // Таймер для авто-смены 
      // Инициализация слайдера 
      this.init(); 
  } 

  init() { 
      // Обновляем пагинацию 
      this.updatePagination(); 
      // Устанавливаем события 
      this.bindEvents(); 
      // Запускаем авто-смену, если включена 
      if (this.auto) this.startAutoSlide(); 
  } 

  goToSlide(index) { 
      // Переход к указанному слайду 
      this.currentSlide = index; 
      this.changeSlide(); 
  } 

  updatePagination() { 
      // Обновляем индикаторы пагинации 
      const paginationDots = document.querySelectorAll('.page_dot'); 
      paginationDots.forEach((dot, index) => { 
          dot.classList.toggle('active_dot', index === this.currentSlide); 
      }); 
  } 

  bindEvents() { 
      // Добавляем обработчики клика для навигации 
      document.querySelector('.prev').addEventListener('click', () => this.prevSlide()); 
      document.querySelector('.next').addEventListener('click', () => this.nextSlide()); 
      // Остановка авто-смены при наведении 
      if (this.stopMouseHover) { 
          this.sliderElement.addEventListener('mouseenter', () => this.stopAutoSlide()); 
          this.sliderElement.addEventListener('mouseleave', () => this.startAutoSlide()); 
      } 
      // Обработка изменений в форме настроек (delay и другие)
      document.getElementById('settings-form').addEventListener('change', (e) => this.updateSettings(e)); 
  } 

  changeSlide() { 
      // Переключение слайда 
      this.slides.style.transform = `translateX(-${this.currentSlide * 100}%)`; 
      this.updatePagination(); 
  } 

  nextSlide() { 
      // Переход к следующему слайду 
      if (this.currentSlide < this.totalSlides - 1) { 
          this.currentSlide++; 
      } else if (this.loop) { 
          this.currentSlide = 0; 
      } 
      this.changeSlide(); 
  } 

  prevSlide() { 
      // Переход к предыдущему слайду 
      if (this.currentSlide > 0) { 
          this.currentSlide--; 
      } else if (this.loop) { 
          this.currentSlide = this.totalSlides - 1; 
      } 
      this.changeSlide(); 
  } 

  startAutoSlide() { 
      // Запуск авто-смены слайдов 
      if (this.auto) { 
          this.interval = setInterval(() => this.nextSlide(), this.delay); 
      } 
  } 

  stopAutoSlide() { 
      // Остановка авто-смены слайдов 
      if (this.interval) { 
          clearInterval(this.interval); 
          this.interval = null; 
      } 
  } 

  updateSettings(e) { 
      // Обновление настроек слайдера 
      const formData = new FormData(e.target.form); 
      this.loop = formData.get('loop') === 'on'; 
      this.auto = formData.get('auto') === 'on'; 
      this.delay = formData.get('delay') * 1000; 
      this.stopMouseHover = formData.get('stopMouseHover') === 'on'; 

      // Обновление отображения навигации и пагинации 
      document.getElementById('nav').style.display = formData.get('navs') === 'on' ? 'flex' : 'none'; 
      document.getElementById('pagination').style.display = formData.get('pags') === 'on' ? 'block' : 'none'; 

      // Перезапуск авто-смены с новыми настройками 
      this.stopAutoSlide(); 
      if (this.auto) this.startAutoSlide(); 
  } 
} 

document.addEventListener('DOMContentLoaded', () => { 
  window.slider = new Slider(document.getElementById('slider'), { 
    loop: true, 
    auto: true, 
    delay: 5, 
    stopMouseHover: true 
}); 
});
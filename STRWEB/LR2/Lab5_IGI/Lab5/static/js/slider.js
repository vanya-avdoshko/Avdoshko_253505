class Slider {
  constructor(options) {
    this.container = document.querySelector(options.container);
    this.slides = this.container.querySelectorAll('figure');
    this.currentIndex = 0;
    this.autoPlay = options.auto || false;
    this.delay = options.delay || 5;
    this.loop = options.loop || false;
    this.timer = null;

    this.init();
  }

  init() {
    document.getElementById('prev-slide').addEventListener('click', () => this.prevSlide());
    document.getElementById('next-slide').addEventListener('click', () => this.nextSlide());
    this.updateSlide();
    if (this.autoPlay) {
      this.startAutoPlay();
    }
  }

  updateSlide() {
    const offset = -this.currentIndex * 100;
    this.container.querySelector('.slider').style.transform = `translateX(${offset}%)`;
    this.updatePagination();
  }

  prevSlide() {
    this.currentIndex--;
    if (this.currentIndex < 0) {
      this.currentIndex = this.loop ? this.slides.length - 1 : 0;
    }
    this.updateSlide();
  }

  nextSlide() {
    this.currentIndex++;
    if (this.currentIndex >= this.slides.length) {
      this.currentIndex = this.loop ? 0 : this.slides.length - 1;
    }
    this.updateSlide();
  }

  updatePagination() {
    const paginationText = document.getElementById('pagination-text');
    paginationText.textContent = `${this.currentIndex + 1}/${this.slides.length}`;
  }

  startAutoPlay() {
    this.timer = setInterval(() => this.nextSlide(), this.delay * 1000);
  }
}

// Инициализация слайдера
const slider = new Slider({
  container: '#slider-container',
  auto: true,
  delay: 5,
  loop: true
});

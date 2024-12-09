document.addEventListener('DOMContentLoaded', () => {
    const styleToggle = document.getElementById('style-toggle');
    const styleControls = document.getElementById('style-controls');
    const fontSizeInput = document.getElementById('font-size');
    const textColorInput = document.getElementById('text-color');
    const bgColorInput = document.getElementById('bg-color');
    const body = document.body;
  
    // Показать или скрыть элементы управления в зависимости от состояния флажка
    styleToggle.addEventListener('change', () => {
      styleControls.style.display = styleToggle.checked ? 'block' : 'none';
    });
  
    // Обработчик изменения размера шрифта
    fontSizeInput.addEventListener('input', () => {
      document.body.style.fontSize = fontSizeInput.value + 'px';
    });
  
    // Обработчик изменения цвета текста
    textColorInput.addEventListener('input', () => {
      document.body.style.color = textColorInput.value;
    });
  
    // Обработчик изменения цвета фона
    bgColorInput.addEventListener('input', () => {
      document.body.style.backgroundColor = bgColorInput.value;
    });
  });
  
document.addEventListener('DOMContentLoaded', () => {
    const timeDisplay = document.getElementById('time');
  
    // Получаем текущее время
    const currentTime = new Date().getTime();
  
    // Проверяем, есть ли сохраненная информация о времени
    let countdownEndTime = localStorage.getItem('countdownEndTime');
  
    // Если нет сохраненного времени, устанавливаем время окончания отсчета через 1 час
    if (!countdownEndTime) {
      countdownEndTime = currentTime + 60 * 60 * 1000; // 1 час от текущего времени
      localStorage.setItem('countdownEndTime', countdownEndTime);
    }
  
    // Функция для обновления времени на странице
    function updateCountdown() {
      const remainingTime = countdownEndTime - new Date().getTime();
      
      if (remainingTime <= 0) {
        timeDisplay.innerHTML = 'Время вышло!';
        localStorage.removeItem('countdownEndTime'); // Удаляем сохраненное время, если отсчет завершен
      } else {
        const minutes = Math.floor((remainingTime % (1000 * 60 * 60)) / (1000 * 60));
        const seconds = Math.floor((remainingTime % (1000 * 60)) / 1000);
        timeDisplay.innerHTML = `${minutes}m ${seconds}s`;
      }
    }
  
    // Обновляем отсчет каждую секунду
    setInterval(updateCountdown, 1000);
    updateCountdown(); // немедленно показываем оставшееся время
  });
  
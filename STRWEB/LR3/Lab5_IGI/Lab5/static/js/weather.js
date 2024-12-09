document.addEventListener("DOMContentLoaded", function () {
    const locationElement = document.getElementById('location');
    const weatherElement = document.getElementById('weather');
    const apiKey = 'f9084d8638e6522e3f36b8dcf9e06247'; 

    // Функция для получения геолокации пользователя
    function getGeolocation() {
        if (navigator.geolocation) {
            navigator.geolocation.getCurrentPosition(
                (position) => {
                    const latitude = position.coords.latitude;
                    const longitude = position.coords.longitude;

                    locationElement.textContent = `Широта: ${latitude}, Долгота: ${longitude}`;
                    getWeather(latitude, longitude); // Получение погоды
                },
                (error) => {
                    console.error(error);
                    locationElement.textContent = 'Не удалось определить местоположение.';
                }
            );
        } else {
            locationElement.textContent = 'Геолокация не поддерживается вашим браузером.';
        }
    }

    // Функция для получения погоды
    async function getWeather(lat, lon) {
        try {
            //http запрос с помощью fetch
            const response = await fetch(
                `https://api.openweathermap.org/data/2.5/weather?lat=${lat}&lon=${lon}&units=metric&lang=ru&appid=${apiKey}`
            );
            if (!response.ok) {
                throw new Error('Ошибка при загрузке данных о погоде');
            }

            const data = await response.json();
            const temp = data.main.temp;
            const weatherDescription = data.weather[0].description;

            weatherElement.textContent = `Температура: ${temp}°C, Описание: ${weatherDescription}`;
        } catch (error) {
            console.error(error);
            weatherElement.textContent = 'Не удалось загрузить данные о погоде.';
        }
    }

    // Запуск
    getGeolocation();
});

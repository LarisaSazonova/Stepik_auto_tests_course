# Праметризация тестов

Инопланетяне оставляют загадочные сообщения на Stepik в фидбеке задач на правильное решение. Мы смогли локализовать несколько url-адресов задач, где появляются кусочки сообщений. Ваша задача — реализовать автотест со следующим сценарием действий: 

- открыть страницу 
- ввести правильный ответ 
- нажать кнопку "Отправить" 
- дождаться фидбека о том, что ответ правильный 
- проверить, что текст в опциональном фидбеке полностью совпадает с "Correct!"

Правильным ответом на задачу в заданных шагах является число: math.log(int(time.time()))

Используйте маркировку pytest для параметризации и передайте в тест список ссылок в качестве параметров: 

- https://stepik.org/lesson/236895/step/1
- https://stepik.org/lesson/236896/step/1
- https://stepik.org/lesson/236897/step/1
- https://stepik.org/lesson/236898/step/1
- https://stepik.org/lesson/236899/step/1
- https://stepik.org/lesson/236903/step/1
- https://stepik.org/lesson/236904/step/1
- https://stepik.org/lesson/236905/step/1

Используйте осмысленное сообщение об ошибке в проверке текста, а также настройте нужные ожидания, чтобы тесты работали стабильно. 

В упавших тестах найдите кусочки послания. Тест должен падать, если текст в опциональном фидбеке не совпадает со строкой "Correct!" Соберите кусочки текста в одно предложение и отправьте в качестве ответа на это задание. 
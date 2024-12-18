# Ingiborg Jump: Полная документация

Добро пожаловать в полную документацию проекта игры Ingiborg Jump. Этот документ поможет вам с установкой, использованием и разработкой игры.

## Содержание
1. [Установка](#установка)
2. [Использование](#использование)
   - [Управление игрой](#управление-игрой)
   - [Цель игры](#цель-игры)
   - [Счет](#счет)
3. [Разработка](#разработка)
   - [Структура проекта](#структура-проекта)
   - [Игровая механика](#игровая-механика)
   - [Добавление новых функций](#добавление-новых-функций)
4. [Вклад](#вклад)

## Установка

Чтобы запустить игру Ingiborg Jump, вам необходимо установить Python и библиотеку Pygame на вашем компьютере. Следуйте этим шагам, чтобы начать:

1. **Установите Python**: Если у вас еще нет Python, вы можете скачать его с официального сайта Python (https://www.python.org/downloads/).
2. **Установите Pygame**: Откройте терминал или командную строку и выполните следующую команду для установки библиотеки Pygame:
```commandline
pip install pygame
```


3. **Скачайте код игры**: Вы можете скачать код игры из предоставленного источника или клонировать репозиторий с помощью Git:
```commandline
git clone https://github.com/starl1ght0/IngiborgJump.git
```

4. **Запустите игру**: Перейдите в каталог проекта и выполните следующую команду, чтобы запустить игру:
```commandline
python main.py 
```
Теперь игра должна запуститься, и вы можете начать играть.

## Использование

### Управление игрой

- **Левая стрелка**: Переместить игрока влево
- **Правая стрелка**: Переместить игрока вправо
- **Перезапуск**: Нажмите кнопку "Перезапуск" на экране "Конец игры"

### Цель игры

Цель Ingiborg Jump — прыгать как можно выше, не упав с экрана. Игрок управляет существом с четырьмя ногами, называемым "Ingiborgr", и должен прыгать с платформы на платформу, чтобы достичь новых высот.

### Счет

Игра отслеживает счет игрока, который отображается в верхней части экрана. Счет увеличивается по мере того, как игрок поднимается выше, и пропорционален пройденному расстоянию.

## Разработка

### Структура проекта

Проект Ingiborg Jump структурирован следующим образом:

- `Ingiborg_jump.py`: Основной файл игры, содержащий логику и рендеринг игры.
- `player.py`: Определяет класс `Player`, который представляет главного персонажа.
- `platform.py`: Определяет класс `Platform`, который представляет платформы, по которым прыгает игрок.
- `game_over_screen.py`: Определяет класс `GameOverScreen`, который обрабатывает экран окончания игры и функциональность перезапуска.
- `reset_game`: Функция рестарта игры которая начинает цикл заново

### Игровая механика

Игровая механика реализована в файле `Ingiborg_jump.py`. Основные компоненты:

1. **Движение игрока**: Движение игрока контролируется клавишами влево и вправо, которые обновляют горизонтальное положение игрока.
2. **Гравитация и прыжки**: Вертикальная скорость игрока зависит от гравитации, и игрок может прыгать при столкновении с платформой.
3. **Генерация платформ**: Новые платформы генерируются в верхней части экрана по мере того, как игрок поднимается выше, а платформы, которые выходят за пределы экрана, удаляются.
4. **Обнаружение столкновений**: Обнаружение столкновений используется для определения, когда игрок приземляется на платформу и когда он падает с экрана.
5. **Счет**: Счет игрока обновляется на основе пройденного расстояния.
6. **Конец игры и перезапуск**: Когда игрок падает с экрана, отображается экран окончания игры, и игрок может перезапустить игру, нажав кнопку "Перезапуск".

## Добавление новых функций
### Обновление 2
#### Добавлено:

1. Счётчик преодоленного расстояния
2. папка **images** с 3 изображениями
3. Изображения:
- Задний фон в виде изображения
- Иконка игрока в виде изображения
- Платформы в виде изображения

#### Исправлено:

1. Баг когда при нажатии кнопки restart игрок продолжал свой путь с того же места.
2. Баг когда в начале игры нет платформы под игроком


## Вклад

Если вы хотите внести свой вклад в проект Ingiborg Jump, не стесняйтесь форкать репозиторий, вносить изменения и отправлять запрос на слияние. Я приветствую вклад любого рода, включая исправления ошибок, новые функции и улучшения документации.

При внесении изменений, пожалуйста, следуйте существующему стилю кода и соглашениям, и убедитесь, что ваши изменения не нарушают существующую функциональность. Кроме того, рассмотрите возможность добавления тестов, чтобы обеспечить стабильность ваших изменений.

Спасибо за ваш интерес к проекту Ingiborg Jump! Если у вас есть какие-либо вопросы или вам нужна дополнительная помощь, не стесняйтесь обращаться.

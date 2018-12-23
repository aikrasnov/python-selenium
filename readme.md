[![Build Status](https://travis-ci.org/aikrasnov/python-selenium.svg?branch=master)](https://travis-ci.org/aikrasnov/python-selenium)
## Как запустить тесты
### Локально
0) Установить firefox, chrome и положить их драйвера в PATH ([chromedriver](http://chromedriver.chromium.org/), [geckodriver](https://github.com/mozilla/geckodriver/releases))
1) Склонировать репу
2) Установить pipenv ([инструкция](https://github.com/pypa/pipenv#installation))
3) Запустить `pipenv install --dev && pipenv run pytest`

### В Sauce Lab 
1) Выполнить все те же шаги (кроме драйверов в PATH)
2) Установить переменные окружения SAUCE_USERNAME and SAUCE_ACCESS_KEY
3) Запустить тесты

### Изменить количество ретраев
`pytest -reruns number` ([подробности](https://pypi.org/project/pytest-rerunfailures/))

### Изменить количество параллельных тестов
`pytest -n number` ([подробности](https://pypi.org/project/pytest-xdist/))

### Изменить браузер
`pytest --browser firefox`
`pytest --browser chrome`

### Посмотреть отчеты
1) Установить allure ([инструкция](https://docs.qameta.io/allure/#_installing_a_commandline))
2) Запустить тесты
3) Выполнить `allure generate report --clean && allure open allure-report`

TODO:
1) Публиковать отчеты по запускам в travis ci
2) Вынести из conftest установку капабилити, создание объектов webdriver.Remote / Firefox / Chrome
3) Кастомизировать отчеты в консоли
4) Добавить репорты в телеграм / слак
5) Вынести повторяющеся ошибки в отдельный модуль
6) Вынести повторяющиеся ассерты из PO
7) "Прорастить" ретраи в allure-отчеты

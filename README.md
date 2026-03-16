# Отправка уведомлений о проверке работ

Данный скрипт использует API сайта [devman](https://dvmn.org) для отправки уведомлений о результатах проверки работ ученику через Telegram бота.

## Установка
- Установите [Python](https://www.python.org/downloads/) версии 3.11.9
- Клонируйте репозиторий на свой ПК
- Создайте виртуальную среду Python (укажите нужную версию Python, если у вас их несколько)

Windows (PowerShell):
```powershell
py -3.11 -m venv venv
```
Linux/macOS:
```bash
python3.11 -m venv venv
```
- Активируйте созданную виртуальную среду командой:

Windows (PowerShell):
```powershell
venv\Scripts\activate
```
Linux\macOS:
```bash
source venv/bin/activate
```
- Перейдите в папку репозитория и используйте команду, указанную ниже для установки необходимых библиотек
```powershell
pip install -r requirements.txt
```
- Перейдите в телеграм-бота [BotFather](https://web.telegram.org/k/#@BotFather) и создайте своего бота, сохраните его токен
- В папке репозитория создайте `.env` файл и укажите в нем следующие параметры:
    * `DVMN_TOKEN` - ваш API Token на сайте [devman](https://dvmn.org/api/docs/)
    * `BOT_TOKEN` - токен вашего Telegram бота
    * `TG_USER_ID` - ID вашего аккаунта в Telegram.

Пример указания параметра в `.env` файле:
```.env
DVMN_TOKEN = 'TOKEN'
```

## Пример запуска скрипта

Для запуска скрипта используйте команду:
```powershell
python script.py
```

### Цель проекта

Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [dvmn.org](https://dvmn.org).

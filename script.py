import os
from time import sleep

import requests
import telegram
from dotenv import load_dotenv


def create_answer(bool, records) -> str:
    title = records['new_attempts'][0]['lesson_title']
    link = records['new_attempts'][0]['lesson_url']
    header = f'У вас проверили работу "{title}"\n\n'
    footer = f'Ссылка на урок: {link}'

    if bool:
        return f'{header}К сожалению, в работе нашлись ошибки.\n\n{footer}'
    else:
        return f'{header}Преподавателю всё понравилось, можно приступать к следующему уроку!\n\n{footer}'


def main():
    load_dotenv()
    dvmn_token = os.environ['DVMN_TOKEN']
    bot_token = os.environ['BOT_TOKEN']
    user_id = os.environ['TG_USER_ID']

    bot = telegram.Bot(token=bot_token)

    timestamp = None

    while True:
        url = 'https://dvmn.org/api/long_polling/'
        headers = {'Authorization': f'Token {dvmn_token}'}
        payload = {'timestamp': timestamp}

        try:
            if timestamp:
                response = requests.get(
                    url,
                    headers=headers,
                    params=payload,
                    timeout=15,
                )
            else:
                response = requests.get(
                    url,
                    headers=headers,
                    timeout=15,
                )
            response.raise_for_status()

            records = response.json()
            timestamp = records['last_attempt_timestamp']

            if records['new_attempts'][0]['is_negative']:
                bot.send_message(
                    chat_id=user_id,
                    text=create_answer(True, records),
                )
            else:
                bot.send_message(
                    chat_id=user_id,
                    text=create_answer(False, records),
                )

        except requests.exceptions.ReadTimeout:
            pass

        except requests.exceptions.ConnectionError:
            print(
                '\nThe Internet connection is lost.',
                '\nThe connection attempt will be repeated after 30 seconds.',
            )
            sleep(30)


if __name__ == '__main__':
    main()
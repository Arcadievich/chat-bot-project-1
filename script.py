import os
import requests
from pprint import pprint
from dotenv import load_dotenv


def main():
    load_dotenv()
    dvmn_token = os.environ['DVMN_TOKEN']

    url = 'https://dvmn.org/api/user_reviews/'
    headers = {'Authorization': f'Token {dvmn_token}'}
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    pprint(response.json())



if __name__ == '__main__':
    main()
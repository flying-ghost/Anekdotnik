import requests
from bs4 import BeautifulSoup
from colorama import init, Fore, Style

def get_joke():
    url = 'https://www.anekdot.ru/random/aphorism/'
    try:
        response = requests.get(url)
        response.raise_for_status()
    except requests.RequestException:
        return 'Пока без анекдота, может попозже'

    soup = BeautifulSoup(response.content, 'html.parser')
    joke_div = soup.find('div', class_='text')

    if joke_div:
        return joke_div.get_text(strip=True)
    else:
        return 'Ну чет они кончились походу'

def main():
    print('Ну привет! Лови сразу первый!')
    while True:
        print(Fore.CYAN + '\n' + get_joke())
        again = input(Fore.YELLOW + '\n' + 'И чего? Просто жми энтер, а если надоест введи "stop"').lower()
        if again == 'stop':
            print(Fore.WHITE + 'Ну и ладно, пока, приходи если будет скучно!')
            break
if __name__ == '__main__':
    main()

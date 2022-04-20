from requests import get
from json import loads


def introduction():
    print("""Witaj w sprawdzaczu pogody!
Aktualna lista miast w których można znaleźć ostatni pomiar temperatury:\n
    """)


def print_cities():
    for city in data():
        print(city['stacja'], end=" | ")
    print()


def data():
    url = 'https://danepubliczne.imgw.pl/api/data/synop'
    response = get(url)
    return loads(response.text)


def main():
    city_choose = input("\nWpisz nazwę miasta by sprawdzić ostatni pomiar: \n")
    for row in data():
        if row['stacja'] in city_choose:
            print(f"\nMiasto: {row['stacja']}")
            print(f"Temp: {row['temperatura']}")
            print(f"Pomiar: {row['data_pomiaru']} {row['godzina_pomiaru']}:00")
    input('\nNaciśnij dowolny klawisz aby zamknąć...')


if __name__ == '__main__':
    introduction()
    print_cities()
    main()

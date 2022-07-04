import requests
import yaml

config = yaml.safe_load(open("config.yml"))


def main():
    sheet = input("Enter sheet code: ")
    code = input("Enter card code: ")
    print("*************************")
    print("Enter line as comma or period seperated values. Blank spaces enter 0. E.g.: 7,18,0,37,42,0,0,0,83")
    one = input("Enter line one: ")
    two = input("Enter line two: ")
    three = input("Enter line three: ")

    response = requests.post(config.get('base_url') + '/bingo/card/create', data={
        'api_key': config.get('api_key'),
        'sheet': sheet,
        'code': code,
        'one': one,
        'two': two,
        'three': three
    })

    if response.status_code == 200:
        print("Card " + code + " created successfully")
        main()
    elif response.status_code == 403:
        print("Invalid API key")
        exit(1)
    else:
        print("Error")


if __name__ == '__main__':
    main()
import requests


def load_cookie():
    with open("cookie.txt", "r") as file:
        cookie = file.readline().rstrip()
    return cookie


def fetch_day_input(day):
    url = f"https://adventofcode.com/2025/day/{day}/input"
    cookie = load_cookie()

    print("getting input for day ", day)
    response = requests.get(url, headers={"Cookie": cookie})

    with open("input.txt", "w") as file:
        text = response.text.rstrip()
        file.write(text)

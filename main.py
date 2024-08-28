import requests
import pprint as pp

user_input = int()

def take_input ():
    global user_input
    user_input = input("Please enter a Id for your pokemon")
    if user_input.isdigit():
        user_input = int(user_input)
        url = f"https://pokeapi.co/api/v2/berry/{user_input}/"
        make_request(url)
    else:
        print("Please enter a Id number")
        user_input=""
        take_input()

def make_request(url):
    response = requests.get(url)
    if response.status_code != 200:
        print(response.text)
    else:
        data = response.json()
        pp.pprint(data)

take_input()
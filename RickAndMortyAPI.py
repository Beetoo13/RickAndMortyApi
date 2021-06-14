import requests

characterNumber = 1
flag = True

while flag:

    flagOption = True

    getCharacter = requests.get(
        f'https://rickandmortyapi.com/api/character/{characterNumber}')

    characterJson = getCharacter.json()

    name = characterJson["name"]
    status = characterJson["status"]
    origin = characterJson["origin"]['name']
    location = characterJson["location"]["name"]
    image = characterJson["image"]

    print("")

    print(f"Character #{characterNumber}: {name}")

    print("")
    print(f"The status is: {status}")
    print(f"The origin is: {origin}")
    print(f"The location is: {location}")
    print(f"The image is: {image}")

    print("")

    print("Show next character?")
    print("1.- Si")
    print("2.- No")

    print("")

    while flagOption:

        option = int(input("Your option: "))

        if option == 1:
            print("")
            characterNumber = characterNumber + 1
            flagOption = False
        elif option == 2:
            flagOption = False
            flag = False
            print("")
            print("Thanks for using it!")
        else:
            print("")
            print("Please introduce a valid option...")
            print("")
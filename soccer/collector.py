from selenium import webdriver
from selenium.common.exceptions import ElementNotVisibleException, NoSuchElementException
from selenium.webdriver.chrome.options import Options
from time import sleep
from soccer_database import soccer_collection
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

options = Options()
options.add_argument("--headless")
options.add_argument("--log-level=3")
options.add_experimental_option("excludeSwitches", ["enable-logging"])
browser = webdriver.Chrome(service=Service("/Users/thealissonshow/Documents/The Universe/brizen-sports/chromedriver"),
                           options=options)


def count_games(competition):
    jump = 0
    for game in soccer_collection.find({"competition": competition}):
        jump += 1
    return jump


def load_page_completely():
    more_games = True
    while more_games is not False:
        try:
            sleep(1)
            more_games = browser.find_element(by=By.LINK_TEXT, value="Show more matches")
            browser.execute_script("arguments[0].click();", more_games)
            sleep(2)
        except (ElementNotVisibleException, NoSuchElementException) as e:
            more_games = False


def get_games_data():
    games = browser.find_elements(by=By.CLASS_NAME, value="event__match--twoLine")
    games = list(reversed(games))
    for i in range(len(games)):
        # First, initialize the variables

        # Scores
        homeFT = 0
        awayFT = 0

        # Get HomeTeam
        homeName = games[i+jump].find_element(by=By.CLASS_NAME, value='event__participant--home').text
        while homeName == "":
            homeName = games[i+jump].find_element(by=By.CLASS_NAME, value='event__participant--home').text

        # Get AwayTeam
        awayName = games[i+jump].find_element(by=By.CLASS_NAME, value='event__participant--away').text
        while awayName == "":
            awayName = games[i+jump].find_element(by=By.CLASS_NAME, value='event__participant--away').text

        # Placares

        homeFT = games[i+jump].find_element(by=By.CLASS_NAME, value="event__score--home").text
        if homeFT == "-":
            homeFT = 0
        awayFT = games[i+jump].find_element(by=By.CLASS_NAME, value="event__score--away").text
        if awayFT == "-":
            awayFT = 0

        game_data = {
            "competition": competition,
            "home": homeName.lower(),
            "away": awayName.lower(),
            "home_ft": int(homeFT),
            "away_ft": int(awayFT),
        }

        soccer_collection.insert_one(game_data)
        print(f"Added: {homeName} {game_data['home_ft']} x {game_data['away_ft']} {awayName}")


try:
    link = input("URL: ")
    link = link + "results/"
    competition = input("Competition: ")
    browser.get(link)
    load_page_completely()
    jump = count_games(competition)
    get_games_data()
    browser.close()
    browser.quit()
except IndexError:
    print("Competition is up to date.")
    browser.close()
    browser.quit()
except KeyboardInterrupt:
    print("Service terminated by user.")
    browser.close()
    browser.quit()
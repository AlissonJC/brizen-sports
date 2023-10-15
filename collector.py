import os

from selenium import webdriver
from selenium.common.exceptions import ElementNotVisibleException, NoSuchElementException
from selenium.webdriver.chrome.options import Options
from time import sleep
from urllib3.exceptions import NewConnectionError
from brizen_database import brizen_collection
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

options = Options()
options.add_argument("--headless")
options.add_argument("--log-level=3")
options.add_experimental_option("excludeSwitches", ["enable-logging"])
browser = webdriver.Chrome(service=Service("./chromedriver"),
                           options=options)


def count_games(competition):
    jump = 0
    for game in brizen_collection.find({"competition": competition}):
        jump += 1
    return jump

def get_sport(link):
    if "football" in link and "american-football" not in link:
        return "football"
    elif "baseball" in link:
        return "baseball"
    elif "nfl" in link or "american-football/usa/ncaa" in link:
        return "american-football"
    elif "basketball" in link:
        return "basketball"
    else:
        return "hockey"


def load_page_completely():
    more_games = True
    while more_games is not False:
        try:
            sleep(1)
            more_games = browser.find_element(by=By.LINK_TEXT, value="Show more matches")
            browser.execute_script("arguments[0].click();", more_games)
            sleep(1)
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

        finished = ""
        try:
            finished = games[i+jump].find_element(by=By.CLASS_NAME, value="event__stage--block").text
            if finished != "" and sport == "hockey":
                if int(homeFT) > int(awayFT):
                    homeFT = int(homeFT) - 1
                elif int(awayFT) > int(homeFT):
                    awayFT = int(awayFT) - 1
            if finished != "" and sport == "football":
                homeFT = games[i + jump].find_element(by=By.CLASS_NAME, value="event__part--home.event__part--2").text
                awayFT = games[i + jump].find_element(by=By.CLASS_NAME, value="event__part--away.event__part--2").text
        except NoSuchElementException as e:
            pass


        game_data = {
            "sport": sport,
            "competition": competition,
            "home": homeName.lower(),
            "away": awayName.lower(),
            "home_ft": int(homeFT),
            "away_ft": int(awayFT)
        }


        brizen_collection.insert_one(game_data)
        print(f"Added: {homeName} {game_data['home_ft']} x {game_data['away_ft']} {awayName}")


try:
    link = input("URL: ")
    sport = get_sport(link)
    link = link + "results/"
    competition = input("Competition: ")
    browser.get(link)
    load_page_completely()
    jump = count_games(competition)
    get_games_data()
    browser.close()
    browser.quit()
except (KeyboardInterrupt or ConnectionRefusedError or ConnectionError or NewConnectionError) as e:
    print(str(e))
    browser.close()
    browser.quit()
except IndexError as e:
    print("Competition is up to date.")
    browser.close()
    browser.quit()
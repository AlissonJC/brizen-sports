from selenium import webdriver
from selenium.common.exceptions import ElementNotVisibleException, NoSuchElementException
from selenium.webdriver.chrome.options import Options
from football_database import football_collection, delete_games
from pymongo.errors import DuplicateKeyError
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from time import sleep

options = Options()
options.add_argument("--headless")
options.add_argument("--log-level=3")
options.add_experimental_option("excludeSwitches", ["enable-logging"])
browser = webdriver.Chrome(service=Service("/Users/thealissonshow/Documents/The Universe/brizen-sports/chromedriver"), options=options)


def load_page_completely():
    more_games = True
    while more_games is not False:
        try:
            sleep(1)
            more_games = browser.find_element(by=By.LINK_TEXT, value="Show more matches")
            browser.execute_script("arguments[0].click();", more_games)
            sleep(2)
        except (ElementNotVisibleException, NoSuchElementException):
            more_games = False

def count_games(competition):
    jump = 0
    for game in football_collection.find({"competition": competition}):
        jump += 1
    return jump

def get_games_data():
    results_window = browser.window_handles[0]
    games = browser.find_elements(By.CLASS_NAME, value="event__match--twoLine")
    games = list(reversed(games))
    for i in range(len(games)):
        browser.execute_script("arguments[0].click();", games[i+jump])
        game_window = browser.window_handles[1]
        browser.switch_to.window(game_window)
        _id = browser.current_url[33:41] + '@' + competition

        # Primeiramente definimos todas as variáveis

        homeFT = 0
        awayFT = 0

        # Get HomeTeam
        _ht = browser.find_element(By.CLASS_NAME, value='duelParticipant__home')
        homeName = _ht.find_element(By.CLASS_NAME, value='participant__participantName').text
        while homeName == "":
            _ht = browser.find_element(By.CLASS_NAME, value='duelParticipant__home')
            homeName = _ht.find_element(By.CLASS_NAME, value='participant__participantName').text

        # Get AwayTeam
        _at = browser.find_element(By.CLASS_NAME, value='duelParticipant__away')
        awayName = _at.find_element(By.CLASS_NAME, value='participant__participantName').text
        while awayName == "":
            _at = browser.find_element(By.CLASS_NAME, value='duelParticipant__away')
            awayName = _at.find_element(By.CLASS_NAME, value='participant__participantName').text

        status = browser.find_element(By.CLASS_NAME, value="detailScore__status").text

        scoreFT = browser.find_element(By.CLASS_NAME, value="detailScore__wrapper").text
        homeFT, separator, awayFT = scoreFT.split()
        
        if status == "Awarded" or status == "Walkover":
            continue

        game_data = {
            "_id": _id,
            "competition": competition,
            "home": homeName.lower(),
            "away": awayName.lower(),
            "home_ft": int(homeFT),
            "away_ft": int(awayFT),
        }

        football_collection.insert_one(game_data)
        print(f"Added: {homeName} {game_data['home_ft']} x {game_data['away_ft']} {awayName}")

        browser.execute_script("window.close();")
        browser.switch_to.window(results_window)

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
except DuplicateKeyError:
    delete_games(competition)
    browser.close()
    browser.quit()
    print(f"Games deleted in {competition.upper()}.")
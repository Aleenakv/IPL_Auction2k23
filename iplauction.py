from selenium import webdriver
from selenium.webdriver.common.by import By
from csv import writer
import time

website = 'https://www.espncricinfo.com/auction/ipl-auction-2023'
path = 'D:\Program files\chromedriver.exe'
driver = webdriver.Chrome(path)
driver.get(website)

def get_name(player):
    try:
        name = player.find_element(By.XPATH, './/span[@class="name"]').text
    except Exception as e:
        name = 'Not available'
    return name


def get_link(player):
    try:
        link = player.find_element(By.XPATH, './/a').get_attribute('href')
    except Exception as e:
        link = 'Not available'
    return link


def get_type(player):
    try:
        type = player.find_element(By.XPATH, './/span[@class="mid"]/text()')
    except Exception as e:
        type = 'Not available'
    return type


def get_lakhs(player):
    try:
        lakhs = player.find_element(By.XPATH, './/span[@class="dolr"]').text
    except Exception as e:
        lakhs = 'Not available'
    return lakhs


def get_dollars(player):
    try:
        dollars = player.find_element(By.XPATH, './/span[@class="last"]').text
    except Exception as e:
        dollars = 'Not available'
    return dollars

def get_player_details(link):
    driver.get(link)
    time.sleep(10)
    player_details = []
    try:

        details = driver.find_elements(By.XPATH, './/span[@class="ds-text-title-s ds-font-bold ds-text-typo"]/h5')
        for detail in details:
            detail_item = detail.text
            player_details.append(detail_item)
    except Exception as e:
        pass
    return player_details


with open('ipl_auction.csv', 'w', newline='', encoding='utf-8') as f:
    theWriter = writer(f)
    heading = ['player_name', 'player_link', 'player_type', 'cost_lakhs', 'cost_dollars', 'born_date', 'player_age',
               'batting_style', 'bowling_style', 'playing_role']
    theWriter.writerow(heading)

    all_players = driver.find_elements(By.XPATH, './/ul[@class="table"]/li[@class]')
    player_link = []
    all_player_info = []
    all_player_details = []
    for player in all_players:
        name = get_name(player)
        link = get_link(player)
        type = get_type(player)
        lakhs = get_lakhs(player)
        dollars = get_dollars(player)
        player_link.append(link)
        player_info = [name, link, type, lakhs, dollars]
        all_player_info.append(player_info)


    for link in player_link:
        player_details = get_player_details(link)
        all_player_details.append(player_details[1:6])

    for i in range(len(player_link)):
        player_all_details = all_player_info[i] + all_player_details[i]
        print(player_all_details)
        theWriter.writerow(player_all_details)

driver.quit()
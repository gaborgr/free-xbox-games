
from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By

def freeGames():
    url = 'https://www.xbox.com/es-CL/games/all-games/console?PlayWith=XboxSeriesX%7CS%2CXboxOne&xr=shellnav'

    options = webdriver.ChromeOptions()
    options.add_experimental_option('detach', True)
    browser = webdriver.Chrome(options=options)
    browser.get(url)
    browser.implicitly_wait(10)

    while True:
        try:
            load_more = browser.find_element(By.XPATH, "//*[contains(text(), 'Cargar más')]")
            load_more.click()
        except:
            break

    lenguage = ['Gratis', 'Free']                                        

    soup = BeautifulSoup(browser.page_source, 'html.parser')
    games = soup.find_all('a', attrs={"aria-label": True})
    for game in games:
            aria_text = game['aria-label'].split(', ')
            if lenguage[0] in aria_text or lenguage[1] in aria_text:
                name = aria_text[0]
                price = aria_text[1]
                link = game['href']
                print(f"{name} - {price} - {link}")
            else:
                continue

if __name__ == '__main__':
    freeGames()
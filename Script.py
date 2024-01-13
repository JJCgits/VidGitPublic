from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as dWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time
import undetected_chromedriver as uc

from selenium.webdriver.common.by import By
from dotenv import dotenv_values
import os

#The setup
from seleniumbase import Driver

config = dotenv_values(".env")


driver = Driver(uc=True, headless=True)
driver.get("https://chat.openai.com/")

#The elements
LoginButton = '//*[@id="__next"]/div[1]/div[2]/div[1]/div/div/button[1]'
googleLoginButton = '/html/body/div/main/section/div/div/div/div[4]/form[2]/button'

googleEmail = '//*[@id="identifierId"]'
googlePassword = '//*[@id="password"]/div[1]/div/div[1]/input'
nextButton = '//*[@id="identifierNext"]/div/button'
pNextButton = '//*[@id="passwordNext"]/div/button'
print(config)
myEmail = config['LOGIN_USER']
password = config['LOGIN_PASSWORD']

next = '//*[@id="headlessui-dialog-panel-:r1:"]/div[2]/div[4]/button/div'
chatNextButton = '//*[@id="headlessui-dialog-panel-:r1:"]/div[2]/div[4]/button'
chatNextButton2 = '//*[@id="headlessui-dialog-panel-:r1:"]/div[2]/div[4]/button[2]'

chatGPT = '//*[@id="prompt-textarea"]'
sendButton = '//*[@id="__next"]/div[1]/div/main/div[1]/div[2]/form/div/div[1]/div/button'


def readyUP():
    
    LButton = driver.find_element(By.XPATH, LoginButton)
    LButton.click()

    time.sleep(4)

    GButton = driver.find_element(By.XPATH, googleLoginButton)
    GButton.click()

    time.sleep(5)

    gmail = driver.find_element(By.XPATH, googleEmail)
    gmail.send_keys(myEmail)

    time.sleep(1)

    nButton = driver.find_element(By.XPATH, nextButton)
    nButton.click()

    time.sleep(4)

    gpassword = driver.find_element(By.XPATH, googlePassword)
    gpassword.send_keys(password)

    time.sleep(1)

    pnButton = driver.find_element(By.XPATH, pNextButton)
    pnButton.click()

    time.sleep(5)

def chatBot():
    chat = input("What do you want your script to be about?\n")

    gpt = driver.find_element(By.XPATH, chatGPT)
    gpt.send_keys(chat)

    gpt.send_keys(Keys.ENTER)

    time.sleep(10)

    try:
        eAnswer = driver.find_element(By.XPATH, '//*[@id="__next"]/div[1]/div[2]/main/div[2]/div[1]/div/div/div/div[3]/div/div/div[2]/div[2]/div[1]/div')
    except:
        eAnswer = driver.find_element(By.XPATH, '//*[@id="__next"]/div[1]/div/main/div[1]/div[1]/div/div/div/div[3]/div/div/div[2]/div[2]/div[1]/div/div')
    gpt = driver.find_element(By.XPATH, chatGPT)
    gpt.send_keys("what is the main topic word of every sentence listed in the previous response? Do not explain, just write out the topic words seperated by a comma with spaces replaced by underscores and do not give a concluding sentence")

    time.sleep(2)

    gpt.send_keys(Keys.ENTER)
    gpt.send_keys(Keys.BACK_SPACE)
    gpt.send_keys(Keys.ENTER)

    time.sleep(10)

    try:
        topics = driver.find_element(By.XPATH, '//*[@id="__next"]/div[1]/div[2]/main/div[2]/div[1]/div/div/div/div[5]/div/div/div[2]/div[2]/div[1]/div')
    except:
        topics = driver.find_element(By.XPATH, '//*[@id="__next"]/div[1]/div/main/div[1]/div[1]/div/div/div/div[5]/div/div/div[2]/div[2]/div[1]/div/div')
    return eAnswer.text, topics.text
    

def main():
    readyUP()
    x, y = chatBot()
    return(x, y)


if __name__ == '__main__':
    main() 
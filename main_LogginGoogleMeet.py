from selenium import webdriver
from selenium.webdriver.common.by import By
import auto_send

import time

delay = 2

email = 'email-ul institutional'
username = 'username-ul contului institutional'
password = 'parola contului institutional'
link = 'link-ul meet-ului'
user_cameraAndMicrophone = False
sentMessage = "mesajul care va fi trimis"
targgets = ["trigger 1", "trigger 2", "..."]

email_var = ''.join(email)
username_var = ''.join(username)
password_var = ''.join(password)
link_var = ''.join(link)

#need ChromeDriver
driver = webdriver.Chrome()
#link for google loggin
driver.get('https://accounts.google.com/')

#TODO: Schimba XPATh cu ID

#login with google account
while True:
    try:
        email = driver.find_element(By.XPATH, '//*[@id="identifierId"]')
        email.send_keys(email_var)
        print('email - check')
        break
    except:
        print('Fail to input email...')

#press next button
while True:
    try:
        next = driver.find_element(By.XPATH, '//*[@id="identifierNext"]/div/button/span')
        if next.is_displayed():
            next.click()
            print('next button - check')
            break
    except:
        print('Fail to press button...')

#now we are on institutional login page TUIASI
while True:
    try:
        #trigger username input
        username = driver.find_element(By.XPATH, '//*[@id="username"]')
        username.send_keys(username_var)
        print('username tuiasi - check')
        #trigger password input
        password = driver.find_element(By.XPATH, '//*[@id="password"]')
        password.send_keys(password_var)
        print('password tuiasi - check')
        #pres login
        next = driver.find_element(By.XPATH, '//*[@id="kc-login"]')
        next.click()
        print('login button - check')
        break
    except:
        print('Wait for enter data of institutional account...')

#pres continue
while True:
    try:
        next = driver.find_element(By.XPATH, '//*[@id="view_container"]/div/div/div[2]/div/div[2]/div/div[1]/div/div/button/span')
        next.click()
        print('press continue button - check')
        break
    except:
        print('Wait for continue button...')

#link with the meet
time.sleep(delay)
driver.get(link_var)

#TODO: NECESITA OPTIMIZARI - FOLOSESTE O FUNCTIE PENTRU A RASFIRA CODUL

if user_cameraAndMicrophone:
    while True:
        try:
            with_mic_camera = driver.find_element(By.XPATH, '//*[@id="yDmH0d"]/div[3]/div[2]/div/div/div/div/div[2]/div/div[1]/button/span')
            with_mic_camera.click()
            print('continue without camera and microphone permissions - check')
            break
        except:
            print('Wait for continue without camera and microphone permissions or link is invalid...')
    #turn off camera
    while True:
        try:
            turnOff_camera = driver.find_element(By.XPATH, '/html/body/div[1]/c-wiz/div/div/div[19]/div[3]/div/div[2]/div[4]/div/div/div[1]/div[1]/div/div[7]/div[2]/div/div[1]/div[1]')
            turnOff_camera.click()
            print('turn off camera - check')
            break
        except:
            print('wait for turn off camera button...')

    #turn off microphone
    while True:
        try:
            turnOff_mic = driver.find_element(By.XPATH, '/html/body/div[1]/c-wiz/div/div/div[19]/div[3]/div/div[2]/div[4]/div/div/div[1]/div[1]/div/div[7]/div[1]/div/div/div[1]/div[1]')
            turnOff_mic.click()
            print('turn off microphone - check')
            break
        except:
            print('wait for turn off microphone...')
else:
    while True:
        try:
            without_mic_camera = driver.find_element(By.XPATH, '//*[@id="yDmH0d"]/div[3]/div[2]/div/div/div/div/div[2]/div/div[2]/button/span')
            without_mic_camera.click()
            print('continue without camera and microphone permissions - check')
            break
        except:
            print('Wait for continue without camera and microphone permissions or link is invalid...')

#join meet
while True:
    try:
        join = driver.find_element(By.XPATH, '//*[@id="yDmH0d"]/c-wiz/div/div/div[19]/div[3]/div/div[2]/div[4]/div/div/div[2]/div[1]/div[2]/div[1]/div[1]/button/span')
        join.click()
        print('join button - check')
        break
    except:
        print('Wait for join button...')

#search the trigger text for the present
repeat = 0
while repeat !=2:
    auto_send.autoSend_PresentMessage(driver, repeat, targgets, sentMessage)
    time.sleep(1500) #25 min
    repeat += 1

print('STOP PROGRAM')



time.sleep(100000000)

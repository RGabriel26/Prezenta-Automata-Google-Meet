from selenium.webdriver.common.by import By
import time

def autoSend_PresentMessage(driver, repeat, targgets, sentMessage):
    time.sleep(2)
    
    text = sentMessage
    text_forSent = ''.join(text)

    search_triggers = targgets
    
    #open meet chat
    try:
        open_meet = driver.find_element(By.XPATH, '//*[@id="ow3"]/div[1]/div/div[19]/div[3]/div[11]/div/div/div[3]/div/div[3]/div/div/span/button/i[1]')
        open_meet.click()
        print('open meet chat - check')
    except:
        print('Fail to open chat...')

    loop = True
    while loop:
        print('wait for trigger...')
        time.sleep(5)
        get_source = driver.page_source
        for trigger in search_triggers:
            count_trigger = get_source.count(trigger)
            if repeat == 0:
                if count_trigger == 1:
                    print(count_trigger)
                    loop = False
                    break
            elif repeat == 1:
                if count_trigger == 2:
                    print(count_trigger)
                    loop = False
                    break

    print('Trigger found!')

    #open meet chat
    try:
        open_meet = driver.find_element(By.XPATH, '//*[@id="ow3"]/div[1]/div/div[19]/div[3]/div[11]/div/div/div[3]/div/div[3]/div/div/span/button/i[1]')
        open_meet.click()
        print('open meet chat - check')
    except:
        print('Fail to open chat...')

    #trigger text zone
    time.sleep(1)
    while True:
        try:
            text_zone = driver.find_element(By.XPATH, '//*[@id="bfTqV"]')
            text_zone.send_keys(text_forSent)

            sentMessage = driver.find_element(By.XPATH, '//*[@id="ow3"]/div[1]/div/div[19]/div[3]/div[4]/div[2]/div/div[2]/div/div[2]/div[1]/span/button/i')
            sentMessage.click()
            break
        except:
            print('Error when sent message...')

    print('Message was sent!')
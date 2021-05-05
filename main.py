import time
import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import argparse
from settings import DRIVER_PATH, BASEMENT_URL, FIRST_FLOOR_URL, SECOND_FLOOR_URL, ERNIE_URL


def get_driver_path():
    if(DRIVER_PATH):
        return DRIVER_PATH
    else:
        raise Exception("You need to set the chrome driver path in the DRIVER_PATH environment variable.")

def get_floor_url(floor):
    if floor == 'basement':
        if(BASEMENT_URL):
            return BASEMENT_URL
        else:
            raise Exception("You need to set the basement floor url in the BASEMENT_URL environment variable.")
    elif floor == 'second':
        if(SECOND_FLOOR_URL):
            return SECOND_FLOOR_URL
        else:
            raise Exception("You need to set the second floor url in the SECOND_FLOOR_URL environment variable.")
    elif floor == 'first':
        if(FIRST_FLOOR_URL):
            return FIRST_FLOOR_URL
        else:
            raise Exception("You need to set the first floor url in the FIRST_FLOOR_URL environment variable.")
    elif floor == 'ernie':
        if(ERNIE_URL):
            return ERNIE_URL
        else:
            raise Exception("You need to set the first floor url in the ERNIE_URL environment variable.")
    else:
        raise Exception("{} is not a viable floor option.".format(floor))



def main(u, pw, floor, gym_time):
    t = datetime.datetime.now()
    print('[STARTING] Signing up for {} gym slot on {} at {}'.format(gym_time, t.strftime('%m:%d'), t.strftime('%H:%M')))

    options = webdriver.ChromeOptions()
    options.add_argument('headless') # comment out to toggle headless mode

    driver = webdriver.Chrome(get_driver_path(), options=options)
    driver.get(get_floor_url(floor))
    
    login(u, pw, driver)

    register(gym_time, driver)
    
    checkout(driver)

    print("[SUCCESS] Signed up for {} floor at {}".format(floor, gym_time))
    
    time.sleep(60)

def login(u, pw, driver):
    driver.find_element_by_xpath("//*[@id='loginLink']").click()

    WebDriverWait(driver, 1).until(
        EC.element_to_be_clickable((By.XPATH, "//*[@id='divLoginOptions']/div[2]/div[2]/div/button"))
    ).click()

    WebDriverWait(driver, 2).until(
        EC.element_to_be_clickable((By.ID, 'username'))
    ).send_keys(u)

    driver.find_element_by_id('password').send_keys(pw)

    driver.find_element_by_css_selector('button.form-element.form-button').click()

def register(gym_time, driver):
    # Converts from military time and removes any leading '0's
    if (gym_time[0] == '0'):
        gym_time = gym_time[1:]
    elif (int(gym_time[:2]) > 12):
        gym_time = str(int(gym_time[:2]) - 12) + gym_time[2:]

    try:
        # Selects gym slot register button with corresponding time
        WebDriverWait(driver, 1).until(
            EC.element_to_be_clickable((By.XPATH, "//*[@id='mainContent']/div[2]/section/div/div/div/div[1]/small[contains(text(), '{}')]/../../div[2]/button".format(gym_time)))
        ).click()
    except:
        raise Exception('The gym time slot {} is unavailable.'.format(gym_time))

def checkout(driver):
    try:
        WebDriverWait(driver, 1).until(
            EC.element_to_be_clickable((By.XPATH, "//*[@id='btnAccept']"))
        ).click()
    except:
        print('Failed to click accept button on first attempt')
        time.sleep(1)
        WebDriverWait(driver, 1).until(
            EC.element_to_be_clickable((By.XPATH, "//*[@id='btnAccept']"))
        ).click()

    WebDriverWait(driver, 60).until(
            EC.element_to_be_clickable((By.XPATH, "//*[@id='checkoutButton']"))
        ).click()
    
    WebDriverWait(driver, 1).until(
        EC.element_to_be_clickable((By.XPATH, "//*[@id='CheckoutModal']/div/div[2]/button[2]"))
    ).click()

if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument('u', type=str, help='Username')
    parser.add_argument('pw', type=str, help='Password')
    parser.add_argument('floor', type=str, help='Select the gym floor you want')
    parser.add_argument('time',  type=str, help='Select the gym time you want')

    args = parser.parse_args()

    main(args.u, args.pw, args.floor, args.time)




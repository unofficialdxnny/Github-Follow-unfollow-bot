from codecs import ignore_errors
import time
import sys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from pystyle import *
import os
import json
import keyboard as kb




banner = '''

        unofficial GitHub CLI                                                  
  _____   _  _    _     _         _           ___    _       _______ 
 (_____) (_)(_)_ (_)   (_)       (_)        _(___)_ (_)     (_______)
(_)  ___  _ (___)(_)___(_) _   _ (_)_      (_)   (_)(_)        (_)   
(_) (___)(_)(_)  (_______)(_) (_)(___)_    (_)    _ (_)        (_)   
(_)___(_)(_)(_)_ (_)   (_)(_)_(_)(_)_(_)   (_)___(_)(_)____  __(_)__ 
 (_____) (_) (__)(_)   (_) (___) (____)      (___)  (______)(_______)
                                                                     
                                  By unofficialdxnny                                   

                          

'''

os.system('cls')
Write.Print(f"{banner}", Colors.red_to_white, interval=0)


f = open(f'config.json')
data = json.load(f)



            
            


while True:
    try:
        main_input = Write.Input(">>> ", Colors.red_to_white, interval=0).lower()
        split = main_input.split()

        if split[0] == 'github' and split[1] == 'help':
            Write.Print(f"Command : Effect", Colors.red_to_white, interval=0)
            print('')
            Write.Print(f"github : Reveals commands available.", Colors.red_to_white, interval=0)
            print('')
            Write.Print(f"github follow <your_username> <your_password> <usename_to_follow_its_followers : Follows followers of the user.", Colors.red_to_white, interval=0)
            print('')


        elif split[0] == 'github' and split[1] == 'follow':

            ## login to github
            # Initializing the headless chrome
            driver = webdriver.Chrome()
            driver.get("https://github.com/login")
            wait = WebDriverWait(driver, 10)

            # Locating username and password field
            username = wait.until(EC.presence_of_element_located((By.ID, "login_field")))
            password = wait.until(EC.presence_of_element_located((By.ID, "password")))

            # password and username need to go into these values
            username.send_keys(data['username'])
            password.send_keys(data['password'])
            login_form = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@value='Sign in']")))
            login_form.click()
            
            # Clicking the sign in button
            login_form = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@value='Sign in']")))
            login_form.click()
            
            # Go to the followers tab
            prepend = [f"{split[4]}"]
            
            for user in prepend:
                for t in range(1, 50):
                    string = "https://github.com/{}?page={}&tab=followers".format(user, t)
                    driver.get(string)
                    time.sleep(1)
            
                    follow_button = driver.find_elements_by_xpath("//input[@value='Follow']")
            
                    try:
                        for i in follow_button:
                            i.submit()
                    except:
                        pass
                    time.sleep(1)
            
            list_end = driver.find_element(By.CLASS_NAME, "mt-4")
            
            if  list_end:
                os.system('cls')
                Write.Print(f"{banner}", Colors.red_to_white, interval=0)                
                driver.close()
        
        elif split[0] == 'github' and split[1] == 'unfollow':
            ## login to github
            # Initializing the headless chrome
            driver = webdriver.Chrome()
            driver.get("https://github.com/login")
            wait = WebDriverWait(driver, 10)

            # Locating username and password field
            username = wait.until(EC.presence_of_element_located((By.ID, "login_field")))
            password = wait.until(EC.presence_of_element_located((By.ID, "password")))

            # password and username need to go into these values
            username.send_keys(data["username"])
            password.send_keys(data["password"])
            sleep(2)
            # Clicking the sign in button
            login_form = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@value='Sign in']")))
            login_form.click()

            prepend = [data["username"]]


            for user in prepend:
                for i in range(0, 100):
                    for t in range(1, 100):
                        string = "https://github.com/{}?tab=following&page={}".format(user, t)
                        driver.get(string)
                        time.sleep(1)

                        follow_button = driver.find_elements_by_xpath("//input[@value='Unfollow']")

                        # time.sleep(1)
                        # print len(follow_button)
                        try:
                            for i in follow_button:
                                i.submit()
                        except:
                            pass
                        time.sleep(1)

        

            driver.close()

            time.sleep(3)

            time.sleep(3)

            driver.close()

      

    except KeyboardInterrupt:
        os.system('cls')
        Write.Print(f"{banner}", Colors.red_to_white, interval=0)
    
    except IndexError:
        print('')
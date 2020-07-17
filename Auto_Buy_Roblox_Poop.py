from selenium import webdriver
import pyfiglet
import time
from selenium.webdriver.edge.options import Options
from selenium.webdriver.support import ui
from selenium.webdriver.common.action_chains import ActionChains
from multiprocessing import Queue
from selenium.webdriver.common.keys import Keys # import special key
import sys
from datetime import datetime
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver import DesiredCapabilities

#intro = pyfiglet.figlet_format("AUTO BUY ROBLOX POOP",font = "slant") 
#print(intro) 
print("    ___   __  ____________     ____  __  ____  __")
print("   /   | / / / /_  __/ __ \   / __ )/ / / /\ \/ /")
print("  / /| |/ / / / / / / / / /  / __  / / / /  \  /")
print(" / ___ / /_/ / / / / /_/ /  / /_/ / /_/ /   / /")
print("/_/  |_\____/ /_/  \____/  /_____/\____/   /_/")
print("")
print("    ____  ____  ____  __    ____ _  __    ____  ____  ____  ____")
print("   / __ \/ __ \/ __ )/ /   / __ \ |/ /   / __ \/ __ \/ __ \/ __ \ ")
print("  / /_/ / / / / __  / /   / / / /   /   / /_/ / / / / / / / /_/ /")
print(" / _, _/ /_/ / /_/ / /___/ /_/ /   |   / ____/ /_/ / /_/ / ____/")
print("/_/ |_|\____/_____/_____/\____/_/|_|  /_/    \____/\____/_/")
print("")
print("")

time.sleep(1)
print("Yo, this program was made by Alan.")
time.sleep(1)

print("This program auto buys Roblox Items under or equal to a certin amount of robux.")
time.sleep(1)

choice = 'a'

while choice!='y' and choice!='n':
    choice = input("Do you want to run it in the background? (y/n): ")


robuxInfo = "robuxInfo.txt"

saved = False
maxItemRobux = 200
maxRobux = 1000
choice2 = "30"

try:
    infoFile  = open(robuxInfo, 'r')
    maxItemRobux = int(infoFile.readline().replace("\n",''))
    maxRobux = int(infoFile.readline().replace("\n",''))
    choice2 = infoFile.readline()
    saved = True
    infoFile.close()

    if maxItemRobux == "":
        maxItemRobux = 200
        maxRobux = 1000
        choice2 = "30"
except:
    saved = False
    maxItemRobux = 200
    maxRobux = 1000
    choice2 = "30"

#choices
choice3 = 'a'
while choice3!='y' and choice3!='n':
    choice3 = input("Is this correct? -> equal or under " + str(maxItemRobux) + " robux per item, maximum of "+ str(maxRobux) + " robux, and " + choice2 + "% discout (y/n): ")

if (choice3 == 'n'):
    maxItemRobux = int(input(' ' * 5 + "Enter the maximum amount of robux for each item(200): "))
    maxRobux = int(input(' ' * 5 + "Enter the maximum amount of robux you want to spend(1000): "))

    choice2 = 'a'
    while choice2!='10' and choice2!='20' and choice2!='30' and choice2!='40' and choice2!='50' :
        choice2 = input(' ' * 5 + "Amount of Discount % (10, 20, 30, 40, or 50): ")

if saved == False or choice3 == 'n':
    file = open(robuxInfo,'w')
    file.write(str(maxItemRobux) + "\n") 
    file.write(str(maxRobux)+ "\n")
    file.write(choice2)
    file.close() 


time.sleep(2)
print(" ")

#getting login info
loginInfo = "loginInfo.txt"
robloxUsername = "Null"
robloxPassword = "Null"
#COOKIE
cookie = "Null"

#Log
logFile = "log.txt"

def saveToLog(info):
    try:
        log = open(logFile, 'a+')    
        log.write(info+"\n")
        log.close()
    except:
        print("Log file couldn't be opened")


try:
    file  = open(loginInfo, 'r')
    robloxUsername = (file.readline()).replace("\n",'')
    robloxPassword = (file.readline()).replace("\n",'')
    cookie = (file.readline()).replace("\n",'')
    print("Roblox Username: " + robloxUsername)
    print("Roblox Password: " + robloxPassword)
    print("Cookie: " + cookie)
    file.close()
    if robloxUsername == "" or robloxPassword == "" or cookie== "":
        print(" ")
        print("Items are empty, please enter again")
        robloxUsername = input("Roblox Username (auto save): ")
        robloxPassword = input("Roblox Password (auto save): ")
        cookie = input("Roblox Cookie (value): ")

        file = open(loginInfo,'w')
        file.write(robloxUsername + "\n") 
        file.write(robloxPassword + "\n")
        file.write(cookie)
        file.close() 
        print("saved")
except:
    robloxUsername = input("Roblox Username (auto save): ")
    robloxPassword = input("Roblox Password (auto save): ")
    cookie = input("Roblox Cookie (value): ")

    file = open(loginInfo,'w')
    file.write(robloxUsername + "\n") 
    file.write(robloxPassword + "\n")
    file.write(cookie)
    file.close() 
    print("saved")

print(" ")

#getting chrome driver
driverPathFile = "driverPathInfo.txt"
chromedriver = ""

try:
    file  = open(driverPathFile, 'r')
    chromedriver = file.readline()
    print("Using chrome driver from " + chromedriver)
    file.close()

    if chromedriver == "":
        chromedriver = input("Chrome Driver Path (Auto Save): ")
        file = open(driverPathFile,'w')
        file.write(chromedriver) 
        file.close() 
        print("saved")
except:
    chromedriver = input("Chrome Driver Path (Auto Save): ")
    file = open(driverPathFile,'w')
    file.write(chromedriver) 
    file.close() 
    print("saved")

print(" ")

options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors-spki-list')
options.add_argument('--ignore-ssl-errors')
options.add_argument('--ignore-certificate-errors')
options.add_argument('log-level=3')

capabilities = DesiredCapabilities.CHROME.copy()
capabilities['acceptSslCerts'] = True 
capabilities['acceptInsecureCerts'] = True

prefs = {"profile.managed_default_content_settings.images": 2}
options.add_experimental_option("prefs", prefs)
print("(images removed to make websites load faster)")

if choice == 'y':
    options.add_argument("headless")
    options.add_argument("window-size=1920,1080")

itemsBought = 0
robuxSpent = 0

#open chrome



try: 
    browser = webdriver.Chrome(executable_path=chromedriver,options=options,desired_capabilities=capabilities)
except:
    print("Couldn't use the chrome driver, please check if the syntax and version is correct! example -> (C:\\Users\\alany\\Downloads\\Python Stuff\\chromedriver.exe)")

browser.get("https://www.rolimons.com/deals")

print("Starting... ")
    
time.sleep(1)
try:
    element = browser.find_element_by_id("filter-category-dropdown")
except:
    print("Bad Wi-Fi, reconnecting...")
    time.sleep(2)
    element = browser.find_element_by_id("filter-category-dropdown")

element.click()

time.sleep(1)

# discount amount
if (choice2 == "10"):
    element= browser.find_element_by_xpath("/html/body/div[8]/div/div[2]/div[1]/a[1]")
if (choice2 == "20"):
    element= browser.find_element_by_xpath("/html/body/div[8]/div/div[2]/div[1]/a[2]")
if (choice2 == "30"):
    element = browser.find_element_by_xpath("/html/body/div[8]/div/div[2]/div[1]/a[3]")
if (choice2 == "40"):
    element= browser.find_element_by_xpath("/html/body/div[8]/div/div[2]/div[1]/a[4]")
if (choice2 == "50"):
    element= browser.find_element_by_xpath("/html/body/div[8]/div/div[2]/div[1]/a[5]")

    
    
try:        
     element.click()
except:
     print("Bad Wi-Fi, reconnecting...")
     time.sleep(10)
     element = browser.find_element_by_id("filter-category-dropdown")
     element.click()
     time.sleep(5)

     if (choice2 == "10"):
        element= browser.find_element_by_xpath("/html/body/div[8]/div/div[2]/div[1]/a[1]")
     if (choice2 == "20"):
        element= browser.find_element_by_xpath("/html/body/div[8]/div/div[2]/div[1]/a[2]")
     if (choice2 == "30"):
         element = browser.find_element_by_xpath("/html/body/div[8]/div/div[2]/div[1]/a[3]")
     if (choice2 == "40"):
         element= browser.find_element_by_xpath("/html/body/div[8]/div/div[2]/div[1]/a[4]")
     if (choice2 == "50"):
         element= browser.find_element_by_xpath("/html/body/div[8]/div/div[2]/div[1]/a[5]")

     element.click()
     time.sleep(2)

time.sleep(2)

boughtItems = []

tryCount = 0
cookieLoaded = False
main_window = browser.current_window_handle
while (True):
    
    tryCount+=1
    print(" ")
    print(' ' *14 + '#'+ str(tryCount))
    print("_" * 30)
    theTime = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    print(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))

    #get items
    n = 0   
    print(" ")
    while (True):
            print(" ")
            n+=1
            try: 
                
                print(' ' * 5 + browser.find_element_by_xpath("/html/body/div[9]/div/div[" + str(n) + "]/a/div/div[1]/p").text)
                print(' ' * 7 + browser.find_element_by_xpath("/html/body/div[9]/div/div[" + str(n) + "]/a/div/div[3]/div[1]/div[2]").text + " Robux")
                print(' ' * 7 + browser.find_element_by_xpath("/html/body/div[9]/div/div[" + str(n) + "]/a/div/div[3]/div[2]/div[2]").text + " RAP")
                rap = browser.find_element_by_xpath("/html/body/div[9]/div/div[" + str(n) + "]/a/div/div[3]/div[2]/div[2]").text + " RAP"

                if (browser.find_element_by_xpath("/html/body/div[9]/div/div[" + str(n) + "]/a/div/div[3]/div[3]/div[1]").text == "Value"):
                    hasV = True
                    value = browser.find_element_by_xpath("/html/body/div[9]/div/div[" + str(n) + "]/a/div/div[3]/div[3]/div[2]").text
                    print(' ' * 7 + browser.find_element_by_xpath("/html/body/div[9]/div/div[" + str(n) + "]/a/div/div[3]/div[3]/div[2]").text + " Value")

                    sale = browser.find_element_by_xpath("/html/body/div[9]/div/div[" + str(n) + "]/a/div/div[3]/div[4]/div[2]").text
                    print(' ' * 7 + browser.find_element_by_xpath("/html/body/div[9]/div/div[" + str(n) + "]/a/div/div[3]/div[4]/div[2]").text + " off")
                else:
                    hasV = False
                    print(' ' * 7 + browser.find_element_by_xpath("/html/body/div[9]/div/div[" + str(n) + "]/a/div/div[3]/div[3]/div[2]").text + " off")
                    sale = browser.find_element_by_xpath("/html/body/div[9]/div/div[" + str(n) + "]/a/div/div[3]/div[3]/div[2]").text

                price = int((browser.find_element_by_xpath("/html/body/div[9]/div/div[" + str(n) + "]/a/div/div[3]/div[1]/div[2]").text).replace(',',''))
               
           
                if (price > maxItemRobux or price+robuxSpent>maxRobux):
                    print(' ' * 5 + "THIS ITEM IS TOO EXPENSIVE")
               
                else:
                    print("Buying....")


                    itemName = browser.find_element_by_xpath("/html/body/div[9]/div/div[" + str(n) + "]/a/div/div[1]/p").text
                    
                    if (itemName in boughtItems): 
                        print("Already bought!")
                        browser.close()
                        browser.switch_to.window(main_window)
                        continue
                    else:
                        link = browser.find_element_by_xpath("/html/body/div[9]/div/div[" + str(n) + "]/a").get_attribute('href')
                        browser.execute_script("window.open('');")
                        time.sleep(1)
                        browser.switch_to.window(browser.window_handles[1])
                        browser.get(link)

                        
                        if not cookieLoaded:
                            print("Loading Roblox Cookie...")
                            #load Roblox Cookie
                            try:
                                rbcookie = {'name':'.ROBLOSECURITY', 'value':cookie}
                                browser.add_cookie(rbcookie)
                                browser.get(link)    
                                print("Roblox Cookie Loaded")
                                cookieLoaded = True
                            except:
                                cookieLoaded = False
                                print("Cookie failed. (expired?)")

                                print("(Mannually) logging in to " + robloxUsername)
                                #login
                                browser.switch_to.window(browser.window_handles[1])
                                print(browser.title)
                                element = browser.find_element_by_xpath("/html/body/div[5]/div[2]/div/div[3]/ul/li[2]/a")
                                element.click()
                              
                                time.sleep(1)

                                element = browser.find_element_by_id("login-username")
                                element.send_keys(robloxUsername)
                    

                                element = browser.find_element_by_id("login-password")
                                element.send_keys(robloxPassword)
                                element.send_keys(Keys.ENTER)

                                time.sleep(5)

                                print("logged in to " + robloxUsername)

                        try:
                            time.sleep(2)

                            money = (browser.find_element_by_id("nav-robux-amount").text).replace(',','')
                            theUsername = (browser.find_element_by_xpath("/html/body/div[6]/div[1]/div/div[3]/div/span").text).replace(':','')

                            if money == "" or theUsername == "":
                                print("Things not found, retrying...")
                                time.sleep(5)
                                money = (browser.find_element_by_id("nav-robux-amount").text).replace(',','')
                                theUsername = browser.find_element_by_xpath("/html/body/div[6]/div[1]/div/div[3]/div/span").text

                                if money == "" or theUsername == "":
                                    print("THIS POOP STILL NOT FOUND, retrying...")
                                    time.sleep(10)
                                    money = (browser.find_element_by_id("nav-robux-amount").text).replace(',','')
                                    theUsername = browser.find_element_by_xpath("/html/body/div[6]/div[1]/div/div[3]/div/span").text


                            element = browser.find_element_by_class_name("action-button")
                            element.click()
                            time.sleep(1)
                            element = browser.find_element_by_id("confirm-btn")
                            element.click()
                        except:
                            try:
                                print("failed retying... (are you logged in?)")
                                time.sleep(2)
                                element = browser.find_element_by_class_name("action-button")
                                element.click()
                                time.sleep(1)
                                element = browser.find_element_by_id("confirm-btn")
                                element.click()
                            except:
                                cookieLoaded = False
                                print("failed again, cookie may have expired or been entered wrong, please check again, quitting...")
                                browser.close()
                                browser.switch_to.window(main_window)
                                break

                        time.sleep(4)

                        if (int(money)<maxRobux):
                            print("Money is less than max robux, changing max robux to money.....  <"+10*'-'+"VALUE CHANGE")
                            maxRobux=int(money)
                            
                        try:
                            #SAVE STUFF TO LOG
                            saveToLog('_'*30)
                            saveToLog(" ")
                            saveToLog("Attempt" + ' ' *7 + '#'+ str(tryCount))
                            saveToLog('_'*30)
                            saveToLog(' ' * 7+theTime)
                            saveToLog(' ' * 7+"ITEM URL " + link)
                            saveToLog(" ")
                            saveToLog(' ' * 7+"BOUGHT BY: " + theUsername)
                            saveToLog(" ")
                            saveToLog(' ' * 9 + itemName)
                            saveToLog(' ' * 7+"PRICE: "+str(price)+" Robux")
                            saveToLog(' ' * 7+"RAP: " + rap)
                            if hasV:
                                saveToLog(' ' * 7+"VALUE: "+value)
                            saveToLog(' ' * 7+"SALE: "+sale+" off")

                            moneyLeft = int(money) - price
                        except:      
                            print("LOG ERROR")

                        try:   
                            if (browser.find_element_by_xpath("/html/body/div[6]/div[4]/div[2]/div[2]/div[2]/div[1]/div/span[2]").txt == "Item Owned"):
                                print(itemName+" BOUGHT SUCCESSFULLY!!!")
                                print("  -" + str(price) + " robux")
                                saveToLog(' ' * 7+"OUTCOME: BOUGHT SUCCESSFULLY!!!")

                                moneyLeft = int(money) - price
                                
                                print(money + " - " + str(price) + " = " + str(moneyLeft) + " robux in account left")
                                saveToLog(money + " - " + str(price) + " = " + str(moneyLeft) + " robux in account left")

                                itemsBought+=1
                                robuxSpent+=price
                                boughtItems.append(itemName)
                                browser.close()
                                browser.switch_to.window(main_window)
                        except:
                            print("not successful.... (do you have enough robux?)")
                            saveToLog(' ' * 7+"OUTCOME: not successful.... (do you have enough robux?)")
                            saveToLog(money + " robux left in account")
                            saveToLog(" ")
                            print(money + " robux left in account")
                            browser.close()
                            browser.switch_to.window(main_window)
               
               
            except:
                break
            
    print(" ")
    if n == 0:
        print("No Items found!")
    else:
        print("found " + str(n-1) + " items!")

    print(" ")
    print(str(robuxSpent) + "/" + str(maxRobux) + " robux spent")
    print(str(itemsBought) + " items bought")
    print("_" * 30)

    try:
        if (browser.find_element_by_id("timeout_dialog").is_displayed()):
            print("refresh pop up, refreshing....")
            browser.get("https://www.rolimons.com/deals")
            time.sleep(1)
    except:
        browser.get("https://www.rolimons.com/deals")

    time.sleep(1)







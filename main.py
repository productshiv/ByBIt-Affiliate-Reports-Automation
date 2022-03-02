from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.action_chains import ActionChains
import shutil
import os

#data
logid = "id"
passwd = "pass"
waitingTime = 3
source_dir = 'H:\\WorkSpace\\Projects\\ByBit Comissions Automation\\Magic\\TMP'
visitedPairs = []

#driver
options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
prefs = {'download.default_directory' : source_dir}
options.add_experimental_option('prefs', prefs)
driver = webdriver.Chrome(options=options)


#openUrl
url = "https://affiliates.bybit.com/v2/affiliate-portal/login"
driver.get(url)


#logs the user in
def login():
    element = driver.find_element_by_id("login_email")
    element.send_keys(logid)

    element = driver.find_element_by_id("login_password")
    element.send_keys(passwd)

    # wait("Press enter after solving captch : ")
    l=driver.find_element_by_xpath("""//*[@id="login"]/div[3]/div/div/div/button""")
    l.click()
    input("solve the damn captcha if it comes : ")
    driver.get("https://affiliates.bybit.com/v2/affiliate-portal/commissions/spot")

def goToNextPairDown():
    actions = ActionChains(driver)
    l=driver.find_element_by_xpath("""//*[@id="commissions-header"]/div[2]/div[1]/div[2]/div/div/div/div""")
    l.click()
    actions.send_keys(Keys.ARROW_DOWN)
    actions.send_keys(Keys.ENTER)
    actions.perform()

def goToNextPairUp():
    actions = ActionChains(driver)
    l=driver.find_element_by_xpath("""//*[@id="commissions-header"]/div[2]/div[1]/div[2]/div/div/div/div""")
    l.click()
    actions.send_keys(Keys.ARROW_UP)
    actions.send_keys(Keys.ENTER)
    actions.perform()

def getPairName():
    l=driver.find_element_by_xpath("""//*[@id="commissions-header"]/div[2]/div[1]/div[2]/div/div/div/div/span[2]""")
    return(l.text)

def changeDates():
    l=driver.find_element_by_xpath("""//*[@id="commissions-header"]/div[2]/div[3]/div[2]/div/div/div/div[1]/input""")
    l.send_keys(Keys.CONTROL,'a')
    l.send_keys('2021-01-01')
    l=driver.find_element_by_xpath("""//*[@id="commissions-header"]/div[2]/div[3]/div[2]/div/div/div/div[3]/input""")
    l.send_keys(Keys.CONTROL,'a')
    l.send_keys('2021-12-31')
    actions = ActionChains(driver)
    actions.send_keys(Keys.ENTER)
    actions.perform()
    l=driver.find_element_by_xpath("""//*[@id="commissions-header"]/div[2]/div[1]/div[2]/div/div/div/div""")
    l.click()
    l.click()

def export():
    l=driver.find_element_by_xpath("""//*[@id="commissions-header"]/div[2]/button""")
    l.click()

def createFolderForPair(pair):
    root_path = "H:\\WorkSpace\\Projects\\ByBit Comissions Automation\\Magic\\"
    try:
        os.mkdir(os.path.join(root_path,pair))
    except:
        pass
    target_dir = root_path + pair
    return(target_dir)

def moveToDestiny(target_dir):
    file_names = os.listdir(source_dir)
    for file_name in file_names:
        shutil.move(os.path.join(source_dir, file_name), target_dir)

login()
pairName = "easy"
while pairName not in visitedPairs:
    visitedPairs.append(pairName)
    changeDates()
    export()
    time.sleep(waitingTime)
    pairName = getPairName()
    target_dir = createFolderForPair(pairName)
    moveToDestiny(target_dir)
    goToNextPairDown()
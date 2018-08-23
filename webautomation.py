import pyautogui
import os
import time
import sys

# PyAutoGUI Failsafe Settings:
pyautogui.FAIL_SAFE = True
pyautogui.PAUSE = 1

def openfirefox():
    #Open Firefox from OS
    os.system('START "" Firefox')
    time.sleep(3)

def findonscreen(imgpath,time):
    find = pyautogui.locateOnScreen(imgpath,time,grayscale=False)
    findx,findy = pyautogui.center(find)
    return findx,findy

def setupproxy(proxyip,portno):
    # Find Settings:
    settingsfindx,settingsfindy = findonscreen('C:/SEO_AUTOMATION/settings.png',10)
    pyautogui.click(settingsfindx,settingsfindy)
    # Find Options:
    optionsfindx,optionsfindy = findonscreen('C:/SEO_AUTOMATION/options.png',10)
    pyautogui.click(optionsfindx,optionsfindy)
    # Find Search:
    searchfindx,searchfindy = findonscreen('C:/SEO_AUTOMATION/findinoptions.png',10)
    pyautogui.click(searchfindx,searchfindy)
    # Type Network in Search:
    pyautogui.typewrite('Network',0.2)
    # Find Network Settings:
    networkfindx,networkfindy = findonscreen('C:/SEO_AUTOMATION/networksettings.png',10)
    pyautogui.click(networkfindx,networkfindy)
    # Find Manual Proxy Config:
    mproxyfindx,mproxyfindy = findonscreen('C:/SEO_AUTOMATION/manualproxyconfig.png',10)
    pyautogui.click(mproxyfindx,mproxyfindy)
    time.sleep(2)
    pyautogui.press('tab')
    pyautogui.typewrite(proxyip,0.2)
    time.sleep(2)
    pyautogui.press('tab')
    pyautogui.typewrite(portno,0.2)
    time.sleep(2)
    pyautogui.press('tab')
    pyautogui.press('space')
    # Find Final_OK:
    finalokfindx,finalokfindy = findonscreen('C:/SEO_AUTOMATION/finalok.png',10)
    pyautogui.click(finalokfindx,finalokfindy)
    print("--->New Proxy Set! Now moving on further procedure!")

def addnewtab():
    tabbuttonx,tabbuttony = findonscreen('C:/SEO_AUTOMATION/newtab.png',10)
    pyautogui.click(tabbuttonx,tabbuttony)
    print("--->New Tab Opened!")

def opengoogle():
    addressbarx,addressbary = findonscreen('C:/SEO_AUTOMATION/addressbar.png',10)
    pyautogui.click(addressbarx,addressbary)
    pyautogui.typewrite('http://google.com',0.2)
    pyautogui.press('enter')
    time.sleep(10)

def getsearchgoingon():
    print("\n4] Browser Work Started!!")
    pyautogui.typewrite('IP',0.2)
    pyautogui.press('enter')
    # gsearchx,gsearchy = findonscreen('C:/SEO_AUTOMATION/gsearch.png',10)
    # pyautogui.click(gsearchx,gsearchy)

def settingscleanup():
    # Opening Settings:
    cleanupsettingsx,cleanupsettingsy = findonscreen('C:/SEO_AUTOMATION/settings.png',10)
    pyautogui.click(cleanupsettingsx,cleanupsettingsy)
    # Opening Options:
    cleanupoptionsx,cleanupoptionsy = findonscreen('C:/SEO_AUTOMATION/options.png',10)
    pyautogui.click(cleanupoptionsx,cleanupoptionsy)
    # Opening Find:
    cleanupsearchx,cleanupsearchy = findonscreen('C:/SEO_AUTOMATION/findinoptions.png',10)
    pyautogui.click(cleanupsearchx,cleanupsearchy)
    pyautogui.typewrite('Network',0.2)
    time.sleep(1)
    # Open Network Settings:
    cleanupnetworkfindx,cleanupnetworkfindy = findonscreen('C:/SEO_AUTOMATION/networksettings.png',10)
    pyautogui.click(cleanupnetworkfindx,cleanupnetworkfindy)
    # Finding the Protocol:
    cleanupprotocolx,cleanupprotocoly = findonscreen('C:/SEO_AUTOMATION/cleanupprotocol.png',10)
    pyautogui.click(cleanupprotocolx,cleanupprotocoly)
    # Clearing up the HTTP Proxy IP:
    cleanuphttpproxyx,cleanuphttpproxyy = findonscreen('C:/SEO_AUTOMATION/cleanuphttpproxy.png',10)
    pyautogui.click(cleanuphttpproxyx,cleanuphttpproxyy)
    for i in range(0,16):
        pyautogui.press('backspace')
    print("--->Proxy IP Cleared!")
    time.sleep(2)
    pyautogui.press('tab')
    pyautogui.press('delete')
    print("--->Port Cleared!")
    # Set No Proxy:
    cleanupnomproxyx,cleanupnomproxyy = findonscreen('C:/SEO_AUTOMATION/cleanupnoproxy.png',10)
    pyautogui.click(cleanupnomproxyx,cleanupnomproxyy)
    # Final OK:
    cleanupfinalokx,cleanupfinaloky = findonscreen('C:/SEO_AUTOMATION/finalok.png',10)
    pyautogui.click(cleanupfinalokx,cleanupfinaloky)
    print("--->Clean Up Done!")
    
if __name__ == '__main__':
    print("\n1] Opening a new Firefox Instance!")
    openfirefox()
    browserExe = "Firefox.exe"

    time.sleep(1)
    try:
        print("\n2] Checking if previosuly Proxy is already set!")
        settingscleanup()
        # os.system("taskkill /f /im "+browserExe)
    except Exception as e:
        print(e)
    finally:
        print("\n3] Setting up new Proxy!!")
        setupproxy('45.57.202.78','3129')
        time.sleep(1)
        addnewtab()
        time.sleep(1)
        opengoogle()
        time.sleep(1)
        getsearchgoingon()
        time.sleep(5)
        pyautogui.hotkey('ctrl','w')
        print("\n5] Process Completed!")
        time.sleep(2)
        print("\n6] Closing all Firefox Instances!!")
        os.system("taskkill /f /im "+browserExe)

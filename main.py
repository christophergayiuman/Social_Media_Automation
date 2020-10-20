from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from tkinter import *
global user_answer
user_answer = int(0)


def auto_facebook():
    # Facebook login
    website_facebook = 'https://www.facebook.com/login/'
    driver.get(website_facebook)
    input_username = driver.find_element_by_xpath('//*[@id="email"]')
    input_username.send_keys("username")
    input_password = driver.find_element_by_xpath('//*[@id="pass"]')
    time.sleep(1)
    input_password.send_keys('password', Keys.RETURN)


def auto_twitter():
    # Twitter Login
    website_twitter = 'https://twitter.com/login'
    driver.get(website_twitter)
    input_username = driver.find_element_by_xpath(
        '//*[@id="react-root"]/div/div/div[2]/main/div/div/div[1]/form/div/div[1]/label/div/div[2]/div/input')
    input_username.send_keys('username')
    input_password = driver.find_element_by_xpath(
        '//*[@id="react-root"]/div/div/div[2]/main/div/div/div[1]/form/div/div[2]/label/div/div[2]/div/input')
    time.sleep(1)
    input_password.send_keys('password', Keys.RETURN)


def auto_reddit():
    website_reddit = 'https://www.reddit.com/login/'
    driver.get(website_reddit)
    input_username = driver.find_element_by_xpath('//*[@id="loginUsername"]')
    input_username.send_keys('username')
    input_password = driver.find_element_by_xpath('//*[@id="loginPassword"]')
    time.sleep(1)
    input_password.send_keys('password', Keys.RETURN)


def facebook_clicked():
    print('facebook clicked!')
    global user_answer
    user_answer = 1
    root.quit()
    return user_answer


def twitter_clicked():
    print('twitter clicked')
    global user_answer
    user_answer = 2
    root.quit()
    return user_answer


def reddit_clicked():
    print('reddit clicked')
    global user_answer
    user_answer = 3
    root.quit()
    return user_answer


def quit_clicked():
    print('quit application')
    root.quit()
    return user_answer


# Setting up the GUI
root = Tk()
root.geometry('400x200')
root.title('Social Media')
topFrame = Frame(root)
topFrame.pack()
bottomFrame = Frame(root)
bottomFrame.pack(side=BOTTOM)

button1 = Button(topFrame, text="Facebook", fg="purple", command=facebook_clicked)
button2 = Button(topFrame, text="Twitter", fg="blue", command=twitter_clicked)
button3 = Button(topFrame, text="Reddit", fg="red", command=reddit_clicked)
button4 = Button(bottomFrame, text="Quit Application", fg="green", command=quit_clicked)

button1.pack(side=LEFT)
button2.pack(side=LEFT)
button3.pack(side=LEFT)
button4.pack(side=BOTTOM)
root.mainloop()
PATH = 'C:\Program Files (x86)\chromedriver.exe'
driver = webdriver.Chrome(PATH)

print(user_answer)
root.quit
if user_answer == int(1):
    auto_facebook()
if user_answer == int(2):
    auto_twitter()
if user_answer == int(3):
    auto_reddit()

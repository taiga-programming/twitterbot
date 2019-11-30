from selenium import webdriver
from selenium.webdriver.common.keys import Keys 
import time 

class TwitterBot:

  def __init__(self, username, password, moji):
     self.username = username
     self.password = password
     self.moji = moji
     self.bot = webdriver.Firefox()

  def login(self):
    bot =self.bot
    bot.get('https://twitter.com/login')
    time.sleep(3)

    email = bot.find_element_by_xpath('/html/body/div[1]/div[2]/div/div/div[1]/form/fieldset/div[1]/input')
    password = bot.find_element_by_xpath('/html/body/div[1]/div[2]/div/div/div[1]/form/fieldset/div[2]/input')
    password.clear()
    email.send_keys(self.username)
    password.send_keys(self.password)
    password.send_keys(Keys.RETURN)
    time.sleep(3)


       
  def todo_tweet(self):
     bot = self.bot
     bot.get('https://twitter.com/compose/tweet')
     bot.get('https://www.youtube.com/watch?v=ywKQGNVpzAs')
     time.sleep(4)
     tweet = bot.find_elements_by_xpath('/html/body/div/div/div/div[1]/div/div/div/div/div[2]/div[2]/div/div[3]/div/div/div[1]/div/div/div/div[2]/div[2]/div/div/div[1]/div[1]/div/svg')
     tweet.send__keys(self.moji)
     time.sleep(10)
ed = TwitterBot('email','password', 'djhdh')
ed.login() 
ed.todo_tweet()



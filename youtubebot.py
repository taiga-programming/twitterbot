from selenium import webdriver
from selenium.webdriver.common.keys import Keys 
import time 

class YoutubeBot:

  def __init__(self, username, password):
     self.username = username
     self.password = password
     self.bot = webdriver.Firefox()
  
  def login(self):
     bot =self.bot
     bot.get('https://accounts.google.com/signin/v2/identifier?service=youtube&uilel=3&passive=true&continue=https%3A%2F%2Fwww.youtube.com%2Fsignin%3Faction_handle_signin%3Dtrue%26app%3Ddesktop%26hl%3Dja%26next%3D%252Fwatch%253Fv%253DywKQGNVpzAs&hl=ja&ec=65620&flowName=GlifWebSignIn&flowEntry=ServiceLogin')
     time.sleep(3)
     email = bot.find_element_by_xpath('//*[@id="identifierId"]')
     email.send_keys(self.username)
     email.send_keys(Keys.RETURN)
     sender = bot.find_element_by_xpath('')
     sender.send_keys(Keys.ENTER)
  


ed = YoutubeBot('','')
ed.login()
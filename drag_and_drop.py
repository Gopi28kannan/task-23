from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException

class drag_drop:
     def __init__(self,url):
          self.driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()))
          self.url=url

     def drag_and_drop(self):
          try:
               #get the url link
               self.driver.get(url)
               #maximize window
               self.driver.maximize_window()
               time.sleep(2)
               #drag and drop boxes insert in iframes. So first switch window in frame
               self.driver.switch_to.frame(self.driver.find_element(By.CLASS_NAME,'demo-frame'))
               time.sleep(2)
               #select drag box use id
               drag_from=self.driver.find_element(By.ID,'draggable')
               #select drop box use x path
               drag_to=self.driver.find_element(By.XPATH,'//*[@id="droppable"]')
               # use actionchains and move the element
               actions = ActionChains(self.driver)
               #drag and drop and element
               actions.drag_and_drop(drag_from, drag_to).perform()
               print("drag and drop is completed")

          except NoSuchElementException as selenium_error:
               #indicate no such element exception
               print(selenium_error)

          finally:
               print("code running completed")
          
     def shutdown(self):
          time.sleep(5)
          # close the window
          self.driver.quit()

url='https://jqueryui.com/droppable/'
d_d=drag_drop(url)
d_d.drag_and_drop()
d_d.shutdown()

from selenium import webdriver
from time import sleep
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


count = 5  # number of posts you want to get

print('Enter the account you want to check: ')
account = input()

print('Enter the number of posts you want to check: ')
count = int(input())
username = input('Enter your Instagram username: ')
password = input('Enter your Instagram password: ')

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://www.instagram.com/accounts/login/')
sleep(3)

username_input = driver.find_element_by_css_selector("input[name='username']")
password_input = driver.find_element_by_css_selector("input[name='password']")
username_input.send_keys(username)
password_input.send_keys(password)
login_button = driver.find_element_by_xpath("//button[@type='submit']")
login_button.click()
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[contains(.,'Not Now')]"))).click()
sleep(3)
          
driver.get('https://www.instagram.com/%s' % account)
sleep(2)

arr = []
WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//body//div[contains(@class,'_2z6nI')]//div//div//div[1]//div[1]//a[1]//div[1]//div[2]"))).click()

sleep(2)
first_post_time = driver.find_element_by_xpath('/html/body/div[5]/div[2]/div/article/div[3]/div[2]/a/time')#finds time that first post was posted
sleep(2)
text1 = first_post_time.text
print(text1)
arr.append(text1)
#find likes
sleep(2)

try:
   num_likes = driver.find_element_by_xpath('/html/body/div[5]/div[2]/div/article/div[3]/section[2]/div/div/button')
except:
   num_likes = driver.find_element_by_xpath('/html/body/div[5]/div[2]/div/article/div[3]/section[2]/div/div/a')
num_likes_text = num_likes.text
if num_likes_text == "like this":
   print('0 likes')
else:
   print(num_likes_text)
print()

arrow1 = driver.find_element_by_xpath('/html/body/div[5]/div[1]/div/div/a') #clicks first arrow
arrow1.click()
sleep(2)


s2 = driver.find_element_by_xpath('/html/body/div[5]/div[2]/div/article/div[3]/div[2]/a/time') #time of the second post
secondtext = s2.text
print(secondtext)
arr.append(secondtext)

#find likes
try:
   num_likes = driver.find_element_by_xpath('/html/body/div[5]/div[2]/div/article/div[3]/section[2]/div/div/button')
except:
   num_likes = driver.find_element_by_xpath('/html/body/div[5]/div[2]/div/article/div[3]/section[2]/div/div/a')
num_likes_text = num_likes.text
if num_likes_text == "like this":
   print('0 likes')
else:
   print(num_likes_text)
print()


for i in range(0,count-2):
   scr5 = driver.find_element_by_xpath('/html/body/div[5]/div[1]/div/div/a[2]') #clicks the next arrows
   scr5.click()
   sleep(2)
   scr4 = driver.find_element_by_xpath('/html/body/div[5]/div[2]/div/article/div[3]/div[2]/a/time')
   sleep(2)
   text2 = scr4.text
   print(text2)
   arr.append(text2)

   sleep(2)
   try:
      num_likes = driver.find_element_by_xpath('/html/body/div[5]/div[2]/div/article/div[3]/section[2]/div/div/button')
   except:
      num_likes = driver.find_element_by_xpath('/html/body/div[5]/div[2]/div/article/div[3]/section[2]/div/div/a')
   num_likes_text = num_likes.text
   if num_likes_text == "like this":
      print('0 likes')
   else:
      print(num_likes_text)
   print()


if arr[0] == arr[len(arr)-1]:
   print("Posted at the same time, Most likely a bot account")

print()


followercount = driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a/span')
followertext = followercount.text
f1 = followertext.replace(',','')
follow = int(f1)

followingcount = driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li[3]/a/span')
followingtext = followingcount.text
f = followingtext.replace(',','')
following = int(f)

ratio = follow/following

if ratio <= 0.2:
   print("follower to following ratio: ", ratio)
   print("Most likely a bot account")
else:
   print("follower to following ratio: ", ratio)



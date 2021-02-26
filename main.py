from selenium import webdriver

driver = webdriver.Chrome("C:\Python\Lib\site-packages\selenium\webdriver\chrome\chromedriver")

driver.get("https://web.whatsapp.com/")

name = input("Enter The Group or User name: ")
message = input("Enter your message: ")
count = int(input("Enter the Count: "))

scode = input("Enter anything after scan code:")

user = driver.find_element_by_xpath('//span[@title="{}"]'.format(name))
user.click()

msg_box = driver.find_element_by_xpath("//*[@id='main']/footer/div[1]/div[2]/div/div[2]")

for i in range(count):

   msg_box.send_keys(message)
   driver.find_element_by_xpath("//*[@id='main']/footer/div[1]/div[3]/button").click()

print("Message Sent Sucessfully!!")

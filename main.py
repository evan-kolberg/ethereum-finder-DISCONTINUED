from selenium import webdriver
from time import sleep
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
driver = webdriver.Chrome(executable_path=r'/Users/-----------/PycharmProjects/ethereum guesser/chromedriver', options=chrome_options)
website = "https://privatekeys.pw/keys/ethereum/1"
text_file = open("private-keys.txt","a")

def loop():
    global text_file, float
    try:
        driver.get(website)
        sleep(2)
        balance = driver.find_element_by_css_selector("h3")
        print(balance.text)
        string = balance.text
        float = float(string.replace("Total balance on the page: ", ""))
        print(float)
        if float != 0:
            text_file.write(driver.find_element_by_xpath("/html/body/main/div/p[2]/strong[1]").text)
            text_file.write("\n")
        sleep(1)
        driver.find_element_by_xpath("/html/body/main/div/div[2]/div[3]/nav/ul/li[3]/a").click()
    except:
        print("ERROR: CLOUDFAIR DECIDED TO BE A PAIN IN THE ASS")

if __name__ == "__main__":
    for i in range(6969420):
        loop()

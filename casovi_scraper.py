from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time,os


options = webdriver.ChromeOptions()
options.binary_location = os.environ.get('GOOGLE_CHROME_BIN')
options.add_argument('--headless')
options.add_argument('--no-sandbox')   
options.add_argument('--disabele-dev-sh-usage')   
driver = webdriver.Chrome(executable_path=os.environ.get('CHROMEDRIVER_PATH'), chrome_options=options)
    
def login():
    url = 'https://privatni-casovi.net/sessions/new'
    driver.get(url)
    time.sleep(1)
    email = driver.find_element_by_id('email-login-input')
    email.send_keys("stefanruvceski@gmail.com")

    driver.find_element_by_xpath('/html/body/main/div/div/form/div[1]/div[2]/input').click()


def get_info(token):
    url = f"https://privatni-casovi.net/sessions/{token}/login"
    driver.get(url)
    time.sleep(1)
    urls =  ['https://privatni-casovi.net/python/predmet',
            'https://privatni-casovi.net/c/predmet' ,
            'https://privatni-casovi.net/web-development/predmet' ,
            'https://privatni-casovi.net/objektno-orijentisano-programiranje-java-c/predmet' ,
            'https://privatni-casovi.net/baze-podataka/predmet' ,
            'https://privatni-casovi.net/iz-programiranja/predmet' ,
            'https://privatni-casovi.net/asp-net/predmet' ,
            'https://privatni-casovi.net/iz-c-i-c-plus-plusa/predmet' ,
            'https://privatni-casovi.net/informatika-i-racunarstvo/predmet'
            ]
    result = []
    for index in range(0,len(urls)):

        driver.get(urls[index])

        profiles = driver.find_elements_by_class_name('profile-card');
        
        i = 0
        for profile in profiles:
            name = profile.find_element_by_class_name('name').find_element_by_tag_name('a').text;
            i+=1
            if(name == 'Stefan Ruvceski'):
                result.append(f'{name} je {i} na listi za predmet {urls[index].split("/")[3]}')
                break
    return result

def quit():  
    driver.quit()
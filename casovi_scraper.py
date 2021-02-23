from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time,os

# driver = webdriver.Chrome()

def login(emaildata):
    options = webdriver.ChromeOptions()
    options.binary_location = os.environ.get('GOOGLE_CHROME_BIN')
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')   
    options.add_argument('--disabele-dev-sh-usage')   
    driver = webdriver.Chrome(executable_path=os.environ.get('CHROMEDRIVER_PATH'), chrome_options=options)
    time.sleep(0.2)
    
    url = 'https://privatni-casovi.net/sessions/new'
    driver.get(url)
    time.sleep(0.2)
    
    email = driver.find_element_by_id('email-login-input')
    email.send_keys(emaildata)

    driver.find_element_by_xpath('/html/body/main/div/div/form/div[1]/div[2]/input').click()
    driver.quit()

def get_info(token):
    options = webdriver.ChromeOptions()
    options.binary_location = os.environ.get('GOOGLE_CHROME_BIN')
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')   
    options.add_argument('--disabele-dev-sh-usage')   
    driver = webdriver.Chrome(executable_path=os.environ.get('CHROMEDRIVER_PATH'), chrome_options=options)
    time.sleep(0.2)
    
    url = f"https://privatni-casovi.net/sessions/{token}/login"
    driver.get(url)
    time.sleep(0.5)
    
    url = 'https://privatni-casovi.net/teacher'
    driver.get(url)
    
    my_name = driver.find_element_by_class_name('profile-name').text
    time.sleep(0.2)
    
    subjects = driver.find_elements_by_class_name('badge')
    urls = []
    for subject in subjects:
        urls.append(subject.find_element_by_tag_name('a').get_attribute('href'))
        
    result = []
    for index in range(0,len(urls)):
        driver.get(urls[index])
        profiles = driver.find_elements_by_class_name('profile-card');
        i = 0
        for profile in profiles:
            name = profile.find_element_by_class_name('name').find_element_by_tag_name('a').text;
            i+=1
            if name == my_name:
                result.append(f'{i} na listi za predmet {urls[index].split("/")[3]}')
                break
    driver.quit()
    return my_name,result

    
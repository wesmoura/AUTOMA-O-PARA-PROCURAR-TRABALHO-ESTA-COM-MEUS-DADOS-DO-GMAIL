import time,math,random,os
import utils,constants,config
import platform

from selenium import webdriver
from selenium.webdriver.common.by import By
from utils import prRed,prYellow,prGreen

from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Linkedin:
    def __init__(self):
        browser = config.browser[0].lower()
        linkedinEmail = config.email
        if (browser == "firefox"):
            if (len(linkedinEmail)>0):
                print(platform.system())
                if (platform.system == "Linux"):
                    prYellow("On Linux you need to define profile path to run the bot with Firefox. Go about:profiles find root directory of your profile paste in line 8 of config file next to firefoxProfileRootDir ")
                    exit()
                else: 
                    self.driver = webdriver.Firefox()
                    self.driver.get("https://www.linkedin.com/login?trk=guest_homepage-basic_nav-header-signin")
                    prYellow("Trying to log in linkedin.")
                    try:    
                        self.driver.find_element("id","username").send_keys(linkedinEmail)
                        self.driver.find_element("id","password").send_keys(config.password)
                        time.sleep(5)
                        # Aguarde até o botão de login estar presente
                        login_button = WebDriverWait(self.driver, 10).until(
                            EC.presence_of_element_located((By.XPATH, '//button[@type="submit"]'))
                        )
                        login_button.click()
                    except Exception as e: 
                        prRed(e)
            else:
                self.driver = webdriver.Firefox()
        elif (browser == "chrome"):
            self.driver = webdriver.Chrome()
            self.driver.get("https://www.linkedin.com/login?trk=guest_homepage-basic_nav-header-signin")
            prYellow("Trying to log in linkedin.")
            try:    
                self.driver.find_element("id","username").send_keys(linkedinEmail)
                time.sleep(5)
                self.driver.find_element("id","password").send_keys(config.password)
                time.sleep(5)
                login_button = self.driver.find_element(By.XPATH, '//button[@type="submit"]')
                login_button.click()
            except:
                prRed("Couldnt log in Linkedin by using chrome please try again for Firefox by creating a firefox profile.")

        # driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        # webdriver.Chrome(ChromeDriverManager().install())
        # webdriver.Firefox(options=utils.browserOptions())
    
    def generateUrls(self):
        if not os.path.exists('data'):
            os.makedirs('data')
        try: 
            with open('data/urlData.txt', 'w',encoding="utf-8" ) as file:
                linkedinJobLinks = utils.LinkedinUrlGenerate().generateUrlLinks()
                for url in linkedinJobLinks:
                    file.write(url+ "\n")
            prGreen("Urls are created successfully, now the bot will visit those urls.")
        except:
            prRed("Couldnt generate url, make sure you have /data folder and modified config.py file for your preferances.")

    def linkJobApply(self):
        self.generateUrls()
        countApplied = 0
        countJobs = 0

        urlData = utils.getUrlDataFile()

        for url in urlData:        
            self.driver.get(url)
            try:
                totalJobs = self.driver.find_element(By.XPATH,'//small').text 
            except:
                print("No Matching Jobs Found")
                continue
            totalPages = utils.jobsToPages(totalJobs)

            urlWords =  utils.urlToKeywords(url)
            lineToWrite = "\n Category: " + urlWords[0] + ", Location: " +urlWords[1] + ", Applying " +str(totalJobs)+ " jobs."
            self.displayWriteResults(lineToWrite)

            for page in range(totalPages):
                currentPageJobs = constants.jobsPerPage * page
                url = url +"&start="+ str(currentPageJobs)
                self.driver.get(url)
                time.sleep(random.uniform(1, constants.botSpeed))

                offersPerPage = self.driver.find_elements(By.XPATH,'//li[@data-occludable-job-id]')

                offerIds = []
                for offer in offersPerPage:
                    offerId = offer.get_attribute("data-occludable-job-id")
                    offerIds.append(int(offerId.split(":")[-1]))

                for jobID in offerIds:
                    offerPage = 'https://www.linkedin.com/jobs/view/' + str(jobID)
                    self.driver.get(offerPage)
                    time.sleep(random.uniform(1, constants.botSpeed))

                    countJobs += 1

                    jobProperties = self.getJobProperties(countJobs) 
                    
                    button = self.easyApplyButton()

                    if button is not False:
                        # Tentar fechar popups de cookies ou overlays
                        try:
                            close_buttons = self.driver.find_elements(By.XPATH, '//button[contains(@aria-label, "Dismiss") or contains(@aria-label, "Fechar") or contains(@aria-label, "Close")]')
                            for close_btn in close_buttons:
                                if close_btn.is_displayed():
                                    close_btn.click()
                                    time.sleep(1)
                        except Exception as e:
                            prYellow(f"Aviso ao tentar fechar popups: {e}")
                        # Supondo que 'button' seja o elemento do botão Easy Apply
                        self.driver.execute_script("arguments[0].scrollIntoView();", button)
                        time.sleep(1)
                        try:
                            button.click()
                        except Exception as e:
                            prYellow(f"Clique normal falhou, tentando via JS: {e}")
                            self.driver.execute_script("arguments[0].click();", button)
                        time.sleep(random.uniform(1, constants.botSpeed))
                        countApplied += 1
                        try:
                            self.driver.find_element(By.CSS_SELECTOR, "button[aria-label='Submit application']").click()
                            time.sleep(random.uniform(1, constants.botSpeed))

                            lineToWrite = jobProperties + " | " + "* 🥳 Just Applied to this job: "  +str(offerPage)
                            self.displayWriteResults(lineToWrite)

                        except:
                            try:
                                self.driver.find_element(By.CSS_SELECTOR,"button[aria-label='Continue to next step']").click()
                                time.sleep(random.uniform(1, constants.botSpeed))
                                comPercentage = self.driver.find_element(By.XPATH,'html/body/div[3]/div/div/div[2]/div/div/span').text
                                percenNumber = int(comPercentage[0:comPercentage.index("%")])
                                result = self.applyProcess(percenNumber,offerPage)
                                lineToWrite = jobProperties + " | " + result
                                self.displayWriteResults(lineToWrite)
                            
                            except Exception as e: 
                                try:
                                    self.driver.find_element(By.CSS_SELECTOR,"option[value='urn:li:country:" + config.country_code + "']").click()
                                    time.sleep(random.uniform(1, constants.botSpeed))
                                    self.driver.find_element(By.CSS_SELECTOR, 'input').send_keys(config.phone_number);
                                    time.sleep(random.uniform(1, constants.botSpeed))
                                    self.driver.find_element(By.CSS_SELECTOR,"button[aria-label='Continue to next step']").click()
                                    time.sleep(random.uniform(1, constants.botSpeed))
                                    comPercentage = self.driver.find_element(By.XPATH,'html/body/div[3]/div/div/div[2]/div/div/span').text
                                    percenNumber = int(comPercentage[0:comPercentage.index("%")])
                                    result = self.applyProcess(percenNumber,offerPage)
                                    lineToWrite = jobProperties + " | " + result
                                    self.displayWriteResults(lineToWrite)
                                except Exception as e:
                                    lineToWrite = jobProperties + " | " + "* 🥵 Cannot apply to this Job! " +str(offerPage)
                                    self.displayWriteResults(lineToWrite)
                    else:
                        lineToWrite = jobProperties + " | " + "* 🥳 Already applied! Job: " +str(offerPage)
                        self.displayWriteResults(lineToWrite)


            prYellow("Category: " + urlWords[0] + "," +urlWords[1]+ " applied: " + str(countApplied) +
                  " jobs out of " + str(countJobs) + ".")
        
        # utils.donate(self)

    def getJobProperties(self, count):
        textToWrite = ""
        jobTitle = ""
        jobCompany = ""
        jobLocation = ""
        jobWOrkPlace = ""
        jobPostedDate = ""
        jobApplications = ""

        try:
            jobTitle = self.driver.find_element(By.XPATH,"//h1[contains(@class, 'job-title')]").get_attribute("innerHTML").strip()
        except Exception as e:
            prYellow("Warning in getting jobTitle: " +str(e)[0:50])
            jobTitle = ""
        try:
            jobCompany = self.driver.find_element(By.XPATH,"//a[contains(@class, 'ember-view t-black t-normal')]").get_attribute("innerHTML").strip()
        except Exception as e:
            prYellow("Warning in getting jobCompany: " +str(e)[0:50])
            jobCompany = ""
        try:
            jobLocation = self.driver.find_element(By.XPATH,"//span[contains(@class, 'bullet')]").get_attribute("innerHTML").strip()
        except Exception as e:
            prYellow("Warning in getting jobLocation: " +str(e)[0:50])
            jobLocation = ""
        try:
            jobWOrkPlace = self.driver.find_element(By.XPATH,"//span[contains(@class, 'workplace-type')]").get_attribute("innerHTML").strip()
        except Exception as e:
            prYellow("Warning in getting jobWorkPlace: " +str(e)[0:50])
            jobWOrkPlace = ""
        try:
            jobPostedDate = self.driver.find_element(By.XPATH,"//span[contains(@class, 'posted-date')]").get_attribute("innerHTML").strip()
        except Exception as e:
            prYellow("Warning in getting jobPostedDate: " +str(e)[0:50])
            jobPostedDate = ""
        try:
            jobApplications= self.driver.find_element(By.XPATH,"//span[contains(@class, 'applicant-count')]").get_attribute("innerHTML").strip()
        except Exception as e:
            prYellow("Warning in getting jobApplications: " +str(e)[0:50])
            jobApplications = ""

        textToWrite = str(count)+ " | " +jobTitle+  " | " +jobCompany+  " | "  +jobLocation+ " | "  +jobWOrkPlace+ " | " +jobPostedDate+ " | " +jobApplications
        return textToWrite

    def easyApplyButton(self):
        try:
            button = self.driver.find_element(By.XPATH,
                '//button[contains(@class, "jobs-apply-button")]')
            EasyApplyButton = button
        except: 
            EasyApplyButton = False

        return EasyApplyButton

    def applyProcess(self, percentage, offerPage):
        applyPages = math.floor(100 / percentage) 
        result = ""  
        try:    
            for pages in range(applyPages-2):
                self.driver.find_element(By.CSS_SELECTOR,"button[aria-label='Continue to next step']").click()
                time.sleep(random.uniform(1, constants.botSpeed))

            self.driver.find_element(By.CSS_SELECTOR,"button[aria-label='Review your application']").click() 
            time.sleep(random.uniform(1, constants.botSpeed))

            if config.followCompanies is False:
                self.driver.find_element(By.CSS_SELECTOR,"label[for='follow-company-checkbox']").click() 
                time.sleep(random.uniform(1, constants.botSpeed))

            self.driver.find_element(By.CSS_SELECTOR,"button[aria-label='Submit application']").click()
            time.sleep(random.uniform(1, constants.botSpeed))

            result = "* 🥳 Just Applied to this job: " +str(offerPage)
        except:
            result = "* 🥵 " +str(applyPages)+ " Pages, couldn't apply to this job! Extra info needed. Link: " +str(offerPage)
        return result

    def displayWriteResults(self,lineToWrite: str):
        try:
            print(lineToWrite)
            utils.writeResults(lineToWrite)
        except Exception as e:
            prRed("Error in DisplayWriteResults: " +str(e))


start = time.time()
while True:
    try:
        Linkedin().linkJobApply()
    except Exception as e:
        prRed("Error in main: " +str(e))
        # close firefox driver
        end = time.time()
        prYellow("---Took: " + str(round((time.time() - start)/60)) + " minute(s).")
        Linkedin().driver.quit()

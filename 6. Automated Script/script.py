import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome("C:/Users/kgbko/chromedriver_win32/chromedriver.exe")
driver.maximize_window()
driver.implicitly_wait(20)
driver.get("https://zeus.gist.ac.kr/sys/main/main.do")
elem = driver.find_element_by_name("login_id") 
elem.send_keys('kgbko1117') 
elem = driver.find_element_by_name("login_pw") 
elem.send_keys('rhrkdqls123!')
elem.send_keys(Keys.ENTER)

# 찾고자 하는 요소가 iframe 안에 있어 NotFound Error가 발생
# 이를 해결하기 위해 'driver.switchTo (). frame ()'명령을 사용하여 iframe으로 전환 후 요소 탐색 진행
element = driver.find_element_by_xpath("//div[@id='ifm_idx_wrap']/iframe")
driver.switch_to_frame(element)

page = driver.find_element_by_xpath('//div[@id="mainframe_VFrameSet_HFrameSet_leftFrame_form_gridMenu_body_gridrow_7_cell_7_0_controltreeTextBoxElement"]')
page.click()
tab = driver.find_element_by_xpath('//*[@id="mainframe_VFrameSet_HFrameSet_leftFrame_form_gridMenu_body_gridrow_12_cell_12_0_controltreeTextBoxElement"]/div')
tab.click()

temp = driver.find_element_by_xpath('//*[@id="mainframe_VFrameSet_HFrameSet_MDIFrameSet_ctxFrameSet_ctxFrame_PERS07^PERS07_08^005^AmcDailyTempRegE_form_div_sample_divMain_divForm_edtTemp_input"]')

temp.send_keys('36.0') # New Error: selenium.common.exceptions.ElementNotInteractableException: Message: element not interactable
time.sleep(10)

save = driver.find_element_by_xpath('//*[@id="mainframe_VFrameSet_HFrameSet_MDIFrameSet_ctxFrameSet_ctxFrame_PERS07^PERS07_08^005^AmcDailyTempRegE_form_div_sample_divMain_btnSave"]').click()
time.sleep(10)
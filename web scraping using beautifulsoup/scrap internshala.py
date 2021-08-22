
import time
from selenium import webdriver
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

path="C:\Program Files (x86)\chromedriver.exe"
driver=webdriver.Chrome(path)

driver.get("https://internshala.com/internships/")
plink=driver.find_element_by_id("close_popup")
plink.click()
time.sleep(1)

all_ele=driver.find_elements_by_class_name('internship_meta')
each_ele=all_ele[1]













































# for i in range(1,len(all_ele)):
#     each_ele=all_ele[i]
#     Intern_name=each_ele.find_element_by_css_selector('div.heading_4_5.profile').text
#     lk=each_ele.find_element_by_tag_name('a')
#     Intern_link=lk.get_property('href')
#     Comp_Name=each_ele.find_element_by_class_name('link_display_like_text').text
#     link=each_ele.find_element_by_class_name('link_display_like_text')
#     Comp_link=link.get_property('href')
#     location=each_ele.find_element_by_tag_name('span').text
#     start=each_ele.find_element_by_id('start-date-first').text
#     n=each_ele.find_element_by_class_name('individual_internship_details.individual_internship_internship')
#     s=n.text.split()
#     dur=''.join(map(str,s))
#     stp=each_ele.find_element_by_class_name('stipend').text
#     deadline=each_ele.find_element_by_class_name('individual_internship_details.individual_internship_internship')

#     d=deadline.text.split()[:]
# # print(d)
#     dead=''.join(map(str,d))
# print(s)

# print(deadline.text)
# print(Intern_name,Comp_Name,Comp_link,location,start,dur,stp,dead,sep='\n')



# driver.
# link.click()
# t=driver.find_element_by_id('total_pages')
# action= ActionChains(driver)
# action.click(link)
# action.perform()
# # i=0
# while(i<t):

#     link=driver.find_element_by_id("navigation-forward")
#     link.click()
#     i+=1
# driver.quit()
# for i in range(228):
#     wait = WebDriverWait(driver, 10)
#     t = wait.until(lambda driver: driver.find_element_by_id('navigation-forward'))
#     t.click()

# # try:
#     main = WebDriverWait(driver, 000.5).until(
#         EC.presence_of_element_located((By.CLASS_NAME, "next_page hideUndoOnClick"))
#     )
#     main.click()

# finally:
#     driver.quit()


# while (i<228):
#     all_ele=driver.find_elements_by_class_name('internship_meta')
#     for each_ele in all_ele:
#         main = WebDriverWait(driver, 10).until(
#         EC.presence_of_element_located((By.CLASS_NAME, "view_detail_button"))
#         )
#         main.click()
#         back=WebDriverWait(driver, 10).until(
#         EC.presence_of_element_located((By.CLASS_NAME, "backToInternship"))
#         )
#         back.click()

        
#     next=WebDriverWait(driver, 10).until(
#     EC.presence_of_element_located((By.ID, "navigation-forward"))
#     )
#     next.click()
#     i+=1
    
# else:
#     print("No page reamin")
    

    


           
            




from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver.common.appiumby import AppiumBy
from PIL import Image
from io import BytesIO
import cv2
import numpy as np
import os
import json
import os

class Utils:
    def __init__(self, driver):
        self.driver = driver
        self.image_url = "../compare_image/"
    
    def scroll_action(self, class_name, description=None):
        if description is not None:
            description_str = f'"{description}"'
            scrollable_element = (
                f'new UiScrollable(new UiSelector().scrollable(true))'
                f'.scrollIntoView(new UiSelector().className("{class_name}").description({description_str}))'
            )
        else:
            scrollable_element = (
                f'new UiScrollable(new UiSelector().scrollable(true))'
                f'.scrollIntoView(new UiSelector().className("{class_name}"))'
            )
        
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, scrollable_element))
        )
        
    def get_all_elements(self, class_name):
        return WebDriverWait(self.driver, 5).until(
            EC.presence_of_all_elements_located((AppiumBy.ANDROID_UIAUTOMATOR, f'new UiSelector().className("{class_name}")')))
    
    def screenshot_image(self, file_name, element):
        element_screenshot = element.screenshot_as_png
        img = Image.open(BytesIO(element_screenshot))
        img.save(file_name, format='PNG')
      
    def compare_image(self, file_name, element, compare_image):
        try:
            current_dir = os.path.dirname(os.path.abspath(__file__))
            compare_image_path = os.path.join(current_dir, '../compare_image', compare_image)
            
            img1 = cv2.imread(compare_image_path)

            if img1 is None:
                print("Error: The comparison image could not be read.")
                return False
            
            height1, width1 = img1.shape[:2]
            element_screenshot = element.screenshot_as_png

            # img2 = Image.open(BytesIO(element_screenshot))
            # img2 = img2.resize((width1, height1), Image.Resampling.LANCZOS)
            # img2.save(file_name, format='PNG')
            img2 = cv2.imread(file_name)

            img1_gray = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
            img2_gray = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

            difference = cv2.absdiff(img1_gray, img2_gray)
            result = not np.any(difference)
            return result
        except cv2.error as e:
            if e.code == -209: 
                return False
            else:
                raise
    
    def get_element_by_content_desc(self, elements, content_desc):
        for element in elements:
            if element.get_attribute("contentDescription") == content_desc:
                return element
        return None
    
    def get_return_popup(self):
        popup = WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.ImageView").instance(0)')))
        close_btn = WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.Button").instance(0)')))
        popup_elements = [popup, close_btn]
        
        return popup_elements
    
    def get_data_json(self, data_vlaue):
        file_path = os.path.join(os.path.dirname(__file__), '../data/test_data.json')
        with open(file_path, 'r') as file:
            data = json.load(file)

        return data.get(data_vlaue)
    
    def get_element_list_print(self, class_name):
        element_list = self.get_all_elements(class_name)
        for i,el in enumerate(element_list):
            print(f'{class_name} / {i} = {el.get_attribute("contentDescription")}')
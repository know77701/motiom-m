from utils.utils import Utils
from config.selectors import Selectors
import time

class Home():
    def __init__(self, driver):
        self.driver = driver
        self.utils = Utils(driver)
        self.selectors = Selectors()
        self.status_list = ["default","busy","metting","off","default"]
    
    def test_run(self):
        # self.test_home_page_ui_check()
        # self.test_profile_image_check()
        # self.test_status_bottom_sheet_ui_check()
        # self.test_status_stting()
        # self.test_user_card_ui_cheek()
        # self.test_user_card_status()
        # self.test_user_card_org_chart_oepn()
        # self.test_user_card_value_copy()
        # self.test_user_card_my_chattroom_open()
        # self.test_user_list_ui_check()
        # self.test_pause_notifications_ui_check()
        self.test_is_notifications_paused()
    
    def test_home_page_ui_check(self):
        view_list = self.utils.get_all_elements(self.selectors.VIEW_CLASS_NAME)
        btn_list = self.utils.get_all_elements(self.selectors.BUTTON_CLASS_NAME)
        image_list = self.utils.get_all_elements(self.selectors.IMAGE_CLASS_NAME)
        
        user_name_replace = self.utils.element_replace(view_list[7].get_attribute("contentDescription"))
        
        assert view_list[5].get_attribute("contentDescription") == "트라이업영문", "home page business name ui test Fail"
        assert user_name_replace == "이말년의사/대표원장", "home page user name ui test Fail"
        assert self.utils.compare_image("user_image.png",view_list[8],"home_user_image.png","home"), "home user image compare test Fail"
        assert self.utils.compare_image("setting_button.png",image_list[0],"home_setting_button.png","home"), "home setting btn ui test Fail"
        assert self.utils.compare_image("status_setting.png",image_list[1],"home_status_setting.png","home"), "home status setting btn ui test Fail"
        assert self.utils.compare_image("alert_setting.png",image_list[2],"home_alert_setting.png","home"), "home alert setting btn ui test Fail"
        assert self.utils.compare_image("user_message_chatting_room.png",btn_list[0],"user_message_chatting_room.png","home"), "meessage chatting room button ui test Fail"
        assert self.utils.compare_image("home_tap.png",image_list[3],"bottom_home_tap.png","home"),"bottom home tap active ui test Fail"
        assert self.utils.compare_image("message_tap.png",image_list[4],"bottom_message_tap.png","home"), "bottom messsage tap enabled ui test Fail"
        assert self.utils.compare_image("organization_chart_enabled.png",image_list[5],"bottom_organization_chart_enabled.png","home"), "bottom organization chart tap enabled ui test Fail"
        
    def test_profile_image_check(self):
        view_list = self.utils.get_all_elements(self.selectors.VIEW_CLASS_NAME)
        view_list[8].click()
        image_list = self.utils.get_all_elements(self.selectors.IMAGE_CLASS_NAME)
        btn_list = self.utils.get_all_elements(self.selectors.BUTTON_CLASS_NAME)
        
        assert self.utils.compare_image("view_user_image.png",image_list[0],"view_user_image.png","home"), "bottom organization chart tap enabled ui test Fail"
        btn_list[0].click()
    
    def test_status_bottom_sheet_ui_check(self):
        view_list = self.utils.get_all_elements(self.selectors.VIEW_CLASS_NAME)
        image_list = self.utils.get_all_elements(self.selectors.IMAGE_CLASS_NAME)
        
        image_list[1].click()
        assert self.utils.compare_image("status_bottom_sheet.png",view_list[3],"status_bottom_sheet.png","home"), "status bottom sheet ui test Fail"
        assert self.utils.compare_image("status_bottom_sheet_default.png",view_list[8],"status_bottom_sheet_default.png","home"), "status bottom sheet default ui test Fail"
        assert self.utils.compare_image("status_bottom_sheet_busy.png",view_list[9],"status_bottom_sheet_busy.png","home"), "status bottom sheet busy ui test Fail"
        assert self.utils.compare_image("status_bottom_sheet_metting.png",view_list[10],"status_bottom_sheet_metting.png","home"), "status bottom sheet metting ui test Fail"
        assert self.utils.compare_image("status_bottom_sheet_out_of_office.png",view_list[11],"status_bottom_sheet_out_of_office.png","home"), "status bottom sheet out of office ui test Fail"
        
        self.utils.bottom_sheet_close()
        
    def status_setting(self, status):
        view_list = self.utils.get_all_elements(self.selectors.VIEW_CLASS_NAME)
        
        if status == "default":
            view_list[8].click()
        elif status == "busy":
            view_list[9].click()
        elif status == "metting":
            view_list[10].click()
        else:
            view_list[11].click()
        
    def check_status_setting(self, view_element=None, btn_element=None, status=None):
        view_list = self.utils.get_all_elements(self.selectors.VIEW_CLASS_NAME)
        
        if view_element:
            view_element.click()
            btn_element.click()
            self.status_setting(status)
            assert self.utils.compare_image(f"status_{status}_user_image.png",view_list[8],f"status_{status}_user_image.png","home"), f"{status} status user image compare test Fail"
            view_element.click()
            btn_element.click()
            assert self.utils.compare_image(f"status_setting_{status}.png", view_list[3], f"status_setting_{status}.png", "home"), f"{status} status setting sheet test Fail"
            self.utils.bottom_sheet_close()
        else:
            btn_element.click()
            self.status_setting(status)
            assert self.utils.compare_image(f"status_{status}_user_image.png",view_list[8],f"status_{status}_user_image.png","home"), f"{status} status user image compare test Fail"
            btn_element.click()
            assert self.utils.compare_image(f"status_setting_{status}.png", view_list[3], f"status_setting_{status}.png", "home"), f"{status} status setting sheet test Fail"
            self.utils.bottom_sheet_close()
        
    def test_status_stting(self):
        image_list = self.utils.get_all_elements(self.selectors.IMAGE_CLASS_NAME)
       
        
        for item in self.status_list:
            self.check_status_setting(btn_element=image_list[1],status=item)
        
    def test_user_card_ui_cheek(self):
        view_list = self.utils.get_all_elements(self.selectors.VIEW_CLASS_NAME)
        view_list[7].click()
        
        image_list = self.utils.get_all_elements(self.selectors.IMAGE_CLASS_NAME)
        btn_list = self.utils.get_all_elements(self.selectors.BUTTON_CLASS_NAME)
        
        compare_text = "이말년의사/대표원장트라이업영문의사/대표원장휴대폰010-7441-7631메일know701@triupcorp.com"
        user_infomation = self.utils.element_replace(view_list[7].get_attribute("contentDescription"))
        
        assert user_infomation == compare_text, "user card infomation text compare test Fail"
        assert self.utils.compare_image("user_card.png", view_list[7], "user_card.png","home"), "user bottom sheet ui test Fail" 
        assert self.utils.compare_image("user_card_my_chattingroom_btn.png", image_list[0], "user_card_my_chattingroom_btn.png","home"), "user card my chatting room btn ui test Fail"
        assert self.utils.compare_image("user_card_status_btn.png",btn_list[0],"user_card_status_btn.png","home"), "user card status btn ui test Fail"
        assert self.utils.compare_image("user_card_org_chart_btn.png",btn_list[1],"user_card_org_chart_btn.png","home"), "user card org chart btn ui test Fail"
        assert self.utils.compare_image("user_card_email_copy_btn.png", image_list[1], "user_card_email_copy_btn.png","home"), "user card email copy btn ui test Fail"
        assert self.utils.compare_image("user_card_phone_copy_btn.png", image_list[2], "user_card_phone_copy_btn.png","home"), "user card phone copy btn ui test Fail"
        self.utils.bottom_sheet_close()
        
    def test_user_card_status(self):
        for element in self.status_list:
            self.user_card_status(element)
    
    def user_card_status(self, status):
        view_list = self.utils.get_all_elements(self.selectors.VIEW_CLASS_NAME)
        btn_list = self.utils.get_all_elements(self.selectors.BUTTON_CLASS_NAME)
        
        self.check_status_setting(view_list[7],btn_list[0],status)
    
    def test_user_card_org_chart_oepn(self):
        view_list = self.utils.get_all_elements(self.selectors.VIEW_CLASS_NAME)
        view_list[7].click()
        
        btn_list = self.utils.get_all_elements(self.selectors.BUTTON_CLASS_NAME)
        btn_list[1].click()
        
        time.sleep(0.5)
        assert view_list[4].get_attribute("contentDescription") == "조직도", "user card org chart open test Fail"
        for index, element in enumerate(view_list):
            replace_desc = self.utils.element_replace(element.get_attribute("contentDescription"))
            if replace_desc == "이말년의사/대표원장":
                assert self.utils.compare_image("org_chart_my_image.png",view_list[index+1],"org_chart_my_image.png","org_chart"), "org chart user image test Fail"
                assert replace_desc == "이말년의사/대표원장", "org chart user oepn test Fail"
                break
        btn_list[0].click()
    
    def test_user_card_value_copy(self):
        view_list = self.utils.get_all_elements(self.selectors.VIEW_CLASS_NAME)
        view_list[7].click()
        
        image_list = self.utils.get_all_elements(self.selectors.IMAGE_CLASS_NAME)
        image_list[1].click()
        mobile_copy = self.utils.return_value_copy()
        print(mobile_copy)
        image_list[2].click()
        email_copy = self.utils.return_value_copy()
        print(email_copy)
    
    def test_user_card_my_chattroom_open(self):
        view_list = self.utils.get_all_elements(self.selectors.VIEW_CLASS_NAME)
        image_list = self.utils.get_all_elements(self.selectors.IMAGE_CLASS_NAME)
        btn_list = self.utils.get_all_elements(self.selectors.BUTTON_CLASS_NAME)

        view_list[7].click()
        image_list[0].click()

        assert self.utils.compare_image("my_chatting_room.png",image_list[0], "my_chatting_room.png","home")
        btn_list[0].click()
        self.utils.bottom_sheet_close()

    
    def test_user_list_ui_check(self):
        view_list = self.utils.get_all_elements(self.selectors.VIEW_CLASS_NAME)
        replace_user_name = self.utils.element_replace(view_list[7].get_attribute("contentDescription"))
        
        if "의사" in replace_user_name:
            view_list[12].click()
        elif "간호" in replace_user_name:
            view_list[14].click()
        elif "상담" in replace_user_name:
            view_list[16].click()
        elif "간호조무사" in replace_user_name:
            view_list[18].click()
        elif "에스테틱" in replace_user_name:
            view_list[20].click()
        elif "영업" in replace_user_name:
            view_list[22].click()
        elif "마케팅" in replace_user_name:
            view_list[24].click()
        self.utils.get_element_list_print(self.selectors.VIEW_CLASS_NAME)
        
    
    def test_user_ui_check(self):
        return
    
    def test_pause_notifications_ui_check(self):
        image_list = self.utils.get_all_elements(self.selectors.IMAGE_CLASS_NAME)
        image_list[2].click()

        view_list = self.utils.get_all_elements(self.selectors.VIEW_CLASS_NAME)
        
        assert self.utils.element_replace(view_list[8].get_attribute("contentDescription")) == '알림일시정지설정안함', "is_notifications_paused text compare test Fail"
        assert self.utils.element_replace(view_list[9].get_attribute("contentDescription")) == '알림수신시간설정꺼짐', "message_auto_setting text compare test Fail"
        assert self.utils.element_replace(view_list[10].get_attribute("contentDescription")) == '메시지자동응답꺼짐', "automatic_message_response text compare test Fail"
        assert self.utils.compare_image("pause_notifications_image.png", view_list[5], "pause_notifications_image.png", "home"), "pause_notifications_image ui test Fail"
        assert self.utils.compare_image("is_notifications_paused.png",image_list[0], "is_notifications_paused.png", "home"), "is_notifications_paused ui test Fail"
        assert self.utils.compare_image("is_notifications_paused_open.png",image_list[1], "is_notifications_paused_open.png", "home"), "is_notifications_paused_open ui test Fail"
        assert self.utils.compare_image("message_auto_setting.png",image_list[2], "message_auto_setting.png", "home"), "message_auto_setting ui test Fail"
        assert self.utils.compare_image("message_auto_setting_open.png",image_list[3], "message_auto_setting_open.png", "home"), "message_auto_setting_open ui test Fail"
        assert self.utils.compare_image("automatic_message_response.png",image_list[4], "automatic_message_response.png", "home"), "automatic_message_response ui test Fail"
        assert self.utils.compare_image("automatic_message_response_open.png",image_list[5], "automatic_message_response_open.png", "home"), "automatic_message_response_open ui test Fail"
        self.utils.bottom_sheet_close()
    
    def test_is_notifications_paused(self):
        view_list = self.utils.get_all_elements(self.selectors.VIEW_CLASS_NAME)
        image_list = self.utils.get_all_elements(self.selectors.IMAGE_CLASS_NAME)
        btn_list = self.utils.get_all_elements(self.selectors.BUTTON_CLASS_NAME)
        image_list[2].click()
        
        image_list[0].click()
        self.utils.get_element_list_print(self.selectors.VIEW_CLASS_NAME)
        self.utils.get_element_list_print(self.selectors.IMAGE_CLASS_NAME)
        self.utils.get_element_list_print(self.selectors.BUTTON_CLASS_NAME)
        
        assert view_list[4].get_attribute("contentDescription") == "알림 일시 정지", "is_notifications_paused title text compare test Fail"
        assert view_list[17].get_attribute("contentDescription") == "알람을 일시적으로 끕니다.", "is_notifications_paused sub text compare test Fail"
        
        
        
    def test_logout(self):
        image_list = self.utils.get_all_elements(self.selectors.IMAGE_CLASS_NAME)
        image_list[0].click()
        image_list[2].click()
        
        
        btn_list = self.utils.get_all_elements(self.selectors.BUTTON_CLASS_NAME)
        btn_list[1].click()
        
        view_list = self.utils.get_all_elements(self.selectors.VIEW_CLASS_NAME)
        assert view_list[4].get_attribute("contentDescription") == "로그아웃 하시겠습니까?", "logout popup description test Fail"
        btn_list[1].click()
    
    
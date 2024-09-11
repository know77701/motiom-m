from utils.utils import Utils
from config.selectors import Selectors

class Home():
    def __init__(self, driver):
        self.driver = driver
        self.utils = Utils(driver)
        self.selectors = Selectors()
    
    def test_run(self):
        # self.test_home_page_ui_check()
        # self.test_profile_image_check()
        # self.test_status_bottom_sheet_ui_check()
        self.test_status_stting()
    
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
        image_list = self.utils.get_all_elements(self.selectors.IMAGE_CLASS_NAME)
        
        image_list[1].click()
        if status == "default":
            view_list[8].click()
        elif status == "busy":
            view_list[9].click()
        elif status == "metting":
            view_list[10].click()
        else:
            view_list[11].click()
        
    def check_status_stting():
        return
        
    def test_status_stting(self):
        view_list = self.utils.get_all_elements(self.selectors.VIEW_CLASS_NAME)
        image_list = self.utils.get_all_elements(self.selectors.IMAGE_CLASS_NAME)

        self.status_setting("default")
        
        assert self.utils.compare_image("status_default_user_image.png",view_list[8],"status_default_user_image.png","home"), "default status user image compare test Fail"
        image_list[1].click()
        assert self.utils.compare_image("status_setting_default.png", view_list[3], "status_setting_default.png", "home")
        self.utils.bottom_sheet_close()
        
        self.status_setting("busy")
        assert self.utils.compare_image("status_busy_user_image.png",view_list[8],"status_busy_user_image.png","home"), "busy status user image compare test Fail"
        image_list[1].click()
        assert self.utils.compare_image("status_setting_busy.png", view_list[3], "status_setting_busy.png", "home")
        self.utils.bottom_sheet_close()

        self.status_setting("metting")
        assert self.utils.compare_image("status_metting_user_image.png",view_list[8],"status_metting_user_image.png","home"), "metting status user image compare test Fail"
        image_list[1].click()
        assert self.utils.compare_image("status_setting_metting.png", view_list[3], "status_setting_metting.png", "home")
        self.utils.bottom_sheet_close()

        self.status_setting("off")
        self.utils.compare_image("status_out_of_office_user_image.png",view_list[8],"status_out_of_office_user_image.png","home"), "off status user image compare test Fail"
        image_list[1].click()
        assert self.utils.compare_image("status_setting_off.png", view_list[3], "status_setting_off.png", "home"), ""
        self.utils.bottom_sheet_close()
        self.status_setting("default")
        
        
    def test_logout(self):
        image_list = self.utils.get_all_elements(self.selectors.IMAGE_CLASS_NAME)
        image_list[0].click()
        image_list[2].click()
        
        btn_list = self.utils.get_all_elements(self.selectors.BUTTON_CLASS_NAME)
        btn_list[1].click()
        
        view_list = self.utils.get_all_elements(self.selectors.VIEW_CLASS_NAME)
        assert view_list[4].get_attribute("contentDescription") == "로그아웃 하시겠습니까?", "logout popup description test Fail"
        btn_list[1].click()
        
        
        
        

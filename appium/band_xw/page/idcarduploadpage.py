from time import sleep
import logging
from appium.webdriver.common.mobileby import MobileBy
from BigbankXW.page.basepage import BasePage
from BigbankXW.page.face_recognition_page import FaceRecognitionPage
from selenium.common.exceptions import NoSuchElementException

logging.getLogger()
logging.basicConfig(filename='runlog.log', level=logging.INFO,
                    format='%(asctime)s %(filename)s [line:%(lineno)d] %(levelname)s %(message)s')

class IdcardUploadPage(BasePage):

    idCardfront_ele = (MobileBy.CSS_SELECTOR, "#app .idCard-front .idCard-UI_card__camera")
    allowtakepicture_ele = (MobileBy.XPATH, "//*[@text='仅在使用该应用时允许'and@class='android.widget.Button']")
    # 选择相机
    select_camera_ele = (MobileBy.XPATH, "//*[@text='相机'and@resource-id='android:id/text1']")
    # 点击拍照元素
    takepicture_ele = (MobileBy.ID, "com.sec.android.app.camera:id/normal_center_button")
    # 确定拍照元素
    confirm_picture_ele = (MobileBy.ID, "com.sec.android.app.camera:id/okay")
    idCardback_ele = (MobileBy.CSS_SELECTOR, "#app .idCard-back .idCard-UI_card__camera")
    # 上传正反面图片后出现身份证姓名
    idname_ele = (MobileBy.XPATH, "//*[@class='van-field__control'and@placeholder='请输入本人姓名']")
    input_companyname_ele = (MobileBy.XPATH, "//*[@class='van-field__control'and@placeholder='请输入公司名称']")
    companyname = '金融科技公司'
    # 点击合同预览
    click_contractview_ele = (MobileBy.CSS_SELECTOR, ".xui-x-agree__text span")
    # 预览合同，向下的箭头
    gobottom_ele = (MobileBy.CSS_SELECTOR, ".xui-x-agree__go-bottom")
    # 同意签署合同
    agree_sign_ele = (MobileBy.CSS_SELECTOR, ".xui-x-agree__btn button")
    # 点击选择职业
    click_select_occupation_ele = (MobileBy.XPATH, "//*[@class='van-field__control'and@placeholder='请选择职业类别']")
    # 选择第二个职业
    select_occupation_ele = (MobileBy.CSS_SELECTOR, ".van-picker-column ul li:nth-child(2)")
    confirm_ele = (MobileBy.CSS_SELECTOR, ".popUp-button button")

    nextstep_ele = (MobileBy.CSS_SELECTOR, ".idCard-UI_ft button")
    # 是否允许获取GPS弹窗 确认按钮
    # allow_gps_alert_ele = (MobileBy.ID, "com.android.chrome:id/positive_button")
    allow_gps_alert_ele = (MobileBy.XPATH, "//*[@text='允许']")
    allow_gps_ele = (MobileBy.XPATH, "//*[@text='仅在使用该应用时允许'and@class='android.widget.Button']")


    def frontphoto_upload(self):
        self.webview_context = self.driver.context
        self.find_and_click(self.idCardfront_ele)
        sleep(1)
        # 切换到原生APP，进行拍照
        self.driver.switch_to.context("NATIVE_APP")
        # 点击授权chrome拍摄照片和录制视频（仅在使用该应用时允许）
        self.find_and_click(self.allowtakepicture_ele)
        sleep(1)
        # 选择相机
        self.find_and_click(self.select_camera_ele)
        # 点击拍照
        self.find_and_click(self.takepicture_ele)
        sleep(2)
        # 点击确定
        self.webdriver_wait(self.confirm_picture_ele).click()
        sleep(10)
        self.driver.switch_to.context(self.webview_context)
        return self

    def backphoto_upload(self):
        # # 判断出现正面图片上传元素，则点击身份证反面图片上传
        # idcardfront = self.webdriver_wait(self.idCardfront_ele)
        # if idcardfront:
        #     self.find_and_click(self.idCardback_ele)
        # else:
        #     print("上传中")

        self.webdriver_wait(self.idCardback_ele, 14).click()
        # 切换到原生APP，进行拍照
        self.driver.switch_to.context("NATIVE_APP")
        # 选择相机
        self.webdriver_wait(self.select_camera_ele).click()
        # 点击拍照
        self.find_and_click(self.takepicture_ele)
        sleep(1.5)
        # 点击确定
        self.webdriver_wait(self.confirm_picture_ele).click()
        self.driver.switch_to.context(self.webview_context)
        return self

    def input_company(self):
        try:
            if self.webdriver_wait(self.idname_ele):
                sleep(1)
                self.find_and_sendkeys(self.input_companyname_ele, self.companyname)
                sleep(0.5)
        except Exception as e:
            logging.info(e.args)
            return False
        else:
            return self

    def select_occupation(self):
        self.find_and_click(self.click_select_occupation_ele)
        sleep(0.5)
        self.find_and_click(self.select_occupation_ele)
        sleep(0.5)
        self.find_and_click(self.confirm_ele)
        sleep(0.5)
        return self

    def agree_contract(self):
        """预览个人征信、授信额度合同、个人信息查询及使用授权书"""
        try:
            sleep(1)
            self.find_and_click(self.click_contractview_ele)
            sleep(0.5)
            # 预览合同，点击向下的箭头
            self.find_and_click(self.gobottom_ele)
            sleep(6)
            # 点击同意签署
            self.find_and_click(self.agree_sign_ele)
            sleep(1)
        except NoSuchElementException:
            logging.info("Contract element is not found!")
        except Exception as e:
            # 访问异常的错误编号和详细信息
            logging.info(e.args)
        else:
            return self

    def click_nextstep(self):
        self.find_and_click(self.nextstep_ele)
        sleep(3)
        return self

    def allow_gps(self):
        try:
            self.driver.switch_to.context("NATIVE_APP")
            self.find_and_click(self.allow_gps_alert_ele)
            self.webdriver_wait(self.allow_gps_ele, 4).click()
            # self.driver.switch_to.alert.accept()
            return FaceRecognitionPage(self.driver)
        except Exception as e:
            logging.info(e.args)
            return FaceRecognitionPage(self.driver)






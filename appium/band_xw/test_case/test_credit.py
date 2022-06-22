import random
import pytest
import yaml
from BigbankXW.page.app import App


class TestCredit:

    # with open("../config/userinfo.yaml", encoding='utf-8') as f:
    #     userinfo = yaml.safe_load(f)  # 读取手机号

    mobile_list = [str(random.randint(19122101152, 19222999999)) for i in range(1)]

    def setup(self):
        self.chrome = App()

    @pytest.mark.parametrize("mobile", mobile_list)
    def test_credit(self, mobile):
        self.loginpage = self.chrome.start().gotofirstpage().selectchannel().\
            setmobile(mobile).click_jump().checkcredit()
        self.idcardpage = self.loginpage.input_mobile(mobile).getsms().inputsms().\
            clicklogin().reg_contract_view()
        self.idcardpage.frontphoto_upload().backphoto_upload().input_company().\
            select_occupation().agree_contract().click_nextstep().allow_gps()

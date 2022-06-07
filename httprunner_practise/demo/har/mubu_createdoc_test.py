# NOTE: Generated By HttpRunner v3.1.11
# FROM: har\mubu_createdoc.yml


from httprunner import HttpRunner, Config, Step, RunRequest, RunTestCase


class TestCaseMubuCreatedoc(HttpRunner):

    config = Config("testcase description").verify(False)

    teststeps = [
        Step(
            RunRequest("/v3/api/user/phone_login")
            .post("https://api2.mubu.com/v3/api/user/phone_login")
            .with_headers(
                **{
                    "accept": "application/json, text/plain, */*",
                    "accept-encoding": "gzip, deflate, br",
                    "accept-language": "zh-CN,zh;q=0.9,zh-TW;q=0.8,en-US;q=0.7,en;q=0.6",
                    "content-length": "65",
                    "content-type": "application/json;charset=UTF-8",
                    "data-unique-id": "99620c70-dd98-11ec-8003-35b78b1e9458",
                    "jwt-token": "",
                    "origin": "https://mubu.com",
                    "referer": "https://mubu.com/",
                    "sec-ch-ua": '" Not A;Brand";v="99", "Chromium";v="100", "Google Chrome";v="100"',
                    "sec-ch-ua-mobile": "?0",
                    "sec-ch-ua-platform": '"Windows"',
                    "sec-fetch-dest": "empty",
                    "sec-fetch-mode": "cors",
                    "sec-fetch-site": "same-site",
                    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36",
                    "version": "3.0.0-2.0.0.1824",
                    "x-request-id": "9d41b7f7-6c38-4a41-a197-bfd1a8154f85",
                }
            )
            .with_json(
                {"callbackType": 0, "password": "gxl10230701", "phone": "15222186256"}
            )
            .validate()
            .assert_equal("status_code", 200)
            .assert_equal("body.code", 0)
        ),
        Step(
            RunRequest("/v3/api/user/profile")
            .post("https://api2.mubu.com/v3/api/user/profile")
            .with_headers(
                **{
                    "accept": "application/json, text/plain, */*",
                    "accept-encoding": "gzip, deflate, br",
                    "accept-language": "zh-CN,zh;q=0.9,zh-TW;q=0.8,en-US;q=0.7,en;q=0.6",
                    "content-length": "0",
                    "data-unique-id": "99620c70-dd98-11ec-8003-35b78b1e9458",
                    "jwt-token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiJ9.eyJhcHAiOiJtdWJ1Iiwic3ViIjoiOTAzNjU3MiIsImxvZ2luVHlwZSI6Im1vYmlsZSIsImV4cCI6MTY1NjIzMjgyNiwiaWF0IjoxNjUzNjQwODI2fQ.pAjYnbr7Lku5kzJ2Nr8dlZQx_V-2yO79frpxqSJcE-EznHQA5w3SXBYN6V2VqRXTz2UaMKCP9KTEocFe-Op-Kw",
                    "origin": "https://mubu.com",
                    "referer": "https://mubu.com/",
                    "sec-ch-ua": '" Not A;Brand";v="99", "Chromium";v="100", "Google Chrome";v="100"',
                    "sec-ch-ua-mobile": "?0",
                    "sec-ch-ua-platform": '"Windows"',
                    "sec-fetch-dest": "empty",
                    "sec-fetch-mode": "cors",
                    "sec-fetch-site": "same-site",
                    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36",
                    "version": "3.0.0-2.0.0.1824",
                    "x-request-id": "f1de07c0-4ca6-4307-8d4a-8d37cf5256dc",
                }
            )
            .with_data("")
            .validate()
            .assert_equal("status_code", 200)
            .assert_equal("body.code", 0)
        ),
        Step(
            RunRequest("/v3/api/activity/five_years/participation")
            .post("https://api2.mubu.com/v3/api/activity/five_years/participation")
            .with_headers(
                **{
                    "accept": "application/json, text/plain, */*",
                    "accept-encoding": "gzip, deflate, br",
                    "accept-language": "zh-CN,zh;q=0.9,zh-TW;q=0.8,en-US;q=0.7,en;q=0.6",
                    "content-length": "0",
                    "data-unique-id": "99620c70-dd98-11ec-8003-35b78b1e9458",
                    "jwt-token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiJ9.eyJhcHAiOiJtdWJ1Iiwic3ViIjoiOTAzNjU3MiIsImxvZ2luVHlwZSI6Im1vYmlsZSIsImV4cCI6MTY1NjIzMjgyNiwiaWF0IjoxNjUzNjQwODI2fQ.pAjYnbr7Lku5kzJ2Nr8dlZQx_V-2yO79frpxqSJcE-EznHQA5w3SXBYN6V2VqRXTz2UaMKCP9KTEocFe-Op-Kw",
                    "origin": "https://mubu.com",
                    "referer": "https://mubu.com/",
                    "sec-ch-ua": '" Not A;Brand";v="99", "Chromium";v="100", "Google Chrome";v="100"',
                    "sec-ch-ua-mobile": "?0",
                    "sec-ch-ua-platform": '"Windows"',
                    "sec-fetch-dest": "empty",
                    "sec-fetch-mode": "cors",
                    "sec-fetch-site": "same-site",
                    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36",
                    "version": "3.0.0-2.0.0.1824",
                    "x-request-id": "41c7b2b3-4fe7-4e13-8e1f-ac30b9412fb2",
                }
            )
            .with_data("")
            .validate()
            .assert_equal("status_code", 200)
            .assert_equal("body.code", 4011)
            .assert_equal("body.msg", "unknown error")
        ),
        Step(
            RunRequest("/v3/api/list/get_all_documents_page")
            .post("https://api2.mubu.com/v3/api/list/get_all_documents_page")
            .with_headers(
                **{
                    "accept": "application/json, text/plain, */*",
                    "accept-encoding": "gzip, deflate, br",
                    "accept-language": "zh-CN,zh;q=0.9,zh-TW;q=0.8,en-US;q=0.7,en;q=0.6",
                    "content-length": "12",
                    "content-type": "application/json;charset=UTF-8",
                    "data-unique-id": "99620c70-dd98-11ec-8003-35b78b1e9458",
                    "jwt-token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiJ9.eyJhcHAiOiJtdWJ1Iiwic3ViIjoiOTAzNjU3MiIsImxvZ2luVHlwZSI6Im1vYmlsZSIsImV4cCI6MTY1NjIzMjgyNiwiaWF0IjoxNjUzNjQwODI2fQ.pAjYnbr7Lku5kzJ2Nr8dlZQx_V-2yO79frpxqSJcE-EznHQA5w3SXBYN6V2VqRXTz2UaMKCP9KTEocFe-Op-Kw",
                    "origin": "https://mubu.com",
                    "referer": "https://mubu.com/",
                    "sec-ch-ua": '" Not A;Brand";v="99", "Chromium";v="100", "Google Chrome";v="100"',
                    "sec-ch-ua-mobile": "?0",
                    "sec-ch-ua-platform": '"Windows"',
                    "sec-fetch-dest": "empty",
                    "sec-fetch-mode": "cors",
                    "sec-fetch-site": "same-site",
                    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36",
                    "version": "3.0.0-2.0.0.1824",
                    "x-request-id": "07ae2309-0b60-48bf-8718-cc6b49cd2c5c",
                }
            )
            .with_json({"start": ""})
            .validate()
            .assert_equal("status_code", 200)
            .assert_equal("body.code", 0)
        ),
        Step(
            RunRequest("/v3/api/list/star_relation/get")
            .get("https://api2.mubu.com/v3/api/list/star_relation/get")
            .with_headers(
                **{
                    "accept": "application/json, text/plain, */*",
                    "accept-encoding": "gzip, deflate, br",
                    "accept-language": "zh-CN,zh;q=0.9,zh-TW;q=0.8,en-US;q=0.7,en;q=0.6",
                    "data-unique-id": "99620c70-dd98-11ec-8003-35b78b1e9458",
                    "jwt-token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiJ9.eyJhcHAiOiJtdWJ1Iiwic3ViIjoiOTAzNjU3MiIsImxvZ2luVHlwZSI6Im1vYmlsZSIsImV4cCI6MTY1NjIzMjgyNiwiaWF0IjoxNjUzNjQwODI2fQ.pAjYnbr7Lku5kzJ2Nr8dlZQx_V-2yO79frpxqSJcE-EznHQA5w3SXBYN6V2VqRXTz2UaMKCP9KTEocFe-Op-Kw",
                    "origin": "https://mubu.com",
                    "referer": "https://mubu.com/",
                    "sec-ch-ua": '" Not A;Brand";v="99", "Chromium";v="100", "Google Chrome";v="100"',
                    "sec-ch-ua-mobile": "?0",
                    "sec-ch-ua-platform": '"Windows"',
                    "sec-fetch-dest": "empty",
                    "sec-fetch-mode": "cors",
                    "sec-fetch-site": "same-site",
                    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36",
                    "version": "3.0.0-2.0.0.1824",
                    "x-request-id": "92aa82c8-d2e1-4992-aecc-b14156219467",
                }
            )
            .validate()
            .assert_equal("status_code", 200)
            .assert_equal("body.code", 0)
        ),
        Step(
            RunRequest("/v3/api/user/get_user_params")
            .post("https://api2.mubu.com/v3/api/user/get_user_params")
            .with_headers(
                **{
                    "accept": "application/json, text/plain, */*",
                    "accept-encoding": "gzip, deflate, br",
                    "accept-language": "zh-CN,zh;q=0.9,zh-TW;q=0.8,en-US;q=0.7,en;q=0.6",
                    "content-length": "0",
                    "data-unique-id": "99620c70-dd98-11ec-8003-35b78b1e9458",
                    "jwt-token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiJ9.eyJhcHAiOiJtdWJ1Iiwic3ViIjoiOTAzNjU3MiIsImxvZ2luVHlwZSI6Im1vYmlsZSIsImV4cCI6MTY1NjIzMjgyNiwiaWF0IjoxNjUzNjQwODI2fQ.pAjYnbr7Lku5kzJ2Nr8dlZQx_V-2yO79frpxqSJcE-EznHQA5w3SXBYN6V2VqRXTz2UaMKCP9KTEocFe-Op-Kw",
                    "origin": "https://mubu.com",
                    "referer": "https://mubu.com/",
                    "sec-ch-ua": '" Not A;Brand";v="99", "Chromium";v="100", "Google Chrome";v="100"',
                    "sec-ch-ua-mobile": "?0",
                    "sec-ch-ua-platform": '"Windows"',
                    "sec-fetch-dest": "empty",
                    "sec-fetch-mode": "cors",
                    "sec-fetch-site": "same-site",
                    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36",
                    "version": "3.0.0-2.0.0.1824",
                    "x-request-id": "2e9348d0-d2c7-479d-a255-8c8499dbe070",
                }
            )
            .with_data("")
            .validate()
            .assert_equal("status_code", 200)
            .assert_equal("body.code", 0)
        ),
        Step(
            RunRequest("/v3/api/message/get_message_unread")
            .post("https://api2.mubu.com/v3/api/message/get_message_unread")
            .with_headers(
                **{
                    "accept": "application/json, text/plain, */*",
                    "accept-encoding": "gzip, deflate, br",
                    "accept-language": "zh-CN,zh;q=0.9,zh-TW;q=0.8,en-US;q=0.7,en;q=0.6",
                    "content-length": "10",
                    "content-type": "application/json;charset=UTF-8",
                    "data-unique-id": "99620c70-dd98-11ec-8003-35b78b1e9458",
                    "jwt-token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiJ9.eyJhcHAiOiJtdWJ1Iiwic3ViIjoiOTAzNjU3MiIsImxvZ2luVHlwZSI6Im1vYmlsZSIsImV4cCI6MTY1NjIzMjgyNiwiaWF0IjoxNjUzNjQwODI2fQ.pAjYnbr7Lku5kzJ2Nr8dlZQx_V-2yO79frpxqSJcE-EznHQA5w3SXBYN6V2VqRXTz2UaMKCP9KTEocFe-Op-Kw",
                    "origin": "https://mubu.com",
                    "referer": "https://mubu.com/",
                    "sec-ch-ua": '" Not A;Brand";v="99", "Chromium";v="100", "Google Chrome";v="100"',
                    "sec-ch-ua-mobile": "?0",
                    "sec-ch-ua-platform": '"Windows"',
                    "sec-fetch-dest": "empty",
                    "sec-fetch-mode": "cors",
                    "sec-fetch-site": "same-site",
                    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36",
                    "version": "3.0.0-2.0.0.1824",
                    "x-request-id": "ad926491-a99c-4e2c-ba88-4a359cb4aedc",
                }
            )
            .with_json({"page": 1})
            .validate()
            .assert_equal("status_code", 200)
            .assert_equal("body.code", 0)
        ),
        Step(
            RunRequest("/v3/api/user/get_onboard_state")
            .post("https://api2.mubu.com/v3/api/user/get_onboard_state")
            .with_headers(
                **{
                    "accept": "application/json, text/plain, */*",
                    "accept-encoding": "gzip, deflate, br",
                    "accept-language": "zh-CN,zh;q=0.9,zh-TW;q=0.8,en-US;q=0.7,en;q=0.6",
                    "content-length": "2",
                    "content-type": "application/json;charset=UTF-8",
                    "data-unique-id": "99620c70-dd98-11ec-8003-35b78b1e9458",
                    "jwt-token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiJ9.eyJhcHAiOiJtdWJ1Iiwic3ViIjoiOTAzNjU3MiIsImxvZ2luVHlwZSI6Im1vYmlsZSIsImV4cCI6MTY1NjIzMjgyNiwiaWF0IjoxNjUzNjQwODI2fQ.pAjYnbr7Lku5kzJ2Nr8dlZQx_V-2yO79frpxqSJcE-EznHQA5w3SXBYN6V2VqRXTz2UaMKCP9KTEocFe-Op-Kw",
                    "origin": "https://mubu.com",
                    "referer": "https://mubu.com/",
                    "sec-ch-ua": '" Not A;Brand";v="99", "Chromium";v="100", "Google Chrome";v="100"',
                    "sec-ch-ua-mobile": "?0",
                    "sec-ch-ua-platform": '"Windows"',
                    "sec-fetch-dest": "empty",
                    "sec-fetch-mode": "cors",
                    "sec-fetch-site": "same-site",
                    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36",
                    "version": "3.0.0-2.0.0.1824",
                    "x-request-id": "5962168b-d1de-41c8-8e22-d58e02bddc23",
                }
            )
            .with_json({})
            .validate()
            .assert_equal("status_code", 200)
            .assert_equal("body.code", 0)
        ),
        Step(
            RunRequest("/v3/api/list/item_count")
            .post("https://api2.mubu.com/v3/api/list/item_count")
            .with_headers(
                **{
                    "accept": "application/json, text/plain, */*",
                    "accept-encoding": "gzip, deflate, br",
                    "accept-language": "zh-CN,zh;q=0.9,zh-TW;q=0.8,en-US;q=0.7,en;q=0.6",
                    "content-length": "30",
                    "content-type": "application/json;charset=UTF-8",
                    "data-unique-id": "99620c70-dd98-11ec-8003-35b78b1e9458",
                    "jwt-token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiJ9.eyJhcHAiOiJtdWJ1Iiwic3ViIjoiOTAzNjU3MiIsImxvZ2luVHlwZSI6Im1vYmlsZSIsImV4cCI6MTY1NjIzMjgyNiwiaWF0IjoxNjUzNjQwODI2fQ.pAjYnbr7Lku5kzJ2Nr8dlZQx_V-2yO79frpxqSJcE-EznHQA5w3SXBYN6V2VqRXTz2UaMKCP9KTEocFe-Op-Kw",
                    "origin": "https://mubu.com",
                    "referer": "https://mubu.com/",
                    "sec-ch-ua": '" Not A;Brand";v="99", "Chromium";v="100", "Google Chrome";v="100"',
                    "sec-ch-ua-mobile": "?0",
                    "sec-ch-ua-platform": '"Windows"',
                    "sec-fetch-dest": "empty",
                    "sec-fetch-mode": "cors",
                    "sec-fetch-site": "same-site",
                    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36",
                    "version": "3.0.0-2.0.0.1824",
                    "x-request-id": "3fa8b686-4337-4ed0-88a5-91a828f1103c",
                }
            )
            .with_json({"folderId": 0, "source": "home"})
            .validate()
            .assert_equal("status_code", 200)
            .assert_equal("body.code", 0)
        ),
        Step(
            RunRequest("/v3/api/advertisement/get")
            .post("https://api2.mubu.com/v3/api/advertisement/get")
            .with_headers(
                **{
                    "accept": "application/json, text/plain, */*",
                    "accept-encoding": "gzip, deflate, br",
                    "accept-language": "zh-CN,zh;q=0.9,zh-TW;q=0.8,en-US;q=0.7,en;q=0.6",
                    "content-length": "10",
                    "content-type": "application/json;charset=UTF-8",
                    "data-unique-id": "99620c70-dd98-11ec-8003-35b78b1e9458",
                    "jwt-token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiJ9.eyJhcHAiOiJtdWJ1Iiwic3ViIjoiOTAzNjU3MiIsImxvZ2luVHlwZSI6Im1vYmlsZSIsImV4cCI6MTY1NjIzMjgyNiwiaWF0IjoxNjUzNjQwODI2fQ.pAjYnbr7Lku5kzJ2Nr8dlZQx_V-2yO79frpxqSJcE-EznHQA5w3SXBYN6V2VqRXTz2UaMKCP9KTEocFe-Op-Kw",
                    "origin": "https://mubu.com",
                    "referer": "https://mubu.com/",
                    "sec-ch-ua": '" Not A;Brand";v="99", "Chromium";v="100", "Google Chrome";v="100"',
                    "sec-ch-ua-mobile": "?0",
                    "sec-ch-ua-platform": '"Windows"',
                    "sec-fetch-dest": "empty",
                    "sec-fetch-mode": "cors",
                    "sec-fetch-site": "same-site",
                    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36",
                    "version": "3.0.0-2.0.0.1824",
                    "x-request-id": "71adbabd-ebc0-4ef6-912c-cafec3e92b32",
                }
            )
            .with_json({"type": 1})
            .validate()
            .assert_equal("status_code", 200)
            .assert_equal("body.code", 0)
        ),
        Step(
            RunRequest("/v3/api/notify/new_tip/get")
            .post("https://api2.mubu.com/v3/api/notify/new_tip/get")
            .with_headers(
                **{
                    "accept": "application/json, text/plain, */*",
                    "accept-encoding": "gzip, deflate, br",
                    "accept-language": "zh-CN,zh;q=0.9,zh-TW;q=0.8,en-US;q=0.7,en;q=0.6",
                    "content-length": "10",
                    "content-type": "application/json;charset=UTF-8",
                    "data-unique-id": "99620c70-dd98-11ec-8003-35b78b1e9458",
                    "jwt-token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiJ9.eyJhcHAiOiJtdWJ1Iiwic3ViIjoiOTAzNjU3MiIsImxvZ2luVHlwZSI6Im1vYmlsZSIsImV4cCI6MTY1NjIzMjgyNiwiaWF0IjoxNjUzNjQwODI2fQ.pAjYnbr7Lku5kzJ2Nr8dlZQx_V-2yO79frpxqSJcE-EznHQA5w3SXBYN6V2VqRXTz2UaMKCP9KTEocFe-Op-Kw",
                    "origin": "https://mubu.com",
                    "referer": "https://mubu.com/",
                    "sec-ch-ua": '" Not A;Brand";v="99", "Chromium";v="100", "Google Chrome";v="100"',
                    "sec-ch-ua-mobile": "?0",
                    "sec-ch-ua-platform": '"Windows"',
                    "sec-fetch-dest": "empty",
                    "sec-fetch-mode": "cors",
                    "sec-fetch-site": "same-site",
                    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36",
                    "version": "3.0.0-2.0.0.1824",
                    "x-request-id": "e41b9d6f-aa46-41d7-8bf0-01f2f6545c13",
                }
            )
            .with_json({"type": 1})
            .validate()
            .assert_equal("status_code", 200)
            .assert_equal("body.code", 0)
        ),
        Step(
            RunRequest("/v3/api/list/create_doc")
            .post("https://api2.mubu.com/v3/api/list/create_doc")
            .with_headers(
                **{
                    "accept": "application/json, text/plain, */*",
                    "accept-encoding": "gzip, deflate, br",
                    "accept-language": "zh-CN,zh;q=0.9,zh-TW;q=0.8,en-US;q=0.7,en;q=0.6",
                    "content-length": "25",
                    "content-type": "application/json;charset=UTF-8",
                    "data-unique-id": "99620c70-dd98-11ec-8003-35b78b1e9458",
                    "jwt-token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiJ9.eyJhcHAiOiJtdWJ1Iiwic3ViIjoiOTAzNjU3MiIsImxvZ2luVHlwZSI6Im1vYmlsZSIsImV4cCI6MTY1NjIzMjgyNiwiaWF0IjoxNjUzNjQwODI2fQ.pAjYnbr7Lku5kzJ2Nr8dlZQx_V-2yO79frpxqSJcE-EznHQA5w3SXBYN6V2VqRXTz2UaMKCP9KTEocFe-Op-Kw",
                    "origin": "https://mubu.com",
                    "referer": "https://mubu.com/",
                    "sec-ch-ua": '" Not A;Brand";v="99", "Chromium";v="100", "Google Chrome";v="100"',
                    "sec-ch-ua-mobile": "?0",
                    "sec-ch-ua-platform": '"Windows"',
                    "sec-fetch-dest": "empty",
                    "sec-fetch-mode": "cors",
                    "sec-fetch-site": "same-site",
                    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36",
                    "version": "3.0.0-2.0.0.1824",
                    "x-request-id": "465ce0c5-e8fa-4bd0-a108-7484271fba48",
                }
            )
            .with_json({"folderId": "0", "type": 0})
            .validate()
            .assert_equal("status_code", 200)
            .assert_equal("body.code", 0)
        ),
        Step(
            RunRequest("/v3/api/list/item_count")
            .post("https://api2.mubu.com/v3/api/list/item_count")
            .with_headers(
                **{
                    "accept": "application/json, text/plain, */*",
                    "accept-encoding": "gzip, deflate, br",
                    "accept-language": "zh-CN,zh;q=0.9,zh-TW;q=0.8,en-US;q=0.7,en;q=0.6",
                    "content-length": "30",
                    "content-type": "application/json;charset=UTF-8",
                    "data-unique-id": "99620c70-dd98-11ec-8003-35b78b1e9458",
                    "jwt-token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiJ9.eyJhcHAiOiJtdWJ1Iiwic3ViIjoiOTAzNjU3MiIsImxvZ2luVHlwZSI6Im1vYmlsZSIsImV4cCI6MTY1NjIzMjgyNiwiaWF0IjoxNjUzNjQwODI2fQ.pAjYnbr7Lku5kzJ2Nr8dlZQx_V-2yO79frpxqSJcE-EznHQA5w3SXBYN6V2VqRXTz2UaMKCP9KTEocFe-Op-Kw",
                    "origin": "https://mubu.com",
                    "referer": "https://mubu.com/",
                    "sec-ch-ua": '" Not A;Brand";v="99", "Chromium";v="100", "Google Chrome";v="100"',
                    "sec-ch-ua-mobile": "?0",
                    "sec-ch-ua-platform": '"Windows"',
                    "sec-fetch-dest": "empty",
                    "sec-fetch-mode": "cors",
                    "sec-fetch-site": "same-site",
                    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36",
                    "version": "3.0.0-2.0.0.1824",
                    "x-request-id": "55c6311f-6c6a-4de3-be66-b27422ee1936",
                }
            )
            .with_json({"folderId": 0, "source": "home"})
            .validate()
            .assert_equal("status_code", 200)
            .assert_equal("body.code", 0)
        ),
        Step(
            RunRequest("/v3/api/document/edit/get")
            .post("https://api2.mubu.com/v3/api/document/edit/get")
            .with_headers(
                **{
                    "accept": "application/json, text/plain, */*",
                    "accept-encoding": "gzip, deflate, br",
                    "accept-language": "zh-CN,zh;q=0.9,zh-TW;q=0.8,en-US;q=0.7,en;q=0.6",
                    "content-length": "37",
                    "content-type": "application/json;charset=UTF-8",
                    "data-unique-id": "99620c70-dd98-11ec-8003-35b78b1e9458",
                    "jwt-token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiJ9.eyJhcHAiOiJtdWJ1Iiwic3ViIjoiOTAzNjU3MiIsImxvZ2luVHlwZSI6Im1vYmlsZSIsImV4cCI6MTY1NjIzMjgyNiwiaWF0IjoxNjUzNjQwODI2fQ.pAjYnbr7Lku5kzJ2Nr8dlZQx_V-2yO79frpxqSJcE-EznHQA5w3SXBYN6V2VqRXTz2UaMKCP9KTEocFe-Op-Kw",
                    "origin": "https://mubu.com",
                    "referer": "https://mubu.com/",
                    "sec-ch-ua": '" Not A;Brand";v="99", "Chromium";v="100", "Google Chrome";v="100"',
                    "sec-ch-ua-mobile": "?0",
                    "sec-ch-ua-platform": '"Windows"',
                    "sec-fetch-dest": "empty",
                    "sec-fetch-mode": "cors",
                    "sec-fetch-site": "same-site",
                    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36",
                    "version": "3.0.0-2.0.0.1824",
                    "x-request-id": "8de9181e-6a01-44ff-aa30-a9143c06b585",
                }
            )
            .with_json({"docId": "1GzYU6TExhc", "password": ""})
            .validate()
            .assert_equal("status_code", 200)
            .assert_equal("body.code", 0)
        ),
        Step(
            RunRequest("/v3/api/refer/doc/list")
            .post("https://api2.mubu.com/v3/api/refer/doc/list")
            .with_headers(
                **{
                    "accept": "application/json, text/plain, */*",
                    "accept-encoding": "gzip, deflate, br",
                    "accept-language": "zh-CN,zh;q=0.9,zh-TW;q=0.8,en-US;q=0.7,en;q=0.6",
                    "content-length": "29",
                    "content-type": "application/json;charset=UTF-8",
                    "data-unique-id": "99620c70-dd98-11ec-8003-35b78b1e9458",
                    "jwt-token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiJ9.eyJhcHAiOiJtdWJ1Iiwic3ViIjoiOTAzNjU3MiIsImxvZ2luVHlwZSI6Im1vYmlsZSIsImV4cCI6MTY1NjIzMjgyNiwiaWF0IjoxNjUzNjQwODI2fQ.pAjYnbr7Lku5kzJ2Nr8dlZQx_V-2yO79frpxqSJcE-EznHQA5w3SXBYN6V2VqRXTz2UaMKCP9KTEocFe-Op-Kw",
                    "origin": "https://mubu.com",
                    "referer": "https://mubu.com/",
                    "sec-ch-ua": '" Not A;Brand";v="99", "Chromium";v="100", "Google Chrome";v="100"',
                    "sec-ch-ua-mobile": "?0",
                    "sec-ch-ua-platform": '"Windows"',
                    "sec-fetch-dest": "empty",
                    "sec-fetch-mode": "cors",
                    "sec-fetch-site": "same-site",
                    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36",
                    "x-request-id": "b3d838de-6a8a-4c00-b826-19649b04c673",
                }
            )
            .with_json({"targetDocId": "1GzYU6TExhc"})
            .validate()
            .assert_equal("status_code", 200)
            .assert_equal("body.code", 0)
        ),
        Step(
            RunRequest("/v3/api/colla/register")
            .get("https://api2.mubu.com/v3/api/colla/register")
            .with_headers(
                **{
                    "accept": "application/json, text/plain, */*",
                    "accept-encoding": "gzip, deflate, br",
                    "accept-language": "zh-CN,zh;q=0.9,zh-TW;q=0.8,en-US;q=0.7,en;q=0.6",
                    "data-unique-id": "99620c70-dd98-11ec-8003-35b78b1e9458",
                    "jwt-token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiJ9.eyJhcHAiOiJtdWJ1Iiwic3ViIjoiOTAzNjU3MiIsImxvZ2luVHlwZSI6Im1vYmlsZSIsImV4cCI6MTY1NjIzMjgyNiwiaWF0IjoxNjUzNjQwODI2fQ.pAjYnbr7Lku5kzJ2Nr8dlZQx_V-2yO79frpxqSJcE-EznHQA5w3SXBYN6V2VqRXTz2UaMKCP9KTEocFe-Op-Kw",
                    "origin": "https://mubu.com",
                    "referer": "https://mubu.com/",
                    "sec-ch-ua": '" Not A;Brand";v="99", "Chromium";v="100", "Google Chrome";v="100"',
                    "sec-ch-ua-mobile": "?0",
                    "sec-ch-ua-platform": '"Windows"',
                    "sec-fetch-dest": "empty",
                    "sec-fetch-mode": "cors",
                    "sec-fetch-site": "same-site",
                    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36",
                    "x-request-id": "bb3e3686-5587-47db-a146-7ff88196da83",
                }
            )
            .validate()
            .assert_equal("status_code", 200)
            .assert_equal("body.code", 0)
        ),
        Step(
            RunRequest("/v3/api/refer/node/count")
            .post("https://api2.mubu.com/v3/api/refer/node/count")
            .with_headers(
                **{
                    "accept": "application/json, text/plain, */*",
                    "accept-encoding": "gzip, deflate, br",
                    "accept-language": "zh-CN,zh;q=0.9,zh-TW;q=0.8,en-US;q=0.7,en;q=0.6",
                    "content-length": "29",
                    "content-type": "application/json;charset=UTF-8",
                    "data-unique-id": "99620c70-dd98-11ec-8003-35b78b1e9458",
                    "jwt-token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiJ9.eyJhcHAiOiJtdWJ1Iiwic3ViIjoiOTAzNjU3MiIsImxvZ2luVHlwZSI6Im1vYmlsZSIsImV4cCI6MTY1NjIzMjgyNiwiaWF0IjoxNjUzNjQwODI2fQ.pAjYnbr7Lku5kzJ2Nr8dlZQx_V-2yO79frpxqSJcE-EznHQA5w3SXBYN6V2VqRXTz2UaMKCP9KTEocFe-Op-Kw",
                    "origin": "https://mubu.com",
                    "referer": "https://mubu.com/",
                    "sec-ch-ua": '" Not A;Brand";v="99", "Chromium";v="100", "Google Chrome";v="100"',
                    "sec-ch-ua-mobile": "?0",
                    "sec-ch-ua-platform": '"Windows"',
                    "sec-fetch-dest": "empty",
                    "sec-fetch-mode": "cors",
                    "sec-fetch-site": "same-site",
                    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36",
                    "version": "3.0.0-2.0.0.1824",
                    "x-request-id": "1797c216-d4f6-4f8e-876e-2e402f7ffdc4",
                }
            )
            .with_json({"targetDocId": "1GzYU6TExhc"})
            .validate()
            .assert_equal("status_code", 200)
            .assert_equal("body.code", 0)
        ),
        Step(
            RunRequest("/v3/api/colla/members_v2")
            .post("https://api2.mubu.com/v3/api/colla/members_v2")
            .with_headers(
                **{
                    "accept": "application/json, text/plain, */*",
                    "accept-encoding": "gzip, deflate, br",
                    "accept-language": "zh-CN,zh;q=0.9,zh-TW;q=0.8,en-US;q=0.7,en;q=0.6",
                    "content-length": "58",
                    "content-type": "application/json;charset=UTF-8",
                    "data-unique-id": "99620c70-dd98-11ec-8003-35b78b1e9458",
                    "jwt-token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiJ9.eyJhcHAiOiJtdWJ1Iiwic3ViIjoiOTAzNjU3MiIsImxvZ2luVHlwZSI6Im1vYmlsZSIsImV4cCI6MTY1NjIzMjgyNiwiaWF0IjoxNjUzNjQwODI2fQ.pAjYnbr7Lku5kzJ2Nr8dlZQx_V-2yO79frpxqSJcE-EznHQA5w3SXBYN6V2VqRXTz2UaMKCP9KTEocFe-Op-Kw",
                    "origin": "https://mubu.com",
                    "referer": "https://mubu.com/",
                    "request-id": "members:8101667156423848:1653640835485",
                    "sec-ch-ua": '" Not A;Brand";v="99", "Chromium";v="100", "Google Chrome";v="100"',
                    "sec-ch-ua-mobile": "?0",
                    "sec-ch-ua-platform": '"Windows"',
                    "sec-fetch-dest": "empty",
                    "sec-fetch-mode": "cors",
                    "sec-fetch-site": "same-site",
                    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36",
                    "x-request-id": "9a81c943-2ccc-422e-877c-cc844a454bff",
                }
            )
            .with_json({"documentId": "1GzYU6TExhc", "memberId": "8101667156423848"})
            .validate()
            .assert_equal("status_code", 200)
            .assert_equal("body.code", 0)
        ),
        Step(
            RunRequest("/v3/api/refer/search_refers")
            .post("https://api2.mubu.com/v3/api/refer/search_refers")
            .with_headers(
                **{
                    "accept": "application/json, text/plain, */*",
                    "accept-encoding": "gzip, deflate, br",
                    "accept-language": "zh-CN,zh;q=0.9,zh-TW;q=0.8,en-US;q=0.7,en;q=0.6",
                    "content-length": "54",
                    "content-type": "application/json;charset=UTF-8",
                    "data-unique-id": "99620c70-dd98-11ec-8003-35b78b1e9458",
                    "jwt-token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiJ9.eyJhcHAiOiJtdWJ1Iiwic3ViIjoiOTAzNjU3MiIsImxvZ2luVHlwZSI6Im1vYmlsZSIsImV4cCI6MTY1NjIzMjgyNiwiaWF0IjoxNjUzNjQwODI2fQ.pAjYnbr7Lku5kzJ2Nr8dlZQx_V-2yO79frpxqSJcE-EznHQA5w3SXBYN6V2VqRXTz2UaMKCP9KTEocFe-Op-Kw",
                    "origin": "https://mubu.com",
                    "referer": "https://mubu.com/",
                    "sec-ch-ua": '" Not A;Brand";v="99", "Chromium";v="100", "Google Chrome";v="100"',
                    "sec-ch-ua-mobile": "?0",
                    "sec-ch-ua-platform": '"Windows"',
                    "sec-fetch-dest": "empty",
                    "sec-fetch-mode": "cors",
                    "sec-fetch-site": "same-site",
                    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36",
                    "x-request-id": "2fb29589-9fb7-4177-bade-b2109bc3c607",
                }
            )
            .with_json({"docId": "1GzYU6TExhc", "keywords": "辩题", "option": 1})
            .validate()
            .assert_equal("status_code", 200)
            .assert_equal("body.code", 0)
        ),
        Step(
            RunRequest("/v3/api/refer/search_refers")
            .post("https://api2.mubu.com/v3/api/refer/search_refers")
            .with_headers(
                **{
                    "accept": "application/json, text/plain, */*",
                    "accept-encoding": "gzip, deflate, br",
                    "accept-language": "zh-CN,zh;q=0.9,zh-TW;q=0.8,en-US;q=0.7,en;q=0.6",
                    "content-length": "54",
                    "content-type": "application/json;charset=UTF-8",
                    "data-unique-id": "99620c70-dd98-11ec-8003-35b78b1e9458",
                    "jwt-token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiJ9.eyJhcHAiOiJtdWJ1Iiwic3ViIjoiOTAzNjU3MiIsImxvZ2luVHlwZSI6Im1vYmlsZSIsImV4cCI6MTY1NjIzMjgyNiwiaWF0IjoxNjUzNjQwODI2fQ.pAjYnbr7Lku5kzJ2Nr8dlZQx_V-2yO79frpxqSJcE-EznHQA5w3SXBYN6V2VqRXTz2UaMKCP9KTEocFe-Op-Kw",
                    "origin": "https://mubu.com",
                    "referer": "https://mubu.com/",
                    "sec-ch-ua": '" Not A;Brand";v="99", "Chromium";v="100", "Google Chrome";v="100"',
                    "sec-ch-ua-mobile": "?0",
                    "sec-ch-ua-platform": '"Windows"',
                    "sec-fetch-dest": "empty",
                    "sec-fetch-mode": "cors",
                    "sec-fetch-site": "same-site",
                    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36",
                    "x-request-id": "c3f038b4-7aa3-46b5-b61c-81c7ce83c6ec",
                }
            )
            .with_json({"docId": "1GzYU6TExhc", "keywords": "标题", "option": 1})
            .validate()
            .assert_equal("status_code", 200)
            .assert_equal("body.code", 0)
        ),
        Step(
            RunRequest("/v3/api/list/item_count")
            .post("https://api2.mubu.com/v3/api/list/item_count")
            .with_headers(
                **{
                    "accept": "application/json, text/plain, */*",
                    "accept-encoding": "gzip, deflate, br",
                    "accept-language": "zh-CN,zh;q=0.9,zh-TW;q=0.8,en-US;q=0.7,en;q=0.6",
                    "content-length": "30",
                    "content-type": "application/json;charset=UTF-8",
                    "data-unique-id": "99620c70-dd98-11ec-8003-35b78b1e9458",
                    "jwt-token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiJ9.eyJhcHAiOiJtdWJ1Iiwic3ViIjoiOTAzNjU3MiIsImxvZ2luVHlwZSI6Im1vYmlsZSIsImV4cCI6MTY1NjIzMjgyNiwiaWF0IjoxNjUzNjQwODI2fQ.pAjYnbr7Lku5kzJ2Nr8dlZQx_V-2yO79frpxqSJcE-EznHQA5w3SXBYN6V2VqRXTz2UaMKCP9KTEocFe-Op-Kw",
                    "origin": "https://mubu.com",
                    "referer": "https://mubu.com/",
                    "sec-ch-ua": '" Not A;Brand";v="99", "Chromium";v="100", "Google Chrome";v="100"',
                    "sec-ch-ua-mobile": "?0",
                    "sec-ch-ua-platform": '"Windows"',
                    "sec-fetch-dest": "empty",
                    "sec-fetch-mode": "cors",
                    "sec-fetch-site": "same-site",
                    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36",
                    "version": "3.0.0-2.0.0.1824",
                    "x-request-id": "c8c9d45f-b246-481e-a50f-7cdee4ee26e0",
                }
            )
            .with_json({"folderId": 0, "source": "home"})
            .validate()
            .assert_equal("status_code", 200)
            .assert_equal("body.code", 0)
        ),
        Step(
            RunRequest("/v3/api/notify/new_tip/get")
            .post("https://api2.mubu.com/v3/api/notify/new_tip/get")
            .with_headers(
                **{
                    "accept": "application/json, text/plain, */*",
                    "accept-encoding": "gzip, deflate, br",
                    "accept-language": "zh-CN,zh;q=0.9,zh-TW;q=0.8,en-US;q=0.7,en;q=0.6",
                    "content-length": "10",
                    "content-type": "application/json;charset=UTF-8",
                    "data-unique-id": "99620c70-dd98-11ec-8003-35b78b1e9458",
                    "jwt-token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiJ9.eyJhcHAiOiJtdWJ1Iiwic3ViIjoiOTAzNjU3MiIsImxvZ2luVHlwZSI6Im1vYmlsZSIsImV4cCI6MTY1NjIzMjgyNiwiaWF0IjoxNjUzNjQwODI2fQ.pAjYnbr7Lku5kzJ2Nr8dlZQx_V-2yO79frpxqSJcE-EznHQA5w3SXBYN6V2VqRXTz2UaMKCP9KTEocFe-Op-Kw",
                    "origin": "https://mubu.com",
                    "referer": "https://mubu.com/",
                    "sec-ch-ua": '" Not A;Brand";v="99", "Chromium";v="100", "Google Chrome";v="100"',
                    "sec-ch-ua-mobile": "?0",
                    "sec-ch-ua-platform": '"Windows"',
                    "sec-fetch-dest": "empty",
                    "sec-fetch-mode": "cors",
                    "sec-fetch-site": "same-site",
                    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36",
                    "version": "3.0.0-2.0.0.1824",
                    "x-request-id": "caf293fb-1998-4791-8924-2d58bb9ed158",
                }
            )
            .with_json({"type": 1})
            .validate()
            .assert_equal("status_code", 200)
            .assert_equal("body.code", 0)
        ),
    ]


if __name__ == "__main__":
    TestCaseMubuCreatedoc().test_start()

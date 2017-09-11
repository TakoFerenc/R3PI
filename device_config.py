
class Config:

    @staticmethod
    def desired_capabilities():
        desired_caps = [{'deviceName': '42004cd04e8e4400',
                        'platformName': 'Android',
                        'platformVersion': '5.1.1',
                        'app': 'c:\\Users\\Fred\\AndroidProject\\wonky-android-calc-master\\bin\\Calculator.apk',
                        'noReset': 'true',
                        'fullReset': 'false',
                        'appPackage': 'com.test.calc',
                        'appActivity': 'com.test.calc.activities.CalculatorActivity'},
                        ]
        return desired_caps

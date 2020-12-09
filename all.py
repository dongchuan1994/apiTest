import pytest,time,os,sys,shutil
sys.path.append("C:\\Users\\DONGCHUAN\\AppData\\Roaming\\Python\\Python37\\site-packages")
p = os.path.join(os.path.dirname(__file__))
sys.path.append(p)
from common.public import filePath,mkdir,sendEmail

if __name__ == '__main__':
    pytest.main(['--alluredir', 'allureReport/allure'])
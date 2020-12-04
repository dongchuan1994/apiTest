import pytest,time,os,shutil
from common.public import filePath,mkdir,sendEmail


if __name__ == '__main__':
    now = time.strftime("%Y-%m-%d_%H-%M", time.localtime())
    path = filePath('report',now)
    mkdir(path)
    path = filePath('report', 'assets')
    mkdir(path)
    filedir = 'report/' + now
    path = filePath(filedir,'测试报告.html')
    path = "--html=" + path
    pytest.main([path])

    p = os.path.join(os.path.dirname(__file__),"report","assets","style.css")
    p1 = os.path.join(os.path.dirname(__file__),"report",now,"assets","style.css")
    shutil.copy(p1,p)
    p = os.path.join(os.path.dirname(__file__), "report", "测试报告.html")
    p1 = os.path.join(os.path.dirname(__file__), "report", now, "测试报告.html")
    shutil.copy(p1, p)
    sendEmail()



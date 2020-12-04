import pytest,os,sys,json
p=os.path.join(os.path.dirname(os.path.dirname(__file__)))
sys.path.append(p)
from common.public import *
from base.method import Requests
from utils.operationExcel import OperationExcel

obj = Requests()
objYaml = OperationExcel()

@pytest.mark.parametrize('datas', objYaml.readExcel('testdata.xlsx'))
def test_001(datas):
    test_001.__doc__ = "登录功能测试：" + datas["Description"]
    datas['Data'] = json.loads(datas['Data'])
    if datas['Data']['token'] == "{token}":
        with open(filePath("data", "usertoken.txt"), "r") as f:
            datas['Data']['token'] = f.read()
    print("请求数据：" + '\n' + str(datas['Data']) + '\n')
    r = obj.post(
        url = datas["Url"],
        json = datas["Data"]
    )
    assert str(r.json()['result']) == datas['ExpectResult']
    assert str(r.json()['message']) == datas['ExpectMessage']
    if datas['CaseId'] == 'test_003':
        with open(filePath('data','usertoken.txt'),'w') as f:
            f.write(r.json()['data']['userToken'])
    print("返回数据：" + '\n' + str(r.json()) + '\n')
if __name__ == '__main__':
    pytest.main(["-s", "-v", "test_dc.py"])


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
    test_001.__doc__ = datas["Description"]
    if datas['Data']['token'] == "{token}":
        with open(filePath("data", "usertoken.txt"), "r") as f:
            datas['Data']['token'] = f.read()
    if '/service/stf/RefreshStaffInfo' in datas['Url']:
        with open(filePath('data', 'teacherIdList.txt'), 'r') as f:
            datas['Data']['data']['Uid'] = f.read().strip('|').split('|')[0]
    if '/service/stf/DelStaffsInfo' in datas['Url']:
        teacherIdList = []
        with open(filePath('data','teacherIdList.txt'),'r') as f:
            for i in f.read().strip('|').split('|'):
                teacherIdList.append(i)
        with open(filePath('data','teacherIdList.txt'),'w') as f:
            pass
        for i in teacherIdList:
            d = {}
            d['Uid'] = i
            d['Status'] = 'D'
            datas['Data']['data']['Statu_Params'].append(d)
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
    if '/service/stf/GetStaffInfo' in datas['Url']:
        with open(filePath('data','teacherIdList.txt'),'a') as f:
            for i in r.json()['data']:
                f.write(i['uid'] + '|')
    print("返回数据：" + '\n' + str(r.json()) + '\n')
if __name__ == '__main__':
    pytest.main(["-s", "-v", "test_dc.py"])


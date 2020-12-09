import xlrd,json
from common.public import filePath,getUrl,getOrgCode,imgBase

class OperationExcel:

    def readExcel(self,fileName):
        # 打开文件
        workBook = xlrd.open_workbook(filePath('data',fileName))
        # sheet索引从0开始
        sheet1_content = workBook.sheet_by_index(0)
        # 获取总行数
        row = sheet1_content.nrows
        # 获取总列数
        #col = sheet1_content.ncols
        result = []
        for i in range(1,row):
            dict_i = dict(zip(sheet1_content.row_values(0),sheet1_content.row_values(i)))
            dict_i['Data'] = json.loads(dict_i['Data'])
            if dict_i['IsRun'] == 'y':
                if dict_i['CaseId'] == 'test_006':
                    dict_i['Data']['data']['ImgName'] = '1.jpg'
                    dict_i['Data']['data']['ImgBase64'] = imgBase('1.jpg')
                dict_i['Url'] = getUrl() + dict_i['Url']
                dict_i['Data']['orgcode'] = getOrgCode()
                result.append(dict_i)
        return  result

if __name__ == '__main__':
    # obj = OperationExcel()
    # for i in obj.readExcel('testdata.xlsx'):
    #     with open(filePath('data','teacherIdList.txt'),'a') as f:
    #         f.write(i['CaseId']+'|')
    #     print(i)
    with open(filePath('data','teacherIdList.txt'),'r') as f:
        str = f.read()
        l = str.strip('|').split('|')
        print(l)



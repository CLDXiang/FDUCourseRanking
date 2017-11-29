# -*- coding:utf-8 -*-

import json
import xlwt
from os import listdir, path, mkdir


class Analyzer():
    def __init__(self):
        if not path.exists('./res'):
            mkdir('res')
        self.wb = xlwt.Workbook()

    def writeExcel(self, path, rankingList):
        # wb = xlwt.Workbook()
        ws = self.wb.add_sheet(path[17:-5].replace(':', '_'))

        for row in range(len(rankingList)):
            for column in range(len(rankingList[row])):
                ws.write(row, column, rankingList[row][column])

                # wb.save('./res/res.xls')

    def analyzeJSON(self, path):
        with open(path, 'r') as f:
            JSON = f.read()
        # 编号 名称 教师 sc lc sc/lc
        lessonsDict = json.loads(JSON)
        rankingList = []
        for k, v in lessonsDict.items():
            if int(v['lc']) != 0:
                lessonTuple = (
                k, v['name'], v['teachers'].replace(',', ' '), v['sc'], v['lc'], int(v['sc']) / int(v['lc']))
                rankingList.append(lessonTuple)
        rankingList.sort(key=lambda lesson: lesson[-1], reverse=True)  # [(),(),(),(),...]
        # res = '\n'.join(['{},{},{},{},{},{}'.format(*t) for t in rankingList])
        # res = '课程序号,名称,教师,选课人数,开课名额,选课比例\n' + res
        # with open('./res/'+path[7:-5]+'.csv', 'w') as f:
        #     f.write(res)
        return rankingList

    def analyzeAndWriteAll(self):
        fileList = [file for file in listdir('./data') if file[:5] == 'data_']
        fileList.sort()
        for file in fileList:
            path = './data/' + file
            self.writeExcel(path, self.analyzeJSON(path))
        self.wb.save('./res/res.xls')


analyzer = Analyzer()

if __name__ == '__main__':
    analyzer.analyzeAndWriteAll()

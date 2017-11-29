# -*- coding:utf-8 -*-

import json
from time import sleep
from datetime import datetime
from getLessonDict import getLessonsDict
from os import path, mkdir


def main(test=False):
    print('<--选课量统计程序启动-->')
    print('版本号v1.0.0')
    if not path.exists('./data'):
        mkdir('data')
    while True:
        try:
            print(datetime.now(), '开始爬取选课量...')
            lessonsDict = getLessonsDict()
            lessonsJson = json.dumps(lessonsDict, ensure_ascii=False)
            print('正在写入data_{}.json'.format(datetime.now().strftime('%Y-%m-%d_%H:%M')))
            with open('./data/data_{}.json'.format(datetime.now().strftime('%Y-%m-%d_%H:%M')), 'w',
                      encoding='utf-8') as f:
                f.write(lessonsJson)
            print(datetime.now(), '写入完成，等待一小时...')
            sleep(3600)
        except:
            sleep(900)


if __name__ == '__main__':
    main(test=True)

# -*- coding:utf-8 -*-

import requests
import json
from time import sleep
from jsReader import js2Dict


def getLessonsDict():
    lessonsDict = {}
    with open('config.json', 'r') as f:
        config = json.load(f)

    session_requests = requests.session()

    username = str(config['username'])
    password = str(config['password'])

    # 登录
    sleep(5)
    print('正在登录选课系统...')
    res1 = session_requests.post(
        url='http://xk.fudan.edu.cn/xk/login.action',
        headers={'Accept-Encoding': 'gzip, deflate',
                 'Connection': 'keep-alive', 'Cache-Control': 'max-age=0', 'Origin': 'http', 'Referer': 'http',
                 'Upgrade-Insecure-Requests': '1',
                 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
                 'Content-Type': 'application/x-www-form-urlencoded', 'Accept-Language': 'zh-CN,zh;q=0.8',
                 'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36',
                 'Host': 'xk.fudan.edu.cn', 'Content-Length': '94'},
        data=
        {
            'username': username,
            'password': password,
            'encodedPassword': '',
            'session_locale': 'zh_CN'
        }
    )
    print('登录成功')

    with open('res1.html', 'wb') as f:
        f.write(res1.content)

    sleep(5)
    print('正在进入选课前页...')
    res2 = session_requests.post(
        url='http://xk.fudan.edu.cn/xk/stdElectCourse!innerIndex.action',
        headers=
        {
            'Host': 'xk.fudan.edu.cn',
            'Connection': 'keep-alive',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3260.0 Safari/537.36',
            'Upgrade-Insecure-Requests': '1',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8'
        }
    )
    print('进入选课前页成功')

    with open('res2.html', 'wb') as f:
        f.write(res2.content)

    sleep(5)
    print('正在进入选课界面...')
    res3 = session_requests.post(
        url='http://xk.fudan.edu.cn/xk/stdElectCourse!defaultPage.action',
        headers=
        {
            'Host': 'xk.fudan.edu.cn',
            'Connection': 'keep-alive',
            'Content-Length': '22',
            'Cache-Control': 'max-age=0',
            'Origin': 'http://xk.fudan.edu.cn',
            'Upgrade-Insecure-Requests': '1',
            'Content-Type': 'application/x-www-form-urlencoded',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3260.0 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
            'Referer': 'http://xk.fudan.edu.cn/xk/stdElectCourse!innerIndex.action',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8'
        },
        data={'electionProfile.id': '724'}
    )
    print('进入选课界面成功')

    with open('res3.html', 'wb') as f:
        f.write(res3.content)

    print('正在请求课程信息...')

    cnt = 0
    for search in config['searchList']:
        cnt += 1
        print('正在请求{} {}/{}'.format(search['courseCode'], str(cnt), str(len(config['searchList']))))
        # 请求课程信息
        sleep(5)
        res = session_requests.post(
            url='http://xk.fudan.edu.cn/xk/stdElectCourse!queryLesson.action?profileId=724',
            headers=
            {'Host': 'xk.fudan.edu.cn',
             'Connection': 'keep-alive',
             'Content-Length': '39',
             'Accept': '*/*',
             'Origin': 'http://xk.fudan.edu.cn',
             'X-Requested-With': 'XMLHttpRequest',
             'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3212.0 Safari/537.36',
             'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
             'Referer': 'http://xk.fudan.edu.cn/xk/stdElectCourse!defaultPage.action',
             'Accept-Encoding': 'gzip, deflate',
             'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8'},
            data={
                'lessonNo': str(search['lessonNo']),
                'courseCode': str(search['courseCode']),
                'courseName': str(search['courseName'])
            }
        )

        with open('res.js', 'wb') as f:
            f.write(res.content)

        newLessonsDict = js2Dict()

        for lesson in newLessonsDict:
            if not str(search['lessonNo']) in str(newLessonsDict[lesson]['no']):
                continue
            if not str(search['courseCode']) in str(newLessonsDict[lesson]['code']):
                continue
            if not str(search['courseName']) in str(newLessonsDict[lesson]['name']):
                continue
            if any([(keyword in str(newLessonsDict[lesson]['name'])) for keyword in config['passKeyword']]):
                continue
            else:
                lessonsDict[lesson] = newLessonsDict[lesson]
                # lessonsDict[lesson]['searchType'] = search['searchType']

    print('请求课程信息完成')
    return lessonsDict


if __name__ == '__main__':
    print(getLessonsDict())

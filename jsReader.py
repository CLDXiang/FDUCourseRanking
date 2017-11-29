# -*- coding:utf-8 -*-

import re
import json


def js2Dict():
    key_list = ['id', 'no', 'name', 'code', 'credits', 'courseId', 'examTime', 'startWeek', 'endWeek', 'courseTypeId',
                'courseTypeName', 'courseTypeCode', 'scheduled', 'hasTextBook', 'period', 'weekHour', 'withdrawable',
                'textbooks', 'teachers', 'campusCode', 'campusName', 'remark', 'arrangeInfo', 'weekDay', 'weekState',
                'startUnit', 'endUnit', 'weekStateDigest', 'rooms']

    with open('res.js', 'r') as f:
        text1 = f.readline()
        lessonJSONs = re.findall('\[{.+}\]', text1)[0]
        text2 = f.readline()
        lessonId2Counts = re.findall('{.+}', text2)[0]

    for key in key_list:
        lessonJSONs = re.sub(key + ':', '\"' + key + '\":', lessonJSONs)
    lessonJSONs = re.sub('\'', '\"', lessonJSONs)

    for key in ['sc', 'lc']:
        lessonId2Counts = re.sub(key, '\"' + key + '\"', lessonId2Counts)
    lessonId2Counts = re.sub('\'', '\"', lessonId2Counts)

    with open('lessonJSONs.json', 'w') as f:
        f.write(lessonJSONs)

    with open('lessonId2Counts.json', 'w') as f:
        f.write(lessonId2Counts)

    with open('lessonJSONs.json', 'r') as f:
        lessonJSONs = json.load(f)

    with open('lessonId2Counts.json', 'r') as f:
        lessonId2Counts = json.load(f)

    for lesson in lessonJSONs:
        lesson['sc'] = lessonId2Counts[str(lesson['id'])]['sc']
        lesson['lc'] = lessonId2Counts[str(lesson['id'])]['lc']

    # key:课程代码 value:课程信息
    lessonDict = dict(zip([lesson['no'] for lesson in lessonJSONs], lessonJSONs))

    return lessonDict

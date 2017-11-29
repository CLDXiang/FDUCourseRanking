复旦大学选课辅助 - 受欢迎程度排行
==========================
[![license](https://img.shields.io/github/license/mashape/apistatus.svg)]()


一个基于Requests库的小爬虫，可以爬取当前选课系统中的课程信息（缺省设置仅包括思政、七模及军理），并对爬取到的选课量进行简单处理得到课程受欢迎程度排行。

![Res Example](https://github.com/CLDXiang/FDUCourseRanking/blob/master/example/res_example.jpg)


## 依赖

* Bash(或其它可运行python脚本的工具)
* [Python3](https://www.python.org/downloads/release/python-363/)
* [Requests](http://docs.python-requests.org/zh_CN/latest/user/quickstart.html)
* [xlwt](https://pypi.python.org/pypi/xlwt)

推荐使用pip安装Requests和xlwt库

```bash
pip3 install requests
pip3 install xlwt
```

## 快速开始

#### 下载源码

```bash
git clone https://github.com/CLDXiang/FDUCourseRanking.git
cd FDUCourseRanking
```

#### 配置信息

进入```config.json```，分别将```username```和```password```的值填写为你的学号和密码（用于登录选课系统），如：
```json
{
  "username": 16302333333,
  "password": "LongMayTheSunshine"
}
```

如果你熟悉（或觉得能看懂）JSON的语法，也可以在```config.json```自行配置想要进行搜索的课程，其中```lessonNo```、```courseCode```、```courseName```分别对应选课界面的课程序号、课程代码和课程名称，填写时注意满足选课系统的搜索条件（如最低字数）。

#### 爬取课程信息

```bash
python3 main.py
```
或使用你自己的工具执行```main.py```

```main.py```会一直运行下去，每一小时爬取一次```config.json```中设置的课程信息，并将其以JSON格式存到```./data```目录下。你可以随时终止进程。

#### 获取排行

```bash
python3 Analyzer.py
```
或使用你自己的工具执行```Analyzer.py```

```Analyzer.py```会自动读取```./data```中所有包含课程信息的JSON文件，并按照设定好的评价指标（缺省设置为选课人数/开课名额）将排行榜写入excel工作表。

输出的excel文件```res.xls```位于```./res```目录。每一个工作表代表一次爬取的结果（即```./data```目录中的一个JSON文件）。

每一行的内容依次为：课程代码，课程名称，教师，选课人数，开课名额，选课人数/开课名额

## 注意

* 私以为第一轮选课的数据更具有参考价值，故建议仅在第一轮选课期间使用。
* 每一次选课系统重新开放时都会有一些调整，导致代码无法继续使用，我应该会尽快更新代码（不排除弃坑的可能）。
* 如果你不再使用这个脚本，请记得及时删除```config.json```文件中自己的学号密码信息，保护好自己的隐私。






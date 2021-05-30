# encoding: utf-8
"""
@author: lyx
@time: 2020/1/26 19:56
@file: script.py 
"""
from flask_script import Manager

from app.models import *
from app.models.job import Job
from exit import db

db_manage = Manager()


@db_manage.command
def add_job():
    new_job = Job(tittle='我是第二批测试用的工作', reward='80/周', place='朝阳', settlement=2,
                  isBagEating=1, encase=2, isTrafficSubsidy=2, royalty=1,
                  content='这是测试工作的内容：1.必须按时报到。2.工作前续联系负责人获取工作群号',
                  detailPlace='朝阳广场附近', startTime="2021-03-15", endTime="2021-03-19",
                  fromCompany="中国电信南宁分公司", recruitNum=1, sex=3, type="其他",
                  withPeople="王女士", status=2)
    db.session.add(new_job)
    db.session.commit()
    print(f"Job{new_job.id}: {new_job}")
    res = db.session.query(Job).all()
    print("\n".join([str(p) for p in res]))


@db_manage.command
def update_job():
    cur_job = db.session.query(Job).filter(Job.recruitNum == 2).first()
    cur_job.tittle = '大朗喇叭厂'
    db.session.commit()

@db_manage.command
def add_user():
    user = User()
    user.name = "韦杨琳"
    user.age = 20
    user.nativePlace = "广东省 广州市 白云区"
    user.place = "广州市"
    user.phoneNumber = "18276869988"
    user.birthday = "1999-01-01"
    user.height = "160cm"
    user.eduStatus = 1
    user.bestEdu = "本科"
    user.email = "949526365@qq.com"
    user.qqNum = "9495263656"
    user.weChat = "helloWYL"
    user.loginName = "wyl"
    user.password = "123456"
    db.session.add(user)
    db.session.commit()


@db_manage.command
def add_edu():
    edu = EduResume()
    edu.userId = 1
    edu.school = '广西民族大学'
    edu.major = '软件工程'
    edu.degree = '本科'
    edu.startTime = '2016-09'
    edu.endTime = '2020-06'
    edu.experience = '我在学校表现得很好很好哦'
    db.session.add(edu)
    db.session.commit()


@db_manage.command
def add_work():
    work = WorkResume()
    work.userId = 1
    work.company = '阿里巴巴'
    work.startTime = '2016-09'
    work.endTime = '2020-06'
    work.experience = '我在公司表现得很好很好哦'
    db.session.add(work)
    db.session.commit()


@db_manage.command
def add_expect():
    other = OtherResume()
    other.userId = 1
    other.expectedJobType = "短期兼职"
    other.shortJobTime = "不限"
    other.ableWorkDay = '每周一天'
    other.isFullTime = 1
    db.session.add(other)
    db.session.commit()


@db_manage.command
def add_snow():
    i = 1
    while i <= 3:
        snow = ComSign2()
        snow.name = "000"
        snow.add()
        i += 1

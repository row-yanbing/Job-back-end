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
    new_jobs = []
    new_jobs.extend([
        Job(tittle="音圈厂流水线", place="松柏朗", reward="15元/小时", settlement=1,
            isTrafficSubsidy=1, royalty=1, detailPlace="松柏朗",
            startTime="2021-06-01", endTime="2021-09-01",
            fromCompany="松柏朗音圈厂", recruitNum=20),
        Job(tittle="表带厂流水线", place="黄草朗", detailPlace="黄草朗", fromCompany="黄草朗表带厂"),
        Job(tittle="松柏朗百一厂", place="松柏朗", detailPlace="松柏朗", fromCompany="松柏朗百一厂"),
        Job(tittle="乌石岭东冠厂", place="乌石岭", detailPlace="乌石岭", fromCompany="乌石岭东冠厂"),
    ])
    db.session.add_all(new_jobs)
    db.session.commit()

    res = db.session.query(Job).all()
    print("\n".join([str(p) for p in res]))


@db_manage.command
def update_job():
    cur_job = db.session.query(Job).filter(Job.recruitNum == 2).first()
    cur_job.tittle = "大朗喇叭厂"
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
    edu.school = "广西民族大学"
    edu.major = "软件工程"
    edu.degree = "本科"
    edu.startTime = "2016-09"
    edu.endTime = "2020-06"
    edu.experience = "我在学校表现得很好很好哦"
    db.session.add(edu)
    db.session.commit()


@db_manage.command
def add_work():
    work = WorkResume()
    work.userId = 1
    work.company = "阿里巴巴"
    work.startTime = "2016-09"
    work.endTime = "2020-06"
    work.experience = "我在公司表现得很好很好哦"
    db.session.add(work)
    db.session.commit()


@db_manage.command
def add_expect():
    other = OtherResume()
    other.userId = 1
    other.expectedJobType = "短期兼职"
    other.shortJobTime = "不限"
    other.ableWorkDay = "每周一天"
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

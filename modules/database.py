from pony.orm import *
# import datetime


db = Database()

class Community(db.Entity):
    guidelines = Optional(str,column='guidelines')
    name = PrimaryKey(int,column='name',auto=True)
    greeting = Required(str,column=greeting)
    # start = Required('Poses',column='start',reverse='starting_pose')
    # end = Required('Poses',column='end',reverse='ending_pose')
    # index = Required(str,column='id')
    # approved = Required(bool,column='approved')
    # starttime = Required(int,column='starttime')
    # endtime = Required(int,column='endtime')
    # createdate =Required(datetime.datetime,column="createdate")
    # PrimaryKey(index,starttime)

class Advocate(db.Entity):
    name = Required(str,column='name')
    email = Required(str,column='email')
    communityid = Required('Community',column='communityid')

    # index = PrimaryKey(int,column='id',auto=True)
    # name = Required(str,column='name')
    # starting_pose = Set('Transitions',reverse='start')
    # ending_pose = Set('Transitions',reverse='end')
    # link = Optional(str,column='link')
    
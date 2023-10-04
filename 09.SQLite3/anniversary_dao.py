import sqlite3 as sq

def get_anniv(aid):
    sql = 'select * from anniversary where aid=?'
    pass


# start date ~ end date, uid field가 'admin' 또는 uid
def get_anniv_list(sdate, edate, uid):
    if uid == 'admin':
        sql = 'select * from anniversary where adate between ? and ? and uid=?'
    else:
        sql = "select * from anniversary where adate between ? and ? and (uid='admin' or uid=?)"
    pass

def insert_anniv(params):
    sql = 'insert into anniversary(aname, adate, is_holiday, uid) values (?, ?, ?, ?)'
    pass


def insert_anniv_many(params_list):
    sql = 'insert into anniversary(aname, adate, is_holiday, uid) values (?, ?, ?, ?)'
    pass

def update_anniv(params):
    spl = 'update anniversary set aname=?, adate=?, is_holiday=? where aid=?'
    pass

def delete_anniv(aid):
    sql = 'delete from anniversary where aid=?'
    pass
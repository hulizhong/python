#!/usr/bin/env python
# coding=utf-8
import psycopg2
import threading

class PgClient(object):
    """
    postgres db client
    make sure python-psycopg2 has been installed by apt-get.
    """
    def __init__(self):
        try:
            dbuser = 'spe'
            dbpasswd = 'spe'
            db = 'spe_db'
            dbhost = '127.0.0.1'
            dbport = 5432
            self.conn = psycopg2.connect(database=db, user=dbuser, password=dbpasswd, host=dbhost, port=dbport)
            self.cursor = self.conn.cursor()
            #print('connect pg succeed')
        except Exception,e:
            #traceback.print_exc()
            print 'PgClient init error, e-sql: ', e, sql

    def __del__(self):
        self.conn.close()
        #print 'close connection to pg'

    def exc(self, sql, isCommit=True):
        try:
            self.cursor.execute(sql)
        except Exception, e:
            print "execute sql failed, e-sql: ", e, sql
            raise e
        else:
            if isCommit:
                self.conn.commit()

    def cancelExe(self):
        """
        rollback since last commit()
        """
        self.conn.rollback()

    def query(self, sql):
        self.cursor.execute(sql)
        rows = self.cursor.fetchall()
        return rows

def fun1(id):
    steps = int(id)
    for i in range(steps):
        cc = PgClient()
        data = str(i)
        sql = "update deadlock.t_transaction set c_data = '" + data + "' where c_id = 2"
        cc.exc(sql)
        sql = "update deadlock.t_transaction set c_data = '" + data + "' where c_id = 1"
        cc.exc(sql)

def fun2(id):
    steps = int(id)
    for i in range(steps):
        cc = PgClient()
        data = str(i)
        sql = "update deadlock.t_transaction set c_data = '" + data + "' where c_id = 3"
        cc.exc(sql)
        sql = "update deadlock.t_transaction set c_data = '" + data + "' where c_id = 2"
        cc.exc(sql)

def fun3(id):
    steps = int(id)
    for i in range(steps):
        cc = PgClient()
        data = str(i)
        sql = "update deadlock.t_transaction set c_data = '" + data + "' where c_id = 4"
        cc.exc(sql)
        sql = "update deadlock.t_transaction set c_data = '" + data + "' where c_id = 3"
        cc.exc(sql)

def funSelect(id):
    steps = int(id)
    for i in range(steps):
        cc = PgClient()
        sql = "select * from deadlock.t_transaction" 
        rows = cc.query(sql)

def funMaxSelect():
    cc = PgClient()
    sql = "select MAX(c_id) from deadlock.t_transaction" 
    rows = cc.query(sql)
    return rows
def funCountSelect():
    cc = PgClient()
    sql = "select count(c_id) from deadlock.t_transaction" 
    rows = cc.query(sql)
    return rows
def funAllSelect():
    cc = PgClient()
    sql = "select * from deadlock.t_transaction" 
    rows = cc.query(sql)
    return rows
def funColumnSelect():
    cc = PgClient()
    sql = "select c_id from deadlock.t_transaction" 
    rows = cc.query(sql)
    return rows

ts = []
tSelect = threading.Thread(target=funSelect, args=('30003',))
ts.append(tSelect)

t1 = threading.Thread(target=fun1, args=('30001',))
ts.append(t1)
t2 = threading.Thread(target=fun2, args=('30002',))
ts.append(t2)
t3 = threading.Thread(target=fun3, args=('30003',))
ts.append(t3)
#for t in ts:
#    #t.setDaemon(True)
#    t.start()
#t.join()


res = funMaxSelect()
print 'max ', res, type(res), len(res)
if res[0][0] is None:
    print 'is None'
if res[0][0] == None:
    print '== None'
res = funCountSelect()
print 'count', res, type(res), len(res)
if res[0][0] == 0:
    print '== 0'
res = funColumnSelect()
print 'column ', res, type(res), len(res)
res = funAllSelect()
print 'all ', res, type(res), len(res)

'''
sql = 'select * from t_transaction'
rows = cc.query(sql)
for row in rows:
    print row

CREATE SCHEMA deadlock;
set search_path = deadlock;
create table t_transaction (c_id int, c_data varchar(128));
ALTER table t_transaction rename column t_data to c_data;  --not cloumn
'''



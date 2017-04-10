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
            print 'PgClient init error, cause: ', e

    def __del__(self):
        self.conn.close()
        #print 'close connection to pg'

    def exc(self, sql, isCommit=True):
        try:
            self.cursor.execute(sql)
        except Exception, e:
            print "execute sql failed cause:", e
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

#create table name.t_increase(c_id SERIAL, c_hulz INT default 0, c_time TIMESTAMP, c_thread int, c_tick int);
def childJob(steps, id):
    try:
        cc = PgClient()
        sql = "select max(c_hulz) from name.t_increase"
        #sql = "insert into name.t_increase(c_time, c_thread, c_tick) values (now(), " + str(steps) + ", " + str(i) + ")"
        rows = cc.query(sql)
        if rows[0][0] is None:
            ver = 1
        else:
            ver = rows[0][0] + 1
        sql = "insert into  name.t_increase(c_hulz, c_time, c_thread, c_tick) values("  + str(ver) + ", now(), " + str(steps) + ", " + str(id) + ")"
        cc.exc(sql)
    except Exception, e:
        print 'error: ', e
        return False
        #cc.cancelExe()
    return True


def fun1(id):
    steps = int(id)
    for i in range(steps):
        res = childJob(steps, id)
        if res == False:
            while True:
                #print '-------------------------> again ', steps, id
                res = childJob(steps, id)
                if res == True:
                    break
                


ts = []
t1 = threading.Thread(target=fun1, args=('10',))
ts.append(t1)
t2 = threading.Thread(target=fun1, args=('12',))
ts.append(t2)
t3 = threading.Thread(target=fun1, args=('14',))
ts.append(t3)
for t in ts:
    t.setDaemon(True)
    t.start()
t.join()


'''
sql = 'select * from t_transaction'
rows = cc.query(sql)
for row in rows:
    print row
'''

'''
#create table name.t_increase(c_id SERIAL, c_hulz INT unique, c_time TIMESTAMP);
def fun1(id):
    steps = int(id)
    for i in range(steps):
        try:
            cc = PgClient()
            sql = "select max(c_hulz)+1 from name.t_increase"
            rows = cc.query(sql)
            if rows[0][0] is None:
                hulz = 1
            else:
                hulz = int(rows[0][0])
            sql = "insert into name.t_increase(c_hulz, c_time) values (" + str(hulz) + ", now())"
            cc.exc(sql)
        except Exception, e:
            cc.cancelExe()

def fun2(id):
    steps = int(id)
    for i in range(steps):
        try:
            cc = PgClient()
            sql = "select max(c_hulz)+1 from name.t_increase"
            rows = cc.query(sql)
            if rows[0][0] is None:
                hulz = 1
            else:
                hulz = int(rows[0][0])
            sql = "insert into name.t_increase(c_hulz, c_time) values (" + str(hulz) + ", now())"
            cc.exc(sql)
        except Exception, e:
            cc.cancelExe()

def fun3(id):
    steps = int(id)
    for i in range(steps):
        try:
            cc = PgClient()
            sql = "select max(c_hulz)+1 from name.t_increase"
            rows = cc.query(sql)
            if rows[0][0] is None:
                hulz = 1
            else:
                hulz = int(rows[0][0])
            sql = "insert into name.t_increase(c_hulz, c_time) values (" + str(hulz) + ", now())"
            cc.exc(sql)
        except Exception, e:
            cc.cancelExe()
'''


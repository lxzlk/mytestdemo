import cx_Oracle
import os
os.environ['NLS_LANG'] = 'SIMPLIFIED CHINESE_CHINA.UTF8'

conn = cx_Oracle.connect('custeval/custeval@10.138.22.223/edw')
cursor = conn.cursor()
cursor.execute("select * from dm_risk_credit")
row = cursor.fetchone()
print(row)
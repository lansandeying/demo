#coding:utf-8
import pymysql
import pandas as pd
 
def get_mysql_data(sql):
    """
    提取mysql中的数据并返回成dataframe
    参数只需要sql语句
 
    """
    conn = pymysql.connect(
        host='192.168.0.132',
        user='root',
        password='kxyx92108',
        db='activity_test',
        port=3306,
        charset="utf8"
    )
    cur = conn.cursor()  # 获取操作游标，也就是开始操作
    sql_select = sql  # 查询命令
    cur.execute(sql_select)  # 执行查询语句
 
    result = cur.fetchall()  # 获取查询结果
    col_result = cur.description  # 获取查询结果的字段描述
 
    columns = []
    for i in range(len(col_result)):
        columns.append(col_result[i][0])  # 获取字段名，咦列表形式保存
 
    df = pd.DataFrame(columns=columns)#传字段名，字段名放在列表columns里
    for i in range(len(result)):
        df.loc[i] = list(result[i])  # 按行插入查询到的数据
 
    conn.close()  # 关闭数据库连接
 
    return df
 
if __name__=="__main__":
    sql="select * from sys_config "#where key_id='6003'
    result_sql=get_mysql_data(sql)
    print(result_sql)
    print("")
    print(result_sql['key_group'])
    print("")
    print(result_sql['descs'])
    print("")
    print(result_sql['key_id'])
    print("")
    print(result_sql['key_id'][0])
    print("")
    print(result_sql['key_id'][2])
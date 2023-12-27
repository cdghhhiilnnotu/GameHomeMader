# import psycopg2

def tuple2dict(tpl, nameCol):
    newDict = {}
    for i in range(len(tpl)):
        newDict[nameCol[i]] = tpl[i]
    return newDict

def listDict(lst, nameCol):
    allUser = []
    for x in lst:
        allUser.append(tuple2dict(x, nameCol))
    return allUser

def getListData(cur, tableStr):
    cur.execute(f"""
        SELECT column_name
        FROM information_schema.columns
        WHERE table_name = '{tableStr}';
    """)
    tableColumn = [x[0] for x in cur.fetchall()]
    tableColsStr = ','.join(tableColumn)
    # print(tableColumn)
    # print(cur.fetchall())

    cur.execute(f"""
        SELECT {tableColsStr} FROM {tableStr};
    """)
    table = cur.fetchall()

    return table, tableColumn

def tryCastInt(str):
    try:
        return int(str)
    except:
        return -1


def getListDataWhere(cur, tableStr, searchStr):
    cur.execute(f"""
        SELECT column_name
        FROM information_schema.columns
        WHERE table_name = '{tableStr}';
    """)
    tableColumn = [x[0] for x in cur.fetchall()]
    tableColsStr = ','.join(tableColumn)
    # print(tableColumn)
    # print(cur.fetchall())

    cur.execute(f"""
        SELECT {tableColsStr} FROM {tableStr} WHERE id={tryCastInt(searchStr)} or name=\'{searchStr}\';
    """)
    table = cur.fetchall()
    # print(table)

    return table, tableColumn

# print(tuple2dict((1, 'Nguyễn Văn A', 'nguyenvanan@example.com', '123456'), ['id', 'name', 'email', 'password']))


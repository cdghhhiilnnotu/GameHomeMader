import psycopg2
import json

class DATABASESERVER():
    def __init__(self):
        self.dataJson = {}

        self.init_data()

    def init_data(self):
        self.userElements = ['id','name','email','password']
        self.gameElements = ['id','name','genre','description','price','demo_file','images','videos']
        self.transactionElements = ['id','user_id','game_id','price','status','created_at','updated_at']
        self.paymentElements = ['id','transaction_id','payment_method','amount','transaction_id_number']

        self.dataJson['users'] = self.get_api(""" SELECT * FROM USERS """, self.userElements)
        self.dataJson['games'] = self.get_api(""" SELECT * FROM GAMES """, self.gameElements)
        self.dataJson['transactions'] = self.get_api("""select id,user_id,game_id,price,status, TO_CHAR(created_at	, 'DD-MM-YYYY'), TO_CHAR(updated_at, 'DD-MM-YYYY')
                                                            from transactions""", self.transactionElements)
        self.dataJson['payments'] = self.get_api(""" SELECT * FROM PAYMENTS """, self.paymentElements)
        # print(self.dataJson)

    def execute_SQL(self,query):
        conn = psycopg2.connect(host="localhost", dbname="GamesTrader", user="postgres",
                        password="1009", port=5432)
        conn.set_client_encoding('UTF8')
        cur = conn.cursor()
        cur.execute(f"""
            {query}
        """)
        
        print(query)
        try:
            result = cur.fetchall()
        except:
            result = ()
        conn.commit()
        cur.close()
        conn.close()
        return result
    
    def get_api(self, query: str, columns:list):
        row = self.execute_SQL(query)
        listRows = []
        for r in row:
            item = {}
            for idx,e in enumerate(columns):
                item[e] = r[idx]

            listRows.append(item)
        # print(listRows)
        return listRows
    
    



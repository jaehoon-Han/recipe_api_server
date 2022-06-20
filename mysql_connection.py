import mysql.connector

def get_connection() :
    connection = mysql.connector.connect(
            host = 'yh.cpos3ccatavx.ap-northeast-2.rds.amazonaws.com',
            database = 'resipe_db',
            user = 'recipe_user',
            password = 'recipe1234')
    
    return connection
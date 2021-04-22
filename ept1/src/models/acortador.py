from src.config.db import DB
import requests

class shortLinkModel():
    def saveData(self, Data):
        cursor = DB.cursor()
        cursor.execute("INSERT INTO shortlinks(shortlink,link,user_id) VALUES (?,?,?)",(Data['shortlink'],Data['link'],Data['user_id'],))
        cursor.close()
    
    def findLink(self,shortLink):
        cursor = DB.cursor()
        cursor.execute("SELECT * FROM shortlinks WHERE shortlink = ?",(shortLink,))
        links = cursor.fetchone()
        cursor.close()
        return links

    def dataUser(self,user):
        links = []
        if 'user' in user:
            cursor = DB.cursor()
            cursor.execute("SELECT * FROM shortlinks WHERE user_id = ?",(user['user'][0],))
            links = cursor.fetchall()
            cursor.close()
        return links

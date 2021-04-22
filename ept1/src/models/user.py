from src.config.db import DB

class userModel():
    def signUp(self, data):
        cursor = DB.cursor()
        cursor.execute("INSERT INTO users(name,email,password) VALUES (?,?,?)",(data['name'],data['email'],data['password'],))
        cursor.close()
    
    def logIn(self, data):
        cursor = DB.cursor()
        cursor.execute("SELECT * FROM users WHERE email = ? AND password = ?",(data['name'],data['password'],))
        into = cursor.fetchone()
        cursor.close()
        return into

    def deleteLink(self, link, session):
        cursor = DB.cursor()
        cursor.execute("DELETE FROM shortlinks WHERE user_id = ? AND shortlink = ?",(session[0],link,))
        cursor.close()
        return link

    def editLink(self,data):
        print(data)
        cursor = DB.cursor()
        cursor.execute("UPDATE shortlinks SET shortlink = ?, link = ? WHERE id = ?",(data['shortlink'], data['link'], data['id'],))
        cursor.close()
        return data

    def uniqueEmail(self,data):
        print(data)



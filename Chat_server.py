import pymysql
import socket
import zlib
import sys
reload(sys)
sys.setdefaultencoding('utf8')
try:
    host = sys.argv[1]
 #   host = 'localhost'
    port = int(sys.argv[2])
   # host = '10.6.16.16'
   # port = 5500
   # print(type(host),type(port))
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind((host,port))

    print("server open")

    
    while True:
        
        db = pymysql.connect("127.0.0.1","bewwy","bewwy","CHAT_SERVER")
        cursor = db.cursor()
        
        data, addr = s.recvfrom(1024)
        sql=data.decode("utf-8")
##        print(sql)
        print("Server Runing "+"User Connect[IP,PORT] : "+str(addr))
        if(sql.split()[0].upper()=="UPDATE"):
            try:
                text="UPDATE SUCCESS"
                cmpstr = zlib.compress(text.encode('utf-8'))
                s.sendto(cmpstr, addr)
                cursor.execute(sql)
                db.commit()
            except:
                text="UPDATE FAIL"
                cmpstr = zlib.compress(text.encode('utf-8'))
                s.sendto(cmpstr, addr)
                db.rollback()

            db.close()
        elif(sql.upper()=="SELECT * FROM SERVER"):
            cursor.execute(sql)#send value on database
            results = cursor.fetchall()#put value from database
            text=""
            for row in results:
               id = row[0]
               username = row[1]
               password = row[2]
               status = row[3]
               text+=("{0} : {1} : {2} : {3}".format(id,username,password,status)+"\n")
            db.close()
            #print(text)
##            print(text)
            cmpstr = zlib.compress(text.encode('utf-8'))
            s.sendto(cmpstr, addr)
        elif(sql.split()[0].upper()=="SELECT" and sql.split()[1].upper()=="user,message".upper()):
            cursor.execute(sql)
            results = cursor.fetchall()
            text=""
            for row in results:
               
               username = row[0]
               message = row[1]
               
               text+=("{0}:{1}".format(username,message)+"\n")
            db.close()
            #print(text)
##            print("text : "+text)
            cmpstr = zlib.compress(text.encode('utf-8'))
##            print(addr)
            s.sendto(cmpstr, addr)
        elif(sql.upper()=="select user,password from account".upper() or sql.upper()=='select user,password from account where status="Y"'.upper()):
            cursor.execute(sql)
            results = cursor.fetchall()
            text=""
            for row in results:
               
               username = row[0]
               password = row[1]
               
               text+=("{0}:{1}".format(username,password)+"\n")
            db.close()
            #print(text)
##            print("text : "+text)
            cmpstr = zlib.compress(text.encode('utf-8'))
##            print(addr)
            s.sendto(cmpstr, addr)
        elif(sql.split()[0].upper()=="INSERT" ):
            try:
                text="INSERT SUCCESS"
                cmpstr = zlib.compress(text.encode('utf-8'))
                s.sendto(cmpstr, addr)
                cursor.execute(sql)
                db.commit()
            except:
                text="INSERT FAIL"
                cmpstr = zlib.compress(text.encode('utf-8'))
                s.sendto(cmpstr, addr)
                db.rollback()

            db.close()
        elif(sql.upper()=="DELETE FROM SERVER"):
            try:
                text="DELETE SUCCESS"
                cmpstr = zlib.compress(text.encode('utf-8'))
                s.sendto(cmpstr, addr)
                cursor.execute(sql)
                db.commit()
            except:
                text="DELETE FAIL"
                cmpstr = zlib.compress(text.encode('utf-8'))
                s.sendto(cmpstr, addr)
                db.rollback()

            db.close()

       # if(sql.split("[CHAT]")[0].upper()=="CHAT"):
        else:  
            text=sql
            cmpstr = zlib.compress(text.encode('utf-8'))
            s.sendto(cmpstr, addr)
            
except KeyboardInterrupt:
    # quit
    sys.exit()
    
    

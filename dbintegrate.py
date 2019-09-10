import sqlite3
conn = sqlite3.connect('/root/dev/proyek/satpam.sq3')
print ("Opened database successfully");
print ("==========================================")

def fungsi1():
   cursor = conn.execute("select s.date,s.time_id ,s.user_id,u.name,s.room_id from shifts as s,users as u where s.user_id=u.id AND s.time_id=1 AND s.user_id=7;")
   for row in cursor:
      x=(row[0], row[1], row[2], row[3], row[4])
     # string=bytes(x,encoding='utf-8')
 #    x.replace(" ","_")
      print(x)
      #print (str(string,encoding='ascii',error='ignore'))
     # print (str(x,encoding='ascii',error='ignore'))
 #  print ("date = ", row[0])
 #  print ("time_shift = ", row[1])
 #  print ("no_satpam = ", row[2])
 #  print ("nama = ", row[3])
 #  print ("room_id = ", row[4])
###! FIND ALL TIMESTART FROM parameter time
def timeStart(time):
   
   cursor = conn.execute("select u.name,s.user_id,s.time_id, t.start ,s.room_id from users as u,times as t,shifts as s where t.id=s.time_id AND u.id=s.user_id AND s.time_id=(%s)" %(time)  )
   for e in cursor:
      x = str("{} # {} # {} # {} # {}".format(e[0],e[1],e[2],e[3],e[4]))
      print(x)

###! menemukan orang yang bekerja pada start tertentu ####
def workstart():
   cursor = conn.execute("select s.date,s.time_id ,s.user_id,u.name,s.room_id from shifts as s,users as u where u.id=s.user_id AND s.time_id=1")
   
   for e in cursor:
      
     # data=(e[0],e[1],e[2],e[3],e[4])
      #data=("{}#{}#{}#{}#{}".format(e[0],e[1],e[2],e[3],e[4]))
      x=str("{}#{}#{}#{}#{}".format(e[0],e[1],e[2],e[3],e[4]))
      #x=str(data)
      print((x))
      #final=(Replace(x))   
     # print(final.replace(" ","_"))
      # print(type(x))
      ##*data string dikirim pada mqtt##
      ## !kirim ke MQTT ##
     # print ('kirim ke MQTT')
#fungsi1()
#workstart()
print("===========================================")
#?FIND TIME START time_id= 1
timeStart(1)
print ("==========================================")
print ("Operation done successfully");
conn.close()

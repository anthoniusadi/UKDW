
## ! dependency modul ##
import modulderive
import mqtt
import sqlite3
import time
import base64
##! database connection 
conn = sqlite3.connect('/root/dev/proyek/satpam.sq3')
print ("Opened database successfully");
print ("==========================================")

# def fungsi1():
#    cursor = conn.execute("select s.date,s.time_id ,s.user_id,u.name,s.room_id from shifts as s,users as u where s.user_id=u.id AND s.time_id=1 AND s.user_id=7;")
#    for row in cursor:
#       x=(row[0], row[1], row[2], row[3], row[4])
#      # string=bytes(x,encoding='utf-8')
 #    x.replace(" ","_")
    #  print(x)
      #print (str(string,encoding='ascii',error='ignore'))
     # print (str(x,encoding='ascii',error='ignore'))
 #  print ("date = ", row[0])
 #  print ("time_shift = ", row[1])
 #  print ("no_satpam = ", row[2])
 #  print ("nama = ", row[3])
 #  print ("room_id = ", row[4])

###! mengirim data untuk semua orang yang bekerja pada time_id=1 saja ####
def workstart():
   global value
   ##! mengambil data date,time_id,user_id,name,room_id dari database ##
   cursor = conn.execute("select s.date,s.time_id ,s.user_id,u.name,s.room_id from shifts as s,users as u where u.id=s.user_id AND s.time_id=1")
   for e in cursor:
     # data=(e[0],e[1],e[2],e[3],e[4])
      #data=("{}#{}#{}#{}#{}".format(e[0],e[1],e[2],e[3],e[4]))
      #x=str("{}#{}#{}#{}#{}".format(e[0],e[1],e[2],e[3],e[4]))
      #x=str(data)
      #print((x))
      ## !Proses enkripsi dari database ##
      func1=str("{}#{}#{}#".format(e[0],e[1],e[4]))     ###?tanggal#time_id#room_id
      func2=str("{}#{}#".format(e[2],e[3]))             ###?user_id#nama_satpam
      modulderive.enkrip(func1,func2)
      value=modulderive.enkrip(func1,func2)
      
      ## !word adalah convert dari tipe data byte value ##
      
      word=str(value)
      print(word)
      print ('kirim ke MQTT')
      strencode = base64.b64encode(value)
      print(strencode)
      ## !kirim ke MQTT ##
      #mqtt.client.publish("tessatpam",strencode)
      mqtt.client.publish("ruang1",strencode)
      mqtt.client.publish("ruang2",strencode)
      mqtt.client.publish("ruang3",strencode)
      ## ! delay 2 detik ##
      time.sleep(2)
    #  print(func1,func2)
    
workstart()

## !contoh pengujian pada system ##
print("\n\n\nkemudian dilakukan scan barcode pada data terakhir \n\n\n")
print("==============contoh testing gagal================")
modulderive.dekrip(b'S\x92^\x99Z\xc8\xb3\xece\xa4\x9fy\x05\x98\xc9\x18\xb9\xa2S\xb2\xf4\xa8Gf\xec{\x87\xc5Q\xd1\xb0g',value)
print ("==================================================\n")
print("\n============contoh testing  berhasil==============")
modulderive.dekrip(b'&\xa9\xddL\xaf\x19\x8f\xc6\xdc\xf8.\x8a\xf4\x876\xe1X\xe2\x83\x19l\x86\x1c\x8af\x0b\x10\xeb\xd8\x9d\xe8\x8e',value)
print ("==================================================")
print ("Operation done successfully");
conn.close()


###! query tabel times atribut start cek jam pada date and time.
###! apabila jam nya ada yang sama maka query yang mengacu pada id di table times ke table shift kemudian lemparkan lagi room id.
###! pada room id punya topik subscribe sendiri kemudian query pada user ambil informasi sesuai yang akan di derive kan master keynya.


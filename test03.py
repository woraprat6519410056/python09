#คุณสมบัติเด่น oop :Encapsulation (ห่อหุ้ม/ซ่อมไว้)
#ห่อหุ้ม/ซ่อม data โดยใส่  _ ไว้หน้าชื่อ data
class MyTestA :
    _data1 = 10
    data2 = 20

# เมื่อ Data ถูก Encap การกำหนดค่าหรือเอาค่ามาใช้
#ให้ผ่านเมธอต get เอาค่ามาใช้/get กำหนดค่า
def getData1(self) :
    return self._data1

def setData1(self,data1) :
    self._data1 = data1

def getData1(self) :
    return self._data3

def setData(self, data3) :
    self._data3 = data3

def __init__(self, data3) :
    self._data1 = data3

def showData(self) :
    print(f'_data1 มีค่า {self._data1}')
    print(f'data2 มีค่า {self.data2}')
    print(f'_data3 มีค่า {self._data3}')
    print('-------------------------')

ob1 = MyTestA(30)
ob1.showData()
ob1.data2 = 200
#ob1._data1 = 100
ob1.showData(100)
# ob1.data3 = 999
ob1.setData3(999)
ob1.showData()
print( ob1.getData3 () )
def sumNumber() :
    pass

# สร้าง Class ใน Python
class IoTSAU : 
    # data/attribute/filed/property memberเหมือนกับตัวแแปลนั้น
    info1 = 20
    info2 = ""

    # method member เหมือนกับฟังก์ชัน
    def showHi(self):
        print('Hi....')
    
    def showInfo(self):
        print(self.info1, self.info1)
        self.showHi()

# สร้าง object
obA = IoTSAU()
obB = IoTSAU()
obC = IoTSAU()

obA.info1 = 100
print(obA.info1 + obB.info1) # 120  
obC.showInfo()
obA.showInfo()

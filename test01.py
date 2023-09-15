#defalt parameter
#ถ้าจะกำหนดค่าต้องกำหนดจากหลังมาหน้าห้ามข้าม
def funcA(x,y=20,z=10):
    print(x+y+z)
    print("^-^") 
funcA(10,20)
funcA(5,6,7)
funcA(555)
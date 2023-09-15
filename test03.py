#คำนวณหาราคาขายสินค้า โดยรับซื้อสินค้าและราคาสินค้า(ต้นทุน)ทางแป้นพิมพ์
#และคำนวณหาราคาของสินค้า โดยราคาขายสินค้าจะคิดเพิ่มจากการ(ต้นทุน)ร้อยละ10
#สูตร ราคาสินค้า =ราคาสินค้า(ต้นทุน)-ราคาสินค้า{ต้นทุน}*10/100

#Feature ในการรับค่า การคำนวณ และการแสดงผลแยกจากกัน
#ดังนั้นอย่างน้อยมี3 ฟังก์ชัน
def inputdata():
    product_name=input("ชื่อสินค้าสินค้า : ")
    product_pride=float(input("ป้อนราคาสินค้า(ต้นทุน) : "))
    return product_name,product_pride

def calproductsale1 (product_pride):
    product_sale=product_pride+(product_pride*10/100)
    return product_sale

def calproductsale (product_name,product_pride,product_sale):
    print(f'ฃื่อสินค้า {product_name} ')
    print(f'ราคาสินค้า(ต้นทุน){product_pride:.2f} บาท')
    print(f'ราคาขายสินค้า{product_sale:.2f} บาท')

product_name,product_pride =  inputdata()
product_sale=calproductsale1(product_pride)
calproductsale (product_name,product_pride,product_sale)
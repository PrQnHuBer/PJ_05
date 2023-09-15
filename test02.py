#ruturn not values
#หมายถึง การสิ้นสุดหรือจบการทำงานของ block scope การทำงานหนึ่งๆ
def func1 () :
 print('AAA')
 print('BBB')
 return 
 print('CCC')

def func2 (x) :
 return
 print(f'X is {x}')

func1()
func2(10)
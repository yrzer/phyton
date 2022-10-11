o=0.0
o = int(input("obudowa?:  | 1: asus | 2:krux | 3:ibox"))
o += int(input("obudowa?:  | 1: dobra | 2:zła | 3:średnia"))/10

p_g = 0.0
p_g+= int(input("płyta główna?:  | 1: msi | 2:asus |"))
p_g+= int(input("płyta główna?:  | 1: dobra | 2:zła | 3:średnia |"))/10

p=0.0
p+= int(input("procesor?:  | 1: intel | 2:reizen |"))
p+= int(input("procesor?:  | cyferka |"))/10

k_g = 0.0
k_g+= int(input("nvidia?:  | cyferka seria(20,30,40) |"))
k_g+= int(input("nvidia?:  | cyferka model |"))/10

d=0.0
d+= int(input("dysk?:  | 1:ssd | 2:ssd mk.2 | 3:hdd |"))
d+= int(input("dysk?:  | wielkość 4cyfry |"))/10000

r=0.0
r+= int(input("ram?:  | 1:ddr3 | 2:ddr4 |"))
r+= int(input("ram?:  | wielkość 3cyfry |"))/1000

print("zasilacz dobry c:")

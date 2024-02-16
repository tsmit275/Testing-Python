def hello():
    print("hello world")

def pack(toothbrushes, toothpaste, soap) :
    return[toothbrushes, toothpaste, soap]

def eat_lunch(my_list):
    if len(my_list) == 0:
        print("My lunchbox is empty")
    else:
        for i in range(len(my_list)):
            if i == 0:
                print(f"First I eat {my_list[0]}")
            else:
                print(f"Next I eat {my_list[i]}")



hello()
print(pack("toothbrushes", "toothpaste", "soap"))
print(pack(1,2,3))
eat_lunch([])
eat_lunch(["spagehtii"])
eat_lunch(["applesauce", "salad", "spagehtii", "chocolate cake"])
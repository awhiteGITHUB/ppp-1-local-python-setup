def hello():
  print("Hello from a function")

hello() 


def pack(fname, mname, lname):
  return [fname, mname,lname]

   
def eat_lunch(my_lst):
  if len(my_lst) == 0:
    print("My lunchbox is empty!")
  else:
    for i in range(len(my_lst)):
      if i == 0:
        print(f"First I eat {my_lst[0]}")
      else:
        print(f"Next I eat {my_lst[i]}")


hello()
print(pack("fname","mname","lname"))
eat_lunch([])
eat_lunch(["sandwich"])
eat_lunch(["Sugar Apple","Green Banana","Crab Cake Sandwich","Another Crab Cake Sandwich","Cookie"])



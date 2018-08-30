checklist = list()

def my_fun_function(say_this):
    print(say_this)
#
my_fun_function('Hello World')
#
checklist = list()
checklist.append('Blue')
print(checklist)
checklist.append('Orange')
print(checklist)

def create(item):
    checklist.append(item)

create("jasmine")

print(checklist)
print(checklist[0])

def read(index):
    return checklist[index]
print(read(2))

def update(index, item):
    checklist[index] = item

update(1, "Rose")
print(checklist)

def destroy(index):
    checklist.pop(index)
destroy(0)
print(checklist)

def list_all_items():
    index = 0
    for list_item in checklist:
        print("{} {}".format(index, list_item))
        index += 1

def mark_completed(index, item):
    checklist = str("check" + item)


def test():
    create("purple sox")
    create("red cloak")

    print(read(0))
    print(read(1))

    update(0, "purple socks")

    destroy(1)

    print(read(0))

list_all_items()

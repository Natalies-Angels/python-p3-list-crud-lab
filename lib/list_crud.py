def create_an_empty_list():
    return []

def create_a_list():
    return ["Boba", "Latte", "Macha", "Mocha"]

def add_element_to_end_of_list(l, element):
    l.append(element)
    return l

def add_element_to_start_of_list(l, element):
    l.insert(0,element)
    return l

def remove_element_from_end_of_list(l):
    l.pop()
    return l

def remove_element_from_start_of_list(l):
     l.pop(0)
     return l


def retrieve_first_element_from_list(l):
   first_element = l[0]
   return first_element

def retrieve_element_from_index(l, index):
    element = l[index]
    return element

def retrieve_last_element_from_list(l):
    last_element = l[-1]
    return last_element

append_element = add_element_to_end_of_list([1,2,3], 4)
print(append_element)

insert_element = add_element_to_start_of_list(["April","Lily","Mae"], "Charlie")
print(insert_element)

remove_last_element = remove_element_from_end_of_list([99.9,67,77.5])
print(remove_last_element)

remove_first_element = remove_element_from_start_of_list([99.9,67,77.5])
print(remove_first_element)

retrieve_first_element = retrieve_first_element_from_list(["happy","cheerful","joyous"])
print(retrieve_first_element)

retrieve_from_index = retrieve_element_from_index(["April","Lily","Mae"], 0)
print(retrieve_from_index)

retrieve_last_element = retrieve_last_element_from_list(["April","Lily","Mae"])
print(retrieve_last_element)
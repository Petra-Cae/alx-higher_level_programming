#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    # divides two lists element by element
    div_list = []
    for el in range(list_length):
        try:
            result = my_list_1[el] / my_list_2[el]
        except (TypeError):
            print("wrong type")
            result = 0
        except (ZeroDivisionError):
            print("division by 0")
            result = 0
        except (IndexError):
            print("out of range")
            result = 0
        finally:
            div_list.append(result)
    return (div_list)

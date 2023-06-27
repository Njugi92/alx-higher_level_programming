#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    """Divides two lists element by element.
    Args:
    my_list_1 (list): First list
    my_list_2 (list): second list
    list_length (int): Total number of elements to divide
    Returns:
    A new list of length list_length with all the divisions.
    """
    new_list = [0] * list_length
    for i in range(list_length):
        try:
            new_list = my_list_1[i] / my_list_2[i]
        except ZeroDivisionError:
            print("Division by )")
        except TypeError:
            print("Wrong type")
            div = 0
        except IndexError:
            print("Out of range")
            div = 0
        finally:
            new_list.append(div)
    return (new_list)

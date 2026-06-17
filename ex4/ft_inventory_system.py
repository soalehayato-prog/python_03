#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   ft_inventory_system.py                               :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: ahmandri <ahmandri@student.42antananarivo.   +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/06/09 21:37:05 by ahmandri            #+#    #+#            #
#   Updated: 2026/06/16 22:14:03 by ahmandri           ###   ########.fr      #
#                                                                             #
# ########################################################################### #


import sys

def main() -> dict:
    inventory = {}
    argument = sys.argv[1:]
    
    print("=== Inventory System Analysis ===")
    for arg in argument:
        if ":" not in arg:
            print(f"Error - invalid parameter '{arg}'")
            continue 
        parts = arg.split(":")
        item = parts[0]
        nbr = parts[1]
        if item in inventory :
            print(f"Redundant item '{item}' - discarding")
            continue
        try:
            qty = int(nbr)
            inventory.update({item : qty})
        except ValueError as e:
            print(f"Quantity error for '{item}':{e}")
    key_dict = list(inventory.keys())
    count_key = len(key_dict)
    l_value = list(inventory.values())
    print(f"Got inventory:{inventory}")
    print(f"Item list:{list(inventory.keys())}")
    print(f"Total quantity of the {count_key} items :{sum(l_value)}")
    total = sum(l_value)
    most_qty = l_value[0]
    most_key = key_dict[0]
    least_qty = l_value[0]
    least_key = key_dict[0]
    for i in range(count_key):
        arm = key_dict[i]
        quantity = l_value[i]
        percentage = round(((quantity/total)*100),1)
        print(f"Item {arm}represents {percentage}%")
    for i in range(count_key):
        
        if l_value[i] > most_qty :
            most_qty = l_value[i]
            most_key = key_dict[i]
        if l_value[i] < least_qty:
            least_qty = l_value[i]
            least_key = key_dict[i] 
    print(f"Item most abundant:{most_key} with quanity {most_qty}")
    print(f"Item least abundant:{least_key} with quanity {least_qty}")
    inventory.update({"magic_item" : 1})
    print(f"Updated inventory:{inventory}")
    return(inventory)       


if __name__ == "__main__":
        main()
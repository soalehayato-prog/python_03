#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   ft_coordinate_system.py                              :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: ahmandri <ahmandri@student.42antananarivo.   +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/06/07 07:55:27 by ahmandri            #+#    #+#            #
#   Updated: 2026/06/07 11:37:08 by ahmandri           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

import math

def get_player_pos() -> tuple[float, float, float]:
    while True:
     user_input: str = input("Enter new coordinates as floats in format 'x,y,z':")
     try:
            parts = user_input.split(",")
            if len(parts) != 3:
                raise ValueError("Invalid syntax")
            x,y,z = parts
            return(float(x),float(y),float(z))
     except ValueError as e:
        if str(e) == "Invalid syntax":
          print(e)
        else:
            print(f"Error on parameter {e}")
def main()->None:
       print("=== Game Coordinate System ===")
       
       print("Get a first set of coordinates")
       first = get_player_pos()
       print(f"Got a first tuple: {first}")
       x,y,z = first
       print(f"It includes: X={x},Y={y},Z={z}")
       center = math.sqrt(x**2+y**2+z**2)
       res_center= round(center,4)
       print(f"Distance to center:{res_center}")

       print("Get a second set of coordinates")
       second = get_player_pos()
       x1,y1,z1 = second
       distance = math.sqrt((x1-x)**2 +(y1-y)**2+(z1-z)**2)
       res_dis = round(distance,4)
       print(f"Distance between the 2 sets of coordinates:{res_dis}")       
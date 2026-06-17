#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   ft_command_quest.py                                  :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: ahmandri <ahmandri@student.42antananarivo.   +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/06/06 21:29:00 by ahmandri            #+#    #+#            #
#   Updated: 2026/06/06 23:24:27 by ahmandri           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

import sys

def main() -> None:
    print("=== Command Quest ===")
    print(f"Program name: {sys.argv[0]}")
    
    arg_total: int = len(sys.argv)
    arg_recevied: int = len(sys.argv) - 1
    
    if arg_recevied == 0:
        print("No arguments provided!")
    else:
        print(f"Arguments received: {arg_recevied}")
    for i in range(1,arg_total):
        print(f"Argument {i}: {sys.argv[i]}")        
    print(f"Total arguments: {arg_total}")    
#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   ft_score_analytics.py                                :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: ahmandri <ahmandri@student.42antananarivo.   +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/06/06 23:32:23 by ahmandri            #+#    #+#            #
#   Updated: 2026/06/07 10:13:47 by ahmandri           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

import sys 

def score_analytics() -> None:
    print("=== Player Score Analytics ===")
    
    arg_total : int = len(sys.argv)
    if arg_total == 0:
        print("No scores provided. Usage: python3 ft_score_analytics.py <score1> <score2> ...")
    score:list = []
    for arg in sys.argv[1:]:
        try:
            score.append(int(arg))
        except ValueError as e:
            print(f"Invalid parameter: {e}")
    print(f"Scores processed: {score}")
    print(f"Total players:{arg_total}")
    print(f"Total score:{sum(score)}")
    average : float = sum(score)/len(score)
    score_range: int = min(score) - max(score)
    maxi: int = max(score)
    mini: int = min(score)
    print(f"Average score: {average}")
    print(f"High score: {maxi}")
    print(f"Low score:{mini}")
    print(f"Score range:{score_range}")
    
    
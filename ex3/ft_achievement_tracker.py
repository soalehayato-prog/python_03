#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   ft_achievement_tracker.py                            :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: ahmandri <ahmandri@student.42antananarivo.   +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/06/07 11:39:01 by ahmandri            #+#    #+#            #
#   Updated: 2026/06/16 22:07:48 by ahmandri           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

import random
achievements =["Crafting Genius","World Savior",
                    "Master Explorer","Collector Supreme",
                    "Untouchable","Boss Slayer","Strategist",
                    "Unstoppable","Speed Runner","Survivor",
                    "Treasure Hunter","First Steps","Sharp Mind"]
def gen_player_achievements() ->set:
     number = random.randint(1,len(achievements))
     return set(random.sample(achievements,number))
def main() -> None:
     All_pos = set(achievements) 
     print("=== Achievement Tracker System ===")
     
     players = ['Alice','Bob','Charlie','Dylan']
     alice = gen_player_achievements()
     bob = gen_player_achievements()
     charlie = gen_player_achievements()
     dylan = gen_player_achievements()
     print(f"Player {players[0]}: {alice}")
     print(f"Player {players[1]}: {bob}")
     print(f"Player {players[2]}: {charlie}")
     print(f"Player {players[3]}: {dylan}")
     all_achievement = alice.union(bob,charlie,dylan)
     print(f"All distinct achievements: {all_achievement}")
     common_ach = alice.intersection(bob,charlie,dylan)
     print(f"Common achievements: {common_ach}")
     print(f"Only {players[0]} has:{alice.difference(bob,charlie,dylan)}")
     print(f"Only {players[1]} has:{bob.difference(alice,charlie,dylan)}")
     print(f"Only {players[2]} has:{charlie.difference(bob,alice,dylan)}")
     print(f"Only {players[3]} has:{dylan.difference(bob,charlie,alice)}")
     print(f"{players[0]} is missing: {All_pos.difference(alice)}")
     print(f"{players[1]} is missing: {All_pos.difference(bob)}")
     print(f"{players[2]} is missing: {All_pos.difference(charlie)}")
     print(f"{players[3]} is missing: {All_pos.difference(dylan)}")

if __name__ == "__main__":
     main()
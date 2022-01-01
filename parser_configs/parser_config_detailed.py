#    This file contains the configuration for computing the detailed top stats in arcdps logs as parsed by Elite Insights.
#    Copyright (C) 2021 Freya Fleckenstein
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <https://www.gnu.org/licenses/>.



# How many players will be listed who achieved top stats most often for each stat?
num_players_listed = {'dmg': 1000, 'rips': 1000, 'stab': 1000, 'prot': 1000, 'aegis': 1000, 'might': 1000, 'fury': 1000, 'cleanses': 1000, 'heal': 1000, 'barrier': 1000, 'dist': 1000, 'dmg_taken': 1000, 'deaths': 1000, 'kills': 1000}
# How many players are considered to be "top" in each fight for each stat?
num_players_considered_top = {'dmg': 10, 'rips': 5, 'stab': 5, 'prot': 5, 'aegis': 5, 'might': 5, 'fury': 5, 'cleanses': 5, 'heal': 5, 'barrier': 5, 'dist': 5, 'dmg_taken': 5, 'deaths': 5, 'kills': 5}


# For what portion of all fights does a player need to be there to be considered for "consistency percentage" awards?
attendance_percentage_for_percentage = 50
# For what portion of all fights does a player need to be there to be considered for "late but great" awards?
attendance_percentage_for_late = 50
# For what portion of all fights does a player need to be there to be considered for "jack of all trades" awards? 
attendance_percentage_for_buildswap = 30

# What portion of the top total player stat does someone need to reach to be considered for total awards?
percentage_of_top_for_consistent = 0
# What portion of the total stat of the top consistent player does someone need to reach to be considered for consistency awards?
percentage_of_top_for_total = 0
# What portion of the percentage the top consistent player reached top does someone need to reach to be considered for percentage awards?
percentage_of_top_for_percentage = 0
# What portion of the percentage the top consistent player reached top does someone need to reach to be considered for late but great awards?
percentage_of_top_for_late = 100
# What portion of the percentage the top consistent player reached top does someone need to reach to be considered for jack of all trades awards?
percentage_of_top_for_buildswap = 100

# minimum number of allied players to consider a fight in the stats
min_allied_players = 10
# minimum duration of a fight to be considered in the stats
min_fight_duration = 30
# minimum number of enemies to consider a fight in the stats
min_enemy_players = 10

# names as which each specialization will show up in the stats
profession_abbreviations = {}
profession_abbreviations["Guardian"] = "Guardian"
profession_abbreviations["Dragonhunter"] = "Dragonhunter"
profession_abbreviations["Firebrand"] = "Firebrand"
profession_abbreviations["Willbender"] = "Willbender"

profession_abbreviations["Revenant"] = "Revenant"
profession_abbreviations["Herald"] = "Herald"
profession_abbreviations["Renegade"] = "Renegade"
profession_abbreviations["Vindicator"] = "Vindicator"    

profession_abbreviations["Warrior"] = "Warrior"
profession_abbreviations["Berserker"] = "Berserker"
profession_abbreviations["Spellbreaker"] = "Spellbreaker"
profession_abbreviations["Bladesworn"] = "Bladesworn"

profession_abbreviations["Engineer"] = "Engineer"
profession_abbreviations["Scrapper"] = "Scrapper"
profession_abbreviations["Holosmith"] = "Holosmith"
profession_abbreviations["Mechanist"] = "Mechanist"    

profession_abbreviations["Ranger"] = "Ranger"
profession_abbreviations["Druid"] = "Druid"
profession_abbreviations["Soulbeast"] = "Soulbeast"
profession_abbreviations["Untamed"] = "Untamed"    

profession_abbreviations["Thief"] = "Thief"
profession_abbreviations["Daredevil"] = "Daredevil"
profession_abbreviations["Deadeye"] = "Deadeye"
profession_abbreviations["Specter"] = "Specter"

profession_abbreviations["Elementalist"] = "Elementalist"
profession_abbreviations["Tempest"] = "Tempest"
profession_abbreviations["Weaver"] = "Weaver"
profession_abbreviations["Catalyst"] = "Catalyst"

profession_abbreviations["Mesmer"] = "Mesmer"
profession_abbreviations["Chronomancer"] = "Chronomancer"
profession_abbreviations["Mirage"] = "Mirage"
profession_abbreviations["Virtuoso"] = "Virtuoso"
    
profession_abbreviations["Necromancer"] = "Necromancer"
profession_abbreviations["Reaper"] = "Reaper"
profession_abbreviations["Scourge"] = "Scourge"
profession_abbreviations["Harbinger"] = "Harbinger"

# name each stat will be written as
stat_names = {}
stat_names["dmg"] = "damage"
stat_names["rips"] = "boon strips"
stat_names["stab"] = "stability output"
stat_names["prot"] = "protection output"
stat_names["aegis"] = "aegis output"
stat_names["might"] = "might output"
stat_names["fury"] = "fury output"
stat_names["cleanses"] = "condition cleanses"
stat_names["heal"] = "healing"
stat_names["barrier"] = "barrier"
stat_names["dist"] = "distance to tag"
stat_names["dmg_taken"] = "damage taken"
stat_names["kills"] = "kills"
stat_names["deaths"] = "deaths"

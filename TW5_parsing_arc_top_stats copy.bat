robocopy /mir %3 %1
mkdir empty_folder
robocopy /mir empty_folder %3
rmdir empty_folder
for %%i in (%1\*.zevtc) do (%2\GuildWars2EliteInsights.exe -c %~dp0\EI_config\EI_detailed_json_combat_replay.conf "%%i")
python %~dp0/TW5_parse_top_stats_detailed.py %1

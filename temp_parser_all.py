import re

# The full text provided by the user
text = """bundesliga Jornada 1
Equipo local
Resultado
Equipo visitante
Bayern Múnich
Bayern Múnich
6-0
Leipzig
Leipzig
1. FC Heidenheim 1846
1. FC Heidenheim 1846
1-3
Wolfsburgo
Wolfsburgo
1. FC Union Berlin
1. FC Union Berlin
2-1
VfB Stuttgart
VfB Stuttgart
Bayer Leverkusen
Bayer Leverkusen
1-2
TSG Hoffenheim
TSG Hoffenheim
Eintracht Frankfurt
Eintracht Frankfurt
4-1
Werder Bremen
Werder Bremen
Friburgo
Friburgo
1-3
Augsburgo
Augsburgo
FC St. Pauli
FC St. Pauli
3-3
Borussia Dortmund
Borussia Dortmund
Mainz 05
Mainz 05
0-1
Colonia
Colonia
Borussia Mönchengladbach
Borussia Mönchengladbach
0-0
Hamburgo
Hamburgo
Ir arriba
Jornada 2
Equipo local
Resultado
Equipo visitante
Hamburgo
Hamburgo
0-2
FC St. Pauli
FC St. Pauli
Leipzig
Leipzig
2-0
1. FC Heidenheim 1846
1. FC Heidenheim 1846
Werder Bremen
Werder Bremen
3-3
Bayer Leverkusen
Bayer Leverkusen
TSG Hoffenheim
TSG Hoffenheim
1-3
Eintracht Frankfurt
Eintracht Frankfurt
VfB Stuttgart
VfB Stuttgart
1-0
Borussia Mönchengladbach
Borussia Mönchengladbach
Augsburgo
Augsburgo
2-3
Bayern Múnich
Bayern Múnich
Wolfsburgo
Wolfsburgo
1-1
Mainz 05
Mainz 05
Borussia Dortmund
Borussia Dortmund
3-0
1. FC Union Berlin
1. FC Union Berlin
Colonia
Colonia
4-1
Friburgo
Friburgo
Ir arriba
Jornada 3
Equipo local
Resultado
Equipo visitante
Bayer Leverkusen
Bayer Leverkusen
3-1
Eintracht Frankfurt
Eintracht Frankfurt
1. FC Heidenheim 1846
1. FC Heidenheim 1846
0-2
Borussia Dortmund
Borussia Dortmund
1. FC Union Berlin
1. FC Union Berlin
2-4
TSG Hoffenheim
TSG Hoffenheim
Mainz 05
Mainz 05
0-1
Leipzig
Leipzig
Friburgo
Friburgo
3-1
VfB Stuttgart
VfB Stuttgart
Wolfsburgo
Wolfsburgo
3-3
Colonia
Colonia
Bayern Múnich
Bayern Múnich
5-0
Hamburgo
Hamburgo
FC St. Pauli
FC St. Pauli
2-1
Augsburgo
Augsburgo
Borussia Mönchengladbach
Borussia Mönchengladbach
0-4
Werder Bremen
Werder Bremen
Ir arriba
Jornada 4
Equipo local
Resultado
Equipo visitante
VfB Stuttgart
VfB Stuttgart
2-0
FC St. Pauli
FC St. Pauli
Augsburgo
Augsburgo
1-4
Mainz 05
Mainz 05
Hamburgo
Hamburgo
2-1
1. FC Heidenheim 1846
1. FC Heidenheim 1846
Werder Bremen
Werder Bremen
0-3
Friburgo
Friburgo
TSG Hoffenheim
TSG Hoffenheim
1-4
Bayern Múnich
Bayern Múnich
Leipzig
Leipzig
3-1
Colonia
Colonia
Eintracht Frankfurt
Eintracht Frankfurt
3-4
1. FC Union Berlin
1. FC Union Berlin
Bayer Leverkusen
Bayer Leverkusen
1-1
Borussia Mönchengladbach
Borussia Mönchengladbach
Borussia Dortmund
Borussia Dortmund
1-0
Wolfsburgo
Wolfsburgo
Ir arriba
Jornada 5
Equipo local
Resultado
Equipo visitante
Bayern Múnich
Bayern Múnich
4-0
Werder Bremen
Werder Bremen
1. FC Heidenheim 1846
1. FC Heidenheim 1846
2-1
Augsburgo
Augsburgo
Mainz 05
Mainz 05
0-2
Borussia Dortmund
Borussia Dortmund
FC St. Pauli
FC St. Pauli
1-2
Bayer Leverkusen
Bayer Leverkusen
Wolfsburgo
Wolfsburgo
0-1
Leipzig
Leipzig
Borussia Mönchengladbach
Borussia Mönchengladbach
4-6
Eintracht Frankfurt
Eintracht Frankfurt
Friburgo
Friburgo
1-1
TSG Hoffenheim
TSG Hoffenheim
Colonia
Colonia
1-2
VfB Stuttgart
VfB Stuttgart
1. FC Union Berlin
1. FC Union Berlin
0-0
Hamburgo
Hamburgo
Ir arriba
Jornada 6
Equipo local
Resultado
Equipo visitante
TSG Hoffenheim
TSG Hoffenheim
0-1
Colonia
Colonia
Bayer Leverkusen
Bayer Leverkusen
2-0
1. FC Union Berlin
1. FC Union Berlin
Borussia Dortmund
Borussia Dortmund
1-1
Leipzig
Leipzig
Augsburgo
Augsburgo
3-1
Wolfsburgo
Wolfsburgo
Werder Bremen
Werder Bremen
1-0
FC St. Pauli
FC St. Pauli
Eintracht Frankfurt
Eintracht Frankfurt
0-3
Bayern Múnich
Bayern Múnich
VfB Stuttgart
VfB Stuttgart
1-0
1. FC Heidenheim 1846
1. FC Heidenheim 1846
Hamburgo
Hamburgo
4-0
Mainz 05
Mainz 05
Borussia Mönchengladbach
Borussia Mönchengladbach
0-0
Friburgo
Friburgo
Ir arriba
Jornada 7
Equipo local
Resultado
Equipo visitante
1. FC Union Berlin
1. FC Union Berlin
3-1
Borussia Mönchengladbach
Borussia Mönchengladbach
1. FC Heidenheim 1846
1. FC Heidenheim 1846
2-2
Werder Bremen
Werder Bremen
Colonia
Colonia
1-1
Augsburgo
Augsburgo
Mainz 05
Mainz 05
3-4
Bayer Leverkusen
Bayer Leverkusen
Leipzig
Leipzig
2-1
Hamburgo
Hamburgo
Wolfsburgo
Wolfsburgo
0-3
VfB Stuttgart
VfB Stuttgart
Bayern Múnich
Bayern Múnich
2-1
Borussia Dortmund
Borussia Dortmund
Friburgo
Friburgo
2-2
Eintracht Frankfurt
Eintracht Frankfurt
FC St. Pauli
FC St. Pauli
0-3
TSG Hoffenheim
TSG Hoffenheim
Ir arriba
Jornada 8
Equipo local
Resultado
Equipo visitante
Werder Bremen
Werder Bremen
1-0
1. FC Union Berlin
1. FC Union Berlin
Eintracht Frankfurt
Eintracht Frankfurt
2-0
FC St. Pauli
FC St. Pauli
Augsburgo
Augsburgo
0-6
Leipzig
Leipzig
Hamburgo
Hamburgo
0-1
Wolfsburgo
Wolfsburgo
TSG Hoffenheim
TSG Hoffenheim
3-1
1. FC Heidenheim 1846
1. FC Heidenheim 1846
Borussia Mönchengladbach
Borussia Mönchengladbach
0-3
Bayern Múnich
Bayern Múnich
Borussia Dortmund
Borussia Dortmund
1-0
Colonia
Colonia
Bayer Leverkusen
Bayer Leverkusen
2-0
Friburgo
Friburgo
VfB Stuttgart
VfB Stuttgart
2-1
Mainz 05
Mainz 05
Ir arriba
Jornada 9
Equipo local
Resultado
Equipo visitante
Augsburgo
Augsburgo
0-1
Borussia Dortmund
Borussia Dortmund
1. FC Heidenheim 1846
1. FC Heidenheim 1846
1-1
Eintracht Frankfurt
Eintracht Frankfurt
1. FC Union Berlin
1. FC Union Berlin
0-0
Friburgo
Friburgo
Mainz 05
Mainz 05
1-1
Werder Bremen
Werder Bremen
FC St. Pauli
FC St. Pauli
0-4
Borussia Mönchengladbach
Borussia Mönchengladbach
Leipzig
Leipzig
3-1
VfB Stuttgart
VfB Stuttgart
Bayern Múnich
Bayern Múnich
3-0
Bayer Leverkusen
Bayer Leverkusen
Colonia
Colonia
4-1
Hamburgo
Hamburgo
Wolfsburgo
Wolfsburgo
2-3
TSG Hoffenheim
TSG Hoffenheim
Ir arriba
Jornada 10
Equipo local
Resultado
Equipo visitante
Werder Bremen
Werder Bremen
2-1
Wolfsburgo
Wolfsburgo
1. FC Union Berlin
1. FC Union Berlin
2-2
Bayern Múnich
Bayern Múnich
Bayer Leverkusen
Bayer Leverkusen
6-0
1. FC Heidenheim 1846
1. FC Heidenheim 1846
Hamburgo
Hamburgo
1-1
Borussia Dortmund
Borussia Dortmund
TSG Hoffenheim
TSG Hoffenheim
3-1
Leipzig
Leipzig
Borussia Mönchengladbach
Borussia Mönchengladbach
3-1
Colonia
Colonia
Friburgo
Friburgo
2-1
FC St. Pauli
FC St. Pauli
VfB Stuttgart
VfB Stuttgart
3-2
Augsburgo
Augsburgo
Eintracht Frankfurt
Eintracht Frankfurt
1-0
Mainz 05
Mainz 05
Ir arriba
Jornada 11
Equipo local
Resultado
Equipo visitante
Mainz 05
Mainz 05
1-1
TSG Hoffenheim
TSG Hoffenheim
1. FC Heidenheim 1846
1. FC Heidenheim 1846
0-3
Borussia Mönchengladbach
Borussia Mönchengladbach
Borussia Dortmund
Borussia Dortmund
3-3
VfB Stuttgart
VfB Stuttgart
Augsburgo
Augsburgo
1-0
Hamburgo
Hamburgo
Bayern Múnich
Bayern Múnich
6-2
Friburgo
Friburgo
Wolfsburgo
Wolfsburgo
1-3
Bayer Leverkusen
Bayer Leverkusen
Colonia
Colonia
3-4
Eintracht Frankfurt
Eintracht Frankfurt
Leipzig
Leipzig
2-0
Werder Bremen
Werder Bremen
FC St. Pauli
FC St. Pauli
0-1
1. FC Union Berlin
1. FC Union Berlin
Ir arriba
Jornada 12
Equipo local
Resultado
Equipo visitante
Borussia Mönchengladbach
Borussia Mönchengladbach
0-0
Leipzig
Leipzig
1. FC Union Berlin
1. FC Union Berlin
1-2
1. FC Heidenheim 1846
1. FC Heidenheim 1846
Bayern Múnich
Bayern Múnich
3-1
FC St. Pauli
FC St. Pauli
Werder Bremen
Werder Bremen
1-1
Colonia
Colonia
TSG Hoffenheim
TSG Hoffenheim
3-0
Augsburgo
Augsburgo
Bayer Leverkusen
Bayer Leverkusen
1-2
Borussia Dortmund
Borussia Dortmund
Hamburgo
Hamburgo
2-1
VfB Stuttgart
VfB Stuttgart
Eintracht Frankfurt
Eintracht Frankfurt
1-1
Wolfsburgo
Wolfsburgo
Friburgo
Friburgo
4-0
Mainz 05
Mainz 05
Ir arriba
Jornada 13
Equipo local
Resultado
Equipo visitante
Mainz 05
Mainz 05
0-1
Borussia Mönchengladbach
Borussia Mönchengladbach
1. FC Heidenheim 1846
1. FC Heidenheim 1846
2-1
Friburgo
Friburgo
Colonia
Colonia
1-1
FC St. Pauli
FC St. Pauli
Augsburgo
Augsburgo
2-0
Bayer Leverkusen
Bayer Leverkusen
VfB Stuttgart
VfB Stuttgart
0-5
Bayern Múnich
Bayern Múnich
Wolfsburgo
Wolfsburgo
3-1
1. FC Union Berlin
1. FC Union Berlin
Leipzig
Leipzig
6-0
Eintracht Frankfurt
Eintracht Frankfurt
Hamburgo
Hamburgo
3-2
Werder Bremen
Werder Bremen
Borussia Dortmund
Borussia Dortmund
2-0
TSG Hoffenheim
TSG Hoffenheim
Ir arriba
Jornada 14
Equipo local
Resultado
Equipo visitante
1. FC Union Berlin
1. FC Union Berlin
3-1
Leipzig
Leipzig
Borussia Mönchengladbach
Borussia Mönchengladbach
1-3
Wolfsburgo
Wolfsburgo
Eintracht Frankfurt
Eintracht Frankfurt
1-0
Augsburgo
Augsburgo
FC St. Pauli
FC St. Pauli
2-1
1. FC Heidenheim 1846
1. FC Heidenheim 1846
TSG Hoffenheim
TSG Hoffenheim
4-1
Hamburgo
Hamburgo
Bayer Leverkusen
Bayer Leverkusen
2-0
Colonia
Colonia
Friburgo
Friburgo
1-1
Borussia Dortmund
Borussia Dortmund
Bayern Múnich
Bayern Múnich
2-2
Mainz 05
Mainz 05
Werder Bremen
Werder Bremen
0-4
VfB Stuttgart
VfB Stuttgart
Ir arriba
Jornada 15
Equipo local
Resultado
Equipo visitante
Borussia Dortmund
Borussia Dortmund
2-0
Borussia Mönchengladbach
Borussia Mönchengladbach
Colonia
Colonia
0-1
1. FC Union Berlin
1. FC Union Berlin
Augsburgo
Augsburgo
0-0
Werder Bremen
Werder Bremen
Hamburgo
Hamburgo
1-1
Eintracht Frankfurt
Eintracht Frankfurt
VfB Stuttgart
VfB Stuttgart
0-0
TSG Hoffenheim
TSG Hoffenheim
Wolfsburgo
Wolfsburgo
3-4
Friburgo
Friburgo
Leipzig
Leipzig
1-3
Bayer Leverkusen
Bayer Leverkusen
Mainz 05
Mainz 05
0-0
FC St. Pauli
FC St. Pauli
1. FC Heidenheim 1846
1. FC Heidenheim 1846
0-4
Bayern Múnich
Bayern Múnich
Ir arriba
Jornada 16
Equipo local
Resultado
Equipo visitante
Eintracht Frankfurt
Eintracht Frankfurt
3-3
Borussia Dortmund
Borussia Dortmund
1. FC Heidenheim 1846
1. FC Heidenheim 1846
2-2
Colonia
Colonia
1. FC Union Berlin
1. FC Union Berlin
2-2
Mainz 05
Mainz 05
Friburgo
Friburgo
2-1
Hamburgo
Hamburgo
Bayer Leverkusen
Bayer Leverkusen
1-4
VfB Stuttgart
VfB Stuttgart
Borussia Mönchengladbach
Borussia Mönchengladbach
4-0
Augsburgo
Augsburgo
Bayern Múnich
Bayern Múnich
8-1
Wolfsburgo
Wolfsburgo
FC St. Pauli
FC St. Pauli
1-1
Leipzig
Leipzig
Werder Bremen
Werder Bremen
0-2
TSG Hoffenheim
TSG Hoffenheim
Ir arriba
Jornada 17
Equipo local
Resultado
Equipo visitante
VfB Stuttgart
VfB Stuttgart
3-2
Eintracht Frankfurt
Eintracht Frankfurt
Mainz 05
Mainz 05
2-1
1. FC Heidenheim 1846
1. FC Heidenheim 1846
Borussia Dortmund
Borussia Dortmund
3-0
Werder Bremen
Werder Bremen
Wolfsburgo
Wolfsburgo
2-1
FC St. Pauli
FC St. Pauli
Colonia
Colonia
1-3
Bayern Múnich
Bayern Múnich
Leipzig
Leipzig
2-0
Friburgo
Friburgo
TSG Hoffenheim
TSG Hoffenheim
5-1
Borussia Mönchengladbach
Borussia Mönchengladbach
Augsburgo
Augsburgo
1-1
1. FC Union Berlin
1. FC Union Berlin
Hamburgo
Hamburgo
0-1
Bayer Leverkusen
Bayer Leverkusen
Ir arriba
Jornada 18
Equipo local
Resultado
Equipo visitante
Werder Bremen
Werder Bremen
3-3
Eintracht Frankfurt
Eintracht Frankfurt
Colonia
Colonia
2-1
Mainz 05
Mainz 05
Borussia Dortmund
Borussia Dortmund
3-2
FC St. Pauli
FC St. Pauli
Hamburgo
Hamburgo
0-0
Borussia Mönchengladbach
Borussia Mönchengladbach
TSG Hoffenheim
TSG Hoffenheim
1-0
Bayer Leverkusen
Bayer Leverkusen
Wolfsburgo
Wolfsburgo
1-1
1. FC Heidenheim 1846
1. FC Heidenheim 1846
Leipzig
Leipzig
1-5
Bayern Múnich
Bayern Múnich
VfB Stuttgart
VfB Stuttgart
1-1
1. FC Union Berlin
1. FC Union Berlin
Augsburgo
Augsburgo
2-2
Friburgo
Friburgo
Ir arriba
Jornada 19
Equipo local
Resultado
Equipo visitante
FC St. Pauli
FC St. Pauli
0-0
Hamburgo
Hamburgo
1. FC Heidenheim 1846
1. FC Heidenheim 1846
0-3
Leipzig
Leipzig
Mainz 05
Mainz 05
3-1
Wolfsburgo
Wolfsburgo
Bayer Leverkusen
Bayer Leverkusen
1-0
Werder Bremen
Werder Bremen
Eintracht Frankfurt
Eintracht Frankfurt
1-3
TSG Hoffenheim
TSG Hoffenheim
Bayern Múnich
Bayern Múnich
1-2
Augsburgo
Augsburgo
1. FC Union Berlin
1. FC Union Berlin
0-3
Borussia Dortmund
Borussia Dortmund
Borussia Mönchengladbach
Borussia Mönchengladbach
0-3
VfB Stuttgart
VfB Stuttgart
Friburgo
Friburgo
2-1
Colonia
Colonia
Ir arriba
Jornada 20
Equipo local
Resultado
Equipo visitante
Colonia
Colonia
1-0
Wolfsburgo
Wolfsburgo
Eintracht Frankfurt
Eintracht Frankfurt
1-3
Bayer Leverkusen
Bayer Leverkusen
Augsburgo
Augsburgo
2-1
FC St. Pauli
FC St. Pauli
Leipzig
Leipzig
1-2
Mainz 05
Mainz 05
Werder Bremen
Werder Bremen
1-1
Borussia Mönchengladbach
Borussia Mönchengladbach
TSG Hoffenheim
TSG Hoffenheim
3-1
1. FC Union Berlin
1. FC Union Berlin
Hamburgo
Hamburgo
2-2
Bayern Múnich
Bayern Múnich
VfB Stuttgart
VfB Stuttgart
1-0
Friburgo
Friburgo
Borussia Dortmund
Borussia Dortmund
3-2
1. FC Heidenheim 1846
1. FC Heidenheim 1846
Ir arriba
Jornada 21
Equipo local
Resultado
Equipo visitante
1. FC Union Berlin
1. FC Union Berlin
1-1
Eintracht Frankfurt
Eintracht Frankfurt
1. FC Heidenheim 1846
1. FC Heidenheim 1846
0-2
Hamburgo
Hamburgo
Mainz 05
Mainz 05
2-0
Augsburgo
Augsburgo
FC St. Pauli
FC St. Pauli
2-1
VfB Stuttgart
VfB Stuttgart
Friburgo
Friburgo
1-0
Werder Bremen
Werder Bremen
Wolfsburgo
Wolfsburgo
1-2
Borussia Dortmund
Borussia Dortmund
Borussia Mönchengladbach
Borussia Mönchengladbach
1-1
Bayer Leverkusen
Bayer Leverkusen
Colonia
Colonia
1-2
Leipzig
Leipzig
Bayern Múnich
Bayern Múnich
5-1
TSG Hoffenheim
TSG Hoffenheim
Ir arriba
Jornada 22
Equipo local
Resultado
Equipo visitante
Borussia Dortmund
Borussia Dortmund
4-0
Mainz 05
Mainz 05
Bayer Leverkusen
Bayer Leverkusen
4-0
FC St. Pauli
FC St. Pauli
Eintracht Frankfurt
Eintracht Frankfurt
3-0
Borussia Mönchengladbach
Borussia Mönchengladbach
Hamburgo
Hamburgo
3-2
1. FC Union Berlin
1. FC Union Berlin
Werder Bremen
Werder Bremen
0-3
Bayern Múnich
Bayern Múnich
TSG Hoffenheim
TSG Hoffenheim
3-0
Friburgo
Friburgo
VfB Stuttgart
VfB Stuttgart
3-1
Colonia
Colonia
Augsburgo
Augsburgo
1-0
1. FC Heidenheim 1846
1. FC Heidenheim 1846
Leipzig
Leipzig
2-2
Wolfsburgo
Wolfsburgo
Ir arriba
Jornada 23
Equipo local
Resultado
Equipo visitante
Mainz 05
Mainz 05
1-1
Hamburgo
Hamburgo
Colonia
Colonia
2-2
TSG Hoffenheim
TSG Hoffenheim
1. FC Union Berlin
1. FC Union Berlin
1-0
Bayer Leverkusen
Bayer Leverkusen
Bayern Múnich
Bayern Múnich
3-2
Eintracht Frankfurt
Eintracht Frankfurt
Wolfsburgo
Wolfsburgo
2-3
Augsburgo
Augsburgo
Leipzig
Leipzig
2-2
Borussia Dortmund
Borussia Dortmund
Friburgo
Friburgo
2-1
Borussia Mönchengladbach
Borussia Mönchengladbach
FC St. Pauli
FC St. Pauli
2-1
Werder Bremen
Werder Bremen
1. FC Heidenheim 1846
1. FC Heidenheim 1846
3-3
VfB Stuttgart
VfB Stuttgart
Ir arriba
Jornada 24
Equipo local
Resultado
Equipo visitante
Augsburgo
Augsburgo
2-0
Colonia
Colonia
Bayer Leverkusen
Bayer Leverkusen
1-1
Mainz 05
Mainz 05
Borussia Mönchengladbach
Borussia Mönchengladbach
1-0
1. FC Union Berlin
1. FC Union Berlin
Werder Bremen
Werder Bremen
2-0
1. FC Heidenheim 1846
1. FC Heidenheim 1846
TSG Hoffenheim
TSG Hoffenheim
0-1
FC St. Pauli
FC St. Pauli
Borussia Dortmund
Borussia Dortmund
2-3
Bayern Múnich
Bayern Múnich
VfB Stuttgart
VfB Stuttgart
4-0
Wolfsburgo
Wolfsburgo
Eintracht Frankfurt
Eintracht Frankfurt
2-0
Friburgo
Friburgo
Hamburgo
Hamburgo
1-2
Leipzig
Leipzig
Ir arriba
Jornada 25
Equipo local
Resultado
Equipo visitante
Bayern Múnich
Bayern Múnich
4-1
Borussia Mönchengladbach
Borussia Mönchengladbach
1. FC Heidenheim 1846
1. FC Heidenheim 1846
2-4
TSG Hoffenheim
TSG Hoffenheim
Mainz 05
Mainz 05
2-2
VfB Stuttgart
VfB Stuttgart
Leipzig
Leipzig
2-1
Augsburgo
Augsburgo
Friburgo
Friburgo
3-3
Bayer Leverkusen
Bayer Leverkusen
Wolfsburgo
Wolfsburgo
1-2
Hamburgo
Hamburgo
Colonia
Colonia
1-2
Borussia Dortmund
Borussia Dortmund
FC St. Pauli
FC St. Pauli
0-0
Eintracht Frankfurt
Eintracht Frankfurt
1. FC Union Berlin
1. FC Union Berlin
1-4
Werder Bremen
Werder Bremen
Ir arriba
Jornada 26
Equipo local
Resultado
Equipo visitante
Borussia Mönchengladbach
Borussia Mönchengladbach
2-0
FC St. Pauli
FC St. Pauli
Bayer Leverkusen
Bayer Leverkusen
1-1
Bayern Múnich
Bayern Múnich
Borussia Dortmund
Borussia Dortmund
2-0
Augsburgo
Augsburgo
Eintracht Frankfurt
Eintracht Frankfurt
1-0
1. FC Heidenheim 1846
1. FC Heidenheim 1846
TSG Hoffenheim
TSG Hoffenheim
1-1
Wolfsburgo
Wolfsburgo
Hamburgo
Hamburgo
1-1
Colonia
Colonia
Werder Bremen
Werder Bremen
0-2
Mainz 05
Mainz 05
Friburgo
Friburgo
0-1
1. FC Union Berlin
1. FC Union Berlin
VfB Stuttgart
VfB Stuttgart
1-0
Leipzig
Leipzig
Ir arriba
Jornada 27
Equipo local
Resultado
Equipo visitante
Leipzig
Leipzig
5-0
TSG Hoffenheim
TSG Hoffenheim
1. FC Heidenheim 1846
1. FC Heidenheim 1846
3-3
Bayer Leverkusen
Bayer Leverkusen
Colonia
Colonia
3-3
Borussia Mönchengladbach
Borussia Mönchengladbach
Bayern Múnich
Bayern Múnich
4-0
1. FC Union Berlin
1. FC Union Berlin
Wolfsburgo
Wolfsburgo
0-1
Werder Bremen
Werder Bremen
Borussia Dortmund
Borussia Dortmund
3-2
Hamburgo
Hamburgo
Mainz 05
Mainz 05
2-1
Eintracht Frankfurt
Eintracht Frankfurt
FC St. Pauli
FC St. Pauli
1-2
Friburgo
Friburgo
Augsburgo
Augsburgo
2-5
VfB Stuttgart
VfB Stuttgart
Ir arriba
Jornada 28
Equipo local
Resultado
Equipo visitante
Bayer Leverkusen
Bayer Leverkusen
6-3
Wolfsburgo
Wolfsburgo
Borussia Mönchengladbach
Borussia Mönchengladbach
2-2
1. FC Heidenheim 1846
1. FC Heidenheim 1846
Hamburgo
Hamburgo
1-1
Augsburgo
Augsburgo
Friburgo
Friburgo
2-3
Bayern Múnich
Bayern Múnich
Werder Bremen
Werder Bremen
1-2
Leipzig
Leipzig
TSG Hoffenheim
TSG Hoffenheim
1-2
Mainz 05
Mainz 05
VfB Stuttgart
VfB Stuttgart
0-2
Borussia Dortmund
Borussia Dortmund
1. FC Union Berlin
1. FC Union Berlin
1-1
FC St. Pauli
FC St. Pauli
Eintracht Frankfurt
Eintracht Frankfurt
2-2
Colonia
Colonia
Ir arriba
Jornada 29
Equipo local
Resultado
Equipo visitante
Augsburgo
Augsburgo
2-2
TSG Hoffenheim
TSG Hoffenheim
1. FC Heidenheim 1846
1. FC Heidenheim 1846
3-1
1. FC Union Berlin
1. FC Union Berlin
Borussia Dortmund
Borussia Dortmund
0-1
Bayer Leverkusen
Bayer Leverkusen
Leipzig
Leipzig
1-0
Borussia Mönchengladbach
Borussia Mönchengladbach
Wolfsburgo
Wolfsburgo
1-2
Eintracht Frankfurt
Eintracht Frankfurt
FC St. Pauli
FC St. Pauli
0-5
Bayern Múnich
Bayern Múnich
Colonia
Colonia
3-1
Werder Bremen
Werder Bremen
VfB Stuttgart
VfB Stuttgart
4-0
Hamburgo
Hamburgo
Mainz 05
Mainz 05
0-1
Friburgo
Friburgo
Ir arriba
Jornada 30
Equipo local
Resultado
Equipo visitante
FC St. Pauli
FC St. Pauli
1-1
Colonia
Colonia
1. FC Union Berlin
1. FC Union Berlin
1-2
Wolfsburgo
Wolfsburgo
Bayer Leverkusen
Bayer Leverkusen
1-2
Augsburgo
Augsburgo
Werder Bremen
Werder Bremen
3-1
Hamburgo
Hamburgo
TSG Hoffenheim
TSG Hoffenheim
2-1
Borussia Dortmund
Borussia Dortmund
Eintracht Frankfurt
Eintracht Frankfurt
1-3
Leipzig
Leipzig
Friburgo
Friburgo
2-1
1. FC Heidenheim 1846
1. FC Heidenheim 1846
Bayern Múnich
Bayern Múnich
4-2
VfB Stuttgart
VfB Stuttgart
Borussia Mönchengladbach
Borussia Mönchengladbach
1-1
Mainz 05
Mainz 05
Ir arriba
Jornada 31
Equipo local
Resultado
Equipo visitante
Leipzig
Leipzig
3-1
1. FC Union Berlin
1. FC Union Berlin
1. FC Heidenheim 1846
1. FC Heidenheim 1846
2-0
FC St. Pauli
FC St. Pauli
Colonia
Colonia
1-2
Bayer Leverkusen
Bayer Leverkusen
Mainz 05
Mainz 05
3-4
Bayern Múnich
Bayern Múnich
Augsburgo
Augsburgo
1-1
Eintracht Frankfurt
Eintracht Frankfurt
Wolfsburgo
Wolfsburgo
0-0
Borussia Mönchengladbach
Borussia Mönchengladbach
Hamburgo
Hamburgo
1-2
TSG Hoffenheim
TSG Hoffenheim
VfB Stuttgart
VfB Stuttgart
1-1
Werder Bremen
Werder Bremen
Borussia Dortmund
Borussia Dortmund
4-0
Friburgo
Friburgo
Ir arriba
Jornada 32
Equipo local
Resultado
Equipo visitante
1. FC Union Berlin
1. FC Union Berlin
02/05
15:30
Colonia
Colonia
Eintracht Frankfurt
Eintracht Frankfurt
02/05
15:30
Hamburgo
Hamburgo
Bayern Múnich
Bayern Múnich
02/05
15:30
1. FC Heidenheim 1846
1. FC Heidenheim 1846
Werder Bremen
Werder Bremen
02/05
15:30
Augsburgo
Augsburgo
TSG Hoffenheim
TSG Hoffenheim
02/05
15:30
VfB Stuttgart
VfB Stuttgart
Bayer Leverkusen
Bayer Leverkusen
02/05
18:30
Leipzig
Leipzig
FC St. Pauli
FC St. Pauli
03/05
15:30
Mainz 05
Mainz 05
Borussia Mönchengladbach
Borussia Mönchengladbach
03/05
17:30
Borussia Dortmund
Borussia Dortmund
Friburgo
Friburgo
03/05
19:30
Wolfsburgo
Wolfsburgo
Ir arriba
Jornada 33
Equipo local
Resultado
Equipo visitante
Borussia Dortmund
Borussia Dortmund
08/05
20:30
Eintracht Frankfurt
Eintracht Frankfurt
Augsburgo
Augsburgo
09/05
15:30
Borussia Mönchengladbach
Borussia Mönchengladbach
Leipzig
Leipzig
09/05
15:30
FC St. Pauli
FC St. Pauli
TSG Hoffenheim
TSG Hoffenheim
09/05
15:30
Werder Bremen
Werder Bremen
VfB Stuttgart
VfB Stuttgart
09/05
15:30
Bayer Leverkusen
Bayer Leverkusen
Wolfsburgo
Wolfsburgo
09/05
18:30
Bayern Múnich
Bayern Múnich
Hamburgo
Hamburgo
10/05
15:30
Friburgo
Friburgo
Colonia
Colonia
10/05
17:30
1. FC Heidenheim 1846
1. FC Heidenheim 1846
Mainz 05
Mainz 05
10/05
19:30
1. FC Union Berlin
1. FC Union Berlin
Ir arriba
Jornada 34
Equipo local
Resultado
Equipo visitante
1. FC Heidenheim 1846
1. FC Heidenheim 1846
16/05
15:30
Mainz 05
Mainz 05
1. FC Union Berlin
1. FC Union Berlin
16/05
15:30
Augsburgo
Augsburgo
Bayer Leverkusen
Bayer Leverkusen
16/05
15:30
Hamburgo
Hamburgo
Borussia Mönchengladbach
Borussia Mönchengladbach
16/05
15:30
TSG Hoffenheim
TSG Hoffenheim
Eintracht Frankfurt
Eintracht Frankfurt
16/05
15:30
VfB Stuttgart
VfB Stuttgart
Bayern Múnich
Bayern Múnich
16/05
15:30
Colonia
Colonia
FC St. Pauli
FC St. Pauli
16/05
15:30
Wolfsburgo
Wolfsburgo
Friburgo
Friburgo
16/05
15:30
Leipzig
Leipzig
Werder Bremen
Werder Bremen
16/05
15:30
Borussia Dortmund
Borussia Dortmund
ahora serie a 
Jornada 1
Equipo local
Resultado
Equipo visitante
Genoa
Genoa
0-0
Lecce
Lecce
Sassuolo
Sassuolo
0-2
Nápoles
Nápoles
Milan
Milan
1-2
Cremonese
Cremonese
Roma
Roma
1-0
Bolonia
Bolonia
Cagliari
Cagliari
1-1
Fiorentina
Fiorentina
Como
Como
2-0
Lazio
Lazio
Atalanta
Atalanta
1-1
Pisa
Pisa
Juventus
Juventus
2-0
Parma
Parma
Udinese
Udinese
1-1
Hellas Verona
Hellas Verona
Inter Milán
Inter Milán
5-0
Torino
Torino
Ir arriba
Jornada 2
Equipo local
Resultado
Equipo visitante
Cremonese
Cremonese
3-2
Sassuolo
Sassuolo
Lecce
Lecce
0-2
Milan
Milan
Bolonia
Bolonia
1-0
Como
Como
Parma
Parma
1-1
Atalanta
Atalanta
Nápoles
Nápoles
1-0
Cagliari
Cagliari
Pisa
Pisa
0-1
Roma
Roma
Genoa
Genoa
0-1
Juventus
Juventus
Torino
Torino
0-0
Fiorentina
Fiorentina
Inter Milán
Inter Milán
1-2
Udinese
Udinese
Lazio
Lazio
4-0
Hellas Verona
Hellas Verona
Ir arriba
Jornada 3
Equipo local
Resultado
Equipo visitante
Cagliari
Cagliari
2-0
Parma
Parma
Juventus
Juventus
4-3
Inter Milán
Inter Milán
Fiorentina
Fiorentina
1-3
Nápoles
Nápoles
Roma
Roma
0-1
Torino
Torino
Atalanta
Atalanta
4-1
Lecce
Lecce
Pisa
Pisa
0-1
Udinese
Udinese
Sassuolo
Sassuolo
1-0
Lazio
Lazio
Milan
Milan
1-0
Bolonia
Bolonia
Hellas Verona
Hellas Verona
0-0
Cremonese
Cremonese
Como
Como
1-1
Genoa
Genoa
Ir arriba
Jornada 4
Equipo local
Resultado
Equipo visitante
Lecce
Lecce
1-2
Cagliari
Cagliari
Bolonia
Bolonia
2-1
Genoa
Genoa
Hellas Verona
Hellas Verona
1-1
Juventus
Juventus
Udinese
Udinese
0-3
Milan
Milan
Lazio
Lazio
0-1
Roma
Roma
Cremonese
Cremonese
0-0
Parma
Parma
Torino
Torino
0-3
Atalanta
Atalanta
Fiorentina
Fiorentina
1-2
Como
Como
Inter Milán
Inter Milán
2-1
Sassuolo
Sassuolo
Nápoles
Nápoles
3-2
Pisa
Pisa
Ir arriba
Jornada 5
Equipo local
Resultado
Equipo visitante
Como
Como
1-1
Cremonese
Cremonese
Juventus
Juventus
1-1
Atalanta
Atalanta
Cagliari
Cagliari
0-2
Inter Milán
Inter Milán
Sassuolo
Sassuolo
3-1
Udinese
Udinese
Pisa
Pisa
0-0
Fiorentina
Fiorentina
Roma
Roma
2-0
Hellas Verona
Hellas Verona
Lecce
Lecce
2-2
Bolonia
Bolonia
Milan
Milan
2-1
Nápoles
Nápoles
Parma
Parma
2-1
Torino
Torino
Genoa
Genoa
0-3
Lazio
Lazio
Ir arriba
Jornada 6
Equipo local
Resultado
Equipo visitante
Hellas Verona
Hellas Verona
0-1
Sassuolo
Sassuolo
Lazio
Lazio
3-3
Torino
Torino
Parma
Parma
0-1
Lecce
Lecce
Inter Milán
Inter Milán
4-1
Cremonese
Cremonese
Atalanta
Atalanta
1-1
Como
Como
Udinese
Udinese
1-1
Cagliari
Cagliari
Bolonia
Bolonia
4-0
Pisa
Pisa
Fiorentina
Fiorentina
1-2
Roma
Roma
Nápoles
Nápoles
2-1
Genoa
Genoa
Juventus
Juventus
0-0
Milan
Milan
Ir arriba
Jornada 7
Equipo local
Resultado
Equipo visitante
Lecce
Lecce
0-0
Sassuolo
Sassuolo
Pisa
Pisa
0-0
Hellas Verona
Hellas Verona
Torino
Torino
1-0
Nápoles
Nápoles
Roma
Roma
0-1
Inter Milán
Inter Milán
Como
Como
2-0
Juventus
Juventus
Cagliari
Cagliari
0-2
Bolonia
Bolonia
Genoa
Genoa
0-0
Parma
Parma
Atalanta
Atalanta
0-0
Lazio
Lazio
Milan
Milan
2-1
Fiorentina
Fiorentina
Cremonese
Cremonese
1-1
Udinese
Udinese
Ir arriba
Jornada 8
Equipo local
Resultado
Equipo visitante
Milan
Milan
2-2
Pisa
Pisa
Parma
Parma
0-0
Como
Como
Udinese
Udinese
3-2
Lecce
Lecce
Nápoles
Nápoles
3-1
Inter Milán
Inter Milán
Cremonese
Cremonese
1-1
Atalanta
Atalanta
Torino
Torino
2-1
Genoa
Genoa
Hellas Verona
Hellas Verona
2-2
Cagliari
Cagliari
Sassuolo
Sassuolo
0-1
Roma
Roma
Fiorentina
Fiorentina
2-2
Bolonia
Bolonia
Lazio
Lazio
1-0
Juventus
Juventus
Ir arriba
Jornada 9
Equipo local
Resultado
Equipo visitante
Lecce
Lecce
0-1
Nápoles
Nápoles
Atalanta
Atalanta
1-1
Milan
Milan
Como
Como
3-1
Hellas Verona
Hellas Verona
Juventus
Juventus
3-1
Udinese
Udinese
Roma
Roma
2-1
Parma
Parma
Bolonia
Bolonia
0-0
Torino
Torino
Genoa
Genoa
0-2
Cremonese
Cremonese
Inter Milán
Inter Milán
3-0
Fiorentina
Fiorentina
Cagliari
Cagliari
1-2
Sassuolo
Sassuolo
Pisa
Pisa
0-0
Lazio
Lazio
Ir arriba
Jornada 10
Equipo local
Resultado
Equipo visitante
Udinese
Udinese
1-0
Atalanta
Atalanta
Nápoles
Nápoles
0-0
Como
Como
Cremonese
Cremonese
1-2
Juventus
Juventus
Hellas Verona
Hellas Verona
1-2
Inter Milán
Inter Milán
Fiorentina
Fiorentina
0-1
Lecce
Lecce
Torino
Torino
2-2
Pisa
Pisa
Parma
Parma
1-3
Bolonia
Bolonia
Milan
Milan
1-0
Roma
Roma
Sassuolo
Sassuolo
1-2
Genoa
Genoa
Lazio
Lazio
2-0
Cagliari
Cagliari
Ir arriba
Jornada 11
Equipo local
Resultado
Equipo visitante
Pisa
Pisa
1-0
Cremonese
Cremonese
Como
Como
0-0
Cagliari
Cagliari
Lecce
Lecce
0-0
Hellas Verona
Hellas Verona
Juventus
Juventus
0-0
Torino
Torino
Parma
Parma
2-2
Milan
Milan
Atalanta
Atalanta
0-3
Sassuolo
Sassuolo
Bolonia
Bolonia
2-0
Nápoles
Nápoles
Genoa
Genoa
2-2
Fiorentina
Fiorentina
Roma
Roma
2-0
Udinese
Udinese
Inter Milán
Inter Milán
2-0
Lazio
Lazio
Ir arriba
Jornada 12
Equipo local
Resultado
Equipo visitante
Cagliari
Cagliari
3-3
Genoa
Genoa
Udinese
Udinese
0-3
Bolonia
Bolonia
Fiorentina
Fiorentina
1-1
Juventus
Juventus
Nápoles
Nápoles
3-1
Atalanta
Atalanta
Hellas Verona
Hellas Verona
1-2
Parma
Parma
Cremonese
Cremonese
1-3
Roma
Roma
Lazio
Lazio
2-0
Lecce
Lecce
Inter Milán
Inter Milán
0-1
Milan
Milan
Torino
Torino
1-5
Como
Como
Sassuolo
Sassuolo
2-2
Pisa
Pisa
Ir arriba
Jornada 13
Equipo local
Resultado
Equipo visitante
Como
Como
2-0
Sassuolo
Sassuolo
Genoa
Genoa
2-1
Hellas Verona
Hellas Verona
Parma
Parma
0-2
Udinese
Udinese
Juventus
Juventus
2-1
Cagliari
Cagliari
Milan
Milan
1-0
Lazio
Lazio
Lecce
Lecce
2-1
Torino
Torino
Pisa
Pisa
0-2
Inter Milán
Inter Milán
Atalanta
Atalanta
2-0
Fiorentina
Fiorentina
Roma
Roma
0-1
Nápoles
Nápoles
Bolonia
Bolonia
1-3
Cremonese
Cremonese
Ir arriba
Jornada 14
Equipo local
Resultado
Equipo visitante
Sassuolo
Sassuolo
3-1
Fiorentina
Fiorentina
Inter Milán
Inter Milán
4-0
Como
Como
Hellas Verona
Hellas Verona
3-1
Atalanta
Atalanta
Cremonese
Cremonese
2-0
Lecce
Lecce
Cagliari
Cagliari
1-0
Roma
Roma
Lazio
Lazio
1-1
Bolonia
Bolonia
Nápoles
Nápoles
2-1
Juventus
Juventus
Pisa
Pisa
0-1
Parma
Parma
Udinese
Udinese
1-2
Genoa
Genoa
Torino
Torino
2-3
Milan
Milan
Ir arriba
Jornada 15
Equipo local
Resultado
Equipo visitante
Lecce
Lecce
1-0
Pisa
Pisa
Torino
Torino
1-0
Cremonese
Cremonese
Parma
Parma
0-1
Lazio
Lazio
Atalanta
Atalanta
2-1
Cagliari
Cagliari
Milan
Milan
2-2
Sassuolo
Sassuolo
Fiorentina
Fiorentina
1-2
Hellas Verona
Hellas Verona
Udinese
Udinese
1-0
Nápoles
Nápoles
Genoa
Genoa
1-2
Inter Milán
Inter Milán
Bolonia
Bolonia
0-1
Juventus
Juventus
Roma
Roma
1-0
Como
Como
Ir arriba
Jornada 16
Equipo local
Resultado
Equipo visitante
Lazio
Lazio
0-0
Cremonese
Cremonese
Juventus
Juventus
2-1
Roma
Roma
Cagliari
Cagliari
2-2
Pisa
Pisa
Sassuolo
Sassuolo
0-1
Torino
Torino
Fiorentina
Fiorentina
5-1
Udinese
Udinese
Genoa
Genoa
0-1
Atalanta
Atalanta
Nápoles
Nápoles
0-0
Parma
Parma
Inter Milán
Inter Milán
1-0
Lecce
Lecce
Hellas Verona
Hellas Verona
2-3
Bolonia
Bolonia
Como
Como
1-3
Milan
Milan
Ir arriba
Jornada 17
Equipo local
Resultado
Equipo visitante
Parma
Parma
1-0
Fiorentina
Fiorentina
Lecce
Lecce
0-3
Como
Como
Torino
Torino
1-2
Cagliari
Cagliari
Udinese
Udinese
1-1
Lazio
Lazio
Pisa
Pisa
0-2
Juventus
Juventus
Milan
Milan
3-0
Hellas Verona
Hellas Verona
Cremonese
Cremonese
0-2
Nápoles
Nápoles
Bolonia
Bolonia
1-1
Sassuolo
Sassuolo
Atalanta
Atalanta
0-1
Inter Milán
Inter Milán
Roma
Roma
3-1
Genoa
Genoa
Ir arriba
Jornada 18
Equipo local
Resultado
Equipo visitante
Cagliari
Cagliari
0-1
Milan
Milan
Como
Como
1-0
Udinese
Udinese
Genoa
Genoa
1-1
Pisa
Pisa
Sassuolo
Sassuolo
1-1
Parma
Parma
Juventus
Juventus
1-1
Lecce
Lecce
Atalanta
Atalanta
1-0
Roma
Roma
Lazio
Lazio
0-2
Nápoles
Nápoles
Fiorentina
Fiorentina
1-0
Cremonese
Cremonese
Hellas Verona
Hellas Verona
0-3
Torino
Torino
Inter Milán
Inter Milán
3-1
Bolonia
Bolonia
Ir arriba
Jornada 19
Equipo local
Resultado
Equipo visitante
Pisa
Pisa
0-3
Como
Como
Lecce
Lecce
0-2
Roma
Roma
Sassuolo
Sassuolo
0-3
Juventus
Juventus
Bolonia
Bolonia
0-2
Atalanta
Atalanta
Nápoles
Nápoles
2-2
Hellas Verona
Hellas Verona
Lazio
Lazio
2-2
Fiorentina
Fiorentina
Parma
Parma
0-2
Inter Milán
Inter Milán
Torino
Torino
1-2
Udinese
Udinese
Cremonese
Cremonese
2-2
Cagliari
Cagliari
Milan
Milan
1-1
Genoa
Genoa
Ir arriba
Jornada 20
Equipo local
Resultado
Equipo visitante
Como
Como
1-1
Bolonia
Bolonia
Udinese
Udinese
2-2
Pisa
Pisa
Roma
Roma
2-0
Sassuolo
Sassuolo
Atalanta
Atalanta
2-0
Torino
Torino
Lecce
Lecce
1-2
Parma
Parma
Fiorentina
Fiorentina
1-1
Milan
Milan
Hellas Verona
Hellas Verona
0-1
Lazio
Lazio
Inter Milán
Inter Milán
2-2
Nápoles
Nápoles
Genoa
Genoa
3-0
Cagliari
Cagliari
Juventus
Juventus
5-0
Cremonese
Cremonese
Ir arriba
Jornada 21
Equipo local
Resultado
Equipo visitante
Pisa
Pisa
1-1
Atalanta
Atalanta
Udinese
Udinese
0-1
Inter Milán
Inter Milán
Nápoles
Nápoles
1-0
Sassuolo
Sassuolo
Cagliari
Cagliari
1-0
Juventus
Juventus
Parma
Parma
0-0
Genoa
Genoa
Bolonia
Bolonia
1-2
Fiorentina
Fiorentina
Torino
Torino
0-2
Roma
Roma
Milan
Milan
1-0
Lecce
Lecce
Cremonese
Cremonese
0-0
Hellas Verona
Hellas Verona
Lazio
Lazio
0-3
Como
Como
Ir arriba
Jornada 22
Equipo local
Resultado
Equipo visitante
Inter Milán
Inter Milán
6-2
Pisa
Pisa
Como
Como
6-0
Torino
Torino
Fiorentina
Fiorentina
1-2
Cagliari
Cagliari
Lecce
Lecce
0-0
Lazio
Lazio
Sassuolo
Sassuolo
1-0
Cremonese
Cremonese
Atalanta
Atalanta
4-0
Parma
Parma
Genoa
Genoa
3-2
Bolonia
Bolonia
Juventus
Juventus
3-0
Nápoles
Nápoles
Roma
Roma
1-1
Milan
Milan
Hellas Verona
Hellas Verona
1-3
Udinese
Udinese
Ir arriba
Jornada 23
Equipo local
Resultado
Equipo visitante
Lazio
Lazio
3-2
Genoa
Genoa
Pisa
Pisa
1-3
Sassuolo
Sassuolo
Nápoles
Nápoles
2-1
Fiorentina
Fiorentina
Cagliari
Cagliari
4-0
Hellas Verona
Hellas Verona
Torino
Torino
1-0
Lecce
Lecce
Como
Como
0-0
Atalanta
Atalanta
Cremonese
Cremonese
0-2
Inter Milán
Inter Milán
Parma
Parma
1-4
Juventus
Juventus
Udinese
Udinese
1-0
Roma
Roma
Bolonia
Bolonia
0-3
Milan
Milan
Ir arriba
Jornada 24
Equipo local
Resultado
Equipo visitante
Hellas Verona
Hellas Verona
0-0
Pisa
Pisa
Genoa
Genoa
2-3
Nápoles
Nápoles
Fiorentina
Fiorentina
2-2
Torino
Torino
Bolonia
Bolonia
0-1
Parma
Parma
Lecce
Lecce
2-1
Udinese
Udinese
Sassuolo
Sassuolo
0-5
Inter Milán
Inter Milán
Juventus
Juventus
2-2
Lazio
Lazio
Atalanta
Atalanta
2-1
Cremonese
Cremonese
Roma
Roma
2-0
Cagliari
Cagliari
Milan
Milan
1-1
Como
Como
Ir arriba
Jornada 25
Equipo local
Resultado
Equipo visitante
Pisa
Pisa
1-2
Milan
Milan
Como
Como
1-2
Fiorentina
Fiorentina
Lazio
Lazio
0-2
Atalanta
Atalanta
Inter Milán
Inter Milán
3-2
Juventus
Juventus
Udinese
Udinese
1-2
Sassuolo
Sassuolo
Cremonese
Cremonese
0-0
Genoa
Genoa
Parma
Parma
2-1
Hellas Verona
Hellas Verona
Torino
Torino
1-2
Bolonia
Bolonia
Nápoles
Nápoles
2-2
Roma
Roma
Cagliari
Cagliari
0-2
Lecce
Lecce
Ir arriba
Jornada 26
Equipo local
Resultado
Equipo visitante
Sassuolo
Sassuolo
3-0
Hellas Verona
Hellas Verona
Juventus
Juventus
0-2
Como
Como
Lecce
Lecce
0-2
Inter Milán
Inter Milán
Cagliari
Cagliari
0-0
Lazio
Lazio
Genoa
Genoa
3-0
Torino
Torino
Atalanta
Atalanta
2-1
Nápoles
Nápoles
Milan
Milan
0-1
Parma
Parma
Roma
Roma
3-0
Cremonese
Cremonese
Fiorentina
Fiorentina
1-0
Pisa
Pisa
Bolonia
Bolonia
1-0
Udinese
Udinese
Ir arriba
Jornada 27
Equipo local
Resultado
Equipo visitante
Parma
Parma
1-1
Cagliari
Cagliari
Como
Como
3-1
Lecce
Lecce
Hellas Verona
Hellas Verona
1-2
Nápoles
Nápoles
Inter Milán
Inter Milán
2-0
Genoa
Genoa
Cremonese
Cremonese
0-2
Milan
Milan
Sassuolo
Sassuolo
2-1
Atalanta
Atalanta
Torino
Torino
2-0
Lazio
Lazio
Roma
Roma
3-3
Juventus
Juventus
Pisa
Pisa
0-1
Bolonia
Bolonia
Udinese
Udinese
3-0
Fiorentina
Fiorentina
Ir arriba
Jornada 28
Equipo local
Resultado
Equipo visitante
Nápoles
Nápoles
2-1
Torino
Torino
Cagliari
Cagliari
1-2
Como
Como
Atalanta
Atalanta
2-2
Udinese
Udinese
Juventus
Juventus
4-0
Pisa
Pisa
Lecce
Lecce
2-1
Cremonese
Cremonese
Bolonia
Bolonia
1-2
Hellas Verona
Hellas Verona
Fiorentina
Fiorentina
0-0
Parma
Parma
Genoa
Genoa
2-1
Roma
Roma
Milan
Milan
1-0
Inter Milán
Inter Milán
Lazio
Lazio
2-1
Sassuolo
Sassuolo
Ir arriba
Jornada 29
Equipo local
Resultado
Equipo visitante
Torino
Torino
4-1
Parma
Parma
Inter Milán
Inter Milán
1-1
Atalanta
Atalanta
Nápoles
Nápoles
2-1
Lecce
Lecce
Udinese
Udinese
0-1
Juventus
Juventus
Hellas Verona
Hellas Verona
0-2
Genoa
Genoa
Pisa
Pisa
3-1
Cagliari
Cagliari
Sassuolo
Sassuolo
0-1
Bolonia
Bolonia
Como
Como
2-1
Roma
Roma
Lazio
Lazio
1-0
Milan
Milan
Cremonese
Cremonese
1-4
Fiorentina
Fiorentina
Ir arriba
Jornada 30
Equipo local
Resultado
Equipo visitante
Cagliari
Cagliari
0-1
Nápoles
Nápoles
Genoa
Genoa
0-2
Udinese
Udinese
Parma
Parma
0-2
Cremonese
Cremonese
Milan
Milan
3-2
Torino
Torino
Juventus
Juventus
1-1
Sassuolo
Sassuolo
Como
Como
5-0
Pisa
Pisa
Atalanta
Atalanta
1-0
Hellas Verona
Hellas Verona
Bolonia
Bolonia
0-2
Lazio
Lazio
Roma
Roma
1-0
Lecce
Lecce
Fiorentina
Fiorentina
1-1
Inter Milán
Inter Milán
Ir arriba
Jornada 31
Equipo local
Resultado
Equipo visitante
Sassuolo
Sassuolo
2-1
Cagliari
Cagliari
Hellas Verona
Hellas Verona
0-1
Fiorentina
Fiorentina
Lazio
Lazio
1-1
Parma
Parma
Cremonese
Cremonese
1-2
Bolonia
Bolonia
Pisa
Pisa
0-1
Torino
Torino
Inter Milán
Inter Milán
5-2
Roma
Roma
Udinese
Udinese
0-0
Como
Como
Lecce
Lecce
0-3
Atalanta
Atalanta
Juventus
Juventus
2-0
Genoa
Genoa
Nápoles
Nápoles
1-0
Milan
Milan
Ir arriba
Jornada 32
Equipo local
Resultado
Equipo visitante
Roma
Roma
3-0
Pisa
Pisa
Cagliari
Cagliari
1-0
Cremonese
Cremonese
Torino
Torino
2-1
Hellas Verona
Hellas Verona
Milan
Milan
0-3
Udinese
Udinese
Atalanta
Atalanta
0-1
Juventus
Juventus
Genoa
Genoa
2-1
Sassuolo
Sassuolo
Parma
Parma
1-1
Nápoles
Nápoles
Bolonia
Bolonia
2-0
Lecce
Lecce
Como
Como
3-4
Inter Milán
Inter Milán
Fiorentina
Fiorentina
1-0
Lazio
Lazio
Ir arriba
Jornada 33
Equipo local
Resultado
Equipo visitante
Sassuolo
Sassuolo
2-1
Como
Como
Inter Milán
Inter Milán
3-0
Cagliari
Cagliari
Udinese
Udinese
0-1
Parma
Parma
Nápoles
Nápoles
0-2
Lazio
Lazio
Roma
Roma
1-1
Atalanta
Atalanta
Cremonese
Cremonese
0-0
Torino
Torino
Hellas Verona
Hellas Verona
0-1
Milan
Milan
Pisa
Pisa
1-2
Genoa
Genoa
Juventus
Juventus
2-0
Bolonia
Bolonia
Lecce
Lecce
1-1
Fiorentina
Fiorentina
Ir arriba
Jornada 34
Equipo local
Resultado
Equipo visitante
Nápoles
Nápoles
4-0
Cremonese
Cremonese
Parma
Parma
1-0
Pisa
Pisa
Bolonia
Bolonia
0-2
Roma
Roma
Hellas Verona
Hellas Verona
0-0
Lecce
Lecce
Fiorentina
Fiorentina
0-0
Sassuolo
Sassuolo
Genoa
Genoa
0-2
Como
Como
Torino
Torino
2-2
Inter Milán
Inter Milán
Milan
Milan
0-0
Juventus
Juventus
Cagliari
Cagliari
3-2
Atalanta
Atalanta
Lazio
Lazio
3-3
Udinese
Udinese
Ir arriba
Jornada 35
Equipo local
Resultado
Equipo visitante
Pisa
Pisa
01/05
20:45
Lecce
Lecce
Udinese
Udinese
02/05
15:00
Torino
Torino
Como
Como
02/05
18:00
Nápoles
Nápoles
Atalanta
Atalanta
02/05
20:45
Genoa
Genoa
Bolonia
Bolonia
03/05
12:30
Cagliari
Cagliari
Sassuolo
Sassuolo
03/05
15:00
Milan
Milan
Juventus
Juventus
03/05
18:00
Hellas Verona
Hellas Verona
Inter Milán
Inter Milán
03/05
20:45
Parma
Parma
Cremonese
Cremonese
04/05
18:30
Lazio
Lazio
Roma
Roma
04/05
20:45
Fiorentina
Fiorentina
Ir arriba
Jornada 36
Equipo local
Resultado
Equipo visitante
Torino
Torino
08/05
20:45
Sassuolo
Sassuolo
Cagliari
Cagliari
09/05
15:00
Udinese
Udinese
Lazio
Lazio
09/05
18:00
Inter Milán
Inter Milán
Lecce
Lecce
09/05
20:45
Juventus
Juventus
Hellas Verona
Hellas Verona
10/05
12:30
Como
Como
Cremonese
Cremonese
10/05
15:00
Pisa
Pisa
Fiorentina
Fiorentina
10/05
15:00
Genoa
Genoa
Parma
Parma
10/05
18:00
Roma
Roma
Milan
Milan
10/05
20:45
Atalanta
Atalanta
Nápoles
Nápoles
11/05
20:45
Bolonia
Bolonia
Ir arriba
Jornada 37
Equipo local
Resultado
Equipo visitante
Atalanta
Atalanta
17/05
15:00
Bolonia
Bolonia
Cagliari
Cagliari
17/05
15:00
Torino
Torino
Como
Como
17/05
15:00
Parma
Parma
Genoa
Genoa
17/05
15:00
Milan
Milan
Inter Milán
Inter Milán
17/05
15:00
Hellas Verona
Hellas Verona
Juventus
Juventus
17/05
15:00
Fiorentina
Fiorentina
Pisa
Pisa
17/05
15:00
Nápoles
Nápoles
Roma
Roma
17/05
15:00
Lazio
Lazio
Sassuolo
Sassuolo
17/05
15:00
Lecce
Lecce
Udinese
Udinese
17/05
15:00
Cremonese
Cremonese
Ir arriba
Jornada 38
Equipo local
Resultado
Equipo visitante
Bolonia
Bolonia
24/05
15:00
Inter Milán
Inter Milán
Cremonese
Cremonese
24/05
15:00
Como
Como
Fiorentina
Fiorentina
24/05
15:00
Atalanta
Atalanta
Hellas Verona
Hellas Verona
24/05
15:00
Roma
Roma
Lazio
Lazio
24/05
15:00
Pisa
Pisa
Lecce
Lecce
24/05
15:00
Genoa
Genoa
Milan
Milan
24/05
15:00
Cagliari
Cagliari
Nápoles
Nápoles
24/05
15:00
Udinese
Udinese
Parma
Parma
24/05
15:00
Sassuolo
Sassuolo
Torino
Torino
24/05
15:00
Juventus
Juventus
     ahora ligue 1
Jornada 1
Equipo local
Resultado
Equipo visitante
Rennes
Rennes
1-0
O. Marsella
O. Marsella
Lens
Lens
0-1
O. Lyon
O. Lyon
Monaco
Monaco
3-1
Le Havre
Le Havre
Niza
Niza
0-1
Toulouse
Toulouse
Brest
Brest
3-3
Lille
Lille
Angers
Angers
1-0
Paris FC
Paris FC
Auxerre
Auxerre
1-0
Lorient
Lorient
Metz
Metz
0-1
Strasbourg
Strasbourg
Nantes
Nantes
0-1
PSG
PSG
Ir arriba
Jornada 2
Equipo local
Resultado
Equipo visitante
PSG
PSG
1-0
Angers
Angers
O. Marsella
O. Marsella
5-2
Paris FC
Paris FC
Niza
Niza
3-1
Auxerre
Auxerre
O. Lyon
O. Lyon
3-0
Metz
Metz
Lorient
Lorient
4-0
Rennes
Rennes
Le Havre
Le Havre
1-2
Lens
Lens
Strasbourg
Strasbourg
1-0
Nantes
Nantes
Toulouse
Toulouse
2-0
Brest
Brest
Lille
Lille
1-0
Monaco
Monaco
Ir arriba
Jornada 3
Equipo local
Resultado
Equipo visitante
Lens
Lens
3-1
Brest
Brest
Lorient
Lorient
1-7
Lille
Lille
Nantes
Nantes
1-0
Auxerre
Auxerre
Toulouse
Toulouse
3-6
PSG
PSG
Angers
Angers
1-1
Rennes
Rennes
Le Havre
Le Havre
3-1
Niza
Niza
Monaco
Monaco
3-2
Strasbourg
Strasbourg
Paris FC
Paris FC
3-2
Metz
Metz
O. Lyon
O. Lyon
1-0
O. Marsella
O. Marsella
Ir arriba
Jornada 4
Equipo local
Resultado
Equipo visitante
O. Marsella
O. Marsella
4-0
Lorient
Lorient
Niza
Niza
1-0
Nantes
Nantes
Auxerre
Auxerre
1-2
Monaco
Monaco
Lille
Lille
2-1
Toulouse
Toulouse
Brest
Brest
1-2
Paris FC
Paris FC
Metz
Metz
1-1
Angers
Angers
PSG
PSG
2-0
Lens
Lens
Strasbourg
Strasbourg
1-0
Le Havre
Le Havre
Rennes
Rennes
3-1
O. Lyon
O. Lyon
Ir arriba
Jornada 5
Equipo local
Resultado
Equipo visitante
O. Lyon
O. Lyon
1-0
Angers
Angers
Nantes
Nantes
2-2
Rennes
Rennes
Brest
Brest
4-1
Niza
Niza
Lens
Lens
3-0
Lille
Lille
Paris FC
Paris FC
2-3
Strasbourg
Strasbourg
Auxerre
Auxerre
1-0
Toulouse
Toulouse
Le Havre
Le Havre
1-1
Lorient
Lorient
Monaco
Monaco
5-2
Metz
Metz
O. Marsella
O. Marsella
1-0
PSG
PSG
Ir arriba
Jornada 6
Equipo local
Resultado
Equipo visitante
Strasbourg
Strasbourg
1-2
O. Marsella
O. Marsella
Lorient
Lorient
3-1
Monaco
Monaco
Toulouse
Toulouse
2-2
Nantes
Nantes
PSG
PSG
2-0
Auxerre
Auxerre
Niza
Niza
1-1
Paris FC
Paris FC
Angers
Angers
0-2
Brest
Brest
Lille
Lille
0-1
O. Lyon
O. Lyon
Metz
Metz
0-0
Le Havre
Le Havre
Rennes
Rennes
0-0
Lens
Lens
Ir arriba
Jornada 7
Equipo local
Resultado
Equipo visitante
Paris FC
Paris FC
2-0
Lorient
Lorient
Metz
Metz
0-3
O. Marsella
O. Marsella
Brest
Brest
0-0
Nantes
Nantes
Auxerre
Auxerre
1-2
Lens
Lens
O. Lyon
O. Lyon
1-2
Toulouse
Toulouse
Le Havre
Le Havre
2-2
Rennes
Rennes
Monaco
Monaco
2-2
Niza
Niza
Strasbourg
Strasbourg
5-0
Angers
Angers
Lille
Lille
1-1
PSG
PSG
Ir arriba
Jornada 8
Equipo local
Resultado
Equipo visitante
PSG
PSG
3-3
Strasbourg
Strasbourg
Niza
Niza
3-2
O. Lyon
O. Lyon
Angers
Angers
1-1
Monaco
Monaco
O. Marsella
O. Marsella
6-2
Le Havre
Le Havre
Lens
Lens
2-1
Paris FC
Paris FC
Lorient
Lorient
3-3
Brest
Brest
Rennes
Rennes
2-2
Auxerre
Auxerre
Toulouse
Toulouse
4-0
Metz
Metz
Nantes
Nantes
0-2
Lille
Lille
Ir arriba
Jornada 9
Equipo local
Resultado
Equipo visitante
Paris FC
Paris FC
1-2
Nantes
Nantes
Brest
Brest
0-3
PSG
PSG
Monaco
Monaco
1-0
Toulouse
Toulouse
Lens
Lens
2-1
O. Marsella
O. Marsella
Lille
Lille
6-1
Metz
Metz
Angers
Angers
2-0
Lorient
Lorient
Auxerre
Auxerre
0-1
Le Havre
Le Havre
Rennes
Rennes
1-2
Niza
Niza
O. Lyon
O. Lyon
2-1
Strasbourg
Strasbourg
Ir arriba
Jornada 10
Equipo local
Resultado
Equipo visitante
Le Havre
Le Havre
1-0
Brest
Brest
Lorient
Lorient
1-1
PSG
PSG
Metz
Metz
2-0
Lens
Lens
Niza
Niza
2-0
Lille
Lille
O. Marsella
O. Marsella
2-2
Angers
Angers
Nantes
Nantes
3-5
Monaco
Monaco
Paris FC
Paris FC
3-3
O. Lyon
O. Lyon
Strasbourg
Strasbourg
3-0
Auxerre
Auxerre
Toulouse
Toulouse
2-2
Rennes
Rennes
Ir arriba
Jornada 11
Equipo local
Resultado
Equipo visitante
PSG
PSG
1-0
Niza
Niza
Monaco
Monaco
0-1
Paris FC
Paris FC
Auxerre
Auxerre
0-1
O. Marsella
O. Marsella
Rennes
Rennes
4-1
Strasbourg
Strasbourg
Lens
Lens
3-0
Lorient
Lorient
Lille
Lille
1-0
Angers
Angers
Nantes
Nantes
0-2
Metz
Metz
Toulouse
Toulouse
0-0
Le Havre
Le Havre
Brest
Brest
0-0
O. Lyon
O. Lyon
Ir arriba
Jornada 12
Equipo local
Resultado
Equipo visitante
Paris FC
Paris FC
0-1
Rennes
Rennes
O. Marsella
O. Marsella
3-0
Brest
Brest
Le Havre
Le Havre
1-1
Nantes
Nantes
Monaco
Monaco
1-4
Lens
Lens
Lorient
Lorient
1-1
Toulouse
Toulouse
Angers
Angers
2-0
Auxerre
Auxerre
Metz
Metz
2-1
Niza
Niza
Strasbourg
Strasbourg
2-0
Lille
Lille
O. Lyon
O. Lyon
2-3
PSG
PSG
Ir arriba
Jornada 13
Equipo local
Resultado
Equipo visitante
Niza
Niza
1-5
O. Marsella
O. Marsella
Lens
Lens
1-0
Strasbourg
Strasbourg
Rennes
Rennes
4-1
Monaco
Monaco
PSG
PSG
3-0
Le Havre
Le Havre
Auxerre
Auxerre
0-0
O. Lyon
O. Lyon
Brest
Brest
3-2
Metz
Metz
Nantes
Nantes
1-1
Lorient
Lorient
Toulouse
Toulouse
0-1
Angers
Angers
Lille
Lille
4-2
Paris FC
Paris FC
Ir arriba
Jornada 14
Equipo local
Resultado
Equipo visitante
Metz
Metz
0-1
Rennes
Rennes
Monaco
Monaco
1-0
PSG
PSG
Paris FC
Paris FC
1-1
Auxerre
Auxerre
O. Marsella
O. Marsella
2-2
Toulouse
Toulouse
Strasbourg
Strasbourg
1-2
Brest
Brest
Angers
Angers
1-2
Lens
Lens
Le Havre
Le Havre
0-1
Lille
Lille
Lorient
Lorient
3-1
Niza
Niza
O. Lyon
O. Lyon
3-0
Nantes
Nantes
Ir arriba
Jornada 15
Equipo local
Resultado
Equipo visitante
Brest
Brest
1-0
Monaco
Monaco
Lille
Lille
1-0
O. Marsella
O. Marsella
Nantes
Nantes
1-2
Lens
Lens
Toulouse
Toulouse
1-0
Strasbourg
Strasbourg
PSG
PSG
5-0
Rennes
Rennes
Niza
Niza
0-1
Angers
Angers
Auxerre
Auxerre
3-1
Metz
Metz
Le Havre
Le Havre
0-0
Paris FC
Paris FC
Lorient
Lorient
1-0
O. Lyon
O. Lyon
Ir arriba
Jornada 16
Equipo local
Resultado
Equipo visitante
Angers
Angers
4-1
Nantes
Nantes
Rennes
Rennes
3-1
Brest
Brest
Metz
Metz
2-3
PSG
PSG
Paris FC
Paris FC
0-3
Toulouse
Toulouse
O. Lyon
O. Lyon
1-0
Le Havre
Le Havre
Auxerre
Auxerre
3-4
Lille
Lille
Lens
Lens
2-0
Niza
Niza
Strasbourg
Strasbourg
0-0
Lorient
Lorient
O. Marsella
O. Marsella
1-0
Monaco
Monaco
Ir arriba
Jornada 17
Equipo local
Resultado
Equipo visitante
Toulouse
Toulouse
0-3
Lens
Lens
Monaco
Monaco
1-3
O. Lyon
O. Lyon
Niza
Niza
1-1
Strasbourg
Strasbourg
Lille
Lille
0-2
Rennes
Rennes
O. Marsella
O. Marsella
0-2
Nantes
Nantes
Brest
Brest
2-0
Auxerre
Auxerre
Le Havre
Le Havre
2-1
Angers
Angers
Lorient
Lorient
1-1
Metz
Metz
PSG
PSG
2-1
Paris FC
Paris FC
Ir arriba
Jornada 18
Equipo local
Resultado
Equipo visitante
Monaco
Monaco
1-3
Lorient
Lorient
PSG
PSG
3-0
Lille
Lille
Lens
Lens
1-0
Auxerre
Auxerre
Toulouse
Toulouse
5-1
Niza
Niza
Angers
Angers
2-5
O. Marsella
O. Marsella
Strasbourg
Strasbourg
2-1
Metz
Metz
Nantes
Nantes
1-2
Paris FC
Paris FC
Rennes
Rennes
1-1
Le Havre
Le Havre
O. Lyon
O. Lyon
2-1
Brest
Brest
Ir arriba
Jornada 19
Equipo local
Resultado
Equipo visitante
Auxerre
Auxerre
0-1
PSG
PSG
Rennes
Rennes
0-2
Lorient
Lorient
Le Havre
Le Havre
0-0
Monaco
Monaco
O. Marsella
O. Marsella
3-1
Lens
Lens
Nantes
Nantes
1-4
Niza
Niza
Brest
Brest
0-2
Toulouse
Toulouse
Metz
Metz
2-5
O. Lyon
O. Lyon
Paris FC
Paris FC
0-0
Angers
Angers
Lille
Lille
1-4
Strasbourg
Strasbourg
Ir arriba
Jornada 20
Equipo local
Resultado
Equipo visitante
Lens
Lens
1-0
Le Havre
Le Havre
Paris FC
Paris FC
2-2
O. Marsella
O. Marsella
Lorient
Lorient
2-1
Nantes
Nantes
Monaco
Monaco
4-0
Rennes
Rennes
O. Lyon
O. Lyon
1-0
Lille
Lille
Angers
Angers
1-0
Metz
Metz
Niza
Niza
2-2
Brest
Brest
Toulouse
Toulouse
0-0
Auxerre
Auxerre
Strasbourg
Strasbourg
1-2
PSG
PSG
Ir arriba
Jornada 21
Equipo local
Resultado
Equipo visitante
Metz
Metz
0-0
Lille
Lille
Lens
Lens
3-1
Rennes
Rennes
Brest
Brest
2-0
Lorient
Lorient
Nantes
Nantes
0-1
O. Lyon
O. Lyon
Niza
Niza
0-0
Monaco
Monaco
Angers
Angers
1-0
Toulouse
Toulouse
Auxerre
Auxerre
0-0
Paris FC
Paris FC
Le Havre
Le Havre
2-1
Strasbourg
Strasbourg
PSG
PSG
5-0
O. Marsella
O. Marsella
Ir arriba
Jornada 22
Equipo local
Resultado
Equipo visitante
Rennes
Rennes
3-1
PSG
PSG
Monaco
Monaco
3-1
Nantes
Nantes
O. Marsella
O. Marsella
2-2
Strasbourg
Strasbourg
Lille
Lille
1-1
Brest
Brest
Paris FC
Paris FC
0-5
Lens
Lens
Le Havre
Le Havre
2-1
Toulouse
Toulouse
Lorient
Lorient
2-0
Angers
Angers
Metz
Metz
1-3
Auxerre
Auxerre
O. Lyon
O. Lyon
2-0
Niza
Niza
Ir arriba
Jornada 23
Equipo local
Resultado
Equipo visitante
Brest
Brest
2-0
O. Marsella
O. Marsella
Lens
Lens
2-3
Monaco
Monaco
Toulouse
Toulouse
1-1
Paris FC
Paris FC
PSG
PSG
3-0
Metz
Metz
Auxerre
Auxerre
0-3
Rennes
Rennes
Angers
Angers
0-1
Lille
Lille
Nantes
Nantes
2-0
Le Havre
Le Havre
Niza
Niza
3-3
Lorient
Lorient
Strasbourg
Strasbourg
3-1
O. Lyon
O. Lyon
Ir arriba
Jornada 24
Equipo local
Resultado
Equipo visitante
Strasbourg
Strasbourg
1-1
Lens
Lens
Rennes
Rennes
1-0
Toulouse
Toulouse
Monaco
Monaco
2-0
Angers
Angers
Le Havre
Le Havre
0-1
PSG
PSG
Paris FC
Paris FC
1-0
Niza
Niza
Lille
Lille
1-0
Nantes
Nantes
Lorient
Lorient
2-2
Auxerre
Auxerre
Metz
Metz
0-1
Brest
Brest
O. Marsella
O. Marsella
3-2
O. Lyon
O. Lyon
Ir arriba
Jornada 25
Equipo local
Resultado
Equipo visitante
PSG
PSG
1-3
Monaco
Monaco
Nantes
Nantes
0-1
Angers
Angers
Auxerre
Auxerre
0-0
Strasbourg
Strasbourg
Toulouse
Toulouse
0-1
O. Marsella
O. Marsella
Lens
Lens
3-0
Metz
Metz
Brest
Brest
2-0
Le Havre
Le Havre
Lille
Lille
1-1
Lorient
Lorient
Niza
Niza
0-4
Rennes
Rennes
O. Lyon
O. Lyon
1-1
Paris FC
Paris FC
Ir arriba
Jornada 26
Equipo local
Resultado
Equipo visitante
O. Marsella
O. Marsella
1-0
Auxerre
Auxerre
Lorient
Lorient
2-1
Lens
Lens
Angers
Angers
0-2
Niza
Niza
Monaco
Monaco
2-0
Brest
Brest
Strasbourg
Strasbourg
0-0
Paris FC
Paris FC
Le Havre
Le Havre
0-0
O. Lyon
O. Lyon
Metz
Metz
3-4
Toulouse
Toulouse
Rennes
Rennes
1-2
Lille
Lille
PSG
PSG
3-0
Nantes
Nantes
Ir arriba
Jornada 27
Equipo local
Resultado
Equipo visitante
Lens
Lens
5-1
Angers
Angers
Toulouse
Toulouse
1-0
Lorient
Lorient
Auxerre
Auxerre
3-0
Brest
Brest
Niza
Niza
0-4
PSG
PSG
O. Lyon
O. Lyon
1-2
Monaco
Monaco
O. Marsella
O. Marsella
1-2
Lille
Lille
Paris FC
Paris FC
3-2
Le Havre
Le Havre
Rennes
Rennes
0-0
Metz
Metz
Nantes
Nantes
2-3
Strasbourg
Strasbourg
Ir arriba
Jornada 28
Equipo local
Resultado
Equipo visitante
PSG
PSG
3-1
Toulouse
Toulouse
Strasbourg
Strasbourg
3-1
Niza
Niza
Brest
Brest
3-4
Rennes
Rennes
Lille
Lille
3-0
Lens
Lens
Angers
Angers
0-0
O. Lyon
O. Lyon
Le Havre
Le Havre
1-1
Auxerre
Auxerre
Lorient
Lorient
1-1
Paris FC
Paris FC
Metz
Metz
0-0
Nantes
Nantes
Monaco
Monaco
2-1
O. Marsella
O. Marsella
Ir arriba
Jornada 29
Equipo local
Resultado
Equipo visitante
Paris FC
Paris FC
4-1
Monaco
Monaco
O. Marsella
O. Marsella
3-1
Metz
Metz
Auxerre
Auxerre
0-0
Nantes
Nantes
Rennes
Rennes
2-1
Angers
Angers
Niza
Niza
1-1
Le Havre
Le Havre
Toulouse
Toulouse
0-4
Lille
Lille
O. Lyon
O. Lyon
2-0
Lorient
Lorient
Brest
Brest
13/05
19:00
Strasbourg
Strasbourg
Lens
Lens
13/05
21:00
PSG
PSG
Ir arriba
Jornada 30
Equipo local
Resultado
Equipo visitante
Lens
Lens
3-2
Toulouse
Toulouse
Lorient
Lorient
2-0
O. Marsella
O. Marsella
Angers
Angers
1-1
Le Havre
Le Havre
Lille
Lille
0-0
Niza
Niza
Monaco
Monaco
2-2
Auxerre
Auxerre
Metz
Metz
1-3
Paris FC
Paris FC
Nantes
Nantes
1-1
Brest
Brest
Strasbourg
Strasbourg
0-3
Rennes
Rennes
PSG
PSG
1-2
O. Lyon
O. Lyon
Ir arriba
Jornada 31
Equipo local
Resultado
Equipo visitante
Brest
Brest
3-3
Lens
Lens
O. Lyon
O. Lyon
3-2
Auxerre
Auxerre
Angers
Angers
0-3
PSG
PSG
Toulouse
Toulouse
2-2
Monaco
Monaco
Lorient
Lorient
2-3
Strasbourg
Strasbourg
Le Havre
Le Havre
4-4
Metz
Metz
Paris FC
Paris FC
0-1
Lille
Lille
Rennes
Rennes
2-1
Nantes
Nantes
O. Marsella
O. Marsella
1-1
Niza
Niza
Ir arriba
Jornada 32
Equipo local
Resultado
Equipo visitante
Nantes
Nantes
02/05
15:00
O. Marsella
O. Marsella
PSG
PSG
02/05
17:00
Lorient
Lorient
Metz
Metz
02/05
19:00
Monaco
Monaco
Niza
Niza
02/05
21:05
Lens
Lens
Lille
Lille
03/05
15:00
Le Havre
Le Havre
Auxerre
Auxerre
03/05
17:15
Angers
Angers
Paris FC
Paris FC
03/05
17:15
Brest
Brest
Strasbourg
Strasbourg
03/05
17:15
Toulouse
Toulouse
O. Lyon
O. Lyon
03/05
20:45
Rennes
Rennes
Ir arriba
Jornada 33
Equipo local
Resultado
Equipo visitante
Lens
Lens
08/05
20:45
Nantes
Nantes
Angers
Angers
10/05
21:00
Strasbourg
Strasbourg
Auxerre
Auxerre
10/05
21:00
Niza
Niza
Le Havre
Le Havre
10/05
21:00
O. Marsella
O. Marsella
Metz
Metz
10/05
21:00
Lorient
Lorient
Monaco
Monaco
10/05
21:00
Lille
Lille
PSG
PSG
10/05
21:00
Brest
Brest
Rennes
Rennes
10/05
21:00
Paris FC
Paris FC
Toulouse
Toulouse
10/05
21:00
O. Lyon
O. Lyon
Ir arriba
Jornada 34
Equipo local
Resultado
Equipo visitante
Brest
Brest
17/05
21:00
Angers
Angers
Lille
Lille
17/05
21:00
Auxerre
Auxerre
Lorient
Lorient
17/05
21:00
Le Havre
Le Havre
O. Lyon
O. Lyon
17/05
21:00
Lens
Lens
O. Marsella
O. Marsella
17/05
21:00
Rennes
Rennes
Nantes
Nantes
17/05
21:00
Toulouse
Toulouse
Niza
Niza
17/05
21:00
Metz
Metz
Paris FC
Paris FC
17/05
21:00
PSG
PSG
Strasbourg
Strasbourg
17/05
21:00
Monaco
Monaco
  y por ultimo la liga         
Jornada 1
Equipo local
Resultado
Equipo visitante
Girona
Girona
1-3
Rayo
Rayo
Villarreal
Villarreal
2-0
Oviedo
Oviedo
Mallorca
Mallorca
0-3
Barcelona
Barcelona
Alavés
Alavés
2-1
Levante
Levante
Valencia
Valencia
1-1
R. Sociedad
R. Sociedad
Celta
Celta
0-2
Getafe
Getafe
Athletic
Athletic
3-2
Sevilla
Sevilla
Espanyol
Espanyol
2-1
Atlético
Atlético
Elche
Elche
1-1
Betis
Betis
Real Madrid
Real Madrid
1-0
Osasuna
Osasuna
Ir arriba
Jornada 2
Equipo local
Resultado
Equipo visitante
Betis
Betis
1-0
Alavés
Alavés
Mallorca
Mallorca
1-1
Celta
Celta
Atlético
Atlético
1-1
Elche
Elche
Levante
Levante
2-3
Barcelona
Barcelona
Osasuna
Osasuna
1-0
Valencia
Valencia
R. Sociedad
R. Sociedad
2-2
Espanyol
Espanyol
Villarreal
Villarreal
5-0
Girona
Girona
Oviedo
Oviedo
0-3
Real Madrid
Real Madrid
Athletic
Athletic
1-0
Rayo
Rayo
Sevilla
Sevilla
1-2
Getafe
Getafe
Ir arriba
Jornada 3
Equipo local
Resultado
Equipo visitante
Elche
Elche
2-0
Levante
Levante
Valencia
Valencia
3-0
Getafe
Getafe
Alavés
Alavés
1-1
Atlético
Atlético
Oviedo
Oviedo
1-0
R. Sociedad
R. Sociedad
Girona
Girona
0-2
Sevilla
Sevilla
Real Madrid
Real Madrid
2-1
Mallorca
Mallorca
Celta
Celta
1-1
Villarreal
Villarreal
Betis
Betis
1-2
Athletic
Athletic
Espanyol
Espanyol
1-0
Osasuna
Osasuna
Rayo
Rayo
1-1
Barcelona
Barcelona
Ir arriba
Jornada 4
Equipo local
Resultado
Equipo visitante
Sevilla
Sevilla
2-2
Elche
Elche
Getafe
Getafe
2-0
Oviedo
Oviedo
R. Sociedad
R. Sociedad
1-2
Real Madrid
Real Madrid
Athletic
Athletic
0-1
Alavés
Alavés
Atlético
Atlético
2-0
Villarreal
Villarreal
Celta
Celta
1-1
Girona
Girona
Levante
Levante
2-2
Betis
Betis
Osasuna
Osasuna
2-0
Rayo
Rayo
Barcelona
Barcelona
6-0
Valencia
Valencia
Espanyol
Espanyol
3-2
Mallorca
Mallorca
Ir arriba
Jornada 5
Equipo local
Resultado
Equipo visitante
Betis
Betis
3-1
R. Sociedad
R. Sociedad
Girona
Girona
0-4
Levante
Levante
Real Madrid
Real Madrid
2-0
Espanyol
Espanyol
Alavés
Alavés
1-2
Sevilla
Sevilla
Villarreal
Villarreal
2-1
Osasuna
Osasuna
Valencia
Valencia
2-0
Athletic
Athletic
Rayo
Rayo
1-1
Celta
Celta
Mallorca
Mallorca
1-1
Atlético
Atlético
Elche
Elche
1-0
Oviedo
Oviedo
Barcelona
Barcelona
3-0
Getafe
Getafe
Ir arriba
Jornada 6
Equipo local
Resultado
Equipo visitante
Celta
Celta
1-1
Betis
Betis
Athletic
Athletic
1-1
Girona
Girona
Espanyol
Espanyol
2-2
Valencia
Valencia
Levante
Levante
1-4
Real Madrid
Real Madrid
Sevilla
Sevilla
1-2
Villarreal
Villarreal
Getafe
Getafe
1-1
Alavés
Alavés
Atlético
Atlético
3-2
Rayo
Rayo
R. Sociedad
R. Sociedad
1-0
Mallorca
Mallorca
Osasuna
Osasuna
1-1
Elche
Elche
Oviedo
Oviedo
1-3
Barcelona
Barcelona
Ir arriba
Jornada 7
Equipo local
Resultado
Equipo visitante
Girona
Girona
0-0
Espanyol
Espanyol
Getafe
Getafe
1-1
Levante
Levante
Atlético
Atlético
5-2
Real Madrid
Real Madrid
Mallorca
Mallorca
1-0
Alavés
Alavés
Villarreal
Villarreal
1-0
Athletic
Athletic
Rayo
Rayo
0-1
Sevilla
Sevilla
Elche
Elche
2-1
Celta
Celta
Barcelona
Barcelona
2-1
R. Sociedad
R. Sociedad
Betis
Betis
2-0
Osasuna
Osasuna
Valencia
Valencia
1-2
Oviedo
Oviedo
Ir arriba
Jornada 8
Equipo local
Resultado
Equipo visitante
Osasuna
Osasuna
2-1
Getafe
Getafe
Oviedo
Oviedo
0-2
Levante
Levante
Girona
Girona
2-1
Valencia
Valencia
Athletic
Athletic
2-1
Mallorca
Mallorca
Real Madrid
Real Madrid
3-1
Villarreal
Villarreal
Alavés
Alavés
3-1
Elche
Elche
Sevilla
Sevilla
4-1
Barcelona
Barcelona
Espanyol
Espanyol
1-2
Betis
Betis
R. Sociedad
R. Sociedad
0-1
Rayo
Rayo
Celta
Celta
1-1
Atlético
Atlético
Ir arriba
Jornada 9
Equipo local
Resultado
Equipo visitante
Oviedo
Oviedo
0-2
Espanyol
Espanyol
Sevilla
Sevilla
1-3
Mallorca
Mallorca
Barcelona
Barcelona
2-1
Girona
Girona
Villarreal
Villarreal
2-2
Betis
Betis
Atlético
Atlético
1-0
Osasuna
Osasuna
Elche
Elche
0-0
Athletic
Athletic
Celta
Celta
1-1
R. Sociedad
R. Sociedad
Levante
Levante
0-3
Rayo
Rayo
Getafe
Getafe
0-1
Real Madrid
Real Madrid
Alavés
Alavés
0-0
Valencia
Valencia
Ir arriba
Jornada 10
Equipo local
Resultado
Equipo visitante
R. Sociedad
R. Sociedad
2-1
Sevilla
Sevilla
Girona
Girona
3-3
Oviedo
Oviedo
Espanyol
Espanyol
1-0
Elche
Elche
Athletic
Athletic
0-1
Getafe
Getafe
Valencia
Valencia
0-2
Villarreal
Villarreal
Mallorca
Mallorca
1-1
Levante
Levante
Real Madrid
Real Madrid
2-1
Barcelona
Barcelona
Osasuna
Osasuna
2-3
Celta
Celta
Rayo
Rayo
1-0
Alavés
Alavés
Betis
Betis
0-2
Atlético
Atlético
Ir arriba
Jornada 11
Equipo local
Resultado
Equipo visitante
Getafe
Getafe
2-1
Girona
Girona
Villarreal
Villarreal
4-0
Rayo
Rayo
Atlético
Atlético
3-0
Sevilla
Sevilla
R. Sociedad
R. Sociedad
3-2
Athletic
Athletic
Real Madrid
Real Madrid
4-0
Valencia
Valencia
Levante
Levante
1-2
Celta
Celta
Alavés
Alavés
2-1
Espanyol
Espanyol
Barcelona
Barcelona
3-1
Elche
Elche
Betis
Betis
3-0
Mallorca
Mallorca
Oviedo
Oviedo
0-0
Osasuna
Osasuna
Ir arriba
Jornada 12
Equipo local
Resultado
Equipo visitante
Elche
Elche
1-1
R. Sociedad
R. Sociedad
Girona
Girona
1-0
Alavés
Alavés
Sevilla
Sevilla
1-0
Osasuna
Osasuna
Atlético
Atlético
3-1
Levante
Levante
Espanyol
Espanyol
0-2
Villarreal
Villarreal
Athletic
Athletic
1-0
Oviedo
Oviedo
Rayo
Rayo
0-0
Real Madrid
Real Madrid
Mallorca
Mallorca
1-0
Getafe
Getafe
Valencia
Valencia
1-1
Betis
Betis
Celta
Celta
2-4
Barcelona
Barcelona
Ir arriba
Jornada 13
Equipo local
Resultado
Equipo visitante
Valencia
Valencia
1-0
Levante
Levante
Alavés
Alavés
0-1
Celta
Celta
Barcelona
Barcelona
4-0
Athletic
Athletic
Osasuna
Osasuna
1-3
R. Sociedad
R. Sociedad
Villarreal
Villarreal
2-1
Mallorca
Mallorca
Oviedo
Oviedo
0-0
Rayo
Rayo
Betis
Betis
1-1
Girona
Girona
Getafe
Getafe
0-1
Atlético
Atlético
Elche
Elche
2-2
Real Madrid
Real Madrid
Espanyol
Espanyol
2-1
Sevilla
Sevilla
Ir arriba
Jornada 14
Equipo local
Resultado
Equipo visitante
Getafe
Getafe
1-0
Elche
Elche
Mallorca
Mallorca
2-2
Osasuna
Osasuna
Barcelona
Barcelona
3-1
Alavés
Alavés
Levante
Levante
0-2
Athletic
Athletic
Atlético
Atlético
2-0
Oviedo
Oviedo
R. Sociedad
R. Sociedad
2-3
Villarreal
Villarreal
Sevilla
Sevilla
0-2
Betis
Betis
Celta
Celta
0-1
Espanyol
Espanyol
Girona
Girona
1-1
Real Madrid
Real Madrid
Rayo
Rayo
1-1
Valencia
Valencia
Ir arriba
Jornada 15
Equipo local
Resultado
Equipo visitante
Oviedo
Oviedo
0-0
Mallorca
Mallorca
Villarreal
Villarreal
2-0
Getafe
Getafe
Alavés
Alavés
1-0
R. Sociedad
R. Sociedad
Betis
Betis
3-5
Barcelona
Barcelona
Athletic
Athletic
1-0
Atlético
Atlético
Elche
Elche
3-0
Girona
Girona
Valencia
Valencia
1-1
Sevilla
Sevilla
Espanyol
Espanyol
1-0
Rayo
Rayo
Real Madrid
Real Madrid
0-2
Celta
Celta
Osasuna
Osasuna
2-0
Levante
Levante
Ir arriba
Jornada 16
Equipo local
Resultado
Equipo visitante
R. Sociedad
R. Sociedad
1-2
Girona
Girona
Atlético
Atlético
2-1
Valencia
Valencia
Mallorca
Mallorca
3-1
Elche
Elche
Barcelona
Barcelona
2-0
Osasuna
Osasuna
Getafe
Getafe
0-1
Espanyol
Espanyol
Sevilla
Sevilla
4-0
Oviedo
Oviedo
Celta
Celta
2-0
Athletic
Athletic
Alavés
Alavés
1-2
Real Madrid
Real Madrid
Rayo
Rayo
0-0
Betis
Betis
Levante
Levante
0-1
Villarreal
Villarreal
Ir arriba
Jornada 17
Equipo local
Resultado
Equipo visitante
Valencia
Valencia
1-1
Mallorca
Mallorca
Oviedo
Oviedo
0-0
Celta
Celta
Levante
Levante
1-1
R. Sociedad
R. Sociedad
Osasuna
Osasuna
3-0
Alavés
Alavés
Real Madrid
Real Madrid
2-0
Sevilla
Sevilla
Girona
Girona
0-3
Atlético
Atlético
Villarreal
Villarreal
0-2
Barcelona
Barcelona
Elche
Elche
4-0
Rayo
Rayo
Betis
Betis
4-0
Getafe
Getafe
Athletic
Athletic
1-2
Espanyol
Espanyol
Ir arriba
Jornada 18
Equipo local
Resultado
Equipo visitante
Rayo
Rayo
1-1
Getafe
Getafe
Celta
Celta
4-1
Valencia
Valencia
Osasuna
Osasuna
1-1
Athletic
Athletic
Elche
Elche
1-3
Villarreal
Villarreal
Espanyol
Espanyol
0-2
Barcelona
Barcelona
Sevilla
Sevilla
0-3
Levante
Levante
Real Madrid
Real Madrid
5-1
Betis
Betis
Alavés
Alavés
1-1
Oviedo
Oviedo
Mallorca
Mallorca
1-2
Girona
Girona
R. Sociedad
R. Sociedad
1-1
Atlético
Atlético
Ir arriba
Jornada 19
Equipo local
Resultado
Equipo visitante
Barcelona
Barcelona
3-1
Atlético
Atlético
Athletic
Athletic
0-3
Real Madrid
Real Madrid
Getafe
Getafe
1-2
R. Sociedad
R. Sociedad
Oviedo
Oviedo
1-1
Betis
Betis
Villarreal
Villarreal
3-1
Alavés
Alavés
Girona
Girona
1-0
Osasuna
Osasuna
Valencia
Valencia
1-1
Elche
Elche
Rayo
Rayo
2-1
Mallorca
Mallorca
Levante
Levante
1-1
Espanyol
Espanyol
Sevilla
Sevilla
0-1
Celta
Celta
Ir arriba
Jornada 20
Equipo local
Resultado
Equipo visitante
Espanyol
Espanyol
0-2
Girona
Girona
Real Madrid
Real Madrid
2-0
Levante
Levante
Mallorca
Mallorca
3-2
Athletic
Athletic
Osasuna
Osasuna
3-2
Oviedo
Oviedo
Betis
Betis
2-0
Villarreal
Villarreal
Getafe
Getafe
0-1
Valencia
Valencia
Atlético
Atlético
1-0
Alavés
Alavés
Celta
Celta
3-0
Rayo
Rayo
R. Sociedad
R. Sociedad
2-1
Barcelona
Barcelona
Elche
Elche
2-2
Sevilla
Sevilla
Ir arriba
Jornada 21
Equipo local
Resultado
Equipo visitante
Levante
Levante
3-2
Elche
Elche
Rayo
Rayo
1-3
Osasuna
Osasuna
Valencia
Valencia
3-2
Espanyol
Espanyol
Sevilla
Sevilla
2-1
Athletic
Athletic
Villarreal
Villarreal
0-2
Real Madrid
Real Madrid
Atlético
Atlético
3-0
Mallorca
Mallorca
Barcelona
Barcelona
3-0
Oviedo
Oviedo
R. Sociedad
R. Sociedad
3-1
Celta
Celta
Alavés
Alavés
2-1
Betis
Betis
Girona
Girona
1-1
Getafe
Getafe
Ir arriba
Jornada 22
Equipo local
Resultado
Equipo visitante
Espanyol
Espanyol
1-2
Alavés
Alavés
Oviedo
Oviedo
1-0
Girona
Girona
Osasuna
Osasuna
2-2
Villarreal
Villarreal
Levante
Levante
0-0
Atlético
Atlético
Elche
Elche
1-3
Barcelona
Barcelona
Real Madrid
Real Madrid
2-1
Rayo
Rayo
Betis
Betis
2-1
Valencia
Valencia
Getafe
Getafe
0-0
Celta
Celta
Athletic
Athletic
1-1
R. Sociedad
R. Sociedad
Mallorca
Mallorca
4-1
Sevilla
Sevilla
Ir arriba
Jornada 23
Equipo local
Resultado
Equipo visitante
Celta
Celta
1-2
Osasuna
Osasuna
Barcelona
Barcelona
3-0
Mallorca
Mallorca
R. Sociedad
R. Sociedad
3-1
Elche
Elche
Alavés
Alavés
0-2
Getafe
Getafe
Athletic
Athletic
4-2
Levante
Levante
Sevilla
Sevilla
1-1
Girona
Girona
Atlético
Atlético
0-1
Betis
Betis
Valencia
Valencia
0-2
Real Madrid
Real Madrid
Villarreal
Villarreal
4-1
Espanyol
Espanyol
Rayo
Rayo
3-0
Oviedo
Oviedo
Ir arriba
Jornada 24
Equipo local
Resultado
Equipo visitante
Elche
Elche
0-0
Osasuna
Osasuna
Espanyol
Espanyol
2-2
Celta
Celta
Getafe
Getafe
2-1
Villarreal
Villarreal
Sevilla
Sevilla
1-1
Alavés
Alavés
Real Madrid
Real Madrid
4-1
R. Sociedad
R. Sociedad
Oviedo
Oviedo
1-2
Athletic
Athletic
Rayo
Rayo
3-0
Atlético
Atlético
Levante
Levante
0-2
Valencia
Valencia
Mallorca
Mallorca
1-2
Betis
Betis
Girona
Girona
2-1
Barcelona
Barcelona
Ir arriba
Jornada 25
Equipo local
Resultado
Equipo visitante
Athletic
Athletic
2-1
Elche
Elche
R. Sociedad
R. Sociedad
3-3
Oviedo
Oviedo
Betis
Betis
1-1
Rayo
Rayo
Osasuna
Osasuna
2-1
Real Madrid
Real Madrid
Atlético
Atlético
4-2
Espanyol
Espanyol
Getafe
Getafe
0-1
Sevilla
Sevilla
Barcelona
Barcelona
3-0
Levante
Levante
Celta
Celta
2-0
Mallorca
Mallorca
Villarreal
Villarreal
2-1
Valencia
Valencia
Alavés
Alavés
2-2
Girona
Girona
Ir arriba
Jornada 26
Equipo local
Resultado
Equipo visitante
Levante
Levante
2-0
Alavés
Alavés
Rayo
Rayo
1-1
Athletic
Athletic
Barcelona
Barcelona
4-1
Villarreal
Villarreal
Mallorca
Mallorca
0-1
R. Sociedad
R. Sociedad
Oviedo
Oviedo
0-1
Atlético
Atlético
Elche
Elche
2-2
Espanyol
Espanyol
Valencia
Valencia
1-0
Osasuna
Osasuna
Betis
Betis
2-2
Sevilla
Sevilla
Girona
Girona
1-2
Celta
Celta
Real Madrid
Real Madrid
0-1
Getafe
Getafe
Ir arriba
Jornada 27
Equipo local
Resultado
Equipo visitante
Celta
Celta
1-2
Real Madrid
Real Madrid
Osasuna
Osasuna
2-2
Mallorca
Mallorca
Levante
Levante
1-1
Girona
Girona
Atlético
Atlético
3-2
R. Sociedad
R. Sociedad
Athletic
Athletic
0-1
Barcelona
Barcelona
Villarreal
Villarreal
2-1
Elche
Elche
Getafe
Getafe
2-0
Betis
Betis
Sevilla
Sevilla
1-1
Rayo
Rayo
Valencia
Valencia
3-2
Alavés
Alavés
Espanyol
Espanyol
1-1
Oviedo
Oviedo
Ir arriba
Jornada 28
Equipo local
Resultado
Equipo visitante
Alavés
Alavés
1-1
Villarreal
Villarreal
Girona
Girona
3-0
Athletic
Athletic
Atlético
Atlético
1-0
Getafe
Getafe
Oviedo
Oviedo
1-0
Valencia
Valencia
Real Madrid
Real Madrid
4-1
Elche
Elche
Mallorca
Mallorca
2-1
Espanyol
Espanyol
Barcelona
Barcelona
5-2
Sevilla
Sevilla
Betis
Betis
1-1
Celta
Celta
R. Sociedad
R. Sociedad
3-1
Osasuna
Osasuna
Rayo
Rayo
1-1
Levante
Levante
Ir arriba
Jornada 29
Equipo local
Resultado
Equipo visitante
Villarreal
Villarreal
3-1
R. Sociedad
R. Sociedad
Elche
Elche
2-1
Mallorca
Mallorca
Espanyol
Espanyol
1-2
Getafe
Getafe
Levante
Levante
4-2
Oviedo
Oviedo
Osasuna
Osasuna
1-0
Girona
Girona
Sevilla
Sevilla
0-2
Valencia
Valencia
Barcelona
Barcelona
1-0
Rayo
Rayo
Celta
Celta
3-4
Alavés
Alavés
Athletic
Athletic
2-1
Betis
Betis
Real Madrid
Real Madrid
3-2
Atlético
Atlético
Ir arriba
Jornada 30
Equipo local
Resultado
Equipo visitante
Rayo
Rayo
1-0
Elche
Elche
R. Sociedad
R. Sociedad
2-0
Levante
Levante
Mallorca
Mallorca
2-1
Real Madrid
Real Madrid
Betis
Betis
0-0
Espanyol
Espanyol
Atlético
Atlético
1-2
Barcelona
Barcelona
Getafe
Getafe
2-0
Athletic
Athletic
Valencia
Valencia
2-3
Celta
Celta
Oviedo
Oviedo
1-0
Sevilla
Sevilla
Alavés
Alavés
2-2
Osasuna
Osasuna
Girona
Girona
1-0
Villarreal
Villarreal
Ir arriba
Jornada 31
Equipo local
Resultado
Equipo visitante
Real Madrid
Real Madrid
1-1
Girona
Girona
R. Sociedad
R. Sociedad
3-3
Alavés
Alavés
Elche
Elche
1-0
Valencia
Valencia
Barcelona
Barcelona
4-1
Espanyol
Espanyol
Sevilla
Sevilla
2-1
Atlético
Atlético
Osasuna
Osasuna
1-1
Betis
Betis
Mallorca
Mallorca
3-0
Rayo
Rayo
Celta
Celta
0-3
Oviedo
Oviedo
Athletic
Athletic
1-2
Villarreal
Villarreal
Levante
Levante
1-0
Getafe
Getafe
Ir arriba
Jornada 32
Equipo local
Resultado
Equipo visitante
Betis
Betis
1-1
Real Madrid
Real Madrid
Alavés
Alavés
2-1
Mallorca
Mallorca
Getafe
Getafe
0-2
Barcelona
Barcelona
Valencia
Valencia
2-1
Girona
Girona
Atlético
Atlético
3-2
Athletic
Athletic
Rayo
Rayo
3-3
R. Sociedad
R. Sociedad
Oviedo
Oviedo
1-2
Elche
Elche
Osasuna
Osasuna
2-1
Sevilla
Sevilla
Villarreal
Villarreal
2-1
Celta
Celta
Espanyol
Espanyol
0-0
Levante
Levante
Ir arriba
Jornada 33
Equipo local
Resultado
Equipo visitante
Athletic
Athletic
1-0
Osasuna
Osasuna
Mallorca
Mallorca
1-1
Valencia
Valencia
Girona
Girona
2-3
Betis
Betis
Real Madrid
Real Madrid
2-1
Alavés
Alavés
Elche
Elche
3-2
Atlético
Atlético
R. Sociedad
R. Sociedad
0-1
Getafe
Getafe
Barcelona
Barcelona
1-0
Celta
Celta
Levante
Levante
2-0
Sevilla
Sevilla
Rayo
Rayo
1-0
Espanyol
Espanyol
Oviedo
Oviedo
1-1
Villarreal
Villarreal
Ir arriba
Jornada 34
Equipo local
Resultado
Equipo visitante
Girona
Girona
01/05
21:00
Mallorca
Mallorca
Villarreal
Villarreal
02/05
14:00
Levante
Levante
Valencia
Valencia
02/05
16:15
Atlético
Atlético
Alavés
Alavés
02/05
18:30
Athletic
Athletic
Osasuna
Osasuna
02/05
21:00
Barcelona
Barcelona
Celta
Celta
03/05
14:00
Elche
Elche
Getafe
Getafe
03/05
16:15
Rayo
Rayo
Betis
Betis
03/05
18:30
Oviedo
Oviedo
Espanyol
Espanyol
03/05
21:00
Real Madrid
Real Madrid
Sevilla
Sevilla
04/05
21:00
R. Sociedad
R. Sociedad
Ir arriba
Jornada 35
Equipo local
Resultado
Equipo visitante
Levante
Levante
08/05
21:00
Osasuna
Osasuna
Elche
Elche
09/05
14:00
Alavés
Alavés
Sevilla
Sevilla
09/05
16:15
Espanyol
Espanyol
Atlético
Atlético
09/05
18:30
Celta
Celta
R. Sociedad
R. Sociedad
09/05
21:00
Betis
Betis
Mallorca
Mallorca
10/05
14:00
Villarreal
Villarreal
Athletic
Athletic
10/05
16:15
Valencia
Valencia
Oviedo
Oviedo
10/05
18:30
Getafe
Getafe
Barcelona
Barcelona
10/05
21:00
Real Madrid
Real Madrid
Rayo
Rayo
11/05
21:00
Girona
Girona
Ir arriba
Jornada 36
Equipo local
Resultado
Equipo visitante
Celta
Celta
12/05
19:00
Levante
Levante
Betis
Betis
12/05
20:00
Elche
Elche
Osasuna
Osasuna
12/05
21:30
Atlético
Atlético
Espanyol
Espanyol
13/05
19:00
Athletic
Athletic
Villarreal
Villarreal
13/05
19:00
Sevilla
Sevilla
Alavés
Alavés
13/05
21:30
Barcelona
Barcelona
Getafe
Getafe
13/05
21:30
Mallorca
Mallorca
Valencia
Valencia
14/05
19:00
Rayo
Rayo
Girona
Girona
14/05
20:00
R. Sociedad
R. Sociedad
Real Madrid
Real Madrid
14/05
21:30
Oviedo
Oviedo
Ir arriba
Jornada 37
Equipo local
Resultado
Equipo visitante
Athletic
Athletic
17/05
17:00
Celta
Celta
Atlético
Atlético
17/05
17:00
Girona
Girona
Barcelona
Barcelona
17/05
17:00
Betis
Betis
Elche
Elche
17/05
17:00
Getafe
Getafe
Levante
Levante
17/05
17:00
Mallorca
Mallorca
Osasuna
Osasuna
17/05
17:00
Espanyol
Espanyol
Rayo
Rayo
17/05
17:00
Villarreal
Villarreal
Oviedo
Oviedo
17/05
17:00
Alavés
Alavés
R. Sociedad
R. Sociedad
17/05
17:00
Valencia
Valencia
Sevilla
Sevilla
17/05
17:00
Real Madrid
Real Madrid
Ir arriba
Jornada 38
Equipo local
Resultado
Equipo visitante
Alavés
Alavés
24/05
17:00
Rayo
Rayo
Celta
Celta
24/05
17:00
Sevilla
Sevilla
Espanyol
Espanyol
24/05
17:00
R. Sociedad
R. Sociedad
Getafe
Getafe
24/05
17:00
Osasuna
Osasuna
Girona
Girona
24/05
17:00
Elche
Elche
Mallorca
Mallorca
24/05
17:00
Oviedo
Oviedo
Betis
Betis
24/05
17:00
Levante
Levante
Real Madrid
Real Madrid
24/05
17:00
Athletic
Athletic
Valencia
Valencia
24/05
17:00
Barcelona
Barcelona
Villarreal
Villarreal
24/05
17:00
Atlético
Atlético
ahora premier league
Jornada 1
Equipo local
Resultado
Equipo visitante
Liverpool
Liverpool
4-2
Bournemouth
Bournemouth
Aston Villa
Aston Villa
0-0
Newcastle United
Newcastle United
Brighton and Hove Albion
Brighton and Hove Albion
1-1
Fulham
Fulham
Sunderland
Sunderland
3-0
West Ham Utd.
West Ham Utd.
Tottenham H.
Tottenham H.
3-0
Burnley
Burnley
Wolverhampton Wanderers
Wolverhampton Wanderers
0-4
M. City
M. City
Chelsea
Chelsea
0-0
Crystal Palace
Crystal Palace
Nottingham Forest
Nottingham Forest
3-1
Brentford
Brentford
M. United
M. United
0-1
Arsenal
Arsenal
Leeds United
Leeds United
1-0
Everton
Everton
Ir arriba
Jornada 2
Equipo local
Resultado
Equipo visitante
West Ham Utd.
West Ham Utd.
1-5
Chelsea
Chelsea
M. City
M. City
0-2
Tottenham H.
Tottenham H.
Bournemouth
Bournemouth
1-0
Wolverhampton Wanderers
Wolverhampton Wanderers
Brentford
Brentford
1-0
Aston Villa
Aston Villa
Burnley
Burnley
2-0
Sunderland
Sunderland
Arsenal
Arsenal
5-0
Leeds United
Leeds United
Crystal Palace
Crystal Palace
1-1
Nottingham Forest
Nottingham Forest
Everton
Everton
2-0
Brighton and Hove Albion
Brighton and Hove Albion
Fulham
Fulham
1-1
M. United
M. United
Newcastle United
Newcastle United
2-3
Liverpool
Liverpool
Ir arriba
Jornada 3
Equipo local
Resultado
Equipo visitante
Chelsea
Chelsea
2-0
Fulham
Fulham
M. United
M. United
3-2
Burnley
Burnley
Sunderland
Sunderland
2-1
Brentford
Brentford
Tottenham H.
Tottenham H.
0-1
Bournemouth
Bournemouth
Wolverhampton Wanderers
Wolverhampton Wanderers
2-3
Everton
Everton
Leeds United
Leeds United
0-0
Newcastle United
Newcastle United
Brighton and Hove Albion
Brighton and Hove Albion
2-1
M. City
M. City
Nottingham Forest
Nottingham Forest
0-3
West Ham Utd.
West Ham Utd.
Liverpool
Liverpool
1-0
Arsenal
Arsenal
Aston Villa
Aston Villa
0-3
Crystal Palace
Crystal Palace
Ir arriba
Jornada 4
Equipo local
Resultado
Equipo visitante
Arsenal
Arsenal
3-0
Nottingham Forest
Nottingham Forest
Bournemouth
Bournemouth
2-1
Brighton and Hove Albion
Brighton and Hove Albion
Crystal Palace
Crystal Palace
0-0
Sunderland
Sunderland
Everton
Everton
0-0
Aston Villa
Aston Villa
Fulham
Fulham
1-0
Leeds United
Leeds United
Newcastle United
Newcastle United
1-0
Wolverhampton Wanderers
Wolverhampton Wanderers
West Ham Utd.
West Ham Utd.
0-3
Tottenham H.
Tottenham H.
Brentford
Brentford
2-2
Chelsea
Chelsea
Burnley
Burnley
0-1
Liverpool
Liverpool
M. City
M. City
3-0
M. United
M. United
Ir arriba
Jornada 5
Equipo local
Resultado
Equipo visitante
Liverpool
Liverpool
2-1
Everton
Everton
Brighton and Hove Albion
Brighton and Hove Albion
2-2
Tottenham H.
Tottenham H.
Burnley
Burnley
1-1
Nottingham Forest
Nottingham Forest
West Ham Utd.
West Ham Utd.
1-2
Crystal Palace
Crystal Palace
Wolverhampton Wanderers
Wolverhampton Wanderers
1-3
Leeds United
Leeds United
M. United
M. United
2-1
Chelsea
Chelsea
Fulham
Fulham
3-1
Brentford
Brentford
Bournemouth
Bournemouth
0-0
Newcastle United
Newcastle United
Sunderland
Sunderland
1-1
Aston Villa
Aston Villa
Arsenal
Arsenal
1-1
M. City
M. City
Ir arriba
Jornada 6
Equipo local
Resultado
Equipo visitante
Brentford
Brentford
3-1
M. United
M. United
Chelsea
Chelsea
1-3
Brighton and Hove Albion
Brighton and Hove Albion
Crystal Palace
Crystal Palace
2-1
Liverpool
Liverpool
Leeds United
Leeds United
2-2
Bournemouth
Bournemouth
M. City
M. City
5-1
Burnley
Burnley
Nottingham Forest
Nottingham Forest
0-1
Sunderland
Sunderland
Tottenham H.
Tottenham H.
1-1
Wolverhampton Wanderers
Wolverhampton Wanderers
Aston Villa
Aston Villa
3-1
Fulham
Fulham
Newcastle United
Newcastle United
1-2
Arsenal
Arsenal
Everton
Everton
1-1
West Ham Utd.
West Ham Utd.
Ir arriba
Jornada 7
Equipo local
Resultado
Equipo visitante
Bournemouth
Bournemouth
3-1
Fulham
Fulham
Leeds United
Leeds United
1-2
Tottenham H.
Tottenham H.
Arsenal
Arsenal
2-0
West Ham Utd.
West Ham Utd.
M. United
M. United
2-0
Sunderland
Sunderland
Chelsea
Chelsea
2-1
Liverpool
Liverpool
Aston Villa
Aston Villa
2-1
Burnley
Burnley
Everton
Everton
2-1
Crystal Palace
Crystal Palace
Newcastle United
Newcastle United
2-0
Nottingham Forest
Nottingham Forest
Wolverhampton Wanderers
Wolverhampton Wanderers
1-1
Brighton and Hove Albion
Brighton and Hove Albion
Brentford
Brentford
0-1
M. City
M. City
Ir arriba
Jornada 8
Equipo local
Resultado
Equipo visitante
Nottingham Forest
Nottingham Forest
0-3
Chelsea
Chelsea
Brighton and Hove Albion
Brighton and Hove Albion
2-1
Newcastle United
Newcastle United
Burnley
Burnley
2-0
Leeds United
Leeds United
Crystal Palace
Crystal Palace
3-3
Bournemouth
Bournemouth
M. City
M. City
2-0
Everton
Everton
Sunderland
Sunderland
2-0
Wolverhampton Wanderers
Wolverhampton Wanderers
Fulham
Fulham
0-1
Arsenal
Arsenal
Tottenham H.
Tottenham H.
1-2
Aston Villa
Aston Villa
Liverpool
Liverpool
1-2
M. United
M. United
West Ham Utd.
West Ham Utd.
0-2
Brentford
Brentford
Ir arriba
Jornada 9
Equipo local
Resultado
Equipo visitante
Leeds United
Leeds United
2-1
West Ham Utd.
West Ham Utd.
Chelsea
Chelsea
1-2
Sunderland
Sunderland
Newcastle United
Newcastle United
2-1
Fulham
Fulham
M. United
M. United
4-2
Brighton and Hove Albion
Brighton and Hove Albion
Brentford
Brentford
3-2
Liverpool
Liverpool
Arsenal
Arsenal
1-0
Crystal Palace
Crystal Palace
Aston Villa
Aston Villa
1-0
M. City
M. City
Bournemouth
Bournemouth
2-0
Nottingham Forest
Nottingham Forest
Wolverhampton Wanderers
Wolverhampton Wanderers
2-3
Burnley
Burnley
Everton
Everton
0-3
Tottenham H.
Tottenham H.
Ir arriba
Jornada 10
Equipo local
Resultado
Equipo visitante
Brighton and Hove Albion
Brighton and Hove Albion
3-0
Leeds United
Leeds United
Burnley
Burnley
0-2
Arsenal
Arsenal
Crystal Palace
Crystal Palace
2-0
Brentford
Brentford
Fulham
Fulham
3-0
Wolverhampton Wanderers
Wolverhampton Wanderers
Nottingham Forest
Nottingham Forest
2-2
M. United
M. United
Tottenham H.
Tottenham H.
0-1
Chelsea
Chelsea
Liverpool
Liverpool
2-0
Aston Villa
Aston Villa
West Ham Utd.
West Ham Utd.
3-1
Newcastle United
Newcastle United
M. City
M. City
3-1
Bournemouth
Bournemouth
Sunderland
Sunderland
1-1
Everton
Everton
Ir arriba
Jornada 11
Equipo local
Resultado
Equipo visitante
Tottenham H.
Tottenham H.
2-2
M. United
M. United
Everton
Everton
2-0
Fulham
Fulham
West Ham Utd.
West Ham Utd.
3-2
Burnley
Burnley
Sunderland
Sunderland
2-2
Arsenal
Arsenal
Chelsea
Chelsea
3-0
Wolverhampton Wanderers
Wolverhampton Wanderers
Aston Villa
Aston Villa
4-0
Bournemouth
Bournemouth
Brentford
Brentford
3-1
Newcastle United
Newcastle United
Crystal Palace
Crystal Palace
0-0
Brighton and Hove Albion
Brighton and Hove Albion
Nottingham Forest
Nottingham Forest
3-1
Leeds United
Leeds United
M. City
M. City
3-0
Liverpool
Liverpool
Ir arriba
Jornada 12
Equipo local
Resultado
Equipo visitante
Burnley
Burnley
0-2
Chelsea
Chelsea
Bournemouth
Bournemouth
2-2
West Ham Utd.
West Ham Utd.
Brighton and Hove Albion
Brighton and Hove Albion
2-1
Brentford
Brentford
Fulham
Fulham
1-0
Sunderland
Sunderland
Liverpool
Liverpool
0-3
Nottingham Forest
Nottingham Forest
Wolverhampton Wanderers
Wolverhampton Wanderers
0-2
Crystal Palace
Crystal Palace
Newcastle United
Newcastle United
2-1
M. City
M. City
Leeds United
Leeds United
1-2
Aston Villa
Aston Villa
Arsenal
Arsenal
4-1
Tottenham H.
Tottenham H.
M. United
M. United
0-1
Everton
Everton
Ir arriba
Jornada 13
Equipo local
Resultado
Equipo visitante
Brentford
Brentford
3-1
Burnley
Burnley
M. City
M. City
3-2
Leeds United
Leeds United
Sunderland
Sunderland
3-2
Bournemouth
Bournemouth
Everton
Everton
1-4
Newcastle United
Newcastle United
Tottenham H.
Tottenham H.
1-2
Fulham
Fulham
Crystal Palace
Crystal Palace
1-2
M. United
M. United
Aston Villa
Aston Villa
1-0
Wolverhampton Wanderers
Wolverhampton Wanderers
Nottingham Forest
Nottingham Forest
0-2
Brighton and Hove Albion
Brighton and Hove Albion
West Ham Utd.
West Ham Utd.
0-2
Liverpool
Liverpool
Chelsea
Chelsea
1-1
Arsenal
Arsenal
Ir arriba
Jornada 14
Equipo local
Resultado
Equipo visitante
Bournemouth
Bournemouth
0-1
Everton
Everton
Fulham
Fulham
4-5
M. City
M. City
Newcastle United
Newcastle United
2-2
Tottenham H.
Tottenham H.
Arsenal
Arsenal
2-0
Brentford
Brentford
Brighton and Hove Albion
Brighton and Hove Albion
3-4
Aston Villa
Aston Villa
Burnley
Burnley
0-1
Crystal Palace
Crystal Palace
Wolverhampton Wanderers
Wolverhampton Wanderers
0-1
Nottingham Forest
Nottingham Forest
Leeds United
Leeds United
3-1
Chelsea
Chelsea
Liverpool
Liverpool
1-1
Sunderland
Sunderland
M. United
M. United
1-1
West Ham Utd.
West Ham Utd.
Ir arriba
Jornada 15
Equipo local
Resultado
Equipo visitante
Aston Villa
Aston Villa
2-1
Arsenal
Arsenal
Bournemouth
Bournemouth
0-0
Chelsea
Chelsea
Everton
Everton
3-0
Nottingham Forest
Nottingham Forest
M. City
M. City
3-0
Sunderland
Sunderland
Newcastle United
Newcastle United
2-1
Burnley
Burnley
Tottenham H.
Tottenham H.
2-0
Brentford
Brentford
Leeds United
Leeds United
3-3
Liverpool
Liverpool
Brighton and Hove Albion
Brighton and Hove Albion
1-1
West Ham Utd.
West Ham Utd.
Fulham
Fulham
1-2
Crystal Palace
Crystal Palace
Wolverhampton Wanderers
Wolverhampton Wanderers
1-4
M. United
M. United
Ir arriba
Jornada 16
Equipo local
Resultado
Equipo visitante
Chelsea
Chelsea
2-0
Everton
Everton
Liverpool
Liverpool
2-0
Brighton and Hove Albion
Brighton and Hove Albion
Burnley
Burnley
2-3
Fulham
Fulham
Arsenal
Arsenal
2-1
Wolverhampton Wanderers
Wolverhampton Wanderers
Crystal Palace
Crystal Palace
0-3
M. City
M. City
Nottingham Forest
Nottingham Forest
3-0
Tottenham H.
Tottenham H.
Sunderland
Sunderland
1-0
Newcastle United
Newcastle United
West Ham Utd.
West Ham Utd.
2-3
Aston Villa
Aston Villa
Brentford
Brentford
1-1
Leeds United
Leeds United
M. United
M. United
4-4
Bournemouth
Bournemouth
Ir arriba
Jornada 17
Equipo local
Resultado
Equipo visitante
Newcastle United
Newcastle United
2-2
Chelsea
Chelsea
Bournemouth
Bournemouth
1-1
Burnley
Burnley
Brighton and Hove Albion
Brighton and Hove Albion
0-0
Sunderland
Sunderland
M. City
M. City
3-0
West Ham Utd.
West Ham Utd.
Wolverhampton Wanderers
Wolverhampton Wanderers
0-2
Brentford
Brentford
Tottenham H.
Tottenham H.
1-2
Liverpool
Liverpool
Everton
Everton
0-1
Arsenal
Arsenal
Leeds United
Leeds United
4-1
Crystal Palace
Crystal Palace
Aston Villa
Aston Villa
2-1
M. United
M. United
Fulham
Fulham
1-0
Nottingham Forest
Nottingham Forest
Ir arriba
Jornada 18
Equipo local
Resultado
Equipo visitante
M. United
M. United
1-0
Newcastle United
Newcastle United
Nottingham Forest
Nottingham Forest
1-2
M. City
M. City
Arsenal
Arsenal
2-1
Brighton and Hove Albion
Brighton and Hove Albion
Brentford
Brentford
4-1
Bournemouth
Bournemouth
Burnley
Burnley
0-0
Everton
Everton
Liverpool
Liverpool
2-1
Wolverhampton Wanderers
Wolverhampton Wanderers
West Ham Utd.
West Ham Utd.
0-1
Fulham
Fulham
Chelsea
Chelsea
1-2
Aston Villa
Aston Villa
Sunderland
Sunderland
1-1
Leeds United
Leeds United
Crystal Palace
Crystal Palace
0-1
Tottenham H.
Tottenham H.
Ir arriba
Jornada 19
Equipo local
Resultado
Equipo visitante
Burnley
Burnley
1-3
Newcastle United
Newcastle United
Chelsea
Chelsea
2-2
Bournemouth
Bournemouth
Nottingham Forest
Nottingham Forest
0-2
Everton
Everton
West Ham Utd.
West Ham Utd.
2-2
Brighton and Hove Albion
Brighton and Hove Albion
Arsenal
Arsenal
4-1
Aston Villa
Aston Villa
M. United
M. United
1-1
Wolverhampton Wanderers
Wolverhampton Wanderers
Crystal Palace
Crystal Palace
1-1
Fulham
Fulham
Liverpool
Liverpool
0-0
Leeds United
Leeds United
Brentford
Brentford
0-0
Tottenham H.
Tottenham H.
Sunderland
Sunderland
0-0
M. City
M. City
Ir arriba
Jornada 20
Equipo local
Resultado
Equipo visitante
Aston Villa
Aston Villa
3-1
Nottingham Forest
Nottingham Forest
Brighton and Hove Albion
Brighton and Hove Albion
2-0
Burnley
Burnley
Wolverhampton Wanderers
Wolverhampton Wanderers
3-0
West Ham Utd.
West Ham Utd.
Bournemouth
Bournemouth
2-3
Arsenal
Arsenal
Leeds United
Leeds United
1-1
M. United
M. United
Everton
Everton
2-4
Brentford
Brentford
Newcastle United
Newcastle United
2-0
Crystal Palace
Crystal Palace
Tottenham H.
Tottenham H.
1-1
Sunderland
Sunderland
Fulham
Fulham
2-2
Liverpool
Liverpool
M. City
M. City
1-1
Chelsea
Chelsea
Ir arriba
Jornada 21
Equipo local
Resultado
Equipo visitante
West Ham Utd.
West Ham Utd.
1-2
Nottingham Forest
Nottingham Forest
Bournemouth
Bournemouth
3-2
Tottenham H.
Tottenham H.
Brentford
Brentford
3-0
Sunderland
Sunderland
Crystal Palace
Crystal Palace
0-0
Aston Villa
Aston Villa
Everton
Everton
1-1
Wolverhampton Wanderers
Wolverhampton Wanderers
Fulham
Fulham
2-1
Chelsea
Chelsea
M. City
M. City
1-1
Brighton and Hove Albion
Brighton and Hove Albion
Burnley
Burnley
2-2
M. United
M. United
Newcastle United
Newcastle United
4-3
Leeds United
Leeds United
Arsenal
Arsenal
0-0
Liverpool
Liverpool
Ir arriba
Jornada 22
Equipo local
Resultado
Equipo visitante
M. United
M. United
2-0
M. City
M. City
Chelsea
Chelsea
2-0
Brentford
Brentford
Leeds United
Leeds United
1-0
Fulham
Fulham
Liverpool
Liverpool
1-1
Burnley
Burnley
Sunderland
Sunderland
2-1
Crystal Palace
Crystal Palace
Tottenham H.
Tottenham H.
1-2
West Ham Utd.
West Ham Utd.
Nottingham Forest
Nottingham Forest
0-0
Arsenal
Arsenal
Wolverhampton Wanderers
Wolverhampton Wanderers
0-0
Newcastle United
Newcastle United
Aston Villa
Aston Villa
0-1
Everton
Everton
Brighton and Hove Albion
Brighton and Hove Albion
1-1
Bournemouth
Bournemouth
Ir arriba
Jornada 23
Equipo local
Resultado
Equipo visitante
West Ham Utd.
West Ham Utd.
3-1
Sunderland
Sunderland
Burnley
Burnley
2-2
Tottenham H.
Tottenham H.
Fulham
Fulham
2-1
Brighton and Hove Albion
Brighton and Hove Albion
M. City
M. City
2-0
Wolverhampton Wanderers
Wolverhampton Wanderers
Bournemouth
Bournemouth
3-2
Liverpool
Liverpool
Brentford
Brentford
0-2
Nottingham Forest
Nottingham Forest
Crystal Palace
Crystal Palace
1-3
Chelsea
Chelsea
Newcastle United
Newcastle United
0-2
Aston Villa
Aston Villa
Arsenal
Arsenal
2-3
M. United
M. United
Everton
Everton
1-1
Leeds United
Leeds United
Ir arriba
Jornada 24
Equipo local
Resultado
Equipo visitante
Brighton and Hove Albion
Brighton and Hove Albion
1-1
Everton
Everton
Leeds United
Leeds United
0-4
Arsenal
Arsenal
Wolverhampton Wanderers
Wolverhampton Wanderers
0-2
Bournemouth
Bournemouth
Chelsea
Chelsea
3-2
West Ham Utd.
West Ham Utd.
Liverpool
Liverpool
4-1
Newcastle United
Newcastle United
Aston Villa
Aston Villa
0-1
Brentford
Brentford
M. United
M. United
3-2
Fulham
Fulham
Nottingham Forest
Nottingham Forest
1-1
Crystal Palace
Crystal Palace
Tottenham H.
Tottenham H.
2-2
M. City
M. City
Sunderland
Sunderland
3-0
Burnley
Burnley
Ir arriba
Jornada 25
Equipo local
Resultado
Equipo visitante
Leeds United
Leeds United
3-1
Nottingham Forest
Nottingham Forest
M. United
M. United
2-0
Tottenham H.
Tottenham H.
Arsenal
Arsenal
3-0
Sunderland
Sunderland
Bournemouth
Bournemouth
1-1
Aston Villa
Aston Villa
Burnley
Burnley
0-2
West Ham Utd.
West Ham Utd.
Fulham
Fulham
1-2
Everton
Everton
Wolverhampton Wanderers
Wolverhampton Wanderers
1-3
Chelsea
Chelsea
Newcastle United
Newcastle United
2-3
Brentford
Brentford
Brighton and Hove Albion
Brighton and Hove Albion
0-1
Crystal Palace
Crystal Palace
Liverpool
Liverpool
1-2
M. City
M. City
Ir arriba
Jornada 26
Equipo local
Resultado
Equipo visitante
Chelsea
Chelsea
2-2
Leeds United
Leeds United
Everton
Everton
1-2
Bournemouth
Bournemouth
Tottenham H.
Tottenham H.
1-2
Newcastle United
Newcastle United
West Ham Utd.
West Ham Utd.
1-1
M. United
M. United
Aston Villa
Aston Villa
1-0
Brighton and Hove Albion
Brighton and Hove Albion
M. City
M. City
3-0
Fulham
Fulham
Nottingham Forest
Nottingham Forest
0-0
Wolverhampton Wanderers
Wolverhampton Wanderers
Crystal Palace
Crystal Palace
2-3
Burnley
Burnley
Sunderland
Sunderland
0-1
Liverpool
Liverpool
Brentford
Brentford
1-1
Arsenal
Arsenal
Ir arriba
Jornada 27
Equipo local
Resultado
Equipo visitante
Aston Villa
Aston Villa
1-1
Leeds United
Leeds United
Brentford
Brentford
0-2
Brighton and Hove Albion
Brighton and Hove Albion
Chelsea
Chelsea
1-1
Burnley
Burnley
West Ham Utd.
West Ham Utd.
0-0
Bournemouth
Bournemouth
M. City
M. City
2-1
Newcastle United
Newcastle United
Crystal Palace
Crystal Palace
1-0
Wolverhampton Wanderers
Wolverhampton Wanderers
Nottingham Forest
Nottingham Forest
0-1
Liverpool
Liverpool
Sunderland
Sunderland
1-3
Fulham
Fulham
Tottenham H.
Tottenham H.
1-4
Arsenal
Arsenal
Everton
Everton
0-1
M. United
M. United
Ir arriba
Jornada 28
Equipo local
Resultado
Equipo visitante
Wolverhampton Wanderers
Wolverhampton Wanderers
2-0
Aston Villa
Aston Villa
Bournemouth
Bournemouth
1-1
Sunderland
Sunderland
Burnley
Burnley
3-4
Brentford
Brentford
Liverpool
Liverpool
5-2
West Ham Utd.
West Ham Utd.
Newcastle United
Newcastle United
2-3
Everton
Everton
Leeds United
Leeds United
0-1
M. City
M. City
Brighton and Hove Albion
Brighton and Hove Albion
2-1
Nottingham Forest
Nottingham Forest
Fulham
Fulham
2-1
Tottenham H.
Tottenham H.
M. United
M. United
2-1
Crystal Palace
Crystal Palace
Arsenal
Arsenal
2-1
Chelsea
Chelsea
Ir arriba
Jornada 29
Equipo local
Resultado
Equipo visitante
Bournemouth
Bournemouth
0-0
Brentford
Brentford
Everton
Everton
2-0
Burnley
Burnley
Leeds United
Leeds United
0-1
Sunderland
Sunderland
Wolverhampton Wanderers
Wolverhampton Wanderers
2-1
Liverpool
Liverpool
Aston Villa
Aston Villa
1-4
Chelsea
Chelsea
Brighton and Hove Albion
Brighton and Hove Albion
0-1
Arsenal
Arsenal
Fulham
Fulham
0-1
West Ham Utd.
West Ham Utd.
M. City
M. City
2-2
Nottingham Forest
Nottingham Forest
Newcastle United
Newcastle United
2-1
M. United
M. United
Tottenham H.
Tottenham H.
1-3
Crystal Palace
Crystal Palace
Ir arriba
Jornada 30
Equipo local
Resultado
Equipo visitante
Burnley
Burnley
0-0
Bournemouth
Bournemouth
Sunderland
Sunderland
0-1
Brighton and Hove Albion
Brighton and Hove Albion
Arsenal
Arsenal
2-0
Everton
Everton
Chelsea
Chelsea
0-1
Newcastle United
Newcastle United
West Ham Utd.
West Ham Utd.
1-1
M. City
M. City
Crystal Palace
Crystal Palace
0-0
Leeds United
Leeds United
M. United
M. United
3-1
Aston Villa
Aston Villa
Nottingham Forest
Nottingham Forest
0-0
Fulham
Fulham
Liverpool
Liverpool
1-1
Tottenham H.
Tottenham H.
Brentford
Brentford
2-2
Wolverhampton Wanderers
Wolverhampton Wanderers
Ir arriba
Jornada 31
Equipo local
Resultado
Equipo visitante
Wolverhampton Wanderers
Wolverhampton Wanderers
2-2
Arsenal
Arsenal
Bournemouth
Bournemouth
2-2
M. United
M. United
Brighton and Hove Albion
Brighton and Hove Albion
2-1
Liverpool
Liverpool
Fulham
Fulham
3-1
Burnley
Burnley
Everton
Everton
3-0
Chelsea
Chelsea
Leeds United
Leeds United
0-0
Brentford
Brentford
Newcastle United
Newcastle United
1-2
Sunderland
Sunderland
Aston Villa
Aston Villa
2-0
West Ham Utd.
West Ham Utd.
Tottenham H.
Tottenham H.
0-3
Nottingham Forest
Nottingham Forest
M. City
M. City
13/05
21:00
Crystal Palace
Crystal Palace
Ir arriba
Jornada 32
Equipo local
Resultado
Equipo visitante
West Ham Utd.
West Ham Utd.
4-0
Wolverhampton Wanderers
Wolverhampton Wanderers
Arsenal
Arsenal
1-2
Bournemouth
Bournemouth
Brentford
Brentford
2-2
Everton
Everton
Burnley
Burnley
0-2
Brighton and Hove Albion
Brighton and Hove Albion
Liverpool
Liverpool
2-0
Fulham
Fulham
Crystal Palace
Crystal Palace
2-1
Newcastle United
Newcastle United
Nottingham Forest
Nottingham Forest
1-1
Aston Villa
Aston Villa
Sunderland
Sunderland
1-0
Tottenham H.
Tottenham H.
Chelsea
Chelsea
0-3
M. City
M. City
M. United
M. United
1-2
Leeds United
Leeds United
Ir arriba
Jornada 33
Equipo local
Resultado
Equipo visitante
Brentford
Brentford
0-0
Fulham
Fulham
Leeds United
Leeds United
3-0
Wolverhampton Wanderers
Wolverhampton Wanderers
Newcastle United
Newcastle United
1-2
Bournemouth
Bournemouth
Tottenham H.
Tottenham H.
2-2
Brighton and Hove Albion
Brighton and Hove Albion
Chelsea
Chelsea
0-1
M. United
M. United
Aston Villa
Aston Villa
4-3
Sunderland
Sunderland
Everton
Everton
1-2
Liverpool
Liverpool
Nottingham Forest
Nottingham Forest
4-1
Burnley
Burnley
M. City
M. City
2-1
Arsenal
Arsenal
Crystal Palace
Crystal Palace
0-0
West Ham Utd.
West Ham Utd.
Ir arriba
Jornada 34
Equipo local
Resultado
Equipo visitante
Brighton and Hove Albion
Brighton and Hove Albion
3-0
Chelsea
Chelsea
Bournemouth
Bournemouth
2-2
Leeds United
Leeds United
Burnley
Burnley
0-1
M. City
M. City
Sunderland
Sunderland
0-5
Nottingham Forest
Nottingham Forest
Fulham
Fulham
1-0
Aston Villa
Aston Villa
Liverpool
Liverpool
3-1
Crystal Palace
Crystal Palace
West Ham Utd.
West Ham Utd.
2-1
Everton
Everton
Wolverhampton Wanderers
Wolverhampton Wanderers
0-1
Tottenham H.
Tottenham H.
Arsenal
Arsenal
1-0
Newcastle United
Newcastle United
M. United
M. United
2-1
Brentford
Brentford
Ir arriba
Jornada 35
Equipo local
Resultado
Equipo visitante
Leeds United
Leeds United
01/05
21:00
Burnley
Burnley
Brentford
Brentford
02/05
16:00
West Ham Utd.
West Ham Utd.
Newcastle United
Newcastle United
02/05
16:00
Brighton and Hove Albion
Brighton and Hove Albion
Wolverhampton Wanderers
Wolverhampton Wanderers
02/05
16:00
Sunderland
Sunderland
Arsenal
Arsenal
02/05
18:30
Fulham
Fulham
Bournemouth
Bournemouth
03/05
15:00
Crystal Palace
Crystal Palace
M. United
M. United
03/05
16:30
Liverpool
Liverpool
Aston Villa
Aston Villa
03/05
20:00
Tottenham H.
Tottenham H.
Chelsea
Chelsea
04/05
16:00
Nottingham Forest
Nottingham Forest
Everton
Everton
04/05
21:00
M. City
M. City
Ir arriba
Jornada 36
Equipo local
Resultado
Equipo visitante
Liverpool
Liverpool
09/05
13:30
Chelsea
Chelsea
Brighton and Hove Albion
Brighton and Hove Albion
09/05
16:00
Wolverhampton Wanderers
Wolverhampton Wanderers
Fulham
Fulham
09/05
16:00
Bournemouth
Bournemouth
Sunderland
Sunderland
09/05
16:00
M. United
M. United
M. City
M. City
09/05
18:30
Brentford
Brentford
Burnley
Burnley
10/05
15:00
Aston Villa
Aston Villa
Crystal Palace
Crystal Palace
10/05
15:00
Everton
Everton
Nottingham Forest
Nottingham Forest
10/05
15:00
Newcastle United
Newcastle United
West Ham Utd.
West Ham Utd.
10/05
17:30
Arsenal
Arsenal
Tottenham H.
Tottenham H.
11/05
21:00
Leeds United
Leeds United
Ir arriba
Jornada 37
Equipo local
Resultado
Equipo visitante
Aston Villa
Aston Villa
17/05
13:30
Liverpool
Liverpool
M. United
M. United
17/05
13:30
Nottingham Forest
Nottingham Forest
Brentford
Brentford
17/05
16:00
Crystal Palace
Crystal Palace
Everton
Everton
17/05
16:00
Sunderland
Sunderland
Leeds United
Leeds United
17/05
16:00
Brighton and Hove Albion
Brighton and Hove Albion
Wolverhampton Wanderers
Wolverhampton Wanderers
17/05
16:00
Fulham
Fulham
Newcastle United
Newcastle United
17/05
18:30
West Ham Utd.
West Ham Utd.
Arsenal
Arsenal
18/05
21:00
Burnley
Burnley
Bournemouth
Bournemouth
19/05
20:30
M. City
M. City
Chelsea
Chelsea
19/05
21:15
Tottenham H.
Tottenham H.
Ir arriba
Jornada 38
Equipo local
Resultado
Equipo visitante
Brighton and Hove Albion
Brighton and Hove Albion
24/05
17:00
M. United
M. United
Burnley
Burnley
24/05
17:00
Wolverhampton Wanderers
Wolverhampton Wanderers
Crystal Palace
Crystal Palace
24/05
17:00
Arsenal
Arsenal
Fulham
Fulham
24/05
17:00
Newcastle United
Newcastle United
Liverpool
Liverpool
24/05
17:00
Brentford
Brentford
M. City
M. City
24/05
17:00
Aston Villa
Aston Villa
Nottingham Forest
Nottingham Forest
24/05
17:00
Bournemouth
Bournemouth
Sunderland
Sunderland
24/05
17:00
Chelsea
Chelsea
Tottenham H.
Tottenham H.
24/05
17:00
Everton
Everton
West Ham Utd.
West Ham Utd.
24/05
17:00
Leeds United
Leeds United
Ir arriba
"""

# Split the text into leagues
bundesliga = text.split("ahora serie a")[0].strip()
serie_a = text.split("ahora serie a")[1].split("ahora ligue 1")[0].strip()
ligue_1 = text.split("ahora ligue 1")[1].split("y por ultimo la liga")[0].strip()
la_liga = text.split("y por ultimo la liga")[1].split("ahora premier league")[0].strip()
premier_league = text.split("ahora premier league")[1].strip()

# Function to parse a league's text
def parse_league(league_text, league_name):
    matches = []
    lines = league_text.split('\n')
    current_round = None
    i = 0
    while i < len(lines):
        line = lines[i].strip()
        if line.startswith('Jornada'):
            current_round = int(re.search(r'Jornada (\d+)', line).group(1))
        elif line in ['Equipo local', 'Resultado', 'Equipo visitante', 'Ir arriba'] or line == '':
            pass  # Skip headers and irrelevant lines
        elif '-' in line and len(line.split('-')) == 2:
            # This is a score line, previous line is home, next is away
            if i > 0 and i < len(lines) - 1:
                home = lines[i-1].strip()
                score = line
                away = lines[i+1].strip()
                if home and away and current_round:
                    matches.append({
                        'round': current_round,
                        'home': home,
                        'score': score,
                        'away': away,
                        'league': league_name
                    })
        i += 1
    return matches

# Parse each league
bundesliga_matches = parse_league(bundesliga, 'Bundesliga')
serie_a_matches = parse_league(serie_a, 'Serie A')
ligue_1_matches = parse_league(ligue_1, 'Ligue 1')
la_liga_matches = parse_league(la_liga, 'La Liga')
premier_league_matches = parse_league(premier_league, 'Premier League')

# Combine all matches
all_matches = bundesliga_matches + serie_a_matches + ligue_1_matches + la_liga_matches + premier_league_matches

# Print summary
print(f"Total matches parsed: {len(all_matches)}")
print(f"Bundesliga: {len(bundesliga_matches)}")
print(f"Serie A: {len(serie_a_matches)}")
print(f"Ligue 1: {len(ligue_1_matches)}")
print(f"La Liga: {len(la_liga_matches)}")
print(f"Premier League: {len(premier_league_matches)}")

# Sample output
for match in all_matches[:10]:
    print(match)

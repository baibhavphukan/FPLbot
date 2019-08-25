import re

player_dict = {
    "Fred": "Frederico Rodrigues de Paula Santos",
    "Ki Sung-yueng": "Sung-yueng Ki",
    "Solly March": "Solomon March",
    "Jonny": "Jonathan Castro Otto",
    "Felipe Anderson": "Felipe Anderson Pereira Gomes",
    "Mat Ryan": "Mathew Ryan",
    "Kenedy": "Robert Kenedy Nunes do Nascimento",
    "Jorginho": "Jorge Luiz Frello Filho",
    "Bernard": "Bernard Anício Caldeira Duarte",
    "Romain Saiss": "Romain Saïss",
    "Bernardo Silva": "Bernardo Mota Veiga de Carvalho e Silva",
    "N&#039;Golo Kanté": "N'Golo Kanté",
    "João Moutinho": "João Filipe Iria Santos Moutinho",
    "Franck Zambo": "André-Frank Zambo Anguissa",
    "Fousseni Diabate": "Fousseni Diabaté",
    "Jazz Richards": "Ashley Darel Jazz Richards",
    "Danilo": "Danilo Luiz da Silva",
    "Richarlison": "Richarlison de Andrade",
    "Bernardo": "Bernardo Fernandes da Silva Junior",
    "Fernandinho": "Fernando Luiz Rosa",
    "Joselu": "Jose Luis Mato Sanmartín",
    "Son Heung-Min": "Heung-Min Son",
    "Diogo Dalot": "José Diogo Dalot Teixeira",
    "José Izquierdo": "José Heriberto Izquierdo Mena",
    "Fabri": "Fabricio Agosto Ramírez",
    "Eddie Nketiah": "Edward Nketiah",
    "Rui Patrício": "Rui Pedro dos Santos Patrício",
    "Greg Cunningham": "Greg Cunninghamm",
    "Junior Hoilett": "David Junior Hoilett",
    "Isaac Success": "Isaac Success Ajayi",
    "Xande Silva": "Alexandre Nascimento Costa Silva",
    "Bruno": "Bruno Saltor Grau",
    "Léo Bonatini": "Bonatini Lohner Maia Bonatini",
    "André Gomes": "André Filipe Tavares Gomes",
    "Kiko Femenía": "Francisco Femenía Far",
    "Dele Alli": "Bamidele Alli",
    "Ricardo Pereira": "Ricardo Domingos Barbosa Pereira",
    "Sokratis": "Sokratis Papastathopoulos",
    "Alisson": "Alisson Ramses Becker",
    "Fabinho": "Fabio Henrique Tavares",
    "Adrien Silva": "Adrien Sebastian Perruchet Silva",
    "David de Gea": "David De Gea",
    "Gabriel Jesus": "Gabriel Fernando de Jesus",
    "Pedro": "Pedro Rodríguez Ledesma",
    "Zanka": "Mathias Jorgensen",
    "David Luiz": "David Luiz Moreira Marinho",
    "Rúben Neves": "Rúben Diogo da Silva Neves",
    "Ben Chilwell": "Benjamin Chilwell",
    "Kepa": "Kepa Arrizabalaga",
    "Emerson": "Emerson Palmieri dos Santos",
    "Ederson": "Ederson Santana de Moraes",
    "Chicharito": "Javier Hernández Balcázar",
    "Rúben Vinagre": "Rúben Gonçalo Silva Nascimento Vinagre",
    "Oriol Romeu": "Oriol Romeu Vidal",
    "Lucas Moura": "Lucas Rodrigues Moura da Silva",
    "Willian": "Willian Borges Da Silva",
}

team_dict = {
    "Manchester City": "Man City",
    "Tottenham": "Spurs",
    "Manchester United": "Man Utd",
    "Wolverhampton Wanderers": "Wolves"
}

desired_attributes = [
    "xG",
    "xA",
    "key_passes",
    "npg",
    "npxG",
    "xGChain",
    "xGBuildup",
    "shots",
    "understat_history"
]

versus_pattern = re.compile(r"!fplbot\s+([A-zÀ-ÿ]+(?:[\s-][A-zÀ-ÿ]+)*)\s+(?:vs.|vs)\s+([A-zÀ-ÿ]+(?:[\s-][A-zÀ-ÿ]+)*)\s*(\d+)?")

to_fpl_team_dict = {
    "arsenal fc": "arsenal",
    "the gunners": "arsenal",
    "afc bournemouth": "bournemouth",
    "the cherries": "bournemouth",
    "boscombe": "bournemouth",
    "the seagulls": "brighton",
    "albion": "brighton",
    "brighton and hove albion": "brighton",
    "brighton & hove albion": "brighton",
    "brighton fc": "brighton",
    "bha": "brighton",
    "burnley fc": "burnley",
    "the clarets": "burnley",
    "chelsea fc": "chelsea",
    "cfc": "chelsea",
    "che": "chelsea",
    "the pensioners": "chelsea",
    "crystal palace fc": "crystal palace",
    "cpfc": "crystal palace",
    "cp": "crystal palace",
    "the eagles": "crystal palace",
    "the glaziers": "crystal palace",
    "everton fc": "everton",
    "the toffees": "everton",
    "leicester city": "leicester",
    "leicester city fc": "leicester",
    "the foxes": "leicester",
    "lfc": "liverpool",
    "liverpool fc": "liverpool",
    "mcfc": "man city",
    "manchester city": "man city",
    "manchester city fc": "man city",
    "man city fc": "man city",
    "citizens": "man city",
    "mufc": "man utd",
    "manchester united": "man utd",
    "manchester utd": "man utd",
    "man u": "man utd",
    "man united": "man utd",
    "the red devils": "man utd",
    "red devils": "man utd",
    "newcastle united": "newcastle",
    "newcastle united fc": "newcastle",
    "nufc": "newcastle",
    "newcastle utd": "newcastle",
    "the magpies": "newcastle",
    "southampton fc": "southampton",
    "the saints": "southampton",
    "tottenham": "spurs",
    "thfc": "spurs",
    "tottenham hotspur": "spurs",
    "tottenham hotspurs": "spurs",
    "tottenham fc": "spurs",
    "watford fc": "watford",
    "wfc": "watford",
    "the hornets": "watford",
    "west ham united": "west ham",
    "west ham utd": "west ham",
    "the hammers": "west ham",
    "west ham fc": "west ham",
    "west ham united fc": "west ham",
    "wolverhampton": "wolves",
    "wolverhampton wanderers": "wolves",
    "wolves fc": "wolves",
    "wolverhampton fc": "wolves",
    "wolverhampton wanderers fc": "wolves",
    "the wanderers": "wolves",
    "avfc": "aston villa",
    "villa": "aston villa",
    "the canaries": "norwich",
    "sheffield": "sheffield utd",
    "sheffield united": "sheffield utd",
    "the blades": "sheffield utd"
}

fpl_team_names = [
    "arsenal",
    "aston villa",
    "bournemouth",
    "brighton",
    "burnley",
    "chelsea",
    "crystal palace",
    "everton",
    "leicester",
    "liverpool",
    "man city",
    "man utd",
    "newcastle",
    "norwich",
    "sheffield utd",
    "southampton",
    "spurs",
    "watford",
    "west ham",
    "wolves"
]

twitter_usernames = {
    "BOU": "afcbournemouth",
    "MCI": "ManCity",
    "LIV": "LFC",
    "ARS": "Arsenal",
    "LEI": "LCFC",
    "MUN": "ManUtd",
    "CRY": "CPFC",
    "SHU": "SheffieldUnited",
    "WAT": "WatfordFC",
    "SOU": "SouthamptonFC",
    "WHU": "WestHam",
    "BHA": "OfficialBHAFC",
    "CHE": "ChelseaFC",
    "NOR": "NorwichCityFC",
    "EVE": "Everton",
    "AVL": "AVFCOfficial",
    "TOT": "SpursOfficial",
    "NEW": "NUFC",
    "WOL": "Wolves",
    "BUR": "BurnleyOfficial"
}

lineup_markers = [
    ("line", "up"),
    ("team", "news")
]

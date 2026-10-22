"""The demo holdings, in portfolio order."""
SUPPORTED = ('CNQ.TO', 'CSCO', 'JPM', 'BMO.TO', 'COST', 'V', 'JWEL.TO', 'VRTX', 'ENB', 'PFE', 'CP.TO', 'ATD.TO', 'SCHW', 'ACN', 'J', 'XYL', 'PEP', 'NTR.TO', 'DIS', 'MG.TO', 'OTEX.TO', 'GIS', 'NVO', 'MC.PA', 'AMTM')
COMPANIES = {'CNQ.TO': 'Canadian Natural Resources', 'CSCO': 'Cisco', 'JPM': 'JPMorgan Chase', 'BMO.TO': 'Bank of Montreal', 'COST': 'Costco', 'V': 'Visa', 'JWEL.TO': 'Jamieson Wellness', 'VRTX': 'Vertex Pharmaceuticals', 'ENB': 'Enbridge', 'PFE': 'Pfizer', 'CP.TO': 'Canadian Pacific Kansas City', 'ATD.TO': 'Alimentation Couche-Tard', 'SCHW': 'Charles Schwab', 'ACN': 'Accenture', 'J': 'Jacobs Solutions', 'XYL': 'Xylem', 'PEP': 'PepsiCo', 'NTR.TO': 'Nutrien', 'DIS': 'Walt Disney', 'MG.TO': 'Magna International', 'OTEX.TO': 'OpenText', 'GIS': 'General Mills', 'NVO': 'Novo Nordisk', 'MC.PA': 'LVMH', 'AMTM': 'Amentum'}

# Additional symbols explicitly requested by research pilot participants.
PILOT_COMPANIES = {'SPGI': 'S&P Global',
 'MCO': 'Moody’s Corporation',
 'TD.TO': 'Toronto-Dominion Bank',
 'GOOGL': 'Alphabet',
 'AMZN': 'Amazon',
 'META': 'Meta Platforms',
 'AMD': 'Advanced Micro Devices',
 'NVDA': 'NVIDIA',
 'MCK': 'McKesson',
 'ISRG': 'Intuitive Surgical',
 'EW': 'Edwards Lifesciences',
 'T': 'AT&T',
 'CAT': 'Caterpillar',
 'MSFT': 'Microsoft',
 'NFLX': 'Netflix',
 'SHOP.TO': 'Shopify',
 'AAPL': 'Apple',
 'TSM': 'Taiwan Semiconductor Manufacturing',
 'MU': 'Micron Technology',
 'CSU.TO': 'Constellation Software',
 'NVAX': 'Novavax',
 'BRK-B': 'Berkshire Hathaway',
 'TMC': 'TMC the metals company',
 'ASML': 'ASML Holding',
 'SYY': 'Sysco'}
SUPPORTED += tuple(PILOT_COMPANIES)
COMPANIES.update(PILOT_COMPANIES)

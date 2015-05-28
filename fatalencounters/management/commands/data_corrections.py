# dict by name, with dicts of fields to correct
# use this instead of csv patch, which isn't robust to column changes
# mostly fixes typos in original file, which haven't been merged upstream

corrections = {
    # state typos
    'Kendall Alexander': {'state': 'LA'},
    'William McKnight': {'state': 'IN'},
    'Stephen P. Bethea': {'state': 'IL'},
    'Lorenzo J. Ciaramella': {'state': 'CA'},
    'James D. Jones': {'state': 'IN'},
    'Bobby Shane Patrick': {'state': 'AR'},
    'Justin Lenard Elmore': {'state': 'GA'},

    #common misspellings
    #Columbia (with a U), DC
    'Jean E. Louis': {'city': 'Washington', 'county': 'District of Columbia'},
    'Michael Ezekel Epps': {'city': 'Washington', 'county': 'District of Columbia'},
    'Robert Brown': {'city': 'Washington', 'county': 'District of Columbia'},
    'Akeem Jamaal Cayo': {'city': 'Washington', 'county': 'District of Columbia'},
    'Osman Abdullahi': {'city': 'Washington', 'county': 'District of Columbia'},
    'Isaac Little': {'city': 'Washington', 'county': 'District of Columbia'},
    'David Kerstetter': {'city': 'Washington', 'county': 'District of Columbia'},
    'Kevin Bolden': {'city': 'Washington', 'county': 'District of Columbia'},

    #Miami-Dade, FL
    'Eddie Lee Macklin': {'county': 'Miami-Dade'},
    'Stephanie Tunc': {'county': 'Miami-Dade'},
    'Corsini Valdes': {'county': 'Miami-Dade'},
    'Rigoberto Alpizar': {'county': 'Miami-Dade'},
    'Travis McNeil': {'county': 'Miami-Dade'},
    'Robert Perez': {'county': 'Miami-Dade'},

    # San Bernardino, CA
    'James Moala Kofu': {'county': 'San Bernardino'},
    'Jonathan Montano': {'county': 'San Bernardino'},
    'Bartholomew Paul Williams': {'county': 'San Bernardino'},

    #Prince George's, MD
    'Robert Antonio Jones': {'county': "Prince George's"},
    'Mark Anthony Blocker': {'county': "Prince George's"},
    'Frederick R. Miller': {'county': "Prince George's"},
    'Elijah Glay': {'county': "Prince George's"},
    'Michael Ricardo Minor': {'county': "Prince George's"},

    #St. Louis, MO
    'Annette Green': {'county': 'St. Louis'},
    'Earl Murray': {'county': 'St. Louis'},
    'Joey Carl': {'county': 'St. Louis'},

    #Alaska municipalities
    'Carl Bowie III': {'county': 'Anchorage'},
    'Gordon E. Samel': {'county': 'Matanuska-Susitna'},

    #miscellaneous typos
    'Mark East': {'county': 'Hinds'},
    'Arnesto Ramos': {'county': 'Lubbock'},
    'Wilson A. Lutz': {'county': 'Winnebago'},
    'Jeremy Acre': {'county': 'Elmore'},
    'Jonathan Dipaola': {'city': 'Meridian'},
    'Kevin Charles Duey': {'county': 'Calaveras'},
    'Kevin Wayne Newland': {'county': 'Clallam'},
    'Sonny Archuleta': {'county': 'Arapahoe'},
    'Kelly Thomas': {'county': 'Orange'},
    'Travis Trisoliere': {'county': 'Maricopa'},
    'Tyler Heilman': {'county': 'Le Sueur'},
    'Mohamed Bah': {'county': 'New York'},
    'Christopher George': {'county': 'Boulder'},
    'Rodney Stevens': {'county': 'St. Johns'},
    'Keith T. Shumway': {'county': 'Tompkins'},
    'Henry Jackson': {'county': 'Carter'},
    'James Genda': {'county': 'Summit'},
    'Michael Madonna': {'state': 'ID', 'county': 'Kootenai'},
    'Seneca Darden': {'county': 'Norfolk'},
    'Levester Carter Jr.': {'county': 'Richmond'},
    'Allan Duarte': {'county': 'Nassau'},
    'Juan Carlos Garcia': {'county': 'Nassau'},
    'Daniel Mendoza': {'county': 'Fresno'},
    'Lawrence H. Faine': {'county': 'Norfolk'},
    'Lonnie Taylor': {'county': 'Solano'},
    'Adrian Suarez': {'county': 'Klickitat'},
    'Dominic Graffeo': {'county': 'Suffolk'},
    'Ennis Labaux': {'county': 'St. John the Baptist Parish'},
    'Aaron Torres': {'county': 'Honolulu'},
    'Calvin Peters': {'county': 'Kings'},
    'Javonta Darden': {'county': 'Clarke'},
    'Ismael Maria-Acevedo': {'county': 'Franklin', 'state': 'WA'},
    'Philip E. Rank': {'county': 'Franklin', 'state': 'PA'},
    'Robert Brooks': {'city': 'Sewickley', 'county': 'Allegheny', 'state': 'PA'},
    'Christopher A. Fredette': {'county': 'Bexar'},
    'Tom Rook': {'county': 'DeSoto'},
    'Jeffrey Holden Jr.': {'county': 'Sedgwick'},

    #Lakeland FL overwritten in several rows
    'Michael Neal Peters': {'city': 'Broad Creek', 'state': 'NC', 'county': 'Carteret'},
    'Donald T. Moskites': {'city': 'Brighton', 'state': 'MA', 'county': 'Suffolk'},
    'Bernard Peters Jr.': {'city': 'Oakland', 'state': 'CA', 'county': 'Alameda'},
    'Angela Darlene Smith': {'city': 'Crossville', 'state': 'TN', 'county': 'Cumberland'}
}

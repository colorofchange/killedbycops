# -*- coding: latin-1 -*-

AGENCY_ACRONYMS = {
  # geographic
  'New York Police Department':'NYPD',
  'Los Angeles Police Department': 'LAPD',
  # turn into nouns
  "Sheriff's Department":'Sheriffs',
  'Sheriff Office':'Sheriffs',
  "Sheriff's Office":'Sheriffs',
  "Sherrif's Department": 'Sheriffs',
  "police officers": "officers",
  # department specific
  'Police Department':'PD',
  'Police Deptartment': 'PD', #typo
  'State Police': 'SP',
  "Drug Enforcement Administration": 'DEA Agents',
  "Special Response Team": 'SWAT', #effectively equivalent
  "uniformed Secret Service": "Secret Service", #too long, shorten
  "U.S. Bureau of Alcohol, Tobacco, Firearms & Explosives": "ATF Agents", #too long, shorten

  "primary": '',
  "assisting": '',
  " and ": ' & ', #ampersands are cool
  }

# gross hack
# but we need some way to link the sequential images with fatal encounters
# and the designer is unable to change the output filename format
IMAGE_ID_LOOKUP = {
  "Raymond Herisse":1,
  "Stanley LaVon Gibson":2,
  "Dason Peters":3,
  "Dylan Samuel-Peters":4,
  "Rosette Samuel":5,
  "Jeremy Powell":6,
  "Kermith Sonnier Jr.":7,
  "Aaron Hunter":8,
  "Ahmede Jabbar Bradley":9,
  "Amos G. Smith":10,
  "Andrena Kitt":11,
  "Anthony Rawls":12,
  "Bobby Moore III":13,
  "Brandon Jones":14,
  "Cameron Massey":15,
  "Carleton J. Wallace":16,
  "Carlos Williams":17,
  "Carulus Hines":18,
  "Cheryl Blount-Burton":19,
  "Dakota Bright":20,
  "David Lee Turner":21,
  "David O. Okot":22,
  "Dawntree Ta'Shawn Williams":23,
  "DeJuan Colbert":24,
  "Demarcus Derell Celestine":25,
  "Deonte Traylor":26,
  "DeOntrel Davis":27,
  "Georgy Louisgene":28,
  "Herman Pickens":29,
  "Ishmael Muhammad":30,
  "Jack Lamar Robertson":31,
  "Jacqueline Culp":32,
  "Jalen Ricks":33,
  "James Brissette":34,
  "James Brown":35,
  "Joetavius Stafford":36,
  "Jonathan A. Ferrell":37,
  "Kedrian Edwards":38,
  "Kendall Walker":39,
  "Kenneth Chamberlain Sr.":40,
  "Kenneth Dewayne Cooper":41,
  "Kenneth Harding":42,
  "Kenneth King":43,
  "Kenneth Suggs":44,
  "Kenneth Walker":45,
  "Kevin Bolden":46,
  "Kevin M. Bailey":47,
  "Kevin Willingham":48,
  "Kimani Gray":49,
  "Korey Marcel Germaine":50,
  "Latricka Sloan":51,
  "Louis DecQuir":52,
  "Mister Bobby Lowe":53,
  "Monroe Isadore":54,
  "Montellis Clark":55,
  "Ray Charles Hayes":56,
  "Raymond A. Smith":57,
  "Ron Pettaway":58,
  "Ronald Madison":59,
  'Sammie "Junebug" Davis Jr.':60,
  "Samuel Thomas Cunningham III":61,
  "Shawn J. Maxwell":62,
  "Shelley Amos":63,
  "Stacy Rondell Bostic":64,
  "Stephen Seignious":65,
  "Taft Sellers":66,
  "Tendai Nhekairo":67,
  "Terrance Lamar Abrams":68,
  "Terry Laffitte":69,
  "Timothy Stansbury Jr.":70,
  "Tony Louis Francis":71,
  "Trevion Davis":72,
  "Waseem Jung":73,
  "Willie Davis Jr.":74,
  "Tyler Damon Woods":75,
  "Aaron Jones":76,
  "Aaron Marcell Campbell":77,
  "Alan Blueford":78,
  "Amir Rashid Crump":79,
  "Angel Jesus Hinojoza":80,
  "Anita Gay":81,
  "Anthony Antwan Davis":82,
  "Anthony Minner":83,
  "Barrington Hall":84,
  "Bernard Pate":85,
  "Billy Ray Finks":86,
  "Booker Carloss II":87,
  "Byron Hammick":88,
  "Casper Banjo":89,
  "Charles M. Rorie III":90,
  "Charles Whaley":91,
  "Christopher Hawkins":92,
  "Damien W. Morton":93,
  "Damon Edward Beal":94,
  "Daniel Taiwan Hathorne":95,
  "Darris Eugene Johnson":96,
  "Davon Jackson":97,
  "Denise Nicole Glasco":98,
  "Deon Johnson":99,
  "Derrick Jones":100,
  "Ernest Williams Jr.":101,
  "Frakelin Marice Hardy":102,
  "Gary King Jr.":103,
  "Glen Willis":104,
  "Glennel Givens Jr.":105,
  "Hezekiah Lewis":106,
  "James Jahar Perez":107,
  "Jamil Wheatfall":108,
  "Jeffrey Williams":109,
  "John Sloan":110,
  "Johnnie Weatherspoon":111,
  "Johnny Lee Wicks":112,
  "Justin Brimmer":113,
  "Keaton Dupree Otis":114,
  "Keith Maurice Williams":115,
  "Kendra James":116,
  "Kyone Johnson":117,
  "Lovelle Mixon":118,
  "Orlando Barlow":119,
  "Raheim Brown":120,
  "Richard Bernard Nolton":121,
  "Ronald Brazier":122,
  "Ronald Neal Joseph Jr.":123,
  "Roshawn Hill":124,
  "Sammie Lee Clay":125,
  "Sharmel Edwards":126,
  "Swauve Devon Lopez":127,
  "Tarance Deshon Hall":128,
  "Terrance Mearis":129,
  "Tommy Lee Gest":130,
  "Trevon Cole":131,
  "Tyrise M. Bell":132,
  "Vernon Allen":133,
  "Willie Thomas Grigsby":134,
  "Willie Wilkens":135,
  "Oscar Grant III":136,
  "Kenneth Jewell Stafford":137,
  "Rodney L. Wright":138,
  "D'Andre Berghardt Jr.":139,
  "Bernard Lofton":140,
  "Shawn Dean":141,
  "Daryl Hicks":142,
  "Alfred Redwine":143,
  "Vincent Wood":144,
  "James Lewis":145,
  "William Billy Lomax":146,
  "Thomas G. Manuel III":147,
  "Alexander Wilson":148,
  "Dennis Clark III":149,
  "Archie Lee Chambers Jr.":150,
  "Larry Hooker":151,
  "Amjustine Hunter":152,
  "Kenzell Hobbs":153,
  "Cary Ball":154,
  "James Coleman":155,
  "Cody Point":156,
  "Byron Carter Jr.":157,
  "Tavontae Jamar Haney":158,
  "Ryan Koontz":159,
  "Kenneth Knight":160,
  "Stephen O'Neal Wattley II":161,
  "Malik Williams":162,
  "John Adams":163,
  "Gabriel Winzer":164,
  "Thomas Dewitt Johnson":165,
  "Eddie Callaway":166,
  "Demetrius Bennett":167,
  "Carnell Moore":168,
  "Jordan West-Morson":169,
  "Marquis James Spencer":170,
  "Tywon Jones":171,
  "Emmanuel Gatewood":172,
  "Kourtney Hahn":173,
  "Kendra Diggs":174,
  "Shaaliver Douse":175,
  "Maurice Leroy Cox":176,
  "Lawrence Smith":177,
  "Mohamed Bah":178,
  "Darrien Hunt":179,
  "Jared Brown-Garnham":180,
  "Alonzo Ashley":181,
  "DeAunta Terrell Farrow":182,
  "Jeremey Lake":183,
  "Edward Ned Jr.":184,
  "Malissa Williams":185,
  "Timothy Russell":186,
  "Kendrick Brown":187,
  "Ricky Junior Toney":188,
  "William Jackson":189,
  "Anthony Dwain Lee":190,
  "Tyrone F. Thomas":191,
  "Peter Jourdan":192,
  "Tysheen Bourne":193,
  "Andre Fields":194,
  "Annette Green":195,
  "Ronald Beasley":196,
  "Earl Murray":197,
  "Dainell Simmons":198,
  "Charles A. Baker Jr.":199,
  "Orlando Santos":200,
  "Kenneth R. Herring":201,
  "Cimarron Lamar Lamb":202,
  "Jacqueline Reynolds":203,
  "Marlon Brown":204,
  "Cameron Tillman":205,
  "Keith T. Shumway":206,
  "Blondel Lassegue":207,
  "Paul Johnson":208,
  "Patricia Thompson":209,
  "Ernest Prather":210,
  "Darryl Bain":211,
  "Tamon Robinson":212,
  "Christian Eaddy":213,
  "Jermaine Darden":214,
  "Hayden Blackman":215,
  "Robert Desir":216,
  "Jose Quinonez":217,
  "Don White":218,
  "Abdul Kamal":219,
  "Shawn M. Rieves":220,
  "Willie James Williams":221,
  "Jason D. White":222,
  "Jonathan Wilcher":223,
  "Sharon Rebecca McDowell":224,
  "James Torres":225,
  "Somourian Jamal Wingo":226,
  "Kendall Alexander":227,
  "Julias Michael Reese":228,
  "Christopher Ridley":229,
  "Jeffrey Ragland":230,
  "Jelani Manigault":231,
  "Jerome Alford":232,
  "Terrence Thomas":233,
  "Timur Person":234,
  "Walter Washington":235,
  "Zikarious Flint":236,
  "Dashawn Vasconcellos":237,
  "Paul Smith":238,
  "Gregory Vaughn Hill Jr":239,
  "Henry Jackson":240,
  "Dominique Smith":241,
  "Ramesh Dwayne Sweeney":242,
  "Vernard Davis":243,
  "Lawrence Rogers":244,
  "Eldrin Smart":245,
  "Pierree Davis":246,
  "Charles Hull":247,
  "Christopher Stirkens":248,
  "Rafael Briscoe":249,
  "Jamil Moore":250,
  "Christopher Brown":251,
  "Anesson Joseph":252,
  "James L. Norris":253,
  "Shantel Davis":254,
  "Reno Sayles":255,
  "Anton Barrett":256,
  "Marshall Tobin":257,
  "Mario Romero":258,
  "Kendrec McDade":259,
  "Terrance Terrell Franklin":260,
  'Gerald "Skip" Tyrone Murphy':261,
  "Louis M. Squires":262,
  "Frankie Pitt":263,
  "Ramarley Graham":264,
  "Lejoy Grissom":265,
  "Terrence Dawson":266,
  "Henry Glover":267,
  'Joshua "Omar" Johnson':268,
  "Anthony Michael Bland":269,
  'Belton "Amir" Lomax':270,
  "Clinton Roebexar Allen":271,
  "Julian Dawkins":272,
  "Thomas Bean":273,
  "Charles Curl":274,
  "Leonard Thomas":275,
  "Ajani Mitchell":276,
  "William Dupree":277,
  "Jaleel Jackson":278,
  "Nathaniel McRae":279,
  "Gary Hatcher":280,
  "Aiyana Mo'Nay Stanley Jones":281,
  "Jermie McCraven":282,
  "Christian Freeman":283,
  "Hernandez Dowdy":284,
  "Lorenzo Davis":285,
  "Delois Epps":286,
  "Makayla Ross":287,
  "Justin Thompson":288,
  "Charles Livingston III":289,
  "Steven Askew":290,
  "Horace Whiting":291,
  "John Walker":292,
  "Marvin Amerson":293,
  "Aaron Dumas":294,
  "Dwight Moorer Jr.":295,
  "Keoshia L. Hill":296,
  "Bill Jackson":297,
  "Edward Mwaura":298,
  "Sherlon Smikle":299,
  "Lana Morris":300,
  "Rustin Wilkerson":301,
  "Virgil Millon":302,
  "Dontae Daveon Lewis Hayes":303,
  "Lee Deante Brown":304,
  'Terry "Big Champ" Rabb':305,
  "Summer Marie Lane":306,
  "Volne Lamont Stokes":307,
  "Joseph Paige":308,
  "Darrius J. Lowery-Baptiste":309,
  "Wayne Arnold Jones":310,
  "Joe White III":311,
  "Antwon Johnson":312,
  "Recardio Shormon Clark":313,
  "Sammie Lamont Wallace":314,
  "Michael Westly":315,
  "Cedric Howard":316,
  "Eliakim Shabazz":317,
  "Jaquaz Walker":318,
  "Lawrence Allen":319,
  "Adolphus Pinkney":320,
  "Darrell Banks":321,
  "Donnell Carter":322,
  "Jourdan Akili Wagner":323,
  "Cacedrick White":324,
  "Elip Cheatham":325,
  "Michael Lembhard":326,
  "Terry Davis":327,
  "Marvin E. Parker":328,
  "Deangelo Lopez":329,
  "James Eric Griffin":330,
  "Willie Sudduth":331,
  "Kenneth Smith":332,
  "Aron Jones":333,
  "Leon James":334,
  "Angelo Ferguson":335,
  "David Crenshaw":336,
  "Laray Renshaw":337,
  "Brandon McCloud":338,
  "Eren Beyah":339,
  "Ricardo Mason":340,
  "Jeffrey Hopkins":341,
  "Stephon Keith Moore":342,
  "Craig Bickerstaff":343,
  "Jermaine Sanders":344,
  "Daniel Harris":345,
  "Icarus Randolph":346,
  "Eric Garner":347,
  "Miriam Iris Carey":348,
  "Larry Eugene Jackson Jr.":349,
  "Michael Brown":350,
  "Dontre Hamilton":351,
  "Bryan Stukes":352,
  "Steven Tyrone Mallory":353,
  "Ezell Ford":354,
  "Micah Anthony Key":355,
  "Seneca Darden":356,
  "David Latham":357,
  "Levester Carter Jr.":358,
  "Tevin Robinson":359,
  "Ronald Roland":360,
  "Darius Colegarrit":361,
  "Michael Myers":362,
  "Warren Robinson":363,
  "Rekia Boyd":364,
  "Flint Farmer":365,
  "Burrell Ramsey-White":366,
  "Travis Floyd":367,
  "Dartanya Bentley, Jr.":368,
  "Timothy Thomas":369,
  "Remis M. Andrews":370,
  "John H. Crawford III":371,
  "Derek Deandre Walker":372,
  "Hydra Lacy Jr.":373,
  "Michelle Cusseaux":374,
  "Milton Hall":375,
  "Stephon Watts":376,
  "Davon Mullins":377,
  "Danroy Henry Jr.":378,
  "Greg Thompson Jr.":379,
  "Idriss Shelley":380,
  "Howard Tucker":381,
  "Nahcream Moore":382,
  "Jerry Brown":383,
  "Londrell E. Johnson":384,
  "Timothy Wall":385,
  "David Ellis":386,
  "Jason Harrison":387,
  "Brian Simms Jr.":388,
  "Quentin Eric Hicks":389,
  "Yvette Smith":390,
  "Kayla Moore":391,
  "Oliver 'Big 'O'' Lefiti":392,
  "Kathryn Johnston":393,
  "Gregory Hooper":394,
  "Antonio Latuanee Pryce":395,
  "Marquez Eugene Smart":396,
  "Albert Duane Denton":397,
  "Victor White III":398,
  "Lajuanzo Brooks":399,
  "Donte Lamonte Jordan":400,
  "Darius Jamal Murphy":401,
  "Michael Anglin Jr.":402,
  "Jose Valerio":403,
  "Rexford Dasrath":404,
  "Mark Anthony Barmore":405,
  "Michael Moore":406,
  "Ismael Sadiq":407,
  "Eurie Stamps":408,
  "Eddie Davis":409,
  "Kajieme Powell":410,
  "Shawn Greenwood":411,
  "Mark Salazar":412,
  "Alfred Sanders":413,
  'Clifton "Pete" Lee Jr.':414,
  "Jacorey Calhoun":415,
  "Nathaniel McRae":416,
  "Maurice Clemmons":417,
  "John Frank Brown":418,
  "Bert W. Bowen":419,
  "Justin Sipp":420,
  "Hailu Brook":421,
  "Wendell Allen":422,
  "Michael McCullen":423,
  "Tarika Wilson":424,
  "Clifford Paul Maxwell":425,
  "John Bior Deng":426,
  "Reginald Bernard Smith":427,
  "Omar Abrego":428,
  "Tommy Yancy":429,
  "La-Reko Williams":430,
  "Roshad McIntosh":431,
  "Desean Pittman":432,
  "Rondre Hornbeak":433,
  "Dante Parker":434,
  "Jacorey Calhoun":435,
  "Steven Lashone Douglas":436,
  "Marcella Byrd":437,
  "Sean Bell":438,
  "Chavis Carter":439,
  "Victor Demarius Steen":440,
  "Lawrence H. Faine":441,
  "Manuel Loggins Jr.":442,
  "Melvin Lawhorn":443,
  "Jordan Baker":444,
  "Timothy Russell":445,
  "Steve Eugene Washington":446,
  "Ousmane Zongo":447,
  "Shurron Grant":448,
  "Gregory Lewis":449,
  "Michael Sanders":450,
  "James Edward Taylor":451,
  "Rodney Abernathy":452,
  "Albert Rucker":453,
  "Robert Ventry":454,
  "Cortez Washington":455,
  "Montez Dewayne Hambric":456,
  "Pierre M. Jackson":457,
  "Tyrone Brown":458,
  "James Rivera":459,
  'Deandre "Trey" Brunston':460,
  "Antoinette Griffin":461,
  "Erica Stevenson":462,
  "Dominique Hurtt":463,
  "Antonio Miller":464,
  "Quentin Maurice Reed":465,
  "David Wayne Summers":466,
  "John Lindsey Myers":467,
  "Julian Alexander":468,
  "Woodrow Player III":469,
  "Alberta Spruill":470,
  "Ernest Vassell":471,
  "Kiwane Carrington":472,
  "Marquise Jones":473,
  "Michael Blair":474,
  "Justin Fields":475,
  "Larry Jerome Jenkins":476,
  "Eugene N. Turner III":477,
  "Mark Fernandes McMullen":478,
  "Maliki Yawmi-Deen Raymond":479,
  "Guy Jermone Jarreau Jr.":480,
  "Russell Lydell Smith":481,
  "James Lamont":482,
  "Desjon Jamal Edwards":483,
  "Donovan Tyrone Graham":484,
  "Frederick Devon McAllister":485,
  'Gary "Chris" Tyson':486,
  "Jamar Marrow":487,
  "Jashon Bryant":488,
  "Jonathan Mosely":489,
  "Mack N. Lucky":490,
  "Marcus G. Brown":491,
  "Raylyn George":492,
  "Robert Davis":493,
  "Tyshan Napoleon":494,
  "Othniel Askew":495,
  "Eric Stuart Allen Jones":496,
  "Allen Newsome":497,
  "Lavon King":498,
  "Aaron Harrison":499,
  "Ryan L. Stokes":500,
  "Gregory Lewis Towns Jr":501,
  "Malcolm Ferguson":502,
  "Marlon Horton":503,
  "Corey Ward":504,
  "Glen Boldware":505,
  "Ronald Boone":506,
  "Manuel DaVeiga":507,
  "Tahiem Goffe":508,
  "Joseph Ramos":509,
  "Kerby Revelus":510,
  "Denis Reynoso":511,
  "Stanley Seney":512,
  "Clyde D. Ratcliff":513,
  "Brandon Payne":514,
  "Delano M. Walker":515,
  "Douglas Cooper":516,
  "Cornel Young Jr.":517,
  "Howard Wallace Bowe Jr.":518,
  "Shem Walker":519,
  "Errol Shaw Sr.":520,
  "James C. Tomlin":521,
  "Clifton Armstrong":522,
  "Antonio Bryant":523,
  "Lennard Whittle":524,
  "Herve Gilles":525,
  "Lonnie Taylor":526,
  "George Harvey":527,
  "Jonathan D. Rogers":528,
  "Shereese Francis":529,
  "Perlie Golden":530,
  "Nathaniel Cobbs":531,
  "Darin John Richardson":532,
  "Khazyier Pugh":533,
  "Duane Brown":534,

  #batch 2
  "Jack Sun Keewatinawin":1,
  "Andy Lopez":2,
  "Adolfo Vargas Tovar":3,
  "Angel Miguel Lopez":4,
  'Bernie Cervantes "Chino" Villegas':5,
  "Carlos Carrillo":6,
  "Christopher Jonathan Gonzales":7,
  "David Miguel Ventura":8,
  "Denis John Chabot":9,
  "Denny Gonzales":10,
  "Eliseo Mercado":11,
  "Eric Marquez":12,
  "Esau Marin":13,
  "Husien Shehada":14,
  "Joel Acevedo":15,

  #batch 3
  "Johnny Castillo-Romero":1,
  "Jonathan F. Vasquez":2,
  "Jose Antonio Hernandez-Gonzalez":3,
  "Jose De la Trinidad":4,
  "Jose Guerena":5,
  "Jose Toloza":6,
  "Julio Cesar Contreras":7,
  "Kevin Arellano":8,
  "Ki Yang":9,
  "Manuel Diaz":10,
  "Martin Angel Hernandez":11,
  "Michael Nida II":12,
  "Mylo Harvey":13,
  "Nelson Martinez-Mendez":14,
  # "Pedro Alberto Vargas":'dns',
  "Ramon Ayala":15,
  "Romero Roberto Moya":16,
  "Rufino Lara":17,
  "Russell Rios":18,
  "Saan Pao Saeteurn":19,
  "Sergio Munoz":20,
  "Susie Young Kim":21,
  "Urbano Moreno Morales":22,
  "Valeria Munique Alvarado":23,
  "Victor Vinh Charles Le":24,
  "Vincent Jimenez":25,
  "Addiel Meza":26,
  "Alberto Castillo":27,
  # "Andres Avita":'dns',
  "Andrew Gonzalez":28,
  "Andrew Moppin-Buckskin":29,
  "Andy Puente Soto":30,
  "Antonio Corona-Mendoza":31,
  "Aquileo Jimenez-Duran":32,
  "Arcangelito Contreras":33,
  "Bernardo Ancheta Caberto":34,
  "Brownie Polk":35,
  # "Bryan Benjamin Hanasz":'dns',
  "Cipriano Gerardo Lopez":36,
  "Daechull Chung":37,
  "Daniel Nunez":38,
  "David Michael Herrera":39,
  "David Paul Gonzalez":40,
  "Dominic Ian Nieto":41,
  "Eddie Homsombath":42,
  "Edmundo Del Valle Jr.":43,
  "Efrain Cuenca Dimas":44,
  "Fernando Saucedo":45,
  # "Francisco Benitez":'dns',
  "Fred Collins":46,
  "Gary Frank Orozco":47,
  "Ivan Alonzo":48,
  "Ivan Guajardo Ariza":49,
  "Jaime Padilla":50,
  "Jason Baires":51,
  "Javier Escamilla":52,
  "Jeremiah Dye":53,
  "Jon Kenji Fukumoto":54,
  "Jose Luis Buenrostro":55,
  "José Santos Victor Mejía Poot":56,
  "Kenneth Ross":57,
  "Kim Saelio":58,
  "Kyle Melendez":59,
  "Leopoldo Tijerina Jr.":60,
  "Lesley Xavier Allen":61,
  "Luis Carlos Silva":62,
  'Mack"Jody" Woodfox':63,
  "Martin Flenaugh":64,
  "Matthew Cicelski":65,
  "Maurice Evans Shavers Jr.":66,
  "Mauricio Hernandez":67,
  "Michael Dean Chevalier":68,
  "Obataiye Edwards":69,
  "Parnell Smith":70,
  "Phillip Conatser":71,
  "Phillip Michael Ramos":72,
  "Placido Torres-Chavez":73,
  "Rafael Olivas":74,
  "Robert Galindo":75,
  "Roberto Antonio Torres":76,
  "Rolando Lappin-Mendez":77,
  "Santana Baca Jr.":78,
  "Santiago A. Cisneros III":79,
  "Saul Morales Garcia":80,
  "Southaly Ketmany":81,
  "Villa Valvatin":82,
  "Jairo Dario Rodriguez":83,
  # "Elizabeth DeMaria":'dns',
  "Nigel Flores":84,
  "Eduardo Lopez-Hernandez":85,
  "Jose Manuel Lopez-Sanchez":86,
  "Jose Roberto Mejia Lang":87,
  "Reymunda Lopez-Vazquez":88,
  "Victor De La Cruz-De Leon":89,
  "Kelly Ryu Stenstrum":90,
  "Julio Angel DeJesus":91,
  "Luis Antonio Elena Rodriguez":92,
  "Israel Hernandez":93,
  "Roberto Arce":94,
  "Leo Lopez":95,
  "Alan Gomez":96,
  "Andrew Lopez":97,
  "Antonio Munoz":98,
  "Daniel Morantes III":99,
  "Felipe Fragoso Herrera":100,
  "Margarito Martinez Gallegos":101,
  "Jonathan Pimentel":102,
  "Xavier Barba":103,
  "Robert Lopez":104,
  "Felipe Corrales":105,
  "Ronald Ontiveros":106,
  "Victor David Ortega":107,
  "Edward Ramirez":108,
  "Yanira Serrano-Garcia":109,
  "Carlos Domingo Oquendo":110,
  "Byron San Jose":111,
  "Carlos Edwin Arevalo":112,
  "Sergio Rojas":113,
  "Marco Ernesto Avila":114,
  "Mohammad Usman Chaudhry":115,
  "Sergio Sedillo":116,
  "Juan Luis Rodriguez":117,
  "Felipe Ramirez Castellanos":118,
  "Alberto Sepulveda":119,
  "Jaspal Singh":120,
  "Ryo Oyamada":121,
  "Jesus Antonio Castillo":122,
  "Michael Rosales":123,
  "Eagle Michael":124,
  "Benites Saimon Sichiro":125,
  "Carlos Saenz":126,
  "Rosa Elvira Flores-Lopez":127,
  "Salvador Munoz":128,
  # "Jerry Vue":'dns',
  "Paul Aguilar":129,
  # "Unknown":'dns',
  "Wesley Maldonado":130,
  "Rocendo Arias":131,
  # "Daniel Tiger":'dns',
  "Emil Mann":132,
  "Eric Hernandez":133,
  "Iman Morales":134,
  "Jose Luis Navarro":135,
  "Rigoberto Alpizar":136,
  "Rocendo Arias":137,
  "Frankie Martinez":138,
  "Juan Mendez":139,
  # "Cuong Tran":'dns',
  "Manuel Oscar Longoria":140,
  "Raul Pinet Jr.":141,
  # "Ricardo Carlon":'dns',
  "Felix Navarette":142,
  "Luis Morin":143,
  "Ana Lucia Rodriguez":144,
  "Rafael Laureano":145,
  "Francisco Carvajal":146,
  "Carlos Lopez":147,
  "Gerardo Delgado":148,
  "Danny Valdes":149,
  "Jose Garcia":150,
  "Julie Serna Gonzales":151,
  "Shane Tasi":152,
  "Samuel Cruz":153,
  # "Esteban J. Smith":'dns',
  "Elias Mejia":154,
  "Khan Tony Nim":155,
  "Mhai Scott":156,
  "Gerardo Diego Ayala":157,
  "Ross Batista":158,
  "Ricardo Diaz-Zeferino":159,
  "Isabel Pablo":160,
  "Hector Jimenez":161,
  "Fernando Luis Sanchez":162,
  "Vanpaseuth Phaisouphanh":163,
  "Victor Fuentes":164,
  "Mohammed Naas":165,
  "Jaime Ceballos":166,
  "Jimmy James Garza Jr.":167,
  # "Jose Elias Mata":'dns',
  "Jaime Gonzalez Jr.":168,
  'Vanna "Tiny" Sok':169,
  "Uriel Juarez":170,
  # "Jorge Abraham Zarazua-Rubio":'dns',
  "Randall Vernon Ellenwood":171,
  "Mario Armando Vasquez":172,
  "Illuminado Lopez":173,
  "Pedro Rios Jr.":174,
  "Rigoberto Arceo":175,
  "Pedro Najar Murillo":176,
  "Timothy Lopez":177,
  "Kwang Lee":178,
  "Richard Kim":179,
  "Mario Albert Madrigal":180,
  "John T. Williams":181,
  "Martin Pena":182,
  "Julio Lopez":183,
  "Miguel Moreno Torrez":184,
  "Errol Chang":185,
  "Oscar Perez Giron":186,
  "Jeanette Anaya":187,
  "Victor Villalpando":188,
  "Arcenio Lujan":189,
  "Abel Barrera-Siguenza":190,
  "Maria Godinez":191,
  "Cau Bich Tran":192,
  "Jesus Huerta":193,
  "Jose Adan Cruz Ocampo":194,
  "Binh Van Nguyen":195,
  "Mah-hi-vist Goodblanket":196,
  "Benjamin Whiteshield":197,
  "Gregory Michael Verzino":198,
  "Juan Castellanos":199,
  "Rosa Hammer":200,
  "Palin Perez Jackson":201,
  "Lisa Tomita Kaina":202,
  "Julio Ramos":203,
  "Dante Cespedes":204,
  'Alejandro "Alex" Nieto':205,
  "Daniel Rodriguez":206,
  "Joseph Valverde":207,
  "Leonel Disla":208,
  "Christopher Tavares":209,
  "Kenny Ray Wilson":210,
  "Jose Venavides":211,
  "Ray Dakota Scholfield":212,
  "Patrick Moses Dorismond":213,
  'Israel "Izzy" Andino':214,
  "Evelyn Vargas":215,
  "Shawn Eli Armajo":216,
  "Yi Tzu Chen":217,
  "Allan Duarte":218,
  "Juan Carlos Garcia":219,
  "Chieu-di Thi Vo":220,
  # "Fuaed Abdo Ahmed":'dns',
  "Tayler Rock":221,
  "German Mata":222,
  "Jorge Azucena":223,
  "Jose Cardenas":224,
  "Samuel Martinez":225,
  "Ricardo Zaragoza":226,
  "Julio Sandoval":227,
  "James Moala Kofu":228,
  "Javier Mendez":229,
  "Gloria Montoya":230,
  "Yeni Lopez":231,
  "Carlos Alberto Ramirez":232,
  "Luis Gonzalez":233,
  "Jonathan Montano":234,
  "Daniel Damian":235,
  "Praminder Singh Shergill":236,
  "Pablo Ortega":237,
  "Floyd Quinones":238,
  "Jose Zermeno-Garcia":239,
  "Adrian Parra":240,
  "Jonathen Santellana":241,
  "Caesar Ray Cruz":242,
  "David Raya":243,
  "Rogelio Serrato":244,
  # "Alex Alvarado":'dns',
  "Valente Galindo":245,
  "Wilbert J. Prado":246,
  "Justin Aguilar":247,
  "Eduardo Prieto":248,
  "Andre Luis DeCastro Martins":249,
  "Veronica Rizzo-Acevedo":250,
  "Angel Hiraldo":251,
  "Angel Luis Cajigas aka Paul Rosado":252,
  "Anibal Rosario-Rodriguez":253,
  "Ernesto Morales":254,
  "Hiram Marrero":255,
  "Jose Maldonado":256,
  "Juan Alberto Negron Gonzalez aka Ruddy Lora":257,
  "Miguel Serrano":258,
  "Noel Mendoza":259,
  "Vicente Bermudez":260,
  "Wilson Alba":261,
  "Mark Anthony Sepulveda":262,
  "Anthony Bartley":263,
  "David Valenzuela":264,
  "Margarito Lopez Morales":265,
  "Ricardo Cabrales":266,
  "Daniel Leon":267,
  # "Edwin Rivera":'dns',
  "Juan Carlos Castillo-Maldonado":268,
  "Eveline Barros-Cepeda":269,
  "Noel Jimines":270,
  "Roger Reyes Padilla":271,
  "Jose Pineda":272,
  "Alfred Torres":273,
  'Arthur "Artie" Sanchez Jr.':274,
  'Maximo "Flaco" Pequero':275,
  "David Garcia":276,
  "Benito A. Gonzalez":277,
  "Luis S. Barrientos":278,
  "Juan Mendez Jr.":279,
  "Carlos LaMadrid":280,
  "Dixon Rodriguez":281,

  #batch 4
  'Gil Collar': 1,
  'Lauren Brown': 2,
  # 'Tamerlan Tsarnaev':'',
  'Lisa Renee Miller': 3,
  'Carl Bowie III': 4,
  'Adam James Stevens': 5,
  'Alexander Zagovalov': 6,
  'Alexzander Coan': 7,
  'Allen Kephart': 8,
  'Andrew Landry': 9,
  'Andrew Lee Scott': 10,
  'Angella Falconi': 11,
  'Anthony Scott Brown': 12,
  'Brandon Barrett': 13,
  'Brent Bayliffe': 14,
  'Brent E. Brozek': 15,
  'Bruce James Weigel': 16,
  'Bryan Don Scott': 17,
  'Cameron Arrigoni': 18,
  'Carl Maggiorini Jr.': 19,
  'Chad Moretz': 20,
  'Chad Runge': 21,
  'Charles G. Carll': 22,
  'Charles Robinson': 23,
  'Cheri Lynn Moore': 24,
  'Christopher Burgess': 25,
  'Clinton Peterson': 26,
  'Cody Loron': 27,
  'Cody Shobe': 28,
  'Danielle Misha Willard': 29,
  'Danny Haskell': 30,
  'Danny L. Walsh': 31,
  'Donny Simmons': 32,
  'Douglas Ostling': 33,
  'Edward Flener': 34,
  'Ethan Corporon': 35,
  'Gregory Gordon': 36,
  # 'Hans P. Walters': '',
  'Ian Burlakoff': 37,
  'Jacob Grassley': 38,
  'Jacob Westberg': 39,
  'Jake Ramsey Maese-Murphy': 40,
  'James F. Popkowski': 41,
  'James Levier': 42,
  'James Lockhart III': 43,
  'James Richard Hill': 44,
  'Jamie Renée Fitzgerald': 45,
  'Jason Edward Prostrollo': 46,
  # 'Jimmy Lee Dykes':'' ,
  'Joel Silvesan': 47,
  'John Edward Dempsey': 48,
  'John Loxas': 49,
  'John N. Torretti': 50,
  'John Stanley Schaefer': 51,
  'Jonathan Dipaola': 52,
  'Joseph Erin Hamley': 53,
  'Justin Crowley-Smilek': 54,
  'Justin Hertl': 55,
  'Katherine Paulson': 56,
  'Kathryn Walters': 57,
  'Kathy Porter': 58,
  'Kelly David Bangle': 59,
  'Kenneth Dennis': 60,
  'Kenneth Ellis III': 61,
  'Kenneth Girardot': 62,
  'Kenneth Lloyd Lessley': 63,
  'Kenneth Wickham': 64,
  'Kent Brewer': 65,
  # 'Kevin Ambrose':'' ,
  'Kevin Carlson': 66,
  'Kevin Charles Duey': 67,
  'Kevin Ryberg': 68,
  'Kevin Wayne Newland': 69,
  'Kevin Worley': 70,
  'Kjeston Rodgers': 71,
  # 'Leon Tilden': '',
  'Leonardo Parera': 72,
  'Martin Y. Potts': 73,
  'Matthew Lyell Berg': 74,
  'Maurice Chad Paladino': 75,
  'Maximillian Walters': 76,
  'Melody Sanchez': 77,
  'Michael Bitters': 78,
  'Michael C. Nestor': 79,
  'Michael Norton': 80,
  'Milton Sanchez': 81,
  'Neil Begin': 82,
  'Nicholas J. Ivie': 83,
  'Nicholas Titus': 84,
  'Paul A. Fritze': 85,
  'Quentin Dodd': 86,
  'Rabih Ozeir': 87,
  'Rachel Lea Soto': 88,
  'Renee Witham': 89,
  'Robert Bellfleur': 90,
  'Robert Long': 91,
  'Robert Parlette Jr.': 92,
  'Roscoe Cambridge': 93,
  'Seth Jacob Beckman': 94,
  'Sonny Archuleta': 95,
  'Steven Hughes Henning': 96,
  'Steven V. Peterson': 97,
  # 'Thomas "Tres" Caffall':'',
  'Thomas P. Mayne': 98,
  # 'Tiffany Bishop':'',
  'Todd S. Weber': 99,
  'Travis Posselt': 100,
  'Troy Lanning Jr.': 101,
  'Wayne Scott Creach': 102,
  'William Spradling': 103,
  'Zachary Cooke': 104,
  'Zachary Premo': 105,
  'Bobby Canipe': 106,
  'Kenneth Roedig': 107,
  # 'Aaron Matthew Collier': '',
  'Adam Lee Cooper': 108,
  'Alan Dale Cash': 109,
  # 'Allen Meister':'',
  'Anthony Brenes': 110,
  'Benjamin Hunter Bowman': 111,
  'Billy Wayne Simms': 112,
  'Bradley Lee Morgan': 113,
  'Brian Edward Shelton': 114,
  'Brian Ramirez': 115,
  'Bruce Perison Clark': 116,
  'Charles Bradley Campbell': 117,
  'Christopher John Tuttle': 118,
  'Craig Boehler': 119,
  'Daniel Cromb': 120,
  'Daniel Vincent Kloskowski': 121,
  'Darryel Dwayne Ferguson': 122,
  'David Collopy': 123,
  'David Earl Hughes': 124,
  'David Jeffrey Freeman': 125,
  'David Orr': 126,
  'David William Higgins': 127,
  'Dennis Lamar Young': 128,
  'Deshira Selimaj': 129,
  'Donald Charles Mettinger': 130,
  'Donna Ann Morrow': 131,
  'Dwayne Richard Novak': 132,
  'Edgar Doubleday': 133,
  'Edward John Scheboth': 134,
  'Edward William Cook': 135,
  'Emit Sebastian Rice': 136,
  'Eric Jason Thatcher': '',
  'Erik Scott': 137,
  'Frederick M. Hedstrom Jr.': 138,
  'Glenn Jeffrey Spyer': 139,
  'Jack Dale Collins': 140,
  # 'James Heitkotter':''
  'James Philip Chasse Jr.': 141,
  'Jason Spoor': 142,
  'Jeffrey Allan Gaddis': 143,
  'Jeffrey Daniels': 144,
  'Jeffrey Dean Martindale': 145,
  'Jerry Goins': 146,
  'John Charles O’Banion': 147,
  'John Frank Jackman': 148,
  'John Hampton Haines': 149,
  'John Paul Hambleton': 150,
  'Joseph Michael Justin': 151,
  'Joshua Russell': 152,
  'Justin Hoey': 153,
  'Justin Mueller': 154,
  'Karoline Michelle Bradley': 155,
  'Kathryn Daily': 156,
  'Keith Alan Engel': 157,
  'Kelly DuPriest': 158,
  'Larry Lloyd Dague': 159,
  'Marc Hull': 160,
  'Mateo Carlo Machella': 161,
  'Merle Mikal Hatch': 162,
  'Micah S. Abbey': 163,
  'Michael Ray Jaquith': 164,
  'Rayburn Bryant': 165,
  'Raymond Dwayne Gwerder': 166,
  'Raymond Leonard Youngberg Jr.': 167,
  'Richard Travis Brown': 168,
  'Robert B. Mills': 169,
  'Robert James Nusbaum': 170,
  'Roger "Jeremy" Ramundo': 171,
  'Ronald James Morrison': 172,
  'Ronald Richard Riebling Jr.': 173,
  'Shawn Jacob Collins': 174,
  'Steven Richard Bolen': 175,
  'Tanner Chamberlin': 176,
  # 'Thomas Higginbotham':''
  'Thomas Lars Domagala': 177,
  'Timothy Grant': 178,
  'Tory Manvilla': 179,
  'Kelly Thomas': 180,
  'Christopher Michael Tallman': 181,
  'Dale Mattson': 182,
  'Daniel Millan Lopez': 183,
  # 'David Krambs': '',
  # 'Devin Peterson': '',
  'Greg Larson': 184,
  'Jace Herndon': 185,
  'Jeffery Allen Violett': 186,
  'John Franklin McCoy': 187,
  'Joseph Parsons': 188,
  'Joshua Scott Lehman':'',
  'Layne Campbell': 189,
  'Michael Paul Wellborn': 190,
  'Monica Ritchey': 191,
  'Ronald Leach': 192,
  'Santiago Martinez': 193,
  'Scott Lance Demars': 194,
  'Steven Alan Jarosz': 195,
  'Stuart Alan Wood': 196,
  'Walter Inzer': 197,
  # 'William Barton Lewis':  '',
  # 'Daniel Dixon':  '',
  'Scott Lavel Zieske': 198,
  'Donna Lee Hewitt': 199,
  'David Pendleton': 200,
  # 'Harvey Ex': '',
  # 'Wesley Louis Skinner': '',
  'Robert McKinney': '',
  'Roy Wilkins': 201,
  'David Sal Silva': 202,
  'Paul Heenan': 203,
  'Ryan Euzene Rich': 204,
  'Abdul Arian': 205,
  'Cherise Daniel Johnson': 206,
  'Derek Steven Post': 207,
  'Delma Towler':  '',
  'Dan Ficker': 208,
  'Jerry Wayne Waller': 209,
  'Kelly Fay Simons': 210,
  'Travis Scott Buffington': 211,
  # 'Stephen Patrick Griffin': '',
  # 'John Anderson': '',
  # 'Ross Harrison Stewart': ''
}
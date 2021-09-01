from enum import Enum
from django.db.models import manager
from django.utils.translation import gettext_lazy as _
from django.db import models
# https://docs.djangoproject.com/en/3.2/ref/models/fields/

class LanguageChoices(models.TextChoices):
    # Variable = value that is held _('text displayed to user')
    ABKHAZ = 'ab', _('Abkhaz')
    AFAR = 'aa', _('Afar')
    AFRIKAANS = 'af', _('Afrikaans')
    AKAN = 'ak', _('Akan')
    ALBANIAN = 'sq', _('Albanian')
    AMHARIC = 'am', _('Amharic')
    ARABIC = 'ar', _('Arabic')
    ARAGONESE = 'an', _('Aragonese')
    ARMENIAN = 'hy', _('Armenian')
    ASSAMESE = 'as', _('Assamese')
    AVARIC = 'av', _('Avaric')
    AVESTAN = 'ae', _('Avestan')
    AYMARA = 'ay', _('Aymara')
    AZERBAIJANI = 'az', _('Azerbaijani')
    BAMBARA = 'bm', _('Bambara')
    BASHKIR = 'ba', _('Bashkir')
    BASQUE = 'eu', _('Basque')
    BELARUSIAN = 'be', _('Belarusian')
    BENGALI = 'bn', _('Bengali')
    BIHARI = 'bh', _('Bihari')
    BISLAMA = 'bi', _('Bislama')
    BOSNIAN = 'bs', _('Bosnian')
    BRETON = 'br', _('Breton')
    BULGARIAN = 'bg', _('Bulgarian')
    BURMESE = 'my', _('Burmese')
    CATALAN_VALENCIAN = 'ca', _('Catalan; Valencian')
    CHAMORRO = 'ch', _('Chamorro')
    CHECHEN = 'ce', _('Chechen')
    CHICHEWA_CHEWA_NYANJA = 'ny', _('Chichewa; Chewa; Nyanja')
    CHINESE = 'zh', _('Chinese')
    CHUVASH = 'cv', _('Chuvash')
    CORNISH = 'kw', _('Cornish')
    CORSICAN = 'co', _('Corsican')
    CREE = 'cr', _('Cree')
    CROATIAN = 'hr', _('Croatian')
    CZECH = 'cs', _('Czech')
    DANISH = 'da', _('Danish')
    DIVEHI_MALDIVIAN = 'dv', _('Divehi; Maldivian;')
    DUTCH = 'nl', _('Dutch')
    DZONGKHA = 'dz', _('Dzongkha')
    ENGLISH = 'en', _('English')
    ESPERANTO = 'eo', _('Esperanto')
    ESTONIAN = 'et', _('Estonian')
    EWE = 'ee', _('Ewe')
    FAROESE = 'fo', _('Faroese')
    FIJIAN = 'fj', _('Fijian')
    FINNISH = 'fi', _('Finnish')
    FRENCH = 'fr', _('French')
    FULA = 'ff', _('Fula')
    GALICIAN = 'gl', _('Galician')
    GEORGIAN = 'ka', _('Georgian')
    GERMAN = 'de', _('German')
    GREEK_MODERN = 'el', _('Greek, Modern')
    GUARANÍ = 'gn', _('Guaraní')
    GUJARATI = 'gu', _('Gujarati')
    HAITIAN = 'ht', _('Haitian')
    HAUSA = 'ha', _('Hausa')
    HEBREW_MODERN = 'he', _('Hebrew (modern)')
    HERERO = 'hz', _('Herero')
    HINDI = 'hi', _('Hindi')
    HIRI_MOTU = 'ho', _('Hiri Motu')
    HUNGARIAN = 'hu', _('Hungarian')
    INTERLINGUA = 'ia', _('Interlingua')
    INDONESIAN = 'id', _('Indonesian')
    INTERLINGUE = 'ie', _('Interlingue')
    IRISH = 'ga', _('Irish')
    IGBO = 'ig', _('Igbo')
    INUPIAQ = 'ik', _('Inupiaq')
    IDO = 'io', _('Ido')
    ICELANDIC = 'is', _('Icelandic')
    ITALIAN = 'it', _('Italian')
    INUKTITUT = 'iu', _('Inuktitut')
    JAPANESE = 'ja', _('Japanese')
    JAVANESE = 'jv', _('Javanese')
    KALAALLISUT = 'kl', _('Kalaallisut')
    KANNADA = 'kn', _('Kannada')
    KANURI = 'kr', _('Kanuri')
    KASHMIRI = 'ks', _('Kashmiri')
    KAZAKH = 'kk', _('Kazakh')
    KHMER = 'km', _('Khmer')
    KIKUYU_GIKUYU = 'ki', _('Kikuyu, Gikuyu')
    KINYARWANDA = 'rw', _('Kinyarwanda')
    KIRGHIZ_KYRGYZ = 'ky', _('Kirghiz, Kyrgyz')
    KOMI = 'kv', _('Komi')
    KONGO = 'kg', _('Kongo')
    KOREAN = 'ko', _('Korean')
    KURDISH = 'ku', _('Kurdish')
    KWANYAMA_KUANYAMA = 'kj', _('Kwanyama, Kuanyama')
    LATIN = 'la', _('Latin')
    LUXEMBOURGISH = 'lb', _('Luxembourgish')
    LUGANDA = 'lg', _('Luganda')
    LIMBURGISH = 'li', _('Limburgish')
    LINGALA = 'ln', _('Lingala')
    LAO = 'lo', _('Lao')
    LITHUANIAN = 'lt', _('Lithuanian')
    LUBA_KATANGA = 'lu', _('Luba-Katanga')
    LATVIAN = 'lv', _('Latvian')
    MANX = 'gv', _('Manx')
    MACEDONIAN = 'mk', _('Macedonian')
    MALAGASY = 'mg', _('Malagasy')
    MALAY = 'ms', _('Malay')
    MALAYALAM = 'ml', _('Malayalam')
    MALTESE = 'mt', _('Maltese')
    MAORI = 'mi', _('Māori')
    MARATHI_MARATHI = 'mr', _('Marathi (Marāṭhī)')
    MARSHALLESE = 'mh', _('Marshallese')
    MONGOLIAN = 'mn', _('Mongolian')
    NAURU = 'na', _('Nauru')
    NAVAJO_NAVAHO = 'nv', _('Navajo, Navaho')
    NORWEGIAN_BOKMÅL = 'nb', _('Norwegian Bokmål')
    NORTH_NDEBELE = 'nd', _('North Ndebele')
    NEPALI = 'ne', _('Nepali')
    NDONGA = 'ng', _('Ndonga')
    NORWEGIAN_NYNORSK = 'nn', _('Norwegian Nynorsk')
    NORWEGIAN = 'no', _('Norwegian')
    NUOSU = 'ii', _('Nuosu')
    SOUTH_NDEBELE = 'nr', _('South Ndebele')
    OCCITAN = 'oc', _('Occitan')
    OJIBWE_OJIBWA = 'oj', _('Ojibwe, Ojibwa')
    OLD_CHURCH_SLAVONIC = 'cu', _('Old Church Slavonic')
    OROMO = 'om', _('Oromo')
    ORIYA = 'or', _('Oriya')
    OSSETIAN_OSSETIC = 'os', _('Ossetian, Ossetic')
    PANJABI_PUNJABI = 'pa', _('Panjabi, Punjabi')
    PĀLI = 'pi', _('Pāli')
    PERSIAN = 'fa', _('Persian')
    POLISH = 'pl', _('Polish')
    PASHTO_PUSHTO = 'ps', _('Pashto, Pushto')
    PORTUGUESE = 'pt', _('Portuguese')
    QUECHUA = 'qu', _('Quechua')
    ROMANSH = 'rm', _('Romansh')
    KIRUNDI = 'rn', _('Kirundi')
    ROMANIAN_MOLDAVAN = 'ro', _('Romanian, Moldavan')
    RUSSIAN = 'ru', _('Russian')
    SANSKRIT = 'sa', _('Sanskrit (Saṁskṛta)')
    SARDINIAN = 'sc', _('Sardinian')
    SINDHI = 'sd', _('Sindhi')
    NORTHERN_SAMI = 'se', _('Northern Sami')
    SAMOAN = 'sm', _('Samoan')
    SANGO = 'sg', _('Sango')
    SERBIAN = 'sr', _('Serbian')
    SCOTTISH_GAELIC = 'gd', _('Scottish Gaelic')
    SHONA = 'sn', _('Shona')
    SINHALA_SINHALESE = 'si', _('Sinhala, Sinhalese')
    SLOVAK = 'sk', _('Slovak')
    SLOVENE = 'sl', _('Slovene')
    SOMALI = 'so', _('Somali')
    SOUTHERN_SOTHO = 'st', _('Southern Sotho')
    SPANISH_CASTILIAN = 'es', _('Spanish; Castilian')
    SUNDANESE = 'su', _('Sundanese')
    SWAHILI = 'sw', _('Swahili')
    SWATI = 'ss', _('Swati')
    SWEDISH = 'sv', _('Swedish')
    TAMIL = 'ta', _('Tamil')
    TELUGU = 'te', _('Telugu')
    TAJIK = 'tg', _('Tajik')
    THAI = 'th', _('Thai')
    TIGRINYA = 'ti', _('Tigrinya')
    TIBETAN = 'bo', _('Tibetan')
    TURKMEN = 'tk', _('Turkmen')
    TAGALOG = 'tl', _('Tagalog')
    TSWANA = 'tn', _('Tswana')
    TONGA = 'to', _('Tonga')
    TURKISH = 'tr', _('Turkish')
    TSONGA = 'ts', _('Tsonga')
    TATAR = 'tt', _('Tatar')
    TWI = 'tw', _('Twi')
    TAHITIAN = 'ty', _('Tahitian')
    UIGHUR_UYGHUR = 'ug', _('Uighur, Uyghur')
    UKRAINIAN = 'uk', _('Ukrainian')
    URDU = 'ur', _('Urdu')
    UZBEK = 'uz', _('Uzbek')
    VENDA = 've', _('Venda')
    VIETNAMESE = 'vi', _('Vietnamese')
    VOLAPÜK = 'vo', _('Volapük')
    WALLOON = 'wa', _('Walloon')
    WELSH = 'cy', _('Welsh')
    WOLOF = 'wo', _('Wolof')
    WESTERN_FRISIAN = 'fy', _('Western Frisian')
    XHOSA = 'xh', _('Xhosa')
    YIDDISH = 'yi', _('Yiddish')
    YORUBA = 'yo', _('Yoruba')
    ZHUANG_CHUANG = 'za', _('Zhuang, Chuang')
    ZULU = 'zu', _('Zulu')

class EpisodeTypes(models.TextChoices):
    # Variable = value that is held _('text displayed to user')
    FULL = 'full', _('Full')
    TRAILER = 'trailer', _('Trailer')
    BONUS = 'bonus', _('Bonus')

class ShowType(models.TextChoices):
    # Variable = value that is held _('text displayed to user')
    EPISODIC = 'episodic', _('Episodic')
    SERIAL = 'serial', _('Serial')

class ExplictSetting(models.TextChoices):
    # Variable = value that is held _('text displayed to user')
    YES = 'yes', _('Yes')
    NO = 'no', _('No')
    CLEAN = 'clean', _('Clean')

# https://help.apple.com/itc/podcasts_connect/#/itc9267a2f12
#
class CategoryChoices(models.TextChoices):
    ART = 'Arts', _('Arts')
    BOOKS = 'Books', _('Books')
    DESIGN = 'Design', _('Design')
    FASHION_AND_BEAUTY = 'Fashion &amp; Beauty', _('Fashion & Beauty')
    FOOD = 'Food', _('Food')
    VISUAL_ARTS = 'Visual Arts', _('Visual Arts')
    PERFORMING_ARTS = 'Performing Arts', _('Performing Arts')
    BUSINESS = 'Business', _('Business')
    CAREERS = 'Careers', _('Careers')
    ENTREPRENEURSHIP = 'Entrepreneurship', _('Entrepreneurship')
    INVESTING = 'Investing', _('Investing')
    MANAGEMENT = 'Management', _('Management')
    MARKETING = 'Marketing', _('Marketing')
    NON_PROFIT = 'Non-Profit', _('Non-Profit')
    COMEDY = 'Comedy', _('Comedy')
    COMEDY_INTERVIEWS = 'Comedy Interviews', _('Comedy Interviews')
    IMPROV = 'Improv', _('Improv')
    STAND_UP = 'Stand-Up', _('Stand-Up')
    EDUCATION = 'Education', _('Education')
    COURSES = 'Courses', _('Courses')
    HOW_TO = 'How To', _('How To')
    LANGUAGE_LEARNING = 'Language Learning', _('Language Learning')
    SELF_IMPROVEMENT = 'Self-Improvement', _('Self-Improvement')
    FICTION = 'Fiction', _('Fiction')
    COMEDY_FICTION = 'Comedy Fiction', _('Comedy Fiction')
    DRAMA = 'Drama', _('Drama')
    SCIENCE_FICTION = 'Science Fiction', _('Science Fiction')
    GOVERNMENT = 'Government', _('Government')
    HISTORY = 'History', _('History')
    HEALTH_AND_FITNESS = 'Health &amp; Fitness', _('Health & Fitness')
    ALTERNATIVE_HEALTH = 'Alternative Health', _('Alternative Health')
    FITNESS = 'Fitness', _('Fitness')
    MEDICINE = 'Medicine', _('Medicine')
    MENTAL_HEALTH = 'Mental Health', _('Mental Health')
    NUTRITION = 'Nutrition', _('Nutrition')
    SEXUALITY = 'Sexuality', _('Sexuality')
    KIDS_AND_FAMILY = 'Kids &amp; Family', _('Kids & Family')
    EDUCATON_FOR_KIDS = 'Education for Kids', _('Education for Kids')
    PARENTING = 'Parenting', _('Parenting')
    PETS_AND_ANIMALS = 'Pets &amp; Animals', _('Pets & Animals')
    STORIES_FOR_KIDS = 'Stories for Kids', _('Stories for Kids')
    LEISURE = 'Leisure', _('Leisure')
    ANIMATION_AND_MANGA = 'Animation &amp; Manga', _('Animation & Manga')
    AUTOMOTIVE = 'Automotive', _('Automotive')
    AVIATION = 'Aviation', _('Aviation')
    CRAFTS = 'Crafts', _('Crafts')
    GAMES = 'Games', _('Games')
    HOBBIES = 'Hobbies', _('Hobbies')
    HOME_AND_GARDEN = 'Home &amp; Garden', _('Home & Garden')
    VIDEO_GAMES = 'Video Games', _('Video Games')
    MUSIC = 'Music', _('Music')
    MUSIC_COMMENTARY = 'Music Commentary', _('Music Commentary')
    MUSIC_HISTORY = 'Music History', _('Music History')
    MUSIC_INTERVIEWS = 'Music Interviews', _('Music Interviews')
    NEWS = 'News', _('News')
    BUSINESS_NEWS = 'Business News', _('Business News')
    DAILY_NEWS = 'Daily News', _('Daily News')
    ENTERTAINMENT_NEWS = 'Entertainment News', _('Entertainment News')
    NEWS_COMMENTARY = 'News Commentary', _('News Commentary')
    POLITICS = 'Politics', _('Politics')
    SPORTS_NEWS = 'Sports News', _('Sports News')
    TECH_NEWS = 'Tech News', _('Tech News')
    RELIGION_AND_SPIRITUALITY = 'Religion &amp; Spirituality', _('Religion & Spirituality')
    BUDDHISM = 'Buddhism', _('Buddhism')
    CHRISTIANITY = 'Christianity', _('Christianity')
    HINDUISM = 'Hinduism', _('Hinduism')
    ISLAM = 'Islam', _('Islam')
    JUDAISM = 'Judaism', _('Judaism')
    RELIGION = 'Religion', _('Religion')
    SPIRITUALITY = 'Spirituality', _('Spirituality')
    SCIENCE = 'Science', _('Science')
    ASTRONOMY = 'Astronomy', _('Astronomy')
    CHEMISTRY = 'Chemistry', _('Chemistry')
    EARTH_SCIENCES = 'Earth Sciences', _('Earth Sciences')
    LIFE_SCIENCES = 'Life Sciences', _('Life Sciences')
    MATHEMATICS = 'Mathematics', _('Mathematics')
    NATURAL_SCIENCES = 'Natural Sciences', _('Natural Sciences')
    NATURE = 'Nature', _('Nature')
    PHYSICS = 'Physics', _('Physics')
    SOCIAL_SCIENCES = 'Social Sciences', _('Social Sciences')
    SOCIETY_AND_CULTURE = 'Society &amp; Culture', _('Society & Culture')
    DOCUMENTARY = 'Documentary', _('Documentary')
    PERSONAL_JOURNALS = 'Personal Journals', _('Personal Journals')
    PHILOSOPHY = 'Philosophy', _('Philosophy')
    PLACES_AND_TRAVEL = 'Places &amp; Travel', _('Places & Travel')
    RELATIONSHIPS = 'Relationships', _('Relationships')
    SPORTS = 'Sports', _('Sports')
    BASEBALL = 'Baseball', _('Baseball')
    BASKETBALL = 'Basketball', _('Basketball')
    CRICKET = 'Cricket', _('Cricket')
    FANTASY_SPORTS = 'Fantasy Sports', _('Fantasy Sports')
    FOOTBALL = 'Football', _('Football')
    GOLF = 'Golf', _('Golf')
    HOCKEY = 'Hockey', _('Hockey')
    RUGBY = 'Rugby', _('Rugby')
    RUNNING = 'Running', _('Running')
    SOCCER = 'Soccer', _('Soccer')
    SWIMMING = 'Swimming', _('Swimming')
    TENNIS = 'Tennis', _('Tennis')
    VOLLEYBALL = 'Volleyball', _('Volleyball')
    WILDERNESS = 'Wilderness', _('Wilderness')
    WRESTLING = 'Wrestling', _('Wrestling')
    TECHONOLOGY = 'Technology', _('Technology')
    TRUE_CRIME = 'True Crime', _('True Crime')
    TV_AND_FILM = 'TV &amp; Film', _('TV & Film')
    FILM_HISTORY = 'Film History', _('Film History')
    FILM_INTERVIEWS = 'Film Interviews', _('Film Interviews')
    FILM_REVIEWS = 'Film Reviews', _('Film Reviews')
    TV_REVIEWS = 'TV Reviews', _('TV Reviews')
    AFTER_SHOWS = 'After Shows', _('After Shows')

    def get_main_category(subcategory):
        category_dict = {

            'Books' : 'Arts',
            'Design' : 'Arts',
            'Fashion &amp; Beauty' : 'Arts',
            'Food' : 'Arts',
            'Visual Arts' : 'Arts',
            'Performing Arts' : 'Arts',

            'Careers' : 'Business',
            'Entrepreneurship' : 'Business',
            'Investing' : 'Business',
            'Management' : 'Business',
            'Marketing' : 'Business',
            'Non-Profit' : 'Business',

            'Comedy Interviews' : 'Comedy',
            'Improv' : 'Comedy',
            'Stand-Up' : 'Comedy',

            'Courses' : 'Education',
            'How To' : 'Education',
            'Language Learning' : 'Education',
            'Self-Improvement' : 'Education',

            'Comedy Fiction' : 'Fiction',
            'Drama' : 'Fiction',
            'Science Fiction' : 'Fiction',

            'Alternative Health' : 'Health &amp; Fitness',
            'Fitness' : 'Health &amp; Fitness',
            'Medicine' : 'Health &amp; Fitness',
            'Mental Health' : 'Health &amp; Fitness',
            'Nutrition' : 'Health &amp; Fitness',
            'Sexuality' : 'Health &amp; Fitness',

            'Education for Kids' : 'Kids &amp; Family',
            'Parenting' : 'Kids &amp; Family',
            'Pets &amp; Animals' : 'Kids &amp; Family',
            'Stories for Kids' : 'Kids &amp; Family',
            
            'Animation &amp; Manga' : 'Leisure',
            'Automotive' : 'Leisure',
            'Aviation' : 'Leisure',
            'Crafts' : 'Leisure',
            'Games' : 'Leisure',
            'Hobbies' : 'Leisure',
            'Home &amp; Garden' : 'Leisure',
            'Video Games' : 'Leisure',

            'Music Commentary' : 'Music',
            'Music History' : 'Music',
            'Music Interviews' : 'Music',

            'Politics' : 'News',
            'Business News' : 'News',
            'Daily News' : 'News',
            'Entertainment News' : 'News',
            'News Commentary' : 'News',
            'Sports News' : 'News',
            'Tech News' : 'News',

            'Buddhism' : 'Religion &amp; Spirituality',
            'Christianity' : 'Religion &amp; Spirituality',
            'Hinduism' : 'Religion &amp; Spirituality',
            'Islam' : 'Religion &amp; Spirituality',
            'Judaism' : 'Religion &amp; Spirituality',
            'Religion' : 'Religion &amp; Spirituality',
            'Spirituality' : 'Religion &amp; Spirituality',

            'Astronomy' : 'Science',
            'Chemistry' : 'Science',
            'Earth Sciences' : 'Science',
            'Life Sciences' : 'Science',
            'Mathematics' : 'Science',
            'Natural Sciences' : 'Science',
            'Nature' : 'Science',
            'Physics' : 'Science',
            'Social Sciences' : 'Science',

            'Documentary' : 'Society &amp; Culture',
            'Personal Journals' : 'Society &amp; Culture',
            'Philosophy' : 'Society &amp; Culture',
            'Places &amp; Travel' : 'Society &amp; Culture',
            'Relationships' : 'Society &amp; Culture',

            'Baseball' : 'Sports',
            'Basketball' : 'Sports',
            'Cricket' : 'Sports',
            'Fantasy Sports' : 'Sports',
            'Golf' : 'Sports',
            'Hockey' : 'Sports',
            'Rugby' : 'Sports',
            'Running' : 'Sports',
            'Soccer' : 'Sports',
            'Swimming' : 'Sports',
            'Tennis' : 'Sports',
            'Volleyball' : 'Sports',
            'Wilderness' : 'Sports',
            'Wrestling' : 'Sports',

            'Film History' : 'TV &amp; Film',
            'Film Interviews' : 'TV &amp; Film',
            'Film Reviews' : 'TV &amp; Film',
            'TV Reviews' : 'TV &amp; Film',
            'After Shows' : 'TV &amp; Film',
        }

        if subcategory in category_dict:
            return category_dict[subcategory]
        else:
            return "" # this means that the input category is the main category
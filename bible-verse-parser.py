import re

inputFile = input('Enter filename here: ')
outputFile = 'output_' + inputFile

# open file
f = open(inputFile,'r')
newData = f.read()
f.close()

# function for indicating working status
def updateWorkingIndicator():
    global workingIndicator
    runningIndication = ["／", "－", "＼", "｜"]
    print("... parsing ... "+runningIndication[workingIndicator])
    if workingIndicator == 3:
        workingIndicator = 0
    else:
        workingIndicator += 1

# function for standardising verse references; use standard set of abbreviations defined below; format references as <abbreviation> <chapter>:<verse>
def standardReference(text, answer):
    fixedText = text
    if answer == 'YES':
        standardAbbreviation = {
            "1": "Gen",
            "2": "Exod",
            "3": "Lev",
            "4": "Num",
            "5": "Deut",
            "6": "Josh",
            "7": "Judg",
            "8": "Ruth",
            "9": "1Sam",
            "10": "2Sam",
            "11": "1Kgs",
            "12": "2Kgs",
            "13": "1Chr",
            "14": "2Chr",
            "15": "Ezra",
            "16": "Neh",
            "17": "Esth",
            "18": "Job",
            "19": "Ps",
            "20": "Prov",
            "21": "Eccl",
            "22": "Song",
            "23": "Isa",
            "24": "Jer",
            "25": "Lam",
            "26": "Ezek",
            "27": "Dan",
            "28": "Hos",
            "29": "Joel",
            "30": "Amos",
            "31": "Obad",
            "32": "Jonah",
            "33": "Mic",
            "34": "Nah",
            "35": "Hab",
            "36": "Zeph",
            "37": "Hag",
            "38": "Zech",
            "39": "Mal",
            "40": "Matt",
            "41": "Mark",
            "42": "Luke",
            "43": "John",
            "44": "Acts",
            "45": "Rom",
            "46": "1Cor",
            "47": "2Cor",
            "48": "Gal",
            "49": "Eph",
            "50": "Phil",
            "51": "Col",
            "52": "1Thess",
            "53": "2Thess",
            "54": "1Tim",
            "55": "2Tim",
            "56": "Titus",
            "57": "Phlm",
            "58": "Heb",
            "59": "Jas",
            "60": "1Pet",
            "61": "2Pet",
            "62": "1John",
            "63": "2John",
            "64": "3John",
            "65": "Jude",
            "66": "Rev",
            "70": "Bar",
            "71": "AddDan",
            "72": "PrAzar",
            "73": "Bel",
            "75": "Sus",
            "76": "1Esd",
            "77": "2Esd",
            "78": "AddEsth",
            "79": "EpJer",
            "80": "Jdt",
            "81": "1Macc",
            "82": "2Macc",
            "83": "3Macc",
            "84": "4Macc",
            "85": "PrMan",
            "86": "Ps151",
            "87": "Sir",
            "88": "Tob",
            "89": "Wis",
            "90": "PssSol",
            "91": "Odes",
            "92": "EpLao",
        }
        for booknumber in standardAbbreviation:
            updateWorkingIndicator()
            abbreviation = standardAbbreviation[booknumber]
            fixedText = re.sub('<ref onclick="bcv\('+booknumber+',([0-9]+?),([0-9]+?)\)">.*?</ref>', '<ref onclick="bcv('+booknumber+r',\1,\2)">'+abbreviation+r' \1:\2</ref>', fixedText)
        print("All verse references had been standardised.")
    else:
        print("Verse references are NOT standardised.")
    return fixedText

# start parsing from here

# set a simple indicator
workingIndicator = 0

# search for books; mark them with book numbers, used by https://marvel.bible
marvelBibleBookNo = {
    "The Song of the Three Holy Children": "72",
    "Song of the Three Holy Children": "72",
    "Epistle to the Laodiceans": "92",
    "The Song of Three Youths": "72",
    "Song of Three Children": "72",
    "The Song of Three Jews": "72",
    "Canticle of Canticles": "22",
    "Epistle to Laodiceans": "92",
    "Second Thessalonians": "53",
    "Song of Three Youths": "72",
    "First Thessalonians": "52",
    "Additions to Daniel": "71",
    "Additions to Esther": "78",
    "Second Corinthians": "47",
    "Apocalypse of John": "66",
    "Revelation to John": "66",
    "Bel and the Dragon": "73",
    "Song of Three Jews": "72",
    "The Rest of Esther": "78",
    "Letter of Jeremiah": "79",
    "Prayer of Manasseh": "85",
    "Prayer of Manasses": "85",
    "Epistle Laodiceans": "92",
    "Second Chronicles": "14",
    "First Corinthians": "46",
    "1st Thessalonians": "52",
    "2nd Thessalonians": "53",
    "Prayer of Azariah": "72",
    "Wisdom of Solomon": "89",
    "Psalms of Solomon": "90",
    "Epist. Laodiceans": "92",
    "First Chronicles": "13",
    "II Thessalonians": "53",
    "Sg. of 3 Childr.": "72",
    "Second Maccabees": "82",
    "Fourth Maccabees": "84",
    "Additional Psalm": "86",
    "Song of Solomon": "22",
    "1st Corinthians": "46",
    "2nd Corinthians": "47",
    "1 Thessalonians": "52",
    "I Thessalonians": "52",
    "2 Thessalonians": "53",
    "First Maccabees": "81",
    "Third Maccabees": "83",
    "1st Chronicles": "13",
    "2nd Chronicles": "14",
    "II Corinthians": "47",
    "1Thessalonians": "52",
    "2Thessalonians": "53",
    "Second Timothy": "55",
    "The Revelation": "66",
    "Rest of Esther": "78",
    "Ecclesiasticus": "87",
    "Psalms Solomon": "90",
    "Second Samuel": "10",
    "Second Chron.": "14",
    "Song of Songs": "22",
    "1 Corinthians": "46",
    "I Corinthians": "46",
    "2 Corinthians": "47",
    "Second Thess.": "53",
    "First Timothy": "54",
    "Song of Three": "72",
    "Second Esdras": "77",
    "1st Maccabees": "81",
    "2nd Maccabees": "82",
    "3rd Maccabees": "83",
    "III Maccabees": "83",
    "4th Maccabees": "84",
    "Wisd. of Sol.": "89",
    "First Samuel": "09",
    "Second Kings": "12",
    "1 Chronicles": "13",
    "First Chron.": "13",
    "2 Chronicles": "14",
    "Ecclesiastes": "21",
    "Lamentations": "25",
    "1Corinthians": "46",
    "2Corinthians": "47",
    "First Thess.": "52",
    "Second Peter": "61",
    "Song of Thr.": "72",
    "First Esdras": "76",
    "II Maccabees": "82",
    "IV Maccabees": "84",
    "Deuteronomy": "05",
    "Second Sam.": "10",
    "First Kings": "11",
    "Second Kgs.": "12",
    "Philippians": "50",
    "1st Timothy": "54",
    "2nd Timothy": "55",
    "Second Tim.": "55",
    "First Peter": "60",
    "Second John": "63",
    "Bel and Dr.": "73",
    "1 Maccabees": "81",
    "I Maccabees": "81",
    "2 Maccabees": "82",
    "3 Maccabees": "83",
    "4 Maccabees": "84",
    "Pr. of Man.": "85",
    "Ps. Solomon": "90",
    "1st Samuel": "09",
    "First Sam.": "09",
    "2nd Samuel": "10",
    "First Kgs.": "11",
    "1st Chron.": "13",
    "2nd Chron.": "14",
    "Colossians": "51",
    "1st Thess.": "52",
    "2nd Thess.": "53",
    "First Tim.": "54",
    "II Timothy": "55",
    "First John": "62",
    "Third John": "64",
    "Revelation": "66",
    "1st Esdras": "76",
    "2nd Esdras": "77",
    "Add. Esth.": "78",
    "1Maccabees": "81",
    "2Maccabees": "82",
    "3Maccabees": "83",
    "4Maccabees": "84",
    "Add. Psalm": "86",
    "Laodiceans": "92",
    "Leviticus": "03",
    "1st Kings": "11",
    "2nd Kings": "12",
    "II Chron.": "14",
    "Canticles": "22",
    "Zephaniah": "36",
    "Zechariah": "38",
    "Galatians": "48",
    "Ephesians": "49",
    "II Thess.": "53",
    "1 Timothy": "54",
    "I Timothy": "54",
    "2 Timothy": "55",
    "1st Peter": "60",
    "2nd Peter": "61",
    "Add. Dan.": "71",
    "Pr. Azar.": "72",
    "Sg. Three": "72",
    "Song Thr.": "72",
    "II Esdras": "77",
    "Let. Jer.": "79",
    "Ltr. Jer.": "79",
    "III Macc.": "83",
    "Ep. Laod.": "92",
    "1 Samuel": "09",
    "1st Sam.": "09",
    "2 Samuel": "10",
    "2nd Sam.": "10",
    "1st Kgs.": "11",
    "2nd Kgs.": "12",
    "1 Chron.": "13",
    "I Chron.": "13",
    "2 Chron.": "14",
    "Nehemiah": "16",
    "Proverbs": "20",
    "Jeremiah": "24",
    "Habakkuk": "35",
    "1 Thess.": "52",
    "I Thess.": "52",
    "2 Thess.": "53",
    "II Thes.": "53",
    "1Timothy": "54",
    "1st Tim.": "54",
    "2Timothy": "55",
    "2nd Tim.": "55",
    "Philemon": "57",
    "II Peter": "61",
    "1st John": "62",
    "2nd John": "63",
    "3rd John": "64",
    "III Jhn.": "64",
    "III Joh.": "64",
    "III John": "64",
    "1 Esdras": "76",
    "1Esdras.": "76",
    "I Esdras": "76",
    "2 Esdras": "77",
    "II Esdr.": "77",
    "Add. Es.": "78",
    "AddEsth.": "78",
    "Ep. Jer.": "79",
    "II Macc.": "82",
    "III Mac.": "83",
    "IV Macc.": "84",
    "Add. Ps.": "86",
    "Ps. Sol.": "90",
    "Ep. Lao.": "92",
    "Genesis": "01",
    "Numbers": "04",
    "II Sam.": "10",
    "1 Kings": "11",
    "2 Kings": "12",
    "II Kgs.": "12",
    "1Chron.": "13",
    "2Chron.": "14",
    "II Chr.": "14",
    "Eccles.": "21",
    "Ezekiel": "26",
    "Obadiah": "31",
    "Malachi": "39",
    "Matthew": "40",
    "II Cor.": "47",
    "Philip.": "50",
    "1 Thes.": "52",
    "1Thess.": "52",
    "I Thes.": "52",
    "2 Thes.": "53",
    "2Thess.": "53",
    "II Tim.": "55",
    "Philem.": "57",
    "Hebrews": "58",
    "1 Peter": "60",
    "I Peter": "60",
    "2 Peter": "61",
    "II Pet.": "61",
    "II Jhn.": "63",
    "II Joh.": "63",
    "II John": "63",
    "III Jn.": "64",
    "III Jo.": "64",
    "AddDan.": "71",
    "PrAzar.": "72",
    "Azariah": "72",
    "Pr. Az.": "72",
    "Susanna": "75",
    "1 Esdr.": "76",
    "I Esdr.": "76",
    "2 Esdr.": "77",
    "2Esdras": "77",
    "II Esd.": "77",
    "1 Macc.": "81",
    "I Macc.": "81",
    "2 Macc.": "82",
    "II Mac.": "82",
    "3 Macc.": "83",
    "III Ma.": "83",
    "4 Macc.": "84",
    "IV Mac.": "84",
    "Pr. Man": "85",
    "Ecclus.": "87",
    "PssSol.": "90",
    "Exodus": "02",
    "Joshua": "06",
    "Judges": "07",
    "1 Sam.": "09",
    "I Sam.": "09",
    "2 Sam.": "10",
    "II Sa.": "10",
    "1 Kgs.": "11",
    "I Kgs.": "11",
    "2 Kgs.": "12",
    "II Ki.": "12",
    "1 Chr.": "13",
    "I Chr.": "13",
    "2 Chr.": "14",
    "II Ch.": "14",
    "Esther": "17",
    "Psalms": "19",
    "Eccle.": "21",
    "Isaiah": "23",
    "Daniel": "27",
    "Haggai": "37",
    "Romans": "45",
    "1 Cor.": "46",
    "I Cor.": "46",
    "2 Cor.": "47",
    "II Co.": "47",
    "Ephes.": "49",
    "1Thes.": "52",
    "2Thes.": "53",
    "II Th.": "53",
    "1 Tim.": "54",
    "I Tim.": "54",
    "2 Tim.": "55",
    "II Ti.": "55",
    "1 Pet.": "60",
    "1Peter": "60",
    "I Pet.": "60",
    "2 Pet.": "61",
    "2Peter": "61",
    "II Pe.": "61",
    "II Pt.": "61",
    "1 Jhn.": "62",
    "1 John": "62",
    "I Jhn.": "62",
    "I Joh.": "62",
    "I John": "62",
    "2 Jhn.": "63",
    "2 John": "63",
    "II Jn.": "63",
    "II Jo.": "63",
    "3 Jhn.": "64",
    "3 John": "64",
    "Baruch": "70",
    "1 Esd.": "76",
    "1Esdr.": "76",
    "I Esd.": "76",
    "2 Esd.": "77",
    "2Esdr.": "77",
    "II Es.": "77",
    "EpJer.": "79",
    "Judith": "80",
    "1 Mac.": "81",
    "1Macc.": "81",
    "I Mac.": "81",
    "2 Mac.": "82",
    "2Macc.": "82",
    "II Ma.": "82",
    "3 Mac.": "83",
    "3Macc.": "83",
    "4 Mac.": "84",
    "4Macc.": "84",
    "IV Ma.": "84",
    "Sirach": "87",
    "Wisdom": "89",
    "PsSol.": "90",
    "Exod.": "02",
    "Deut.": "05",
    "Josh.": "06",
    "Jdgs.": "07",
    "Judg.": "07",
    "1 Sa.": "09",
    "1 Sm.": "09",
    "1Sam.": "09",
    "I Sa.": "09",
    "2 Sa.": "10",
    "2 Sm.": "10",
    "2Sam.": "10",
    "1 Ki.": "11",
    "1Kgs.": "11",
    "1Kin.": "11",
    "I Ki.": "11",
    "2 Ki.": "12",
    "2Kgs.": "12",
    "2Kin.": "12",
    "1 Ch.": "13",
    "1Chr.": "13",
    "I Ch.": "13",
    "2 Ch.": "14",
    "2Chr.": "14",
    "Esth.": "17",
    "Psalm": "19",
    "Pslm.": "19",
    "Prov.": "20",
    "Eccl.": "21",
    "Cant.": "22",
    "Ezek.": "26",
    "Hosea": "28",
    "Obad.": "31",
    "Jonah": "32",
    "Micah": "33",
    "Nahum": "34",
    "Zeph.": "36",
    "Zech.": "38",
    "Matt.": "40",
    "1 Co.": "46",
    "1Cor.": "46",
    "I Co.": "46",
    "2 Co.": "47",
    "2Cor.": "47",
    "Phil.": "50",
    "1 Th.": "52",
    "I Th.": "52",
    "2 Th.": "53",
    "1 Ti.": "54",
    "1Tim.": "54",
    "I Ti.": "54",
    "2 Ti.": "55",
    "2Tim.": "55",
    "Titus": "56",
    "Phlm.": "57",
    "James": "59",
    "1 Pe.": "60",
    "1 Pt.": "60",
    "1Pet.": "60",
    "I Pe.": "60",
    "I Pt.": "60",
    "2 Pe.": "61",
    "2 Pt.": "61",
    "2Pet.": "61",
    "1 Jn.": "62",
    "1Jhn.": "62",
    "1Joh.": "62",
    "1John": "62",
    "I Jn.": "62",
    "I Jo.": "62",
    "2 Jn.": "63",
    "2Jhn.": "63",
    "2Joh.": "63",
    "2John": "63",
    "3 Jn.": "64",
    "3Jhn.": "64",
    "3Joh.": "64",
    "3John": "64",
    "1Esd.": "76",
    "I Es.": "76",
    "2Esd.": "77",
    "Jdth.": "80",
    "1Mac.": "81",
    "I Ma.": "81",
    "2Mac.": "82",
    "3Mac.": "83",
    "4Mac.": "84",
    "Tobit": "88",
    "Laod.": "92",
    "Gen.": "01",
    "Exo.": "02",
    "Lev.": "03",
    "Num.": "04",
    "Jos.": "06",
    "Jsh.": "06",
    "Jdg.": "07",
    "Rth.": "08",
    "Ruth": "08",
    "1 S.": "09",
    "1Sa.": "09",
    "2 S.": "10",
    "2Sa.": "10",
    "1Ki.": "11",
    "2Ki.": "12",
    "1Ch.": "13",
    "2Ch.": "14",
    "Ezr.": "15",
    "Ezra": "15",
    "Neh.": "16",
    "Est.": "17",
    "Psa.": "19",
    "Psm.": "19",
    "Pss.": "19",
    "Pro.": "20",
    "Prv.": "20",
    "Ecc.": "21",
    "Qoh.": "21",
    "SOS.": "22",
    "Song": "22",
    "Isa.": "23",
    "Jer.": "24",
    "Lam.": "25",
    "Eze.": "26",
    "Ezk.": "26",
    "Dan.": "27",
    "Hos.": "28",
    "Joe.": "29",
    "Joel": "29",
    "Amo.": "30",
    "Amos": "30",
    "Oba.": "31",
    "Jnh.": "32",
    "Jon.": "32",
    "Mic.": "33",
    "Nah.": "34",
    "Hab.": "35",
    "Zep.": "36",
    "Hag.": "37",
    "Zec.": "38",
    "Mal.": "39",
    "Mat.": "40",
    "Mar.": "41",
    "Mark": "41",
    "Mrk.": "41",
    "Luk.": "42",
    "Luke": "42",
    "Jhn.": "43",
    "Joh.": "43",
    "John": "43",
    "Act.": "44",
    "Acts": "44",
    "Rom.": "45",
    "1Co.": "46",
    "2Co.": "47",
    "Gal.": "48",
    "Eph.": "49",
    "Php.": "50",
    "Col.": "51",
    "1Th.": "52",
    "2Th.": "53",
    "1Ti.": "54",
    "2Ti.": "55",
    "Tit.": "56",
    "Phm.": "57",
    "Heb.": "58",
    "Jam.": "59",
    "Jas.": "59",
    "1 P.": "60",
    "1Pe.": "60",
    "1Pt.": "60",
    "2 P.": "61",
    "2Pe.": "61",
    "2Pt.": "61",
    "1 J.": "62",
    "1Jn.": "62",
    "1Jo.": "62",
    "2 J.": "63",
    "2Jn.": "63",
    "2Jo.": "63",
    "3 J.": "64",
    "3Jn.": "64",
    "3Jo.": "64",
    "Jud.": "65",
    "Jude": "65",
    "Rev.": "66",
    "Bar.": "70",
    "Bel.": "73",
    "Sus.": "75",
    "1Es.": "76",
    "2Es.": "77",
    "AEs.": "78",
    "LJe.": "79",
    "Jdt.": "80",
    "Jth.": "80",
    "1Ma.": "81",
    "2Ma.": "82",
    "3Ma.": "83",
    "4Ma.": "84",
    "PMa.": "85",
    "Sir.": "87",
    "Tob.": "88",
    "Wis.": "89",
    "Ode.": "91",
    "Odes": "91",
    "Ge.": "01",
    "Gn.": "01",
    "Ex.": "02",
    "Le.": "03",
    "Lv.": "03",
    "Nb.": "04",
    "Nm.": "04",
    "Nu.": "04",
    "De.": "05",
    "Dt.": "05",
    "Jg.": "07",
    "Ru.": "08",
    "1S.": "09",
    "2S.": "10",
    "1K.": "11",
    "2K.": "12",
    "Ez.": "15",
    "Ne.": "16",
    "Es.": "17",
    "Jb.": "18",
    "Job": "18",
    "Ps.": "19",
    "Pr.": "20",
    "Ec.": "21",
    "So.": "22",
    "Is.": "23",
    "Je.": "24",
    "Jr.": "24",
    "La.": "25",
    "Da.": "27",
    "Dn.": "27",
    "Ho.": "28",
    "Jl.": "29",
    "Am.": "30",
    "Ob.": "31",
    "Mc.": "33",
    "Na.": "34",
    "Hb.": "35",
    "Zp.": "36",
    "Hg.": "37",
    "Zc.": "38",
    "Ml.": "39",
    "Mt.": "40",
    "Mk.": "41",
    "Mr.": "41",
    "Lk.": "42",
    "Jn.": "43",
    "Ac.": "44",
    "Rm.": "45",
    "Ro.": "45",
    "Ga.": "48",
    "Pp.": "50",
    "Co.": "51",
    "ti.": "56",
    "Pm.": "57",
    "Jm.": "59",
    "1P.": "60",
    "2P.": "61",
    "1J.": "62",
    "2J.": "63",
    "3J.": "64",
    "Jd.": "65",
    "Re.": "66",
    "1M.": "81",
    "2M.": "82",
    "3M.": "83",
    "4M.": "84",
    "Tb.": "88",
    "Ws.": "89",
}
for book in marvelBibleBookNo:
    updateWorkingIndicator()
    # get the string of book name
    bookString = book
    # make dot "." optional for an abbreviation
    bookString = re.sub('\.', r'[\.]*?', bookString, flags=re.M)
    # make space " " optional in some cases
    bookString = re.sub('^([0-9]+?) ', r'\1[ ]*?', bookString, flags=re.M)
    bookString = re.sub('^([I]+?) ', r'\1[ ]*?', bookString, flags=re.M)
    bookString = re.sub('^(IV) ', r'\1[ ]*?', bookString, flags=re.M)
    # get assigned book number from dictionary
    booknumber = marvelBibleBookNo[book]
    # search & replace for marking book
    newData = re.sub('('+bookString+') ([0-9])', '『'+booknumber+r'｜\1』 \2', newData)

# add first set of taggings:
updateWorkingIndicator()
newData = re.sub('『([0-9]+?)｜([^\n『』]*?)』 ([0-9]+?):([0-9]+?)([^0-9])', r'<ref onclick="bcv(\1,\3,\4)">\2 \3:\4</ref>\5', newData)
updateWorkingIndicator()
newData = re.sub('『([0-9]+?)｜([^\n『』]*?)』 ([0-9]+?)([^0-9])', r'<ref onclick="bcv(\1,\3,)">\2 \3</ref>\4', newData)

# fix references without verse numbers
# fix books with chapter 1 ONLY; oneChapterBook = [31,57,63,64,65,72,73,75,79,85]
updateWorkingIndicator()
newData = re.sub('<ref onclick="bcv\((31|57|63|64|65|72|73|75|79|85),([0-9]+?),\)">', r'<ref onclick="bcv(\1,1,\2)">', newData)
# fix references of chapters without verse number; assign verse number 1 in taggings
updateWorkingIndicator()
newData = re.sub('<ref onclick="bcv\(([0-9]+?),([0-9]+?),\)">', r'<ref onclick="bcv(\1,\2,1)">＊', newData)

# check if verses following tagged references, e.g. Book 1:1-2:1; 3:2-4, 5; Jude 1
p = re.compile('</ref>[,-;][ ]*?[0-9]', flags=re.M)
s = p.search(newData)
while s:
    updateWorkingIndicator()
    newData = re.sub('<ref onclick="bcv\(([0-9]+?),([0-9]+?),([0-9]+?)\)">(.*?)</ref>([,-;][ ]*?)([0-9]+?):([0-9]+?)([^0-9])', r'<ref onclick="bcv(\1,\2,\3)">\4</ref>\5<ref onclick="bcv(\1,\6,\7)">\6:\7</ref>\8', newData)
    newData = re.sub('<ref onclick="bcv\(([0-9]+?),([0-9]+?),([0-9]+?)\)">([^＊].*?)</ref>([,-;][ ]*?)([0-9]+?)([^:0-9])', r'<ref onclick="bcv(\1,\2,\3)">\4</ref>\5<ref onclick="bcv(\1,\2,\6)">\6</ref>\7', newData)
    newData = re.sub('<ref onclick="bcv\(([0-9]+?),([0-9]+?),([0-9]+?)\)">(＊.*?)</ref>([,-;][ ]*?)([0-9]+?)([^:0-9])', r'<ref onclick="bcv(\1,\2,\3)">\4</ref>\5<ref onclick="bcv(\1,\6,1)">＊\6</ref>\7', newData)
    s = p.search(newData)

# clear special markers
updateWorkingIndicator()
newData = re.sub('『[0-9]+?|([^\n『』]*?)』', r'\1', newData)
newData = re.sub('(<ref onclick="bcv\([0-9]+?,[0-9]+?,[0-9]+?\)">)＊', r'\1', newData)

# ask if standardising abbreviations and reference format
newData = standardReference(newData, input("Do you want to standardise all verse references [YES/NO]? "))

# close file
f = open(outputFile,'w')
f.write(newData)
f.close()

print("Parsing COMPLETED! Output file is saved as '"+outputFile+"'")
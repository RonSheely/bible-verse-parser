import re

inputFile = input('Enter filename here: ')
outputFile = 'output_' + inputFile

# open file
try:
    f = open(inputFile,'r')
except:
    print("File note found! Please make sure if you enter filename correctly and try again.")
    exit()
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
    "Genesis": "1",
    "Gen.": "1",
    "Ge.": "1",
    "Gn.": "1",
    "Exodus": "2",
    "Ex.": "2",
    "Exod.": "2",
    "Exo.": "2",
    "Leviticus": "3",
    "Lev.": "3",
    "Le.": "3",
    "Lv.": "3",
    "Numbers": "4",
    "Num.": "4",
    "Nu.": "4",
    "Nm.": "4",
    "Nb.": "4",
    "Deuteronomy": "5",
    "Deut.": "5",
    "De.": "5",
    "Dt.": "5",
    "Joshua": "6",
    "Josh.": "6",
    "Jos.": "6",
    "Jsh.": "6",
    "Judges": "7",
    "Judg.": "7",
    "Jdg.": "7",
    "Jg.": "7",
    "Jdgs.": "7",
    "Ruth": "8",
    "Rth.": "8",
    "Ru.": "8",
    "1 Samuel": "9",
    "1 Sam.": "9",
    "1 Sm.": "9",
    "1 Sa.": "9",
    "1 S.": "9",
    "I Sam.": "9",
    "I Sa.": "9",
    "1Sam.": "9",
    "1Sa.": "9",
    "1S.": "9",
    "1st Samuel": "9",
    "1st Sam.": "9",
    "First Samuel": "9",
    "First Sam.": "9",
    "2 Samuel": "10",
    "2 Sam.": "10",
    "2 Sm.": "10",
    "2 Sa.": "10",
    "2 S.": "10",
    "II Sam.": "10",
    "II Sa.": "10",
    "2Sam.": "10",
    "2Sa.": "10",
    "2S.": "10",
    "2nd Samuel": "10",
    "2nd Sam.": "10",
    "Second Samuel": "10",
    "Second Sam.": "10",
    "1 Kings": "11",
    "1 Kgs.": "11",
    "1 Ki.": "11",
    "1Kgs.": "11",
    "1Kin.": "11",
    "1Ki.": "11",
    "1K.": "11",
    "I Kgs.": "11",
    "I Ki.": "11",
    "1st Kings": "11",
    "1st Kgs.": "11",
    "First Kings": "11",
    "First Kgs.": "11",
    "2 Kings": "12",
    "2 Kgs.": "12",
    "2 Ki.": "12",
    "2Kgs.": "12",
    "2Kin.": "12",
    "2Ki.": "12",
    "2K.": "12",
    "II Kgs.": "12",
    "II Ki.": "12",
    "2nd Kings": "12",
    "2nd Kgs.": "12",
    "Second Kings": "12",
    "Second Kgs.": "12",
    "1 Chronicles": "13",
    "1 Chron.": "13",
    "1 Chr.": "13",
    "1 Ch.": "13",
    "1Chron.": "13",
    "1Chr.": "13",
    "1Ch.": "13",
    "I Chron.": "13",
    "I Chr.": "13",
    "I Ch.": "13",
    "1st Chronicles": "13",
    "1st Chron.": "13",
    "First Chronicles": "13",
    "First Chron.": "13",
    "2 Chronicles": "14",
    "2 Chron.": "14",
    "2 Chr.": "14",
    "2 Ch.": "14",
    "2Chron.": "14",
    "2Chr.": "14",
    "2Ch.": "14",
    "II Chron.": "14",
    "II Chr.": "14",
    "II Ch.": "14",
    "2nd Chronicles": "14",
    "2nd Chron.": "14",
    "Second Chronicles": "14",
    "Second Chron.": "14",
    "Ezra": "15",
    "Ezr.": "15",
    "Ez.": "15",
    "Nehemiah": "16",
    "Neh.": "16",
    "Ne.": "16",
    "Esther": "17",
    "Est.": "17",
    "Esth.": "17",
    "Es.": "17",
    "Job": "18",
    "Jb.": "18",
    "Psalms": "19",
    "Ps.": "19",
    "Psalm": "19",
    "Pslm.": "19",
    "Psa.": "19",
    "Psm.": "19",
    "Pss.": "19",
    "Proverbs": "20",
    "Prov.": "20",
    "Pro.": "20",
    "Prv.": "20",
    "Pr.": "20",
    "Ecclesiastes": "21",
    "Eccles.": "21",
    "Eccle.": "21",
    "Eccl.": "21",
    "Ecc.": "21",
    "Ec.": "21",
    "Qoh.": "21",
    "Song of Solomon": "22",
    "Song": "22",
    "Song of Songs": "22",
    "SOS.": "22",
    "So.": "22",
    "Canticle of Canticles": "22",
    "Canticles": "22",
    "Cant.": "22",
    "Isaiah": "23",
    "Isa.": "23",
    "Is.": "23",
    "Jeremiah": "24",
    "Jer.": "24",
    "Je.": "24",
    "Jr.": "24",
    "Lamentations": "25",
    "Lam.": "25",
    "La.": "25",
    "Ezekiel": "26",
    "Ezek.": "26",
    "Eze.": "26",
    "Ezk.": "26",
    "Daniel": "27",
    "Dan.": "27",
    "Da.": "27",
    "Dn.": "27",
    "Hosea": "28",
    "Hos.": "28",
    "Ho.": "28",
    "Joel": "29",
    "Joe.": "29",
    "Jl.": "29",
    "Amos": "30",
    "Amo.": "30",
    "Am.": "30",
    "Obadiah": "31",
    "Obad.": "31",
    "Oba.": "31",
    "Ob.": "31",
    "Jonah": "32",
    "Jnh.": "32",
    "Jon.": "32",
    "Micah": "33",
    "Mic.": "33",
    "Mc.": "33",
    "Nahum": "34",
    "Nah.": "34",
    "Na.": "34",
    "Habakkuk": "35",
    "Hab.": "35",
    "Hb.": "35",
    "Zephaniah": "36",
    "Zeph.": "36",
    "Zep.": "36",
    "Zp.": "36",
    "Haggai": "37",
    "Hag.": "37",
    "Hg.": "37",
    "Zechariah": "38",
    "Zech.": "38",
    "Zec.": "38",
    "Zc.": "38",
    "Malachi": "39",
    "Mal.": "39",
    "Ml.": "39",
    "Matthew": "40",
    "Matt.": "40",
    "Mat.": "40",
    "Mt.": "40",
    "Mark": "41",
    "Mrk.": "41",
    "Mar.": "41",
    "Mk.": "41",
    "Mr.": "41",
    "Luke": "42",
    "Luk.": "42",
    "Lk.": "42",
    "John": "43",
    "Joh.": "43",
    "Jhn.": "43",
    "Jn.": "43",
    "Acts": "44",
    "Act.": "44",
    "Ac.": "44",
    "Romans": "45",
    "Rom.": "45",
    "Ro.": "45",
    "Rm.": "45",
    "1 Corinthians": "46",
    "1 Cor.": "46",
    "1 Co.": "46",
    "I Cor.": "46",
    "I Co.": "46",
    "1Cor.": "46",
    "1Co.": "46",
    "I Corinthians": "46",
    "1Corinthians": "46",
    "1st Corinthians": "46",
    "First Corinthians": "46",
    "2 Corinthians": "47",
    "2 Cor.": "47",
    "2 Co.": "47",
    "II Cor.": "47",
    "II Co.": "47",
    "2Cor.": "47",
    "2Co.": "47",
    "II Corinthians": "47",
    "2Corinthians": "47",
    "2nd Corinthians": "47",
    "Second Corinthians": "47",
    "Galatians": "48",
    "Gal.": "48",
    "Ga.": "48",
    "Ephesians": "49",
    "Eph.": "49",
    "Ephes.": "49",
    "Philippians": "50",
    "Philip.": "50",
    "Phil.": "50",
    "Php.": "50",
    "Pp.": "50",
    "Colossians": "51",
    "Col.": "51",
    "Co.": "51",
    "1 Thessalonians": "52",
    "1 Thess.": "52",
    "1 Thes.": "52",
    "1 Th.": "52",
    "I Thessalonians": "52",
    "I Thess.": "52",
    "I Thes.": "52",
    "I Th.": "52",
    "1Thessalonians": "52",
    "1Thess.": "52",
    "1Thes.": "52",
    "1Th.": "52",
    "1st Thessalonians": "52",
    "1st Thess.": "52",
    "First Thessalonians": "52",
    "First Thess.": "52",
    "2 Thessalonians": "53",
    "2 Thess.": "53",
    "2 Thes.": "53",
    "2 Th.": "53",
    "II Thessalonians": "53",
    "II Thess.": "53",
    "II Thes.": "53",
    "II Th.": "53",
    "2Thessalonians": "53",
    "2Thess.": "53",
    "2Thes.": "53",
    "2Th.": "53",
    "2nd Thessalonians": "53",
    "2nd Thess.": "53",
    "Second Thessalonians": "53",
    "Second Thess.": "53",
    "1 Timothy": "54",
    "1 Tim.": "54",
    "1 Ti.": "54",
    "I Timothy": "54",
    "I Tim.": "54",
    "I Ti.": "54",
    "1Timothy": "54",
    "1Tim.": "54",
    "1Ti.": "54",
    "1st Timothy": "54",
    "1st Tim.": "54",
    "First Timothy": "54",
    "First Tim.": "54",
    "2 Timothy": "55",
    "2 Tim.": "55",
    "2 Ti.": "55",
    "II Timothy": "55",
    "II Tim.": "55",
    "II Ti.": "55",
    "2Timothy": "55",
    "2Tim.": "55",
    "2Ti.": "55",
    "2nd Timothy": "55",
    "2nd Tim.": "55",
    "Second Timothy": "55",
    "Second Tim.": "55",
    "Titus": "56",
    "Tit.": "56",
    "ti.": "56",
    "Philemon": "57",
    "Philem.": "57",
    "Phlm.": "57",
    "Phm.": "57",
    "Pm.": "57",
    "Hebrews": "58",
    "Heb.": "58",
    "James": "59",
    "Jam.": "59",
    "Jas.": "59",
    "Jm.": "59",
    "1 Peter": "60",
    "1 Pet.": "60",
    "1 Pe.": "60",
    "1 Pt.": "60",
    "1 P.": "60",
    "I Pet.": "60",
    "I Pt.": "60",
    "I Pe.": "60",
    "1Peter": "60",
    "1Pet.": "60",
    "1Pe.": "60",
    "1Pt.": "60",
    "1P.": "60",
    "I Peter": "60",
    "1st Peter": "60",
    "First Peter": "60",
    "2 Peter": "61",
    "2 Pet.": "61",
    "2 Pe.": "61",
    "2 Pt.": "61",
    "2 P.": "61",
    "II Peter": "61",
    "II Pet.": "61",
    "II Pt.": "61",
    "II Pe.": "61",
    "2Peter": "61",
    "2Pet.": "61",
    "2Pe.": "61",
    "2Pt.": "61",
    "2P.": "61",
    "2nd Peter": "61",
    "Second Peter": "61",
    "1 John": "62",
    "1 Jhn.": "62",
    "1 Jn.": "62",
    "1 J.": "62",
    "1John": "62",
    "1Jhn.": "62",
    "1Joh.": "62",
    "1Jn.": "62",
    "1Jo.": "62",
    "1J.": "62",
    "I John": "62",
    "I Jhn.": "62",
    "I Joh.": "62",
    "I Jn.": "62",
    "I Jo.": "62",
    "1st John": "62",
    "First John": "62",
    "2 John": "63",
    "2 Jhn.": "63",
    "2 Jn.": "63",
    "2 J.": "63",
    "2John": "63",
    "2Jhn.": "63",
    "2Joh.": "63",
    "2Jn.": "63",
    "2Jo.": "63",
    "2J.": "63",
    "II John": "63",
    "II Jhn.": "63",
    "II Joh.": "63",
    "II Jn.": "63",
    "II Jo.": "63",
    "2nd John": "63",
    "Second John": "63",
    "3 John": "64",
    "3 Jhn.": "64",
    "3 Jn.": "64",
    "3 J.": "64",
    "3John": "64",
    "3Jhn.": "64",
    "3Joh.": "64",
    "3Jn.": "64",
    "3Jo.": "64",
    "3J.": "64",
    "III John": "64",
    "III Jhn.": "64",
    "III Joh.": "64",
    "III Jn.": "64",
    "III Jo.": "64",
    "3rd John": "64",
    "Third John": "64",
    "Jude": "65",
    "Jud.": "65",
    "Jd.": "65",
    "Revelation": "66",
    "Rev.": "66",
    "Re.": "66",
    "The Revelation": "66",
    "Revelation to John": "66",
    "Apocalypse of John": "66",
    "Baruch": "70",
    "Bar.": "70",
    "Additions to Daniel": "71",
    "Add. Dan.": "71",
    "AddDan.": "71",
    "Prayer of Azariah": "72",
    "Azariah": "72",
    "Pr. Azar.": "72",
    "PrAzar.": "72",
    "Pr. Az.": "72",
    "Song of Three Youths": "72",
    "Sg. Three": "72",
    "Sg. of 3 Childr.": "72",
    "Song of Three": "72",
    "Song of Thr.": "72",
    "Song Thr.": "72",
    "The Song of Three Youths": "72",
    "The Song of the Three Holy Children": "72",
    "Song of the Three Holy Children": "72",
    "Song of Three Children": "72",
    "The Song of Three Jews": "72",
    "Song of Three Jews": "72",
    "Bel and the Dragon": "73",
    "Bel and Dr.": "73",
    "Bel.": "73",
    "Susanna": "75",
    "Sus.": "75",
    "1 Esdras": "76",
    "1 Esd.": "76",
    "1 Esdr.": "76",
    "1Esdras.": "76",
    "1Esdr.": "76",
    "1Esd.": "76",
    "1Es.": "76",
    "I Esdras": "76",
    "I Esdr.": "76",
    "I Esd.": "76",
    "I Es.": "76",
    "1st Esdras": "76",
    "First Esdras": "76",
    "2 Esdras": "77",
    "2 Esd.": "77",
    "2 Esdr.": "77",
    "2Esdras": "77",
    "2Esdr.": "77",
    "2Esd.": "77",
    "2Es.": "77",
    "II Esdras": "77",
    "II Esdr.": "77",
    "II Esd.": "77",
    "II Es.": "77",
    "2nd Esdras": "77",
    "Second Esdras": "77",
    "Additions to Esther": "78",
    "Add. Esth.": "78",
    "Add. Es.": "78",
    "Rest of Esther": "78",
    "The Rest of Esther": "78",
    "AEs.": "78",
    "AddEsth.": "78",
    "Letter of Jeremiah": "79",
    "Ep. Jer.": "79",
    "Let. Jer.": "79",
    "Ltr. Jer.": "79",
    "LJe.": "79",
    "EpJer.": "79",
    "Judith": "80",
    "Jth.": "80",
    "Jdth.": "80",
    "Jdt.": "80",
    "1 Maccabees": "81",
    "1 Macc.": "81",
    "1 Mac.": "81",
    "1Maccabees": "81",
    "1Macc.": "81",
    "1Mac.": "81",
    "1Ma.": "81",
    "1M.": "81",
    "I Maccabees": "81",
    "I Macc.": "81",
    "I Mac.": "81",
    "I Ma.": "81",
    "1st Maccabees": "81",
    "First Maccabees": "81",
    "2 Maccabees": "82",
    "2 Macc.": "82",
    "2 Mac.": "82",
    "2Maccabees": "82",
    "2Macc.": "82",
    "2Mac.": "82",
    "2Ma.": "82",
    "2M.": "82",
    "II Maccabees": "82",
    "II Macc.": "82",
    "II Mac.": "82",
    "II Ma.": "82",
    "2nd Maccabees": "82",
    "Second Maccabees": "82",
    "3 Maccabees": "83",
    "3 Macc.": "83",
    "3 Mac.": "83",
    "3Maccabees": "83",
    "3Macc.": "83",
    "3Mac.": "83",
    "3Ma.": "83",
    "3M.": "83",
    "III Maccabees": "83",
    "III Macc.": "83",
    "III Mac.": "83",
    "III Ma.": "83",
    "3rd Maccabees": "83",
    "Third Maccabees": "83",
    "4 Maccabees": "84",
    "4 Macc.": "84",
    "4 Mac.": "84",
    "4Maccabees": "84",
    "4Macc.": "84",
    "4Mac.": "84",
    "4Ma.": "84",
    "4M.": "84",
    "IV Maccabees": "84",
    "IV Macc.": "84",
    "IV Mac.": "84",
    "IV Ma.": "84",
    "4th Maccabees": "84",
    "Fourth Maccabees": "84",
    "Prayer of Manasseh": "85",
    "Pr. of Man.": "85",
    "PMa.": "85",
    "Prayer of Manasses": "85",
    "Pr. Man": "85",
    "Additional Psalm": "86",
    "Add. Psalm": "86",
    "Add. Ps.": "86",
    "Sirach": "87",
    "Sir.": "87",
    "Ecclesiasticus": "87",
    "Ecclus.": "87",
    "Tobit": "88",
    "Tob.": "88",
    "Tb.": "88",
    "Wisdom of Solomon": "89",
    "Wisd. of Sol.": "89",
    "Wisdom": "89",
    "Wis.": "89",
    "Ws.": "89",
    "Psalms of Solomon": "90",
    "Ps. Solomon": "90",
    "Ps. Sol.": "90",
    "Psalms Solomon": "90",
    "PsSol.": "90",
    "PssSol.": "90",
    "Odes": "91",
    "Ode.": "91",
    "Epistle to the Laodiceans": "92",
    "Ep. Lao.": "92",
    "Epistle to Laodiceans": "92",
    "Epistle Laodiceans": "92",
    "Epist. Laodiceans": "92",
    "Ep. Laod.": "92",
    "Laodiceans": "92",
    "Laod.": "92",
}

# sort dictionary by alphabet of keys
updateWorkingIndicator()
marvelBibleBookNoTemp = {}
for book in sorted(marvelBibleBookNo.keys()) :
    marvelBibleBookNoTemp[book] = marvelBibleBookNo[book]

# sort dictionary by length of keys
updateWorkingIndicator()
marvelBibleBookNo = {}
for book in sorted(marvelBibleBookNoTemp, key=len, reverse=True):
    marvelBibleBookNo[book] = marvelBibleBookNoTemp[book]

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
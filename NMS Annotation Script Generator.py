import xml.etree.ElementTree as ET

#Your Language Localisation Table, e.g.
#"NMS_LOC1_ENGLISH.exml"
loc = ET.parse("sample.exml")
#Your Update3 Language Localisation Table, e.g.
#"NMS_UPDATE3_ENGLISH.exml"
loc2 = ET.parse("sample2.exml")
#TechTable, e.g. NMS_REALITY_GCTECHNOLOGYTABLE.exml
tech = ET.parse("techsample.exml")
#ProductTable, e.g. NMS_REALITY_GCPRODUCTTABLE.exml
prod = ET.parse("prodsample.exml")
#SubstanceTable, e.g. NMS_REALITY_GCSUBSTANCETABLE.exml
sub = ET.parse("subsample.exml")
locscan = loc.getroot()
loc2scan = loc2.getroot()
techscan = tech.getroot()
prodscan = prod.getroot()
subscan = sub.getroot()

TechN = []
TechNL = []
TechChrgReso = []
TechReqReso = []
for gentech in techscan.findall(".//Property[@value='GcTechnology.xml']"):
    for N in gentech.findall(".//Property/[@name='Name']"):
        TechN.append(N.get('value'))
        #TechSet = set(TechN)
    for NL in gentech.findall(".//Property/[@name='NameLower']"):
        TechNL.append(NL.get('value'))
        #TechSet = set(TechN)
    for techchrg in gentech.findall('.//Property[@name="ChargeBy"]'):
        for chrgreso in techchrg.findall('.//Property[@name="Value"]'):
            TechChrgReso.append(chrgreso.get('value'))
            #TechChrgSet = set(TechChrgReso)
    for techreq in gentech.findall('.//Property[@name="Requirements"]'):
        for reqreso in techreq.findall('.//Property[@name="ID"]'):
            TechReqReso.append(reqreso.get('value'))
            #TechReqSet = set(TechReqReso)

#print(TechN)
#print(TechNL)
#print(TechChrgReso)
#print(TechReqReso)

ProdN = []
ProdNL = []
ProdID = []
ProdReqReso = []
for genprod in prodscan.findall(".//Property[@value='GcProductData.xml']"):
    for N in genprod.findall(".//Property/[@name='Name']"):
        ProdN.append(N.get('value'))
        #ProdSet = set(ProdN)
    for NL in genprod.findall(".//Property/[@name='NameLower']"):
        ProdNL.append(NL.get('value'))
        #ProdSet = set(ProdN)
    for Id in genprod.findall(".//Property/[@name='Id']"):
        ProdID.append(Id.get('value'))
        #ProdIDSet = set(ProdID)
    for prodreq in genprod.findall('.//Property[@name="Requirements"]'):
        for reqreso in prodreq.findall('.//Property[@name="ID"]'):
            ProdReqReso.append(reqreso.get('value'))
            #ProdReqSet = set(ProdReqReso)

#print(ProdN)
#print(ProdNL)
#print(ProdID)
#print(ProdReqReso)

SubN = []
SubNL = []
SubID = []
for gensub in subscan.findall(".//Property[@value='GcRealitySubstanceData.xml']"):
    for N in gensub.findall(".//Property/[@name='Name']"):
        SubN.append(N.get('value'))
        #SubSet = set(SubN)
        #print(SubNL)
    for NL in gensub.findall(".//Property/[@name='NameLower']"):
        SubNL.append(NL.get('value'))
        #SubSet = set(SubN)
        #print(SubNL)
    for ID in gensub.findall(".//Property/[@name='ID']"):
        SubID.append(ID.get('value'))
        #SubIDSet = set(SubID)

#print(SubN)
#print(SubID)

TechIDGet = []
ProdIDGet = []
SubIDGet = []

TechLIDGet = []
ProdLIDGet = []
SubLIDGet = []
for gentechn2 in locscan.findall(".//Property/[@value='TkLocalisationEntry.xml']"):
    if gentechn2.find(".//Property/[@name='Id']").get('value') in TechN:
        TechIDGet.append(gentechn2.find(".//Property/[@name='Id']").get('value'))
    if gentechn2.find(".//Property/[@name='Id']").get('value') in ProdN:
        ProdIDGet.append(gentechn2.find(".//Property/[@name='Id']").get('value'))
    if gentechn2.find(".//Property/[@name='Id']").get('value') in SubN:
        SubIDGet.append(gentechn2.find(".//Property/[@name='Id']").get('value'))
    # LowerCase Funk
    if gentechn2.find(".//Property/[@name='Id']").get('value') in TechNL:
        TechLIDGet.append(gentechn2.find(".//Property/[@name='Id']").get('value'))
    if gentechn2.find(".//Property/[@name='Id']").get('value') in ProdNL:
        ProdLIDGet.append(gentechn2.find(".//Property/[@name='Id']").get('value'))
    if gentechn2.find(".//Property/[@name='Id']").get('value') in SubNL:
        SubLIDGet.append(gentechn2.find(".//Property/[@name='Id']").get('value'))

#print(TechIDGet)
#print(ProdIDGet)
#print(SubIDGet)

TechID2Get = []
ProdID2Get = []
SubID2Get = []

TechLID2Get = []
ProdLID2Get = []
SubLID2Get = []
for gentechn2 in loc2scan.findall(".//Property/[@value='TkLocalisationEntry.xml']"):
    if gentechn2.find(".//Property/[@name='Id']").get('value') in TechN:
        TechID2Get.append(gentechn2.find(".//Property/[@name='Id']").get('value'))
    if gentechn2.find(".//Property/[@name='Id']").get('value') in ProdN:
        ProdID2Get.append(gentechn2.find(".//Property/[@name='Id']").get('value'))
    if gentechn2.find(".//Property/[@name='Id']").get('value') in SubN:
        SubID2Get.append(gentechn2.find(".//Property/[@name='Id']").get('value'))
    # LowerCase Funk
    if gentechn2.find(".//Property/[@name='Id']").get('value') in TechNL:
        TechLID2Get.append(gentechn2.find(".//Property/[@name='Id']").get('value'))
    if gentechn2.find(".//Property/[@name='Id']").get('value') in ProdNL:
        ProdLID2Get.append(gentechn2.find(".//Property/[@name='Id']").get('value'))
    if gentechn2.find(".//Property/[@name='Id']").get('value') in SubNL:
        SubLID2Get.append(gentechn2.find(".//Property/[@name='Id']").get('value'))

#print(TechID2Get)
#print(ProdID2Get)
#print(SubID2Get)

FullTechID = []
FullTechID.extend(TechIDGet)
FullTechID.extend(TechID2Get)

FullProdID = []
FullProdID.extend(ProdIDGet)
FullProdID.extend(ProdID2Get)

FullSubID = []
FullSubID.extend(SubIDGet)
FullSubID.extend(SubID2Get)

#print(FullTechID)
#print(FullProdID)
#print(FullSubID)

FullLTechID = []
FullLTechID.extend(TechLIDGet)
FullLTechID.extend(TechLID2Get)

FullLProdID = []
FullLProdID.extend(ProdLIDGet)
FullLProdID.extend(ProdLID2Get)

FullLSubID = []
FullLSubID.extend(SubLIDGet)
FullLSubID.extend(SubLID2Get)

#print(FullLTechID)
#print(FullLProdID)
#print(FullLSubID)

TechTranslGet = []
ProdTranslGet = []
SubTranslGet = []

TechLTranslGet = []
ProdLTranslGet = []
SubLTranslGet = []
for gentechn2 in locscan.findall(".//Property/[@value='TkLocalisationEntry.xml']"):
    if gentechn2.find(".//Property/[@name='Id']").get('value') in TechN:
        TechTranslGet.append(gentechn2.find(".//Property/[@name='Value']").get('value'))
    if gentechn2.find(".//Property/[@name='Id']").get('value') in ProdN:
        ProdTranslGet.append(gentechn2.find(".//Property/[@name='Value']").get('value'))
    if gentechn2.find(".//Property/[@name='Id']").get('value') in SubN:
        SubTranslGet.append(gentechn2.find(".//Property/[@name='Value']").get('value'))
    # LowerCase Funk
    if gentechn2.find(".//Property/[@name='Id']").get('value') in TechNL:
        TechLTranslGet.append(gentechn2.find(".//Property/[@name='Value']").get('value'))
    if gentechn2.find(".//Property/[@name='Id']").get('value') in ProdNL:
        ProdLTranslGet.append(gentechn2.find(".//Property/[@name='Value']").get('value'))
    if gentechn2.find(".//Property/[@name='Id']").get('value') in SubNL:
        SubLTranslGet.append(gentechn2.find(".//Property/[@name='Value']").get('value'))

#print(TechTranslGet)
#print(ProdTranslGet)
#print(SubTranslGet)

TechTransl2Get = []
ProdTransl2Get = []
SubTransl2Get = []

TechLTransl2Get = []
ProdLTransl2Get = []
SubLTransl2Get = []
for gentechn2 in loc2scan.findall(".//Property/[@value='TkLocalisationEntry.xml']"):
    if gentechn2.find(".//Property/[@name='Id']").get('value') in TechN:
        TechTransl2Get.append(gentechn2.find(".//Property/[@name='Value']").get('value'))
    if gentechn2.find(".//Property/[@name='Id']").get('value') in ProdN:
        ProdTransl2Get.append(gentechn2.find(".//Property/[@name='Value']").get('value'))
    if gentechn2.find(".//Property/[@name='Id']").get('value') in SubN:
        SubTransl2Get.append(gentechn2.find(".//Property/[@name='Value']").get('value'))
    # LowerCase Funk
    if gentechn2.find(".//Property/[@name='Id']").get('value') in TechNL:
        TechLTransl2Get.append(gentechn2.find(".//Property/[@name='Value']").get('value'))
    if gentechn2.find(".//Property/[@name='Id']").get('value') in ProdNL:
        ProdLTransl2Get.append(gentechn2.find(".//Property/[@name='Value']").get('value'))
    if gentechn2.find(".//Property/[@name='Id']").get('value') in SubNL:
        SubLTransl2Get.append(gentechn2.find(".//Property/[@name='Value']").get('value'))

#print(TechTransl2Get)
#print(ProdTransl2Get)
#print(SubTransl2Get)

FullTechTransl = []
FullTechTransl.extend(TechTranslGet)
FullTechTransl.extend(TechTransl2Get)

FullProdTransl = []
FullProdTransl.extend(ProdTranslGet)
FullProdTransl.extend(ProdTransl2Get)

FullSubTransl = []
FullSubTransl.extend(SubTranslGet)
FullSubTransl.extend(SubTransl2Get)

#print(FullTechTransl)
#print(FullProdTransl)
#print(FullSubTransl)

FullLTechTransl = []
FullLTechTransl.extend(TechLTranslGet)
FullLTechTransl.extend(TechLTransl2Get)

FullLProdTransl = []
FullLProdTransl.extend(ProdLTranslGet)
FullLProdTransl.extend(ProdLTransl2Get)

FullLSubTransl = []
FullLSubTransl.extend(SubLTranslGet)
FullLSubTransl.extend(SubLTransl2Get)

#print(FullLTechTransl)
#print(FullLProdTransl)
#print(FullLSubTransl)

KeepCount = []
for x in range(1, 500):
    z = str(x)
    KeepCount.append(z)

with open('Tech Annotation Script.py', 'w') as tcs:
    tcs.write("import xml.etree.ElementTree as ET\n\n"
              "#Reminder! Change what's in ET.parse(' ') to the appropriate filename\n"
              "#to run this script!\n\n"
              "tree = ET.parse('techsample.exml')\n"
              "root = tree.getroot()\n\n"
              "for gentech in root.findall(\".//Property[@value='GcTechnology.xml']\"):\n")
    for h, g, e in zip(KeepCount, FullLTechID, FullLTechTransl):
        technamesl =("  for techNL{0} in gentech.findall('./Property[@name=\"NameLower\"][@value=\"{1}\"]'):\n"
                    "      check = ET.tostring(techNL{0})\n"
                    "      print(check)\n"
                    "      tech{0}nm = ET.Comment(' {2} ')\n"
                    "      techNL{0}.append(tech{0}nm)\n\n".format(h, g, e))
        #print(technamesl)
        tcs.write(technamesl)
    for i, j, k in zip(KeepCount, FullTechID, FullTechTransl):
        technamesc =("  for techN{0} in gentech.findall('./Property[@name=\"Name\"][@value=\"{1}\"]'):\n"
                    "      check = ET.tostring(techN{0})\n"
                    "      print(check)\n"
                    "      tech{0}nm = ET.Comment(' {2} ')\n"
                    "      techN{0}.append(tech{0}nm)\n\n".format(i, j, k))
        #print(technamesc)
        tcs.write(technamesc)
    tcs.write("tree.write('Annotated Tech Table.xml')")
    
with open('Prod Annotation Script.py', 'w') as pcs:
    pcs.write("import xml.etree.ElementTree as ET\n\n"
              "#Reminder! Change what's in ET.parse(' ') to the appropriate filename\n"
              "#to run this script!\n\n"
              "tree = ET.parse('prodsample.exml')\n"
              "root = tree.getroot()\n\n"
              "#Heads up! This won't run properly until you add '\\' to\n"
              "#Vy'keen Dagger, Effigy, & Dawn's End below! E.g. Vy\\'keen\n\n"
              "for genprod in root.findall(\".//Property[@value='GcProductData.xml']\"):\n")

    for c, n, q in zip(KeepCount, FullLProdID, FullLProdTransl):
        prodnamesl = ("  for prodNL{0} in genprod.findall('.//Property[@value=\"{1}\"]'):\n"
                     "      check = ET.tostring(prodNL{0})\n"
                     "      print(check)\n"
                     "      prod{0}nm = ET.Comment('  {2}  ')\n"
                     "      prodNL{0}.append(prod{0}nm)\n\n".format(c, n, q))
        #print(prodnamesl)
        pcs.write(prodnamesl)
    for d, o, r in zip(KeepCount, FullProdID, FullProdTransl):
        prodnamesc = ("  for prodN{0} in genprod.findall('.//Property[@value=\"{1}\"]'):\n"
                     "      check = ET.tostring(prodN{0})\n"
                     "      print(check)\n"
                     "      prod{0}nm = ET.Comment('  {2}  ')\n"
                     "      prodN{0}.append(prod{0}nm)\n\n".format(d, o, r))
        #print(prodnamesc)
        pcs.write(prodnamesc)
    pcs.write("tree.write('Annotated Product Table.xml')")

with open('Sub Annotation Script.py', 'w') as scs:
    scs.write("import xml.etree.ElementTree as ET\n\n"
              "#Reminder! Change what's in ET.parse(' ') to the appropriate filename\n"
              "#to run this script!\n\n"
              "tree = ET.parse('subsample.exml')\n"
              "root = tree.getroot()\n\n"
              "for gensub in root.findall(\".//Property[@value='GcRealitySubstanceData.xml']\"):\n")

    for b, m, p in zip(KeepCount, FullLSubID, FullLSubTransl):
        subnamesl = ("  for subNL{0} in gensub.findall('.//Property[@value=\"{1}\"]'):\n"
                     "      check = ET.tostring(subNL{0})\n"
                     "      print(check)\n"
                     "      sub{0}nm = ET.Comment('  {2}  ')\n"
                     "      subNL{0}.append(sub{0}nm)\n\n".format(b, m, p))
        #print(subnamesl)
        scs.write(subnamesl)
    for a, l, u in zip(KeepCount, FullSubID, FullSubTransl):
        subnamesc = ("  for subN{0} in gensub.findall('.//Property[@value=\"{1}\"]'):\n"
                     "      check = ET.tostring(subN{0})\n"
                     "      print(check)\n"
                     "      sub{0}nm = ET.Comment('  {2}  ')\n"
                     "      subN{0}.append(sub{0}nm)\n\n".format(a, l, u))
        #print(subnamesc)
        scs.write(subnamesc)
    scs.write("tree.write('Annotated Substance Table.xml')")

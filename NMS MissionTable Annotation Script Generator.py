import xml.etree.ElementTree as ET

#Your Language Localisation Table, e.g.
#"NMS_LOC1_ENGLISH.exml"
loc = ET.parse("sample.exml")
#Your Update3 Language Localisation Table, e.g.
#"NMS_UPDATE3_ENGLISH.exml"
loc2 = ET.parse("sample2.exml")

'''CMT, e.g. COREMISSIONTABLE.exml, but also: ATLASPATHTABLE.exml,
MISSIONTABLE.exml, NPCMISSIONTABLE.exml, TUTORIALMISSIONTABLE.exml, &
WIKIMISSIONTABLE.exml

Make sure to jump to the bottom & change output filename, so it's named
appropriately, e.g. NPCMissionTable Annotation Script.

Similarly ensure it's pathed properly to parse the relevant table.'''
cmt = ET.parse("TMTSample.exml")
locscan = loc.getroot()
loc2scan = loc2.getroot()
cmtscan = cmt.getroot()

TextA = []
TextOpt = []
TextRes = []
for gentech in cmtscan.findall(".//Property[@value='GcAlienPuzzleEntry.xml']"):
    for TA in gentech.findall(".//Property/[@name='TextAlien']"):
        TextA.append(TA.get('value'))
    for TO in gentech.findall(".//Property/[@name='Name']"):
        TextOpt.append(TO.get('value'))
    for TR in gentech.findall('.//Property[@name="Text"]'):
        TextRes.append(TR.get('value'))

#print(TextA)
#print(TextOpt)
#print(TextRes)

Msg = []
OSTMsg = []
ObjID = []
ObjTID = []
for gentech2 in cmtscan.findall(".//Property[@name='NotificationSequence']"):
    for M in gentech2.findall(".//Property/[@name='Message']"):
        Msg.append(M.get('value'))
        #TechSet = set(TechN)
    for OM in gentech2.findall(".//Property/[@name='OSTMessage']"):
        OSTMsg.append(OM.get('value'))
        #TechSet = set(TechN)
    for O in gentech2.findall('.//Property[@name="ObjectiveID"]'):
        ObjID.append(O.get('value'))
    for OT in gentech2.findall('.//Property[@name="ObjectiveTipID"]'):
        ObjTID.append(OT.get('value'))

#print(Msg)
#print(OSTMsg)
#print(ObjID)
#print(ObjTID)
        
OSDMsg = []
for gentech2 in cmtscan.findall(".//Property[@name='ScanEvents']"):
    for OSM in gentech2.findall(".//Property/[@name='OSDMessage']"):
        OSDMsg.append(OSM.get('value'))

#print(OSDMsg)

MTitle = []
MSTitle = []
MDesc = []
for gentech2 in cmtscan.findall(".//Property[@value='GcGenericMissionSequence.xml']"):
    for MTS in gentech2.findall(".//Property[@name='MissionTitles']"):
        for MT in MTS.findall(".//Property[@name='Format']"):
            MTitle.append(MT.get('value'))
    for MSTS in gentech2.findall(".//Property[@name='MissionSubtitles']"):
        for MST in MSTS.findall(".//Property[@name='Format']"):
            MSTitle.append(MST.get('value'))
    for MDS in gentech2.findall(".//Property[@name='MissionDescriptions']"):
        for MD in MDS.findall(".//Property[@name='Format']"):
            MDesc.append(MD.get('value'))

#print(MTitle)
#print(MSTitle)
#print(MDesc)

TextAGet = []

TextOptGet = []
TextResGet = []

MsgGet = []
OSTMsgGet = []
ObjIDGet = []
ObjTIDGet = []

OSDMsgGet = []

MTitleGet = []
MSTitleGet = []
MDescGet = []
for gentechn2 in locscan.findall(".//Property/[@value='TkLocalisationEntry.xml']"):
    if gentechn2.find(".//Property/[@name='Id']").get('value') in TextA:
        TextAGet.append(gentechn2.find(".//Property/[@name='Id']").get('value'))
    # TextOpt/Res Funk
    if gentechn2.find(".//Property/[@name='Id']").get('value') in TextOpt:
        TextOptGet.append(gentechn2.find(".//Property/[@name='Id']").get('value'))
    if gentechn2.find(".//Property/[@name='Id']").get('value') in TextRes:
        TextResGet.append(gentechn2.find(".//Property/[@name='Id']").get('value'))
    # Msg/OSTMsg/ObjID/ObjTID Funk
    if gentechn2.find(".//Property/[@name='Id']").get('value') in Msg:
        MsgGet.append(gentechn2.find(".//Property/[@name='Id']").get('value'))
    if gentechn2.find(".//Property/[@name='Id']").get('value') in OSTMsg:
        OSTMsgGet.append(gentechn2.find(".//Property/[@name='Id']").get('value'))
    if gentechn2.find(".//Property/[@name='Id']").get('value') in ObjID:
        ObjIDGet.append(gentechn2.find(".//Property/[@name='Id']").get('value'))
    if gentechn2.find(".//Property/[@name='Id']").get('value') in ObjTID:
        ObjTIDGet.append(gentechn2.find(".//Property/[@name='Id']").get('value'))
    # ScanEvent OSDMsg Funk
    if gentechn2.find(".//Property/[@name='Id']").get('value') in OSDMsg:
        OSDMsgGet.append(gentechn2.find(".//Property/[@name='Id']").get('value'))
    # MissionTitles/Subtitles/Descriptions Funk
    if gentechn2.find(".//Property/[@name='Id']").get('value') in MTitle:
        MTitleGet.append(gentechn2.find(".//Property/[@name='Id']").get('value'))
    if gentechn2.find(".//Property/[@name='Id']").get('value') in MSTitle:
        MSTitleGet.append(gentechn2.find(".//Property/[@name='Id']").get('value'))
    if gentechn2.find(".//Property/[@name='Id']").get('value') in MDesc:
        MDescGet.append(gentechn2.find(".//Property/[@name='Id']").get('value'))
    
#print(TextAGet)
#print(TextOptGet)
#print(TextResGet)

#print(MsgGet)
#print(OSTMsgGet)
#print(ObjIDGet)
#print(ObjTIDGet)

#print(OSDMsgGet)
#print(MTitleGet)
#print(MSTitleGet)
#print(MDescGet)

TextA2Get = []

TextOpt2Get = []
TextRes2Get = []

Msg2Get = []
OSTMsg2Get = []
ObjID2Get = []
ObjTID2Get = []

OSDMsg2Get = []

MTitle2Get = []
MSTitle2Get = []
MDesc2Get = []
for gentechn2 in loc2scan.findall(".//Property/[@value='TkLocalisationEntry.xml']"):
    if gentechn2.find(".//Property/[@name='Id']").get('value') in TextA:
        TextA2Get.append(gentechn2.find(".//Property/[@name='Id']").get('value'))
    # TextOpt/Res Funk
    if gentechn2.find(".//Property/[@name='Id']").get('value') in TextOpt:
        TextOpt2Get.append(gentechn2.find(".//Property/[@name='Id']").get('value'))
    if gentechn2.find(".//Property/[@name='Id']").get('value') in TextRes:
        TextRes2Get.append(gentechn2.find(".//Property/[@name='Id']").get('value'))
    # Msg/OSTMsg/ObjID/ObjTID Funk
    if gentechn2.find(".//Property/[@name='Id']").get('value') in Msg:
        Msg2Get.append(gentechn2.find(".//Property/[@name='Id']").get('value'))
    if gentechn2.find(".//Property/[@name='Id']").get('value') in OSTMsg:
        OSTMsg2Get.append(gentechn2.find(".//Property/[@name='Id']").get('value'))
    if gentechn2.find(".//Property/[@name='Id']").get('value') in ObjID:
        ObjID2Get.append(gentechn2.find(".//Property/[@name='Id']").get('value'))
    if gentechn2.find(".//Property/[@name='Id']").get('value') in ObjTID:
        ObjTID2Get.append(gentechn2.find(".//Property/[@name='Id']").get('value'))
    # ScanEvent OSDMsg Funk
    if gentechn2.find(".//Property/[@name='Id']").get('value') in OSDMsg:
        OSDMsg2Get.append(gentechn2.find(".//Property/[@name='Id']").get('value'))
    # MissionTitles/Subtitles/Descriptions Funk
    if gentechn2.find(".//Property/[@name='Id']").get('value') in MTitle:
        MTitleGet.append(gentechn2.find(".//Property/[@name='Id']").get('value'))
    if gentechn2.find(".//Property/[@name='Id']").get('value') in MSTitle:
        MSTitle2Get.append(gentechn2.find(".//Property/[@name='Id']").get('value'))
    if gentechn2.find(".//Property/[@name='Id']").get('value') in MDesc:
        MDesc2Get.append(gentechn2.find(".//Property/[@name='Id']").get('value'))

#print(TextA2Get)
#print(TextOpt2Get)
#print(TextRes2Get)

#print(Msg2Get)
#print(OSTMsg2Get)
#print(ObjID2Get)
#print(ObjTID2Get)

#print(OSDMsg2Get)
#print(MTitle2Get)
#print(MSTitle2Get)
#print(MDesc2Get)
        
FullTextA = []
FullTextA.extend(TextAGet)
FullTextA.extend(TextA2Get)

FullTextOpt = []
FullTextOpt.extend(TextOptGet)
FullTextOpt.extend(TextOpt2Get)

FullTextRes = []
FullTextRes.extend(TextResGet)
FullTextRes.extend(TextRes2Get)

FullMsg = []
FullMsg.extend(MsgGet)
FullMsg.extend(Msg2Get)

FullOSTMsg = []
FullOSTMsg.extend(OSTMsgGet)
FullOSTMsg.extend(OSTMsg2Get)

FullObjID = []
FullObjID.extend(ObjIDGet)
FullObjID.extend(ObjID2Get)

FullObjTID = []
FullObjTID.extend(ObjTIDGet)
FullObjTID.extend(ObjTID2Get)

FullOSDMsg = []
FullOSDMsg.extend(OSDMsgGet)
FullOSDMsg.extend(OSDMsg2Get)

FullMTitle = []
FullMTitle.extend(MTitleGet)
FullMTitle.extend(MTitle2Get)

FullMSTitle = []
FullMSTitle.extend(MSTitleGet)
FullMSTitle.extend(MSTitle2Get)

FullMDesc = []
FullMDesc.extend(MDescGet)
FullMDesc.extend(MDesc2Get)

#print(FullTextA)
#print(FullTextOpt)
#print(FullTextRes)
#print(FullMsg)

#print(FullOSTMsg)
#print(FullObjID)
#print(FullObjTID)

#print(FullOSDMsg)
#print(FullMTitle)
#print(FullMSTitle)
#print(FullMDesc)

TextATranslGet = []

TextOptTranslGet = []
TextResTranslGet = []

MsgTranslGet = []
OSTMsgTranslGet = []
ObjIDTranslGet = []
ObjTIDTranslGet = []

OSDMsgTranslGet = []

MTitleTranslGet = []
MSTitleTranslGet = []
MDescTranslGet = []
for gentechn2 in locscan.findall(".//Property/[@value='TkLocalisationEntry.xml']"):
    if gentechn2.find(".//Property/[@name='Id']").get('value') in TextA:
        TextATranslGet.append(gentechn2.find(".//Property/[@name='Value']").get('value'))
    # TextOpt/Res Funk
    if gentechn2.find(".//Property/[@name='Id']").get('value') in TextOpt:
        TextOptTranslGet.append(gentechn2.find(".//Property/[@name='Value']").get('value'))
    if gentechn2.find(".//Property/[@name='Id']").get('value') in TextRes:
        TextResTranslGet.append(gentechn2.find(".//Property/[@name='Value']").get('value'))
    # Msg/OSTMsg/ObjID/ObjTID Funk
    if gentechn2.find(".//Property/[@name='Id']").get('value') in Msg:
        MsgTranslGet.append(gentechn2.find(".//Property/[@name='Value']").get('value'))
    if gentechn2.find(".//Property/[@name='Id']").get('value') in OSTMsg:
        OSTMsgTranslGet.append(gentechn2.find(".//Property/[@name='Value']").get('value'))
    if gentechn2.find(".//Property/[@name='Id']").get('value') in ObjID:
        ObjIDTranslGet.append(gentechn2.find(".//Property/[@name='Value']").get('value'))
    if gentechn2.find(".//Property/[@name='Id']").get('value') in ObjTID:
        ObjTIDTranslGet.append(gentechn2.find(".//Property/[@name='Value']").get('value'))
    # ScanEvent OSDMsg Funk
    if gentechn2.find(".//Property/[@name='Id']").get('value') in OSDMsg:
        OSDMsgTranslGet.append(gentechn2.find(".//Property/[@name='Value']").get('value'))
    # MissionTitles/Subtitles/Descriptions Funk
    if gentechn2.find(".//Property/[@name='Id']").get('value') in MTitle:
        MTitleTranslGet.append(gentechn2.find(".//Property/[@name='Value']").get('value'))
    if gentechn2.find(".//Property/[@name='Id']").get('value') in MSTitle:
        MSTitleTranslGet.append(gentechn2.find(".//Property/[@name='Value']").get('value'))
    if gentechn2.find(".//Property/[@name='Id']").get('value') in MDesc:
        MDescTranslGet.append(gentechn2.find(".//Property/[@name='Value']").get('value'))

#print(TextATranslGet)
#print(TextOptTranslGet)
#print(TextResTranslGet)

#print(MsgTranslGet)
#print(OSTMsgTranslGet)
#print(ObjIDTranslGet)
#print(ObjTIDTranslGet)

#print(OSDMsgTranslGet)
#print(MTitleTranslGet)
#print(MSTitleTranslGet)
#print(MDescTranslGet)

TextATransl2Get = []

TextOptTransl2Get = []
TextResTransl2Get = []

MsgTransl2Get = []
OSTMsgTransl2Get = []
ObjIDTransl2Get = []
ObjTIDTransl2Get = []

OSDMsgTransl2Get = []

MTitleTransl2Get = []
MSTitleTransl2Get = []
MDescTransl2Get = []
for gentechn2 in loc2scan.findall(".//Property/[@value='TkLocalisationEntry.xml']"):
    if gentechn2.find(".//Property/[@name='Id']").get('value') in TextA:
        TextATransl2Get.append(gentechn2.find(".//Property/[@name='Value']").get('value'))
    # TextOpt/Res Funk
    if gentechn2.find(".//Property/[@name='Id']").get('value') in TextOpt:
        TextOptTransl2Get.append(gentechn2.find(".//Property/[@name='Value']").get('value'))
    if gentechn2.find(".//Property/[@name='Id']").get('value') in TextRes:
        TextResTransl2Get.append(gentechn2.find(".//Property/[@name='Value']").get('value'))
    # Msg/OSTMsg/ObjID/ObjTID Funk
    if gentechn2.find(".//Property/[@name='Id']").get('value') in Msg:
        MsgTransl2Get.append(gentechn2.find(".//Property/[@name='Value']").get('value'))
    if gentechn2.find(".//Property/[@name='Id']").get('value') in OSTMsg:
        OSTMsgTransl2Get.append(gentechn2.find(".//Property/[@name='Value']").get('value'))
    if gentechn2.find(".//Property/[@name='Id']").get('value') in ObjID:
        ObjIDTransl2Get.append(gentechn2.find(".//Property/[@name='Value']").get('value'))
    if gentechn2.find(".//Property/[@name='Id']").get('value') in ObjTID:
        ObjTIDTransl2Get.append(gentechn2.find(".//Property/[@name='Value']").get('value'))
    # ScanEvent OSDMsg Funk
    if gentechn2.find(".//Property/[@name='Id']").get('value') in OSDMsg:
        OSDMsgTransl2Get.append(gentechn2.find(".//Property/[@name='Value']").get('value'))
    # MissionTitles/Subtitles/Descriptions Funk
    if gentechn2.find(".//Property/[@name='Id']").get('value') in MTitle:
        MTitleTransl2Get.append(gentechn2.find(".//Property/[@name='Value']").get('value'))
    if gentechn2.find(".//Property/[@name='Id']").get('value') in MSTitle:
        MSTitleTransl2Get.append(gentechn2.find(".//Property/[@name='Value']").get('value'))
    if gentechn2.find(".//Property/[@name='Id']").get('value') in MDesc:
        MDescTransl2Get.append(gentechn2.find(".//Property/[@name='Value']").get('value'))

#print(TextATransl2Get)
#print(TextOptTransl2Get)
#print(TextResTransl2Get)

#print(MsgTransl2Get)
#print(OSTMsgTransl2Get)
#print(ObjIDTransl2Get)
#print(ObjTIDTransl2Get)

#print(OSDMsgTransl2Get)
#print(MTitleTransl2Get)
#print(MSTitleTransl2Get)
#print(MDescTransl2Get)

FullTextATransl = []
FullTextATransl.extend(TextATranslGet)
FullTextATransl.extend(TextATransl2Get)

#print(FullTextATransl)

FullTextOptTransl = []
FullTextOptTransl.extend(TextOptTranslGet)
FullTextOptTransl.extend(TextOptTransl2Get)

#print(FullTextOptTransl)

FullTextResTransl = []
FullTextResTransl.extend(TextResTranslGet)
FullTextResTransl.extend(TextResTransl2Get)

#print(FullTextResTransl)

FullMsgTransl = []
FullMsgTransl.extend(MsgTranslGet)
FullMsgTransl.extend(MsgTransl2Get)

#print(FullMsgTransl)

FullOSTMsgTransl = []
FullOSTMsgTransl.extend(OSTMsgTranslGet)
FullOSTMsgTransl.extend(OSTMsgTransl2Get)

#print(FullOSTMsgTransl)

FullObjIDTransl = []
FullObjIDTransl.extend(ObjIDTranslGet)
FullObjIDTransl.extend(ObjIDTransl2Get)

#print(FullObjIDTransl)

FullObjTIDTransl = []
FullObjTIDTransl.extend(ObjTIDTranslGet)
FullObjTIDTransl.extend(ObjTIDTransl2Get)

#print(FullObjTIDTransl)

FullOSDMsgTransl = []
FullOSDMsgTransl.extend(OSDMsgTranslGet)
FullOSDMsgTransl.extend(OSDMsgTransl2Get)

#print(FullOSDMsgTransl)

FullMTitleTransl = []
FullMTitleTransl.extend(MTitleTranslGet)
FullMTitleTransl.extend(MTitleTransl2Get)

#print(FullMTitleTransl)

FullMSTitleTransl = []
FullMSTitleTransl.extend(MSTitleTranslGet)
FullMSTitleTransl.extend(MSTitleTransl2Get)

#print(FullMSTitleTransl)

FullMDescTransl = []
FullMDescTransl.extend(MDescTranslGet)
FullMDescTransl.extend(MDescTransl2Get)

#print(FullMDescTransl)

KeepCount = []
for x in range(1, 9999):
    z = str(x)
    KeepCount.append(z)

with open('TutorialMissionTable Annotation Script.py', 'w') as tcs:
    tcs.write("import xml.etree.ElementTree as ET\n\n"
              "#Reminder! Change what's in ET.parse(' ') to the appropriate filename\n"
              "#to run this script!\n\n"
              "tree = ET.parse('TMTSample.exml')\n"
              "root = tree.getroot()\n\n"
              "for gentech in root.findall(\".//Property[@value='GcAlienPuzzleEntry.xml']\"):\n")
    for h, g, e in zip(KeepCount, FullTextA, FullTextATransl):
        technamesl =("  for techNL{0} in gentech.findall('./Property[@name=\"TextAlien\"][@value=\"{1}\"]'):\n"
                    "      check = ET.tostring(techNL{0})\n"
                    "      print(check)\n"
                    "      tech{0}nm = ET.Comment(''' {2} ''')\n"
                    "      techNL{0}.append(tech{0}nm)\n\n".format(h, g, e))
        #print(technamesl)
        tcs.write(technamesl)
    for o, z, v in zip(KeepCount, FullTextRes, FullTextResTransl):
        technamesl =("  for techND{0} in gentech.findall('./Property[@name=\"Text\"][@value=\"{1}\"]'):\n"
                    "      check = ET.tostring(techND{0})\n"
                    "      print(check)\n"
                    "      tech{0}nm = ET.Comment(''' {2} ''')\n"
                    "      techND{0}.append(tech{0}nm)\n\n".format(o, z, v))
        #print(technamesl)
        tcs.write(technamesl)

    tcs.write("for gentech2 in root.findall(\".//Property[@value='GcAlienPuzzleOption.xml']\"):\n")
    for i, j, k in zip(KeepCount, FullTextOpt, FullTextOptTransl):
        technamesc =("  for techN{0} in gentech2.findall('./Property[@name=\"Name\"][@value=\"{1}\"]'):\n"
                    "      check = ET.tostring(techN{0})\n"
                    "      print(check)\n"
                    "      tech{0}nm = ET.Comment(''' {2} ''')\n"
                    "      techN{0}.append(tech{0}nm)\n\n".format(i, j, k))
        #print(technamesc)
        tcs.write(technamesc)
    for c, n, q in zip(KeepCount, FullTextRes, FullTextResTransl):
        technamesc =("  for techNR{0} in gentech2.findall('./Property[@name=\"Text\"][@value=\"{1}\"]'):\n"
                    "      check = ET.tostring(techNR{0})\n"
                    "      print(check)\n"
                    "      tech{0}nm = ET.Comment(''' {2} ''')\n"
                    "      techNR{0}.append(tech{0}nm)\n\n".format(c, n, q))
        #print(technamesc)
        tcs.write(technamesc)

    tcs.write("for gentech3 in root.findall(\".//Property[@name='NotificationSequence']\"):\n")
    for d, a, r in zip(KeepCount, FullMsg, MsgTransl2Get):
        technamesc =("  for M{0} in gentech3.findall('.//Property[@name=\"Message\"][@value=\"{1}\"]'):\n"
                    "      check = ET.tostring(M{0})\n"
                    "      print(check)\n"
                    "      tech{0}nm = ET.Comment(''' {2} ''')\n"
                    "      M{0}.append(tech{0}nm)\n\n".format(d, a, r))
        #print(technamesc)
        tcs.write(technamesc)
    for b, m, p in zip(KeepCount, FullOSTMsg, OSTMsgTransl2Get):
        technamesc =("  for OM{0} in gentech3.findall('.//Property[@name=\"OSTMessage\"][@value=\"{1}\"]'):\n"
                    "      check = ET.tostring(OM{0})\n"
                    "      print(check)\n"
                    "      tech{0}nm = ET.Comment(''' {2} ''')\n"
                    "      OM{0}.append(tech{0}nm)\n\n".format(b, m, p))
        #print(technamesc)
        tcs.write(technamesc)
    for u, f, t in zip(KeepCount, FullObjID, FullObjIDTransl):
        technamesc =("  for O{0} in gentech3.findall('.//Property[@name=\"ObjectiveID\"][@value=\"{1}\"]'):\n"
                    "      check = ET.tostring(O{0})\n"
                    "      print(check)\n"
                    "      tech{0}nm = ET.Comment(\''' {2} \''')\n"
                    "      O{0}.append(tech{0}nm)\n\n".format(u, f, t))
        #print(technamesc)
        tcs.write(technamesc)
    for w, l, x in zip(KeepCount, FullObjTID, FullObjTIDTransl):
        technamesc =("  for OT{0} in gentech3.findall('.//Property[@name=\"ObjectiveTipID\"][@value=\"{1}\"]'):\n"
                    "      check = ET.tostring(OT{0})\n"
                    "      print(check)\n"
                    "      tech{0}nm = ET.Comment(''' {2} ''')\n"
                    "      OT{0}.append(tech{0}nm)\n\n".format(w, l, x))
        #print(technamesc)
        tcs.write(technamesc)

    tcs.write("for gentech4 in root.findall(\".//Property[@name='ScanEvents']\"):\n")
    for wo, li, si in zip(KeepCount, FullOSDMsg, FullOSDMsgTransl):
        technamesc =("  for OSM{0} in gentech4.findall('.//Property[@name=\"OSDMessage\"][@value=\"{1}\"]'):\n"
                    "      check = ET.tostring(OSM{0})\n"
                    "      print(check)\n"
                    "      tech{0}nm = ET.Comment(''' {2} ''')\n"
                    "      OSM{0}.append(tech{0}nm)\n\n".format(wo, li, si))
        #print(technamesc)
        tcs.write(technamesc)

    tcs.write("for gentech5 in root.findall(\".//Property[@value='GcGenericMissionSequence.xml']\"):\n")
    for om, la, su in zip(KeepCount, FullMTitle, FullMTitleTransl):
        technamesc =("  for MTS{0} in gentech5.findall('.//Property[@name=\"MissionTitles\"]'):\n"
                    "       for MT{0} in MTS{0}.findall('.//Property[@name=\"Format\"][@value=\"{1}\"]'):\n"
                    "          check = ET.tostring(MT{0})\n"
                    "          print(check)\n"
                    "          tech{0}nm = ET.Comment(''' {2} ''')\n"
                    "          MT{0}.append(tech{0}nm)\n\n".format(om, la, su))
        #print(technamesc)
        tcs.write(technamesc)
    for um, so, ta in zip(KeepCount, FullMSTitle, FullMSTitleTransl):
        technamesc =("  for MSTS{0} in gentech5.findall('.//Property[@name=\"MissionSubtitles\"]'):\n"
                    "       for MST{0} in MSTS{0}.findall('.//Property[@name=\"Format\"][@value=\"{1}\"]'):\n"
                    "          check = ET.tostring(MST{0})\n"
                    "          print(check)\n"
                    "          tech{0}nm = ET.Comment(''' {2} ''')\n"
                    "          MST{0}.append(tech{0}nm)\n\n".format(um, so, ta))
        #print(technamesc)
        tcs.write(technamesc)
    for wa, vi, za in zip(KeepCount, FullMDesc, FullMDescTransl):
        technamesc =("  for MDS{0} in gentech5.findall('.//Property[@name=\"MissionDescriptions\"]'):\n"
                    "       for MD{0} in MDS{0}.findall('.//Property[@name=\"Format\"][@value=\"{1}\"]'):\n"
                    "          check = ET.tostring(MD{0})\n"
                    "          print(check)\n"
                    "          tech{0}nm = ET.Comment(''' {2} ''')\n"
                    "          MD{0}.append(tech{0}nm)\n\n".format(wa, vi, za))
        #print(technamesc)
        tcs.write(technamesc)
    
    tcs.write("tree.write('Annotated TutorialMission Table.xml')")

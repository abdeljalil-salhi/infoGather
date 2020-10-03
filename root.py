#@abdeljalilsalhi
from tkinter import *
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
from datetime import datetime, date
from phonenumbers import carrier, timezone, geocoder
import os, requests, random, string, socket, phonenumbers, webbrowser

root = Tk(className="Info Gather @abdeljalilsalhi")
root.iconphoto(False, PhotoImage(file='icon.png'))
root.configure(bg="black")
root.resizable(width=False, height=False)

#MY IP FRAME
def myIPscan():
    res1 = requests.get("http://ip-api.com/json/")
    data1 = res1.json()
    #GET INFORMATIONS - MY IP FRAME
    global ip1, lat1, lon1, countryCode1, country1, region1, regionName1, city1, isp1, as1, zip1, org1
    ip1 = data1['query']
    lat1 = str(data1['lat'])
    lon1 = str(data1['lon'])
    countryCode1 = data1['countryCode']
    country1 = data1['country']
    region1 = data1['region']
    regionName1 = data1['regionName']
    city1 = data1['city']
    isp1 = data1['isp']
    as1 = data1['as']
    zip1 = str(data1['zip'])
    org1 = data1['org']
    #APPLY RESULTS - MY IP FRAME
    myIPreset()
    myIPentryVar.set(ip1)
    countryIPentryVar.set("[{}] {}".format(countryCode1, country1))
    regionIPentryVar.set("[{}] {}".format(region1, regionName1))
    cityIPentryVar.set(city1)
    zipIPentryVar.set(zip1)
    latitudeIPentryVar.set(lat1)
    longitudeIPentryVar.set(lon1)
    organizationIPentryVar.set(org1)
    ispIPentryVar.set(isp1)
    asIPentryVar.set(as1)
def myIPreset():
    #RESET ENTRIES - MY IP FRAME
    myIPentryVar.set('')
    countryIPentryVar.set('')
    regionIPentryVar.set('')
    cityIPentryVar.set('')
    zipIPentryVar.set('')
    latitudeIPentryVar.set('')
    longitudeIPentryVar.set('')
    organizationIPentryVar.set('')
    ispIPentryVar.set('')
    asIPentryVar.set('')
def myIPsave():
    #SAVE RESULTS - MY IP FRAME
    folder1 = filedialog.askdirectory()
    filename1 = "myIP.txt"
    file1_path = os.path.join(folder1, filename1)
    f1 = open(file1_path, 'w+')
    f1.write("IP: {} \nCountry: [{}] {}\nRegion: [{}] {}\nCity: {}\nZIP: {}\nLatitude: {}\nLongitude: {}\nOrganization: {}\nOrganization ISP: {}\nOrganization AS: {}\n"
             .format(ip1, countryCode1, country1, region1, regionName1,
                     city1, zip1, lat1, lon1, org1, isp1, as1))
    f1.close()
    messagebox.showinfo("Saved (TXT)", "Saved to: {}".format(file1_path))
    
#CUSTOM IP FRAME
def customIPscan():
    global ip2, lat2, lon2, countryCode2, country2, region2, regionName2, city2, isp2, as2, zip2, org2
    customIPvalue = customIPentryVar.get()
    res2 = requests.get("http://ip-api.com/json/" + customIPvalue)
    data2 = res2.json()
    #GET INFORMATIONS - CUSTOM IP FRAME
    ip2 = data2['query']
    lat2 = str(data2['lat'])
    lon2 = str(data2['lon'])
    countryCode2 = data2['countryCode']
    country2 = data2['country']
    region2 = data2['region']
    regionName2 = data2['regionName']
    city2 = data2['city']
    isp2 = data2['isp']
    as2 = data2['as']
    zip2 = str(data2['zip'])
    org2 = data2['org']
    #APPLY RESULTS - CUSTOM IP FRAME
    customIPreset()
    customIPentryVar.set(ip2)
    countryCIPentryVar.set("[{}] {}".format(countryCode2, country2))
    regionCIPentryVar.set("[{}] {}".format(region2, regionName2))
    cityCIPentryVar.set(city2)
    zipCIPentryVar.set(zip2)
    latitudeCIPentryVar.set(lat2)
    longitudeCIPentryVar.set(lon2)
    organizationCIPentryVar.set(org2)
    ispCIPentryVar.set(isp2)
    asCIPentryVar.set(as2)
def customIPreset():
    #RESET ENTRIES - CUSTOM IP FRAME
    customIPentryVar.set('')
    countryCIPentryVar.set('')
    regionCIPentryVar.set('')
    cityCIPentryVar.set('')
    zipCIPentryVar.set('')
    latitudeCIPentryVar.set('')
    longitudeCIPentryVar.set('')
    organizationCIPentryVar.set('')
    ispCIPentryVar.set('')
    asCIPentryVar.set('')
def customIPsave():
    #SAVE RESULTS - CUSTOM IP FRAME
    folder2 = filedialog.askdirectory()
    filename2 = "customIP_{}.txt".format(ip2)
    file2_path = os.path.join(folder2, filename2)
    f2 = open(file2_path, 'w+')
    f2.write("IP: {} \nCountry: [{}] {}\nRegion: [{}] {}\nCity: {}\nZIP: {}\nLatitude: {}\nLongitude: {}\nOrganization: {}\nOrganization ISP: {}\nOrganization AS: {}\n"
             .format(ip2, countryCode2, country2, region2, regionName2,
                     city2, zip2, lat2, lon2, org2, isp2, as2))
    f2.close()
    messagebox.showinfo("Saved (TXT)", "Saved to: {}".format(file2_path))

#MY DNS FRAME
def myDNSscan():
    global ipedns3, geoedns3, region3, regionName3, city3, isp3, as3
    randomDNS = "".join(random.choice(string.ascii_letters) for i in range(32))
    res3 = requests.get("http://{}.edns.ip-api.com/json/".format(randomDNS))
    data3 = res3.json()
    res3_2 = requests.get("http://ip-api.com/json/")
    data3_2 = res3_2.json()
    #GET INFORMATIONS - MY DNS FRAME
    region3 = data3_2['region']
    regionName3 = data3_2['regionName']
    city3 = data3_2['city']
    isp3 = data3_2['isp']
    as3 = data3_2['as']
    edns3 = data3['dns']
    ipedns3 = edns3['ip']
    geoedns3 = edns3['geo']
    #APPLY RESULTS - MY DNS FRAME
    myDNSreset()
    myDNSentryVar.set(ipedns3)
    geoDNSentryVar.set(geoedns3)
    posDNSentryVar.set("[{}] {} / {}".format(region3, regionName3, city3))
    ispDNSentryVar.set(isp3)
    asDNSentryVar.set(as3)
def myDNSreset():
    #RESET ENTRIES - MY DNS FRAME
    myDNSentryVar.set('')
    geoDNSentryVar.set('')
    posDNSentryVar.set('')
    ispDNSentryVar.set('')
    asDNSentryVar.set('')
def myDNSsave():
    #SAVE RESULTS - MY DNS FRAME
    folder3 = filedialog.askdirectory()
    filename3 = "myDNS.txt"
    file3_path = os.path.join(folder3, filename3)
    f3 = open(file3_path, 'w+')
    f3.write("eDNS IP: {}\neDNS GEO: {}\neDNS POS: [{}] {} / {}\neDNS ISP: {}\neDNS AS: {}\n"
             .format(ipedns3, geoedns3, region3, regionName3, city3, isp3, as3))
    f3.close()
    messagebox.showinfo("Saved (TXT)", "Saved to: {}".format(file3_path))

#PORT SCANNER FRAME
def portScan():
    global openPorts, remoteServerIP
    openPorts = []
    remoteServer = portSCANentryVar.get()
    remoteServerIP = socket.gethostbyname(remoteServer)
    portScanTIMER1 = datetime.now()
    portSCANtext.delete(0.0, END)
    #GET OPEN PORTS - PORT SCANNER FRAME
    try:
        for port in range(1,1025):
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(0.5)
            result = sock.connect_ex((remoteServerIP, port))
            if result == 0:
                openPorts.append(port)
                portSCANtext.insert(END, "[{}] Port {} Open\n".format(datetime.now()-portScanTIMER1, port))
            sock.close()
    #HANDLING EXCEPTIONS - PORT SCANNER FRAME
    except KeyboardInterrupt:
        portSCANtext.insert(END, "CTRL+C Pressed.")
    except socket.gaierror:
        portSCANtext.insert(END, "Host not resolved.")
    except socket.error:
        portSCANtext.insert(END, "Couldn't connect to server.")
    portScanTIMER2 = datetime.now()
    portSCANtext.insert(END, "{} open Ports found.".format(str(len(openPorts))))
    portScanTIMER = str(portScanTIMER2 - portScanTIMER1)
    portSCANtext.insert(END, "Scanning Completed in {}".format(portScanTIMER))
def portSave():
    #SAVE RESULTS - PORT SCANNER FRAME
    folder4 = filedialog.askdirectory()
    filename4 = "scanPort_{}.txt".format(remoteServerIP)
    file4_path = os.path.join(folder4, filename4)
    f4 = open(file4_path, 'w+')
    f4.write(remoteServerIP + "\n")
    for a in range(len(openPorts)):
        f4.write("Port: %d\n" % openPorts[a])
    f4.close()
    messagebox.showinfo("Saved (TXT)", "Saved to: {}".format(file4_path))
    openPortsLIST = messagebox.askquestion("Ports List", "Open Ports/Protocols Names in Browser?", icon="question")
    if openPortsLIST == True:
        webbrowser.open("http://www.iana.org/assignments/service-names-port-numbers/service-names-port-numbers.txt")

#PHONE NUMBER SCANNER FRAME
def numberScan():
    global phoneNumberGET, phoneNumber, numberNSCAN, numberCC, numberC, numberLOCAL, numberINTER, countryNSCAN, locationNSCAN, carrierNameNSCAN
    phoneNumberGET = numberSCANentryVar.get()
    #GET INFORMATIONS - PHONE NUMBER SCANNER FRAME
    phoneNumber = phonenumbers.parse(phoneNumberGET, None)
    numberNSCAN = phonenumbers.format_number(phoneNumber, phonenumbers.PhoneNumberFormat.E164).replace('+', '')
    numberCC = phonenumbers.format_number(phoneNumber, phonenumbers.PhoneNumberFormat.INTERNATIONAL).split(' ')[0]
    numberC = phonenumbers.region_code_for_country_code(int(numberCC))
    numberLOCAL = phonenumbers.format_number(phoneNumber, phonenumbers.PhoneNumberFormat.E164).replace(numberCC, '')
    numberINTER = phonenumbers.format_number(phoneNumber, phonenumbers.PhoneNumberFormat.INTERNATIONAL)
    countryNSCAN = geocoder.country_name_for_number(phoneNumber, 'en')
    locationNSCAN = geocoder.description_for_number(phoneNumber, 'en')
    carrierNameNSCAN = carrier.name_for_number(phoneNumber, 'en')
    #APPLY RESULTS - PHONE NUMBER SCANNER FRAME
    numberReset()
    numberSCANentryVar.set(phoneNumberGET)
    localNSCANentryVar.set(numberLOCAL)
    interNSCANentryVar.set(numberINTER)
    countryNSCANentryVar.set("{} ({})".format(countryNSCAN, numberCC))
    areaNSCANentryVar.set(locationNSCAN)
    carrierNSCANentryVar.set(carrierNameNSCAN)
    for timezoneResult in timezone.time_zones_for_number(phoneNumber):
        timezoneNSCANentryVar.set(timezoneResult)
    if phonenumbers.is_possible_number(phoneNumber):
        validNSCANentryVar.set("VALID+POSSIBLE")
    else:
        validNSCANentryVar.set("INVALID")
def numberReset():
    #RESET ENTRIES - PHONE NUMBER SCANNER FRAME
    numberSCANentryVar.set('')
    localNSCANentryVar.set('')
    interNSCANentryVar.set('')
    countryNSCANentryVar.set('')
    areaNSCANentryVar.set('')
    carrierNSCANentryVar.set('')
    timezoneNSCANentryVar.set('')
    validNSCANentryVar.set('')
def numberSave():
    #SAVE RESULTS - PHONE NUMBER SCANNER FRAME
    folder5 = filedialog.askdirectory()
    filename5 = "scanPhone_{}.txt".format(phoneNumberGET)
    file5_path = os.path.join(folder5, filename5)
    f5 = open(file5_path, 'w+')
    f5.write("INTER FORMAT: {}\nLOCAL FORMAT: {}\nCOUNTRY: {} ({})\nCITY/AREA: {}\nCARRIER: {}\n"
             .format(numberINTER, numberLOCAL, countryNSCAN, numberCC, locationNSCAN, carrierNameNSCAN))
    for timezoneResult in timezone.time_zones_for_number(phoneNumber):
        f5.write("TIMEZONE: {}\n".format(timezoneResult))
    if phonenumbers.is_possible_number(phoneNumber):
        f5.write("VALID + POSSIBLE NUMBER.\n")
    f5.close()
    messagebox.showinfo("Saved (TXT)", "Saved to: {}".format(file5_path))

rootTitle = Label(root, text="Info Gather @abdeljalilsalhi", font=32, bg="black", fg="#33ff00")
rootTitle.grid(row=0, column=1)
#MY IP FRAME
myIPframe = LabelFrame(root, text="MY IP", fg="#33ff00", bg="black")
myIPframe.grid(row=1, column=0, columnspan=3, padx=10, pady=5)
myIPlabel = Label(myIPframe, text="IP", fg="#33ff00", bg="black")
myIPlabel.grid(row=0, column=0, sticky=W)
myIPentryVar = StringVar()
myIPentry = Entry(myIPframe, textvariable=myIPentryVar, width=20)
myIPentry.grid(row=1, column=0)
countryIPlabel = Label(myIPframe, text="COUNTRY", fg="#33ff00", bg="black")
countryIPlabel.grid(row=0, column=1, sticky=W)
countryIPentryVar = StringVar()
countryIPentry = Entry(myIPframe, textvariable=countryIPentryVar, width=20)
countryIPentry.grid(row=1, column=1)
regionIPlabel = Label(myIPframe, text="REGION", fg="#33ff00", bg="black")
regionIPlabel.grid(row=0, column=2, sticky=W)
regionIPentryVar = StringVar()
regionIPentry = Entry(myIPframe, textvariable=regionIPentryVar, width=20)
regionIPentry.grid(row=1, column=2)
cityIPlabel = Label(myIPframe, text="CITY", fg="#33ff00", bg="black")
cityIPlabel.grid(row=0, column=3, sticky=W)
cityIPentryVar = StringVar()
cityIPentry = Entry(myIPframe, textvariable=cityIPentryVar, width=20)
cityIPentry.grid(row=1, column=3)
zipIPlabel = Label(myIPframe, text="ZIP", fg="#33ff00", bg="black")
zipIPlabel.grid(row=0, column=4, sticky=W)
zipIPentryVar = StringVar()
zipIPentry = Entry(myIPframe, textvariable=zipIPentryVar, width=20)
zipIPentry.grid(row=1, column=4)
latitudeIPlabel = Label(myIPframe, text="LATITUDE", fg="#33ff00", bg="black")
latitudeIPlabel.grid(row=2, column=0, sticky=W)
latitudeIPentryVar = StringVar()
latitudeIPentry = Entry(myIPframe, textvariable=latitudeIPentryVar, width=20)
latitudeIPentry.grid(row=3, column=0)
longitudeIPlabel = Label(myIPframe, text="LONGITUDE", fg="#33ff00", bg="black")
longitudeIPlabel.grid(row=2, column=1, sticky=W)
longitudeIPentryVar = StringVar()
longitudeIPentry = Entry(myIPframe, textvariable=longitudeIPentryVar, width=20)
longitudeIPentry.grid(row=3, column=1)
organizationIPlabel = Label(myIPframe, text="ORGANIZATION", fg="#33ff00", bg="black")
organizationIPlabel.grid(row=2, column=2, sticky=W)
organizationIPentryVar = StringVar()
organizationIPentry = Entry(myIPframe, textvariable=organizationIPentryVar, width=20)
organizationIPentry.grid(row=3, column=2)
ispIPlabel = Label(myIPframe, text="ISP", fg="#33ff00", bg="black")
ispIPlabel.grid(row=2, column=3, sticky=W)
ispIPentryVar = StringVar()
ispIPentry = Entry(myIPframe, textvariable=ispIPentryVar, width=20)
ispIPentry.grid(row=3, column=3)
asIPlabel = Label(myIPframe, text="AS", fg="#33ff00", bg="black")
asIPlabel.grid(row=2, column=4, sticky=W)
asIPentryVar = StringVar()
asIPentry = Entry(myIPframe, textvariable=asIPentryVar, width=20)
asIPentry.grid(row=3, column=4)
resetIP = Button(myIPframe, text="RESET", cursor="cross", command=myIPreset,
                  bg="black", fg="#33ff00", pady=5)
resetIP.grid(row=5, column=3)
submitIP = Button(myIPframe, text="SCAN", cursor="cross", command=myIPscan,
                   bg="black", fg="#33ff00", pady=5)
submitIP.grid(row=5, column=4)
saveIP = Button(myIPframe, text="SAVE (TXT)", cursor="cross", command=myIPsave,
                   bg="black", fg="#33ff00", pady=5)
saveIP.grid(row=5, column=1)
#CUSTOM IP FRAME
customIPframe = LabelFrame(root, text="CUSTOM IP", fg="#33ff00", bg="black")
customIPframe.grid(row=2, column=0, columnspan=3, padx=10, pady=5)
customIPlabel = Label(customIPframe, text="IP ADDRESS?", fg="#33ff00", bg="black")
customIPlabel.grid(row=0, column=0, sticky=W)
customIPentryVar = StringVar()
customIPentryVar.set("TARGET IP HERE")
customIPentry = Entry(customIPframe, textvariable=customIPentryVar, width=20)
customIPentry.grid(row=1, column=0)
countryCIPlabel = Label(customIPframe, text="COUNTRY", fg="#33ff00", bg="black")
countryCIPlabel.grid(row=0, column=1, sticky=W)
countryCIPentryVar = StringVar()
countryCIPentry = Entry(customIPframe, textvariable=countryCIPentryVar, width=20)
countryCIPentry.grid(row=1, column=1)
regionCIPlabel = Label(customIPframe, text="REGION", fg="#33ff00", bg="black")
regionCIPlabel.grid(row=0, column=2, sticky=W)
regionCIPentryVar = StringVar()
regionCIPentry = Entry(customIPframe, textvariable=regionCIPentryVar, width=20)
regionCIPentry.grid(row=1, column=2)
cityCIPlabel = Label(customIPframe, text="CITY", fg="#33ff00", bg="black")
cityCIPlabel.grid(row=0, column=3, sticky=W)
cityCIPentryVar = StringVar()
cityCIPentry = Entry(customIPframe, textvariable=cityCIPentryVar, width=20)
cityCIPentry.grid(row=1, column=3)
zipCIPlabel = Label(customIPframe, text="ZIP", fg="#33ff00", bg="black")
zipCIPlabel.grid(row=0, column=4, sticky=W)
zipCIPentryVar = StringVar()
zipCIPentry = Entry(customIPframe, textvariable=zipCIPentryVar, width=20)
zipCIPentry.grid(row=1, column=4)
latitudeCIPlabel = Label(customIPframe, text="LATITUDE", fg="#33ff00", bg="black")
latitudeCIPlabel.grid(row=2, column=0, sticky=W)
latitudeCIPentryVar = StringVar()
latitudeCIPentry = Entry(customIPframe, textvariable=latitudeCIPentryVar, width=20)
latitudeCIPentry.grid(row=3, column=0)
longitudeCIPlabel = Label(customIPframe, text="LONGITUDE", fg="#33ff00", bg="black")
longitudeCIPlabel.grid(row=2, column=1, sticky=W)
longitudeCIPentryVar = StringVar()
longitudeCIPentry = Entry(customIPframe, textvariable=longitudeCIPentryVar, width=20)
longitudeCIPentry.grid(row=3, column=1)
organizationCIPlabel = Label(customIPframe, text="ORGANIZATION", fg="#33ff00", bg="black")
organizationCIPlabel.grid(row=2, column=2, sticky=W)
organizationCIPentryVar = StringVar()
organizationCIPentry = Entry(customIPframe, textvariable=organizationCIPentryVar, width=20)
organizationCIPentry.grid(row=3, column=2)
ispCIPlabel = Label(customIPframe, text="ISP", fg="#33ff00", bg="black")
ispCIPlabel.grid(row=2, column=3, sticky=W)
ispCIPentryVar = StringVar()
ispCIPentry = Entry(customIPframe, textvariable=ispCIPentryVar, width=20)
ispCIPentry.grid(row=3, column=3)
asCIPlabel = Label(customIPframe, text="AS", fg="#33ff00", bg="black")
asCIPlabel.grid(row=2, column=4, sticky=W)
asCIPentryVar = StringVar()
asCIPentry = Entry(customIPframe, textvariable=asCIPentryVar, width=20)
asCIPentry.grid(row=3, column=4)
resetCIP = Button(customIPframe, text="RESET", cursor="cross", command=customIPreset,
                  bg="black", fg="#33ff00", pady=5)
resetCIP.grid(row=5, column=3)
submitCIP = Button(customIPframe, text="SCAN", cursor="cross", command=customIPscan,
                   bg="black", fg="#33ff00", pady=5)
submitCIP.grid(row=5, column=4)
saveCIP = Button(customIPframe, text="SAVE (TXT)", cursor="cross", command=customIPsave,
                   bg="black", fg="#33ff00", pady=5)
saveCIP.grid(row=5, column=1)
#MY DNS FRAME
myDNSframe = LabelFrame(root, text="MY DNS", fg="#33ff00", bg="black")
myDNSframe.grid(row=3, column=0, columnspan=2, sticky=W, padx=10, pady=5)
myDNSlabel = Label(myDNSframe, text="eDNS", fg="#33ff00", bg="black")
myDNSlabel.grid(row=0, column=0, sticky=W)
myDNSentryVar = StringVar()
myDNSentry = Entry(myDNSframe, textvariable=myDNSentryVar, width=20)
myDNSentry.grid(row=1, column=0)
geoDNSlabel = Label(myDNSframe, text="GEO", fg="#33ff00", bg="black")
geoDNSlabel.grid(row=0, column=1, sticky=W)
geoDNSentryVar = StringVar()
geoDNSentry = Entry(myDNSframe, textvariable=geoDNSentryVar, width=20)
geoDNSentry.grid(row=1, column=1)
posDNSlabel = Label(myDNSframe, text="POS", fg="#33ff00", bg="black")
posDNSlabel.grid(row=0, column=2, sticky=W)
posDNSentryVar = StringVar()
posDNSentry = Entry(myDNSframe, textvariable=posDNSentryVar, width=20)
posDNSentry.grid(row=1, column=2)
ispDNSlabel = Label(myDNSframe, text="ISP", fg="#33ff00", bg="black")
ispDNSlabel.grid(row=2, column=0, sticky=W)
ispDNSentryVar = StringVar()
ispDNSentry = Entry(myDNSframe, textvariable=ispDNSentryVar, width=20)
ispDNSentry.grid(row=3, column=0)
asDNSlabel = Label(myDNSframe, text="AS", fg="#33ff00", bg="black")
asDNSlabel.grid(row=2, column=1, sticky=W)
asDNSentryVar = StringVar()
asDNSentry = Entry(myDNSframe, textvariable=asDNSentryVar, width=20)
asDNSentry.grid(row=3, column=1)
resetDNS = Button(myDNSframe, text="RESET", cursor="cross", command=myDNSreset,
                  bg="black", fg="#33ff00", pady=5)
resetDNS.grid(row=4, column=1)
submitDNS = Button(myDNSframe, text="SCAN", cursor="cross", command=myDNSscan,
                   bg="black", fg="#33ff00", pady=5)
submitDNS.grid(row=4, column=2)
saveDNS = Button(myDNSframe, text="SAVE (TXT)", cursor="cross", command=myDNSsave,
                   bg="black", fg="#33ff00", pady=5)
saveDNS.grid(row=4, column=0)
#PORT SCANNER FRAME
portSCANframe = LabelFrame(root, text="PORT SCANNER", fg="#33ff00", bg="black")
portSCANframe.grid(row=3, column=2, columnspan=2, sticky=E, padx=10, pady=5)
portSCANlabel = Label(portSCANframe, text="HOST??", fg="#33ff00", bg="black")
portSCANlabel.grid(row=0, column=0, sticky=W)
portSCANentryVar = StringVar()
portSCANentryVar.set("TARGET IP HERE")
portSCANentry = Entry(portSCANframe, textvariable=portSCANentryVar, width=20)
portSCANentry.grid(row=1, column=0, columnspan=3)
portSCANtext = Text(portSCANframe, height=5, width=20)
portSCANtext.grid(row=2, column=0, columnspan=3, pady=5, padx=10)
submitportSCAN = Button(portSCANframe, text="SCAN", cursor="cross", command=portScan,
                        bg="black", fg="#33ff00")
submitportSCAN.grid(row=0, column=2, sticky=E)
saveportSCAN = Button(portSCANframe, text="SAVE (TXT)", cursor="cross", command=portSave,
                      bg="black", fg="#33ff00")
saveportSCAN.grid(row=0, column=1, sticky=E)
#NUMBER SCANNER FRAME
numberSCANframe = LabelFrame(root, text="PHONE NUMBER SCANNER", fg="#33ff00", bg="black")
numberSCANframe.grid(row=4, column=0, columnspan=3, padx=10, pady=5)
numberSCANlabel = Label(numberSCANframe, text="PHONE NUMBER??", fg="#33ff00", bg="black")
numberSCANlabel.grid(row=0, column=0, sticky=W)
numberSCANentryVar = StringVar()
numberSCANentry = Entry(numberSCANframe, textvariable=numberSCANentryVar, width=20)
numberSCANentry.grid(row=1, column=0)
interNSCANlabel = Label(numberSCANframe, text="INTER FORMAT", fg="#33ff00", bg="black")
interNSCANlabel.grid(row=0, column=1, sticky=W)
interNSCANentryVar = StringVar()
interNSCANentry = Entry(numberSCANframe, textvariable=interNSCANentryVar, width=20)
interNSCANentry.grid(row=1, column=1)
localNSCANlabel = Label(numberSCANframe, text="LOCAL FORMAT", fg="#33ff00", bg="black")
localNSCANlabel.grid(row=0, column=2, sticky=W)
localNSCANentryVar = StringVar()
localNSCANentry = Entry(numberSCANframe, textvariable=localNSCANentryVar, width=20)
localNSCANentry.grid(row=1, column=2)
validNSCANlabel = Label(numberSCANframe, text="VALID?", fg="#33ff00", bg="black")
validNSCANlabel.grid(row=0, column=3, sticky=W)
validNSCANentryVar = StringVar()
validNSCANentry = Entry(numberSCANframe, textvariable=validNSCANentryVar, width=20)
validNSCANentry.grid(row=1, column=3)
countryNSCANlabel = Label(numberSCANframe, text="COUNTRY", fg="#33ff00", bg="black")
countryNSCANlabel.grid(row=2, column=0, sticky=W)
countryNSCANentryVar = StringVar()
countryNSCANentry = Entry(numberSCANframe, textvariable=countryNSCANentryVar, width=20)
countryNSCANentry.grid(row=3, column=0)
areaNSCANlabel = Label(numberSCANframe, text="CITY/AREA", fg="#33ff00", bg="black")
areaNSCANlabel.grid(row=2, column=1, sticky=W)
areaNSCANentryVar = StringVar()
areaNSCANentry = Entry(numberSCANframe, textvariable=areaNSCANentryVar, width=20)
areaNSCANentry.grid(row=3, column=1)
carrierNSCANlabel = Label(numberSCANframe, text="CARRIER", fg="#33ff00", bg="black")
carrierNSCANlabel.grid(row=2, column=2, sticky=W)
carrierNSCANentryVar = StringVar()
carrierNSCANentry = Entry(numberSCANframe, textvariable=carrierNSCANentryVar, width=20)
carrierNSCANentry.grid(row=3, column=2)
timezoneNSCANlabel = Label(numberSCANframe, text="TIMEZONE", fg="#33ff00", bg="black")
timezoneNSCANlabel.grid(row=2, column=3, sticky=W)
timezoneNSCANentryVar = StringVar()
timezoneNSCANentry = Entry(numberSCANframe, textvariable=timezoneNSCANentryVar, width=20)
timezoneNSCANentry.grid(row=3, column=3)
resetN = Button(numberSCANframe, text="RESET", cursor="cross", command=numberReset,
                  bg="black", fg="#33ff00", pady=5)
resetN.grid(row=4, column=1)
submitN = Button(numberSCANframe, text="SCAN", cursor="cross", command=numberScan,
                   bg="black", fg="#33ff00", pady=5)
submitN.grid(row=4, column=2)
saveN = Button(numberSCANframe, text="SAVE (TXT)", cursor="cross", command=numberSave,
                   bg="black", fg="#33ff00", pady=5)
saveN.grid(row=4, column=0)
#SIGNATURE
signature = Label(root, text="@SALHI", fg="#33ff00", bg="black")
signature.grid(row=4, column=2, sticky=(E,S))

root.mainloop()

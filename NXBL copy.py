import requests
import json
import time

SR = '7492baca-c1b4-440d-a391-b7ef364a8d40'

RawToken = requests.get('https://raw.githubusercontent.com/ZeroLogic9/Grabify/master/Token')
Token = RawToken.text.replace('Authorization: ', '')

headers = {
    'Authorization': Token.replace('\n', ''), 
    'x-xbl-contract-version': '105',
    'If-None-Match': '495427962d8b64af5adb5db2d20c2783'

}
def main():
 r = requests.get('https://sessiondirectory.xboxlive.com/serviceconfigs/' + SR + '/sessiontemplates/chat/sessions?xuid=2535411755592533&followed=true', headers=headers)
 Data = r.json()
 results = Data['results']
 json_str = json.dumps(results)
 A1 = json_str.replace('[]', '(BLM)')
 A2 = A1.replace('[', '')
 A3 = A2.replace(']', '')
 Data = A3.replace('(BLM)', '[]')
 if Data == '[]':
     print('You are not in a Party!')
     exit()
 JsonData = json.loads(Data)
 SessionData = JsonData['sessionRef']
 SN = SessionData['name']
 
 r = requests.get('https://sessiondirectory.xboxlive.com/serviceconfigs/' + SR + '/sessiontemplates/chat/sessions/' + SN + '?nocommit=true&followed=true', headers=headers)
 Data = r.json()
 members = Data['members']
 NumMem = list(members.keys())
 a = NumMem.count
 if a('0') == 1:
     b = members['0']
     c = b['constants']
     d = c['system']
     Xuid = d['xuid']
     GT = b['gamertag']
     A = {GT : Xuid}
     prop = b['properties']
     sys = prop['system']
     sub = sys['subscription']
     ty = sub['changeTypes']
     Num0 = ty.count('host')
     if Num0 == 1:
         Host = {'host': Xuid}
 else:
     A = {}
 if a('1') == 1:
     b = members['1']
     c = b['constants']
     d = c['system']
     Xuid = d['xuid']
     GT = b['gamertag']
     B = {GT : Xuid}
     prop = b['properties']
     sys = prop['system']
     sub = sys['subscription']
     ty = sub['changeTypes']
     Num0 = ty.count('host')
     if Num0 == 1:
         Host = {'host': Xuid}
 else:
     B = {}
 if a('2') == 1:
     b = members['2']
     c = b['constants']
     d = c['system']
     Xuid = d['xuid']
     GT = b['gamertag']
     C = {GT : Xuid}
     prop = b['properties']
     sys = prop['system']
     sub = sys['subscription']
     ty = sub['changeTypes']
     Num0 = ty.count('host')
     if Num0 == 1:
         Host = {'host': Xuid}
 else:
     C = {}
 if a('3') == 1:
     b = members['3']
     c = b['constants']
     d = c['system']
     Xuid = d['xuid']
     GT = b['gamertag']
     D = {GT : Xuid}
     prop = b['properties']
     sys = prop['system']
     sub = sys['subscription']
     ty = sub['changeTypes']
     Num0 = ty.count('host')
     if Num0 == 1:
         Host = {'host': Xuid}
 else:
     D = {}
 if a('4') == 1:
     b = members['4']
     c = b['constants']
     d = c['system']
     Xuid = d['xuid']
     GT = b['gamertag']
     E = {GT : Xuid}
     prop = b['properties']
     sys = prop['system']
     sub = sys['subscription']
     ty = sub['changeTypes']
     Num0 = ty.count('host')
     if Num0 == 1:
         Host = {'host': Xuid}
 else:
     E = {}
 if a('5') == 1:
     b = members['5']
     c = b['constants']
     d = c['system']
     Xuid = d['xuid']
     GT = b['gamertag']
     F = {GT : Xuid}
     prop = b['properties']
     sys = prop['system']
     sub = sys['subscription']
     ty = sub['changeTypes']
     Num0 = ty.count('host')
     if Num0 == 1:
         Host = {'host': Xuid}
 else:
     F = {}
 if a('6') == 1:
     b = members['6']
     c = b['constants']
     d = c['system']
     Xuid = d['xuid']
     GT = b['gamertag']
     G = {GT : Xuid}
     prop = b['properties']
     sys = prop['system']
     sub = sys['subscription']
     ty = sub['changeTypes']
     Num0 = ty.count('host')
     if Num0 == 1:
         Host = {'host': Xuid}
 else:
     G = {}
 if a('7') == 1:
     b = members['7']
     c = b['constants']
     d = c['system']
     Xuid = d['xuid']
     GT = b['gamertag']
     H = {GT : Xuid}
     prop = b['properties']
     sys = prop['system']
     sub = sys['subscription']
     ty = sub['changeTypes']
     Num0 = ty.count('host')
     if Num0 == 1:
         Host = {'host': Xuid}
 else:
     H = {}
 if a('8') == 1:
     b = members['8']
     c = b['constants']
     d = c['system']
     Xuid = d['xuid']
     GT = b['gamertag']
     I = {GT : Xuid}
     prop = b['properties']
     sys = prop['system']
     sub = sys['subscription']
     ty = sub['changeTypes']
     Num0 = ty.count('host')
     if Num0 == 1:
         Host = {'host': Xuid}
 else:
     I = {}
 if a('9') == 1:
     b = members['9']
     c = b['constants']
     d = c['system']
     Xuid = d['xuid']
     GT = b['gamertag']
     J = {GT : Xuid}
     prop = b['properties']
     sys = prop['system']
     sub = sys['subscription']
     ty = sub['changeTypes']
     Num0 = ty.count('host')
     if Num0 == 1:
         Host = {'host': Xuid}
 else:
     J = {}
 if a('10') == 1:
     b = members['10']
     c = b['constants']
     d = c['system']
     Xuid = d['xuid']
     GT = b['gamertag']
     K = {GT : Xuid}
     prop = b['properties']
     sys = prop['system']
     sub = sys['subscription']
     ty = sub['changeTypes']
     Num0 = ty.count('host')
     if Num0 == 1:
         Host = {'host': Xuid}
 else:
     K = {}
 if a('11') == 1:
     b = members['11']
     c = b['constants']
     d = c['system']
     Xuid = d['xuid']
     GT = b['gamertag']
     L = {GT : Xuid}
     prop = b['properties']
     sys = prop['system']
     sub = sys['subscription']
     ty = sub['changeTypes']
     Num0 = ty.count('host')
     if Num0 == 1:
         Host = {'host': Xuid}
 else:
     L = {}
 if a('12') == 1:
     b = members['12']
     c = b['constants']
     d = c['system']
     Xuid = d['xuid']
     GT = b['gamertag']
     M = {GT : Xuid}
     prop = b['properties']
     sys = prop['system']
     sub = sys['subscription']
     ty = sub['changeTypes']
     Num0 = ty.count('host')
     if Num0 == 1:
         Host = {'Host': Xuid}
 else:
     M = {}
 if a('13') == 1:
     b = members['13']
     c = b['constants']
     d = c['system']
     Xuid = d['xuid']
     GT = b['gamertag']
     N = {GT : Xuid}
     prop = b['properties']
     sys = prop['system']
     sub = sys['subscription']
     ty = sub['changeTypes']
     Num0 = ty.count('host')
     if Num0 == 1:
         Host = {'Host': Xuid}
 else:
     N = {}
 if a('14') == 1:
     b = members['14']
     c = b['constants']
     d = c['system']
     Xuid = d['xuid']
     GT = b['gamertag']
     O = {GT : Xuid}
     prop = b['properties']
     sys = prop['system']
     sub = sys['subscription']
     ty = sub['changeTypes']
     Num0 = ty.count('host')
     if Num0 == 1:
         Host = {'Host': Xuid}
 else:
     O = {}
 if a('15') == 1:
     b = members['15']
     c = b['constants']
     d = c['system']
     Xuid = d['xuid']
     GT = b['gamertag']
     P = {GT : Xuid}
     prop = b['properties']
     sys = prop['system']
     sub = sys['subscription']
     ty = sub['changeTypes']
     Num0 = ty.count('host')
     if Num0 == 1:
         Host = {'Host': Xuid}
 else:
     P = {}
 if a('16') == 1:
     b = members['16']
     c = b['constants']
     d = c['system']
     Xuid = d['xuid']
     GT = b['gamertag']
     Q = {GT : Xuid}
     prop = b['properties']
     sys = prop['system']
     sub = sys['subscription']
     ty = sub['changeTypes']
     Num0 = ty.count('host')
     if Num0 == 1:
         Host = {'Host': Xuid}
 else:
     Q = {}
 hbe = Data['membersOnly']
 host = hbe['bumblelionRelayCreator']
 Dict = {**A, **B, **C, **D, **E, **F, **G, **H, **I, **J, **K, **L, **M, **N, **O, **P, **Q,}
 List = list(Dict.keys())

 for wwq in List:
     print(wwq)
 time.sleep(1)
 print(' ')
 GTToKick = input('Type in Gamertag to kick: ')
 UUQ = 'Zer0Logic0'
 V = List.count(GTToKick)
 if V == 0:
     print('Could not find selected target, ' + GTToKick + '.')
     print('-------------------------------------')
     main()
 elif GTToKick == UUQ:
     print('Failed to Kick, ' + UUQ + '.')
     main()
 ToKick = Dict[GTToKick]
 Data1 = {
     'properties':
     {
         'custom':
         {
             'kickusers':
             {
                 ToKick:host
             }
         }
     }
 }
 Data = json.dumps(Data1)
 print(Data)

 r = requests.put('https://sessiondirectory.xboxlive.com/serviceconfigs/' + SR + '/sessiontemplates/chat/sessions/' + SN, headers=headers, data=Data)
 if r.status_code == 400:
     print('Failed to Kick, ' + GTToKick + '.')
     print(r.json)
     main()
 print('Successfully Kicked ' + GTToKick + '!')
 print(r.content)
 RD1 = {"members":{"me_2535411755592533":{"constants":{"system":{"index":0}},"properties":{"custom":{"simpleConnectionState":1,"mesh_0":{"connectionState":2,"port":50102},"meshUnreachable":[]}}}}}
 D1 = json.dumps(RD1)
 RD2 = {"members":{"me_2535411755592533":{"constants":{"system":{"index":0}},"properties":{"custom":{"simpleConnectionState":2,"mesh_0":{"connectionState":4,"port":50102},"meshUnreachable":[]}}}}}
 D2 = json.dumps(RD2)
 r1 = requests.put('https://sessiondirectory.xboxlive.com/serviceconfigs/' + SR + '/sessiontemplates/chat/sessions/' + SN + '?nocommit=true&followed=true', headers=headers, data=D1)
 r2 = requests.put('https://sessiondirectory.xboxlive.com/serviceconfigs/' + SR + '/sessiontemplates/chat/sessions/' + SN + '?nocommit=true&followed=true', headers=headers, data=D2)
 r3 = requests.get('https://sessiondirectory.xboxlive.com/serviceconfigs/' + SR + '/sessiontemplates/chat/sessions/' + SN + '?nocommit=true&followed=true', headers=headers)
 print(r1.content)
 print(r2.content)
 print(r3.json)
 main()
main()


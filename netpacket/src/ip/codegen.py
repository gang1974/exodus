
# 1,0,22,150,       - Unassigned (Released 18 October 2005),

s = """0,0,0,0,EOOL   - End of Options List,[RFC791][Jon_Postel]
0,0,1,1,NOP    - No Operation,[RFC791][Jon_Postel]
1,0,2,130,SEC    - Security,[RFC1108]
1,0,3,131,LSR    - Loose Source Route,[RFC791][Jon_Postel]
0,2,4,68,TS     - Time Stamp,[RFC791][Jon_Postel]
1,0,5,133,E-SEC  - Extended Security,[RFC1108]
1,0,6,134,CIPSO  - Commercial Security,[draft-ietf-cipso-ipsecurity-01]
0,0,7,7,RR     - Record Route,[RFC791][Jon_Postel]
1,0,8,136,SID    - Stream ID,[RFC791][Jon_Postel][RFC6814][1]
1,0,9,137,SSR    - Strict Source Route,[RFC791][Jon_Postel]
0,0,10,10,ZSU    - Experimental Measurement,[ZSu]
0,0,11,11,MTUP   - MTU Probe,[RFC1063][RFC1191][1]
0,0,12,12,MTUR   - MTU Reply,[RFC1063][RFC1191][1]
1,2,13,205,FINN   - Experimental Flow Control,[Greg_Finn]
1,0,14,142,VISA   - Experimental Access Control,[Deborah_Estrin][RFC6814][1]
0,0,15,15,ENCODE - ???,[VerSteeg][RFC6814][1]
1,0,16,144,IMITD  - IMI Traffic Descriptor,[Lee]
1,0,17,145,EIP    - Extended Internet Protocol,[RFC1385][RFC6814][1]
0,2,18,82,TR     - Traceroute,[RFC1393][RFC6814][1]
1,0,19,147,ADDEXT - Address Extension,[Ullmann IPv7][RFC6814][1]
1,0,20,148,RTRALT - Router Alert,[RFC2113]
1,0,21,149,SDB    - Selective Directed Broadcast,[Charles_Bud_Graff][RFC6814][1]
1,0,23,151,DPS    - Dynamic Packet State,[Andy_Malis][RFC6814][1]
1,0,24,152,UMP    - Upstream Multicast Pkt.,[Dino_Farinacci][RFC6814][1]
0,0,25,25,QS     - Quick-Start,[RFC4782]
0,0,30,30,EXP1    - RFC3692-style Experiment [2],[RFC4727]
0,2,30,94,EXP2    - RFC3692-style Experiment [2],[RFC4727]
1,0,30,158,EXP3    - RFC3692-style Experiment [2],[RFC4727]
1,2,30,222,EXP4    - RFC3692-style Experiment [2],[RFC4727]"""

data = {}
code = ""
for line in s.split("\n"):
    copy, kind, number, value, name_descp, refs = line.split(",")
    name = name_descp.split(" - ")[0].strip().replace("-", "_")
    descp = name_descp.split(" - ")[1].strip()
    copy = int(copy)
    kind = int(kind)
    number = int(number)
    value = int(value)
    data[name] = {
        'copy': copy,
        'kind': kind,
        'number': number,
        'value': value,
        'name': name,
        'descp': descp,
        'refs': refs,
        'class': int(bin(copy).replace("0b", "").zfill(1) + bin(kind).replace("0b", "").zfill(2) + bin(number).replace("0b", "").zfill(5), 2)
    }





for k in data:
    v = data[k]
    name = v['name']
    class_number = v['class']
    value = v['value']
    code += """    /// copied(%d) class(%d) number(%d) value(%d)    %s, %s
    pub fn is_%s(&self) -> bool {
        self.ccn == %d && self.value == %d
    }\n""" % ( v['copy'], v['kind'], v['number'], v['value'], v['descp'], v['refs'],  name.lower(), class_number, value)

print(code)
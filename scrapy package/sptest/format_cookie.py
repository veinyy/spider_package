
cook='_ha_ref.xs.d15e=%5B%22%22%2C%22%22%2C1442157501%2C%22https%3A%2F%2Fwww.google.com%2F%22%5D; _ha_id.xs.d15e=43-6F-15-65-1B-EF-93-5C-61-AC-B5-7A-0C-0C-53-A0.1442157514.0.1442157514..; _ha_ses.xs.d15e=5d910d8e527a91bc2f1fa5f358bad32fa2d070c9; _ga=GA1.2.2039450903.1441258932; s_fid=22B5489B3FD06E56-07C599F372993F3A; ttc=1442228178232; HWFORUM_SESSION=s92j4ioiv1k1je306gkcdeue63; online_update=1442157500; authmethod=authpwd; hwsso_uniportal=1F3BEDBABD9FD230DF80A08FE2225ACD59B889761C134086298FBDBCC2BA13774FD3648381CCC7EC0D2B13CA769DAE02528ADEE9693DC27DF02468FC39A275DE9612043DA1950F5B82CF61354A6E95DCDE94565E7BD1BBD668372432891964C55D4C52437955E2FF94DCB97254D23BDBCB2F967B9F713574CE36CA219B1B423FB649F8B281D9DB1F0F4ED5E98EBEC461; hwssotinter=C9-65-9E-D0-53-E1-C2-15-07-19-17-51-BD-42-F5-6C; lang=zh; sid=72-C3-05-75-56-B7-5E-74-D8-31-F3-41-51-72-83-F8-98-8B-18-1F-64-65-24-A0-0C-8B-F7-C3-65-99-2A-F1-31-41-73-38-18-C3-D3-B0; uid=43-6F-15-65-1B-EF-93-5C-61-AC-B5-7A-0C-0C-53-A0; suid=43-6F-15-65-1B-EF-93-5C-61-AC-B5-7A-0C-0C-53-A0; sip=19-C9-2D-28-1F-57-C2-B2-D7-E9-EC-09-C3-52-93-8B-DD-80-3A-2E-CE-AA-89-6B; logFlag=in; hwssotinter3=24770722257331; TS_think_language=zh-cn'
cook=cook.replace(' ','')
cookies=cook.split(';')
file=open('input.txt','w')
for var in cookies:
    file.write(var)
    file.write('\n')
file.close()

file=open('input.txt','r')
file_output = open("output.txt", "w")
list = {}
temp_list = file.readlines()
for var in temp_list:
    list[var.split('=')[0]] = var.split('=')[1].replace('\n','')
for key in list.keys():
    str = "'%s':'%s', \n"% (key,list[key])
    file_output.write(str)
file.close()
file_output.close()

file.close()



student_data={'ide1':{'name' :'jack','age':5,'subject':'math'},
'ide2':{'name':'sam','age':6,'subject':'sci'},'ide3':{'name':'ayyoob','age':'4','subject':'arbic'},'ide4':{'name':'ayyoob','age':'4','subject':'arbic'}}
result={}
seen_keys=[]
for student_id,details in student_data.items():
    uinq_key=(details["name"],details["age"],details["subject"])
    if uinq_key not in seen_keys:
        seen_keys.append(uinq_key)
        result[student_id]=details
for k,v in result.items():
    print(k,v)

import re
import os
import base64

def get_all_log():
    basepath = 'log/'
    logs = []
    count = 0
    for entry in os.listdir(basepath):
        with open(os.path.join(basepath, entry), "r", encoding="utf-8") as f:
            content = f.readlines()
        for x in range(len(content)):
            temp = content[x].split(',')[2]
            if count == 0:
                borrower = {"email": '',"full_name": '', "documents": {"tabungan": {"file" : '', "name": ''}, "npwp": {"file" : '', "name": ''}, "ktp" : {"file" : '', "name": ''}, "selfie": {"file" : '', "name": ''}}}
            if 'partners/v1/ecommerce/bukalapak/applyloan' in temp:
                borrower['full_name'] = re.findall(r"(\"full_name\":\"\w+(\s{1}\w+)?(\s{1}\w+)?\")", content[x])[0][0].split(':')[1]
                borrower['email'] = re.findall(r"(\"email\":\"[a-zA-z0-9!@#$%^&*(),.?\"\:\{\}\-\_|\<\>]+@[a-zA-z0-9]+\.\w{3}\")", content[x])[0].split(':')[1]
                borrower['full_name'] = borrower['full_name'].replace("\"","")
                borrower['email'] = borrower['email'].replace("\"","")
                count += 1
            elif '/partners/v1/ecommerce/document' in temp:
                file_name = re.findall(r'\"file_name\":\"[a-zA-Z0-9!@#$%^&*(),.?":{}\-\_|<>]+\"', content[x])[0].split(':')[1].replace('\"', '')
                # print(file_name)
                account = content[x].split(',')[5]
                account = account.replace(' Payload: {"document_string":"', '')
                account = account.replace('\"', '')
                if 'tabungan' in temp:
                    borrower['documents']['tabungan']['file'] = account
                    borrower['documents']['tabungan']['name'] = file_name
                elif 'npwp' in temp:
                    borrower['documents']['npwp']['file'] = account
                    borrower['documents']['npwp']['name'] = file_name
                elif 'ktp' in temp:
                    borrower['documents']['ktp']['file'] = account
                    borrower['documents']['ktp']['name'] = file_name
                elif 'selfie' in temp:
                    borrower['documents']['selfie']['file'] = account
                    borrower['documents']['selfie']['name'] = file_name
                count += 1
            else:
                count += 1
            
            if count == 6:
                logs.append(borrower)
                count = 0
    return logs

def write_file(logs):
    basepath = 'output/'
    for borrower in logs:
        try:
            folder_path = os.path.join(basepath, borrower['full_name'])
            if not os.path.exists(folder_path):
                os.makedirs(folder_path)
            # Tabungan
            tabungan_file=base64.b64decode(borrower['documents']['tabungan']['file'])
            tabungan_file_name = os.path.join(folder_path, borrower['documents']['tabungan']['name'])
            with open(tabungan_file_name, 'wb') as f:
                f.write(tabungan_file)
            #ktp
            ktp_file=base64.b64decode(borrower['documents']['ktp']['file'])
            ktp_file_name = os.path.join(folder_path, borrower['documents']['ktp']['name'])
            with open(ktp_file_name, 'wb') as f:
                f.write(ktp_file)
            #npwp
            npwp_file=base64.b64decode(borrower['documents']['npwp']['file'])
            npwp_file_name = os.path.join(folder_path, borrower['documents']['npwp']['name'])
            with open(npwp_file_name, 'wb') as f:
                f.write(npwp_file)
            #selfie
            selfie_file=base64.b64decode(borrower['documents']['selfie']['file'])
            selfie_file_name = os.path.join(folder_path, borrower['documents']['selfie']['name'])
            with open(selfie_file_name, 'wb') as f:
                f.write(selfie_file)            
        except Exception as e:
            raise e

print('==================MULAI==================')
logs = get_all_log()
write_file(logs)
print('==================SELESAI==================')

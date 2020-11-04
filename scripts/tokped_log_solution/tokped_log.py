from openpyxl import Workbook, load_workbook
import re
import os

print("mulai...")
new_file = input("ini ticket nomor berapa? : ")

# initialize
log_filename = []
email_list = []
request = []
response = []

# list all the log
basepath = "notepad/"
wb = load_workbook(filename="./book/log_error_collected_template.xlsx")
for entry in os.listdir(basepath):
    if os.path.isfile(os.path.join(basepath, entry)):
        log_date = entry[4:len(entry) - 4]
        log_filename.append(log_date)

# create new sheet base on log filename
active_sheet = wb.active
for log in log_filename:
    new_sheet = wb.copy_worksheet(active_sheet)
    new_sheet.title = log

# assign all the variable with data inside log
for entry in os.listdir(basepath):
    if os.path.isfile(os.path.join(basepath, entry)):
        log_date = entry[4:len(entry) - 4]
        with open(os.path.join(basepath, entry), "r", encoding="utf-8") as f:
            content = f.readlines()
        for x in range(len(content)):
            if "INFO --> request" in content[x]:
                temp_request = content[x][40:len(content[x])]
                temp_response = content[x+2][41:len(content[x+2])]
                if "01" in temp_response or "ERROR" in temp_response:
                    # add email
                    email = re.findall(
                        r"\"email_address\":\"[\w\.-]+@[\w\.-]+\"", temp_request)
                    email = email[0][16:len(email[0])]
                    email = email.replace("\"", "")
                    email_list.append(email)

                    # add to request
                    request.append(temp_request)

                    # add to response
                    response.append(temp_response)

        # write to new sheet
        new_sheet = wb[log_date]
        for i in range(len(request)):
            new_sheet.append([email_list[i], request[i], response[i]])

    # clear resource for another log
    request.clear()
    response.clear()
    email_list.clear()

wb.remove(active_sheet)
wb.save(r"./write/{}.xlsx".format(new_file))
print("kelar...")

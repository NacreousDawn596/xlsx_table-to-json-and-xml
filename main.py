import xlrd
import sys
import json
worksheet = xlrd.open_workbook(sys.argv[1]).sheet_by_index(0)
all = []
columns = worksheet.row_values(0)
for idk in range(1, worksheet.nrows):
    ugh = {}
    for i in range(0, len(columns)):
        ugh[columns[i]] = worksheet.row_values(idk)[i]
    all.append(ugh) 
uhh = open(f"{sys.argv[1].split('.')[0].replace(' ', '-')}.json", "w")
uhh.write("".join(f"{all}".replace("'", '"')))
uhh.close()
new_xml = open(f"{sys.argv[1].split('.')[0].replace(' ', '-')}.xml", "w")
idk = json.loads(open(f"{sys.argv[1].split('.')[0].replace(' ', '-')}.json", "r").read())
new_xml.write("".join("""<?xml version="1.0" encoding="UTF-8" standalone="yes"?>\n"""))
new_xml.write(f"""<{sys.argv[1].split('.')[0].replace(' ', '-')} xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">\n""")
for i in idk:
    new_xml.write(f"""\t<record>\n""")
    for uh in columns:
        new_xml.write(f"""\t\t<{uh}>{i[uh]}</{uh}>\n""")
    new_xml.write(f"""\t</record>\n""")
new_xml.write(f"""</{sys.argv[1].split('.')[1].replace(' ', '-')}>""")
new_xml.close()
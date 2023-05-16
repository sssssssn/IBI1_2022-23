import openpyxl
import xml.dom.minidom

# Create an Excel workbook and select the active sheet
excel_sheet = openpyxl.Workbook()
sheet = excel_sheet.active

# Write headers to the spreadsheet
headers = ["id", "name", "definition", "childnodes"]
sheet.append(headers)

dom = xml.dom.minidom.parse('/Users/shennuo/IBI1_2022-23/Practical 14/go_obo.xml')
collection = dom.documentElement

term_elements = collection.getElementsByTagName("term")

for term_element in term_elements:
    defstr_elements = term_element.getElementsByTagName("defstr")
    for defstr_element in defstr_elements:
        if 'autophagosome' in defstr_element.firstChild.nodeValue:
            # Find the id, name, and defstr elements within the term element
            id_element = term_element.getElementsByTagName('id')[0]
            name_element = term_element.getElementsByTagName('name')[0]
            defstr = defstr_element.firstChild.nodeValue

            # Extract the id, name, and definition
            go_id = id_element.firstChild.data if id_element.firstChild else ''
            term_name = name_element.firstChild.data if name_element.firstChild else ''

            # Count the number of child nodes
            child_nodes = term_element.getElementsByTagName("is_a")
            child_count = child_nodes.length

            # Create a row with the data
            row_data = [go_id, term_name, defstr, child_count]
            sheet.append(row_data)

# Save the workbook as an Excel file
excel_sheet.save("autophagosome.xlsx")


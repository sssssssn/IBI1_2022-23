import openpyxl
import xml.dom.minidom

# Count the number of child nodes
def count_child_nodes(child_id):
    child_node_count = 0
    for term_element in term_elements:
        id_node_child = term_element.getElementsByTagName('id')[0]
        is_a_nodes = term_element.getElementsByTagName('is_a')
        for is_a_node in is_a_nodes:
            is_a_value = is_a_node.firstChild.nodeValue
            if child_id == is_a_value:
               child_node_count += count_child_nodes(id_node_child.firstChild.nodeValue) + 1            
    return child_node_count 

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
            child_count = count_child_nodes(id_element.firstChild.data)
            # Extract the id, name, and definition
            go_id = id_element.firstChild.data if id_element.firstChild else ''
            term_name = name_element.firstChild.data if name_element.firstChild else ''

      
          
            
            # Create a row with the data
            row_data = [go_id, term_name, defstr, child_count]
            sheet.append(row_data)

# Save the workbook as an Excel file
excel_sheet.save("autophagosome.xlsx")


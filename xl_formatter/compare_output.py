import csv

nicola = ('xl_formatter/nicola_nodes.csv', 'r')
formatter = ('xl_formatter/test_export.csv', 'r')
compare_file = ('xl_formatter/comparison.csv', 'w')

master_list = {}

with open('xl_formatter/sun_care_nodes.csv', 'r') as master:
    nicola_file = csv.reader(master)
    for row in nicola_file:
        master_list[row[0]] = ''


with open('xl_formatter/test_export_nodes.csv', 'r') as test:
    node_file = csv.reader(test)
    for row in node_file:
        if row[0] in master_list:
            print('row deleted', row[0])
            del master_list[row[0]]
        else:
            print('row written', row[0])
            master_list[row[0]] = ''

with open('xl_formatter/comparison.csv', 'w') as comparison:
    comparison_file = csv.writer(comparison)
    for key in master_list:
        comparison_file.writerow([key])




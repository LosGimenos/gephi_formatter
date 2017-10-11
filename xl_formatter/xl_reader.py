import re
from openpyxl import load_workbook, Workbook
from .models import TwitterData, InstagramData

def load_input(filename):
    file_path = 'xl_formatter/input_files/' + filename +'.xlsx'
    input_data = load_workbook(file_path, read_only=True)
    ws = input_data.active

    for index, row in enumerate(ws.rows):

        if index == 0:
            continue

        type = row[1].value

        def clean_integer_data(value):
            if value == 'NA':
                value = None
            return value

        content = row[7].value
        clout = row[6].value
        followers = row[105].value

        try:
            author = row[9].value.lower()
        except:
            author = row[9].value

        brand_source = row[121].value
        try:
            brand_source = re.sub(r'\s', '', brand_source)
        except:
            print('Brand Source err', brand_source)

        if (content == 'None' or content == '' or content == None):
            content = row[8].value

        if clout == 'None':
            clout = 0

        if followers == 'NA':
            followers = 0

        if type == 'twitter':

            twitter_data = TwitterData(
                url=row[0].value,
                date=row[2].value,
                author_gender=row[3].value,
                city=row[4].value,
                sentiment=row[5].value,
                author_clout=clout,
                contents=content,
                author=author,
                followers=followers,
                brand_source=brand_source,
                type=type
            )

            twitter_data.save()

        if type == 'instagram':

            instagram_data = InstagramData(
                url=row[0].value,
                date=row[2].value,
                author_gender=row[3].value,
                city=row[4].value,
                sentiment=row[5].value,
                author_clout=clout,
                contents=content,
                author=author,
                followers=followers,
                brand_source=brand_source,
                type = type
            )

            instagram_data.save()

        print(index)

def split_input():
    print('Loading input data')
    file_path = 'xl_formatter/sun_care.xlsx'
    input_data = load_workbook(file_path, read_only=True)
    print('Data load complete!')
    print('Grabbing sheet')
    ws = input_data['Sheet']
    print('Grabbed that sheet!')

    print('start new workbook stuff')
    new_workbook = Workbook(write_only=True)
    new_sheet = new_workbook.create_sheet()
    print('workbook stuff done playa')

    counter = 0
    print('starting the writing process')
    for row in ws.iter_rows():
        row_data = []
        for cell in row:
            row_data.append(cell.value)
        print('appending row!', counter)
        counter += 1
        new_sheet.append(row_data)

    print('All Done writing playa!!!')
    print('Starting save!')
    new_workbook.save('xl_formatter/sun_care_sheet.xlsx')
    print('All done save!')





import csv

from .models import TwitterMention, TwitterData, InstagramMention, InstagramData

def consolodate_edges(edge_edge_fieldnames,edge_ country, source, force_directed=False):
    mention_dict = {}
    base_filename = 'xl_formatter/csv_exports/' + country

    if source == 'twitter':
        mentions = TwitterMention.objects.all()
        filename = base_filename + '_twitter_edges.csv'
    if source == 'instagram':
        mentions = InstagramMention.objects.all()
        filename = base_filename + '_insta_edges.csv'


    for mention in mentions:
        if mention.is_Direct or force_directed:
            direct_or_mixed = 'Directed'
        else:
            direct_or_mixed = 'Mixed'

        if mention.author is None:
            continue

        mention_key = mention.author + ';' + mention.mention + ';' + direct_or_mixed

        if mention_key in mention_dict:
            mention_dict[mention_key]['count'] += 1
        else:
            mention_dict[mention_key] = {'count': 1}

            if source == 'twitter':
                data_id = mention.twitter_data_id
                mention_dict[mention_key]['sort_number'] = data_id
            if source == 'instagram':
                data_id = mention.instagram_data_id
                mention_dict[mention_key]['sort_number'] = data_id

            for fieldname in edge_fieldnames:edge_
                if fieldname == 'Source':
                    mention_dict[mention_key]['author'] = mention.author
                elif fieldname == 'Target':
                    mention_dict[mention_key]['mention'] = mention.mention
                elif fieldname == 'Type':
                    mention_dict[mention_key]['direct_or_mixed'] = direct_or_mixed

    mention_dict_keys = mention_dict.keys()

    with open(filename, 'w') as csv_file:
        writer = csv.DictWriter(csv_file, delimiter=';', fieldnames=edge_fieldnames)
        writer.writeheader()

        for key in mention_dict_keys:
            dict_to_write = {}

            for fieldname in edge_fieldnames:
                if fieldname == 'Source':
                    dict_to_write['Source'] = mention_dict[key]['author']
                elif fieldname == 'Target':
                    dict_to_write['Target'] = mention_dict[key]['mention']
                elif fieldname == 'Type':
                    dict_to_write['Type'] = mention_dict[key]['direct_or_mixed']
                elif fieldname == 'Weight':
                    dict_to_write['Weight'] = mention_dict[key]['count']

            writer.writerow(dict_to_write)

def consolodate_nodes(node_fieldnames, country, source):

    base_filename = 'xl_formatter/csv_exports/' + country

    if source == 'twitter':
        author_data = TwitterData.objects.distinct('author')
        export_filename = base_filename + '_twitter_nodes.csv'
    if source == 'instagram':
        author_data = InstagramData.objects.distinct('author')
        export_filename = base_filename + '_insta_nodes.csv'

    with open(export_filename, 'w') as csv_file:
        fieldnames = ['Id', 'Label', 'Followers', 'Gender', 'BrandSource']
        node_fieldnames.extend(('Id', 'Label'))

        writer = csv.DictWriter(csv_file, delimiter=';', fieldnames=node_fieldnames)
        writer.writeheader()

        for row in authors_data:
            dict_to_write = {
                'Id': row.author,
                'Label': row.author,
            }

            try:
                gender = row.author_gender.lower()
            except:
                gender = 'unknown'

            if gender == 'male':
                gender = 'male'
            elif gender == 'female':
                gender = 'female'
            else:
                gender = 'unknown'

            for fieldname in node_fieldnames:
                if fieldname == 'Followers':
                    dict_to_write['Followers'] = row.followers
                elif fieldname == 'Url':
                    dict_to_write['Url'] = row.url
                elif fieldname == 'Date':
                    dict_to_write['Date'] = row.date
                elif fieldname == 'Gender':
                    dict_to_write['Gender'] = gender
                elif fieldname == 'City':
                    dict_to_write['City'] = row.city
                elif fieldname == 'Sentiment':
                    dict_to_write['Sentiment'] = row.sentiment
                elif fieldname == 'Emotion':
                    dict_to_write['Emotion'] = row.emotion
                elif fieldname == 'Clout':
                    dict_to_write['Clout'] = row.author_clout
                elif fieldname == 'Contents':
                    dict_to_write['Contents'] = row.Contents
                elif fieldname == 'MediaUrlHttp':
                    dict_to_write['Media_Url_Http'] = row.media_url_http
                elif fieldname == 'MediaUrlHttps':
                    dict_to_write['Media_Url_Https'] = row.media_url_https
                elif fieldname == 'Lattitude':
                    dict_to_write['Lattitude'] = row.lattitude
                elif fieldname == 'Longitude':
                    dict_to_write['Longitude'] = row.longitude
                elif fieldname == 'Followers':
                    dict_to_write['Followers'] = row.followers
                elif fieldname == 'Statuses':
                    dict_to_write['Statuses'] = row.statuses
                elif fieldname == 'BrandSource':
                    dict_to_write['BrandSource'] = row.brand_source

            writer.writerow(dict_to_write)


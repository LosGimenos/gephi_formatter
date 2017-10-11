import csv

from .models import TwitterMention, TwitterData, InstagramMention, InstagramData

def consolodate_mentions(country, source, force_directed=False):
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
            if source == 'twitter':
                data_id = mention.twitter_data_id
            if source == 'instagram':
                data_id = mention.instagram_data_id

            mention_dict[mention_key] = {
                'count': 1,
                'author': mention.author,
                'mention': mention.mention,
                'direct_or_mixed': direct_or_mixed,
                'sort_number': data_id
            }

    mention_dict_keys = mention_dict.keys()

    with open(filename, 'w') as csv_file:
        fieldnames = ['Source', 'Target', 'Type', 'Weight']
        writer = csv.DictWriter(csv_file, delimiter=';', fieldnames=fieldnames)
        writer.writeheader()

        for key in mention_dict_keys:
            writer.writerow({
                'Source': mention_dict[key]["author"],
                'Target': mention_dict[key]["mention"],
                'Type': mention_dict[key]["direct_or_mixed"],
                'Weight': mention_dict[key]["count"]
            })

def consolodate_authors(country, source):

    base_filename = 'xl_formatter/csv_exports/' + country

    if source == 'twitter':
        authors_data = TwitterData.objects.distinct('author')
        export_filename = base_filename + '_twitter_nodes.csv'
    if source == 'instagram':
        authors_data = InstagramData.objects.distinct('author')
        export_filename = base_filename + '_insta_nodes.csv'

    with open(export_filename, 'w') as csv_file:
        fieldnames = ['Id', 'Label', 'Followers', 'Gender', 'BrandSource']
        writer = csv.DictWriter(csv_file, delimiter=';', fieldnames=fieldnames)
        writer.writeheader()

        for row in authors_data:
            gender = row.author_gender
            if gender == 'male':
                gender = 'male'
            elif gender == 'female':
                gender = 'female'
            else:
                gender = 'unknown'

            writer.writerow({
                'Id': row.author,
                'Label': row.author,
                'Followers': row.followers,
                'Gender': gender,
                'Source': row.brand_source
            })
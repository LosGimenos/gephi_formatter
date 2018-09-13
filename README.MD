# Gephi Prep Tool

## Initializing

Pull in data from the xl_reader.
xl_reader takes in arguments of the category list of wanted columns.
Also takes in filename.

``` ['followers', 'brand', 'gender', 'content', 'author'] ```

## Extract mentions from data
mention_extractor

Output to csv_export.

``` ['Followers', 'Gender'] ```

nodes:
Id;Label;Followers;Gender

id: username
label: username
followers
gender

Edges:
Source;Target;Type;Weight
source: who tweeted
target: to whom
type: mixed/directed
weight: how many times

## Next steps:
* Consider error handling by type
* Design for better automation and scale



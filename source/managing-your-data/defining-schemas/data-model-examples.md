# Data Model Examples

The following examples illustrate ways to use primary index, and date indexes with your data.

## Example 1: Using a primary, secondary, and date index

If your data has multiple properties that you can use to identify and aggregate data, consider specifying a primary and secondary index on the two most significant properties.

This example dataset stores data on favorite movies. The movie *title* is the main identifier, the movie *director* is the next most significant identifier, and the *date viewed* provides chronological context.

Here is the example data:

```
title,director,cinematography,date viewed 
CODA,Sian Heder,Paula Huidobro,2021-08-13 
Dune,Greig Fraser,Greig Fraser,2021-11-06 
Drive My Car,Ryusuke Hamaguchi,Hidetoshi Shinomiya,2022-04-01 
Wheel of Fortune and Fantasy,Ryusuke Hamaguchi,Yukiko Iioka,2021-05-23
```

After uploading the data and editing the schema, the Movie Favorites Unique Index follows this format.

**Unique Index** = *title + director + date viewed*

Here is a figurative sample Unique Index for the first data row.

**Unique Index** = CODA-SianHeder-20210813

The Movie Favorites dataset *explicitly* specifies the primary index, secondary index, and date components. Next, examine a dataset that *implicitly* uses the ingestion date.

## Example 2: Using an implicit date index

If you have no date data or want time-series data but your date properties are unsuitable, do not specify a date index. Instead, you can implicitly use the current date: the date the data is ingested.

For example, a shopping list needs only a list of items and has no obvious need for a date. So go with the default date. The dates may be useful later. For example, you may want to analyze the frequency you added an item (e.g., toilet paper) and schedule a reminder for that item. The following content represents data for a Shopping List:

```
item 
toothpaste 
apples 
lettuce 
mineral water
```

You can ingest the data into a dataset that explicitly specifies only a primary index. The dataset will use the current date as date index automatically. The Unique Index for the Shopping List is illustrated below.

Format:

**Unique Index** = *item + (nothing) + current date*

Sample:

**Unique Index** = toothpaste-20220411

Now you know how to use a Unique Index to fit your data needs.
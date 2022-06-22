# Examining a Schema

TODO intro

## TODO

TODO move this content to defining your schema

1. TODO. The **Edit schema** interface appears.

    ![](./getting-started-with-an-example-dataset/sample-aapl-dataset-edit-schema.png)

    **Dataset ID** - Name your dataset by giving it a unique ID. On data ingestion, the product makes a best effort to name your dataset, using the data source name (e.g., file name). If a dataset exists with that name, the product suggests a suffix to make the dataset ID unique. 

    ```{important}
    The `_system` prefix (case-insensitive) is reserved for Apperate system tables and columns. You are forbidden to prefix your dataset ID or dataset property names with `_system`.
    ```

    **Properties (table)** The product makes a best effort to
    derive data property names using the column names the dataset provides and
    to derive data types from the data values. Lastly, the product attempted
    to determine a Unique Index
    composed of a primary index key, secondary index key (optional), and date index key.

    In this case, the product correctly set *symbol* as the primary index key and *date* as the date index key. The property types were detected correctly too. We could set a secondary index key too, but we will decline.

    There are more options and content below the *Properties* table.

    ![edit-schema-bottom-sections.png](./getting-started-with-an-example-dataset/edit-schema-bottom-sections.png)

    **Sample API Call** - Shows a URL for getting data from the dataset using the current Unique Index.

    **Unique Index Example** - Illustrates the current Unique Index, composed of the Primary index, Secondary index (optional), and Date index.

    **Opt in to IEX Cloud's Metadata Graph** - Provides the opportunity to map a property to IEX Cloud's metadata data graph of [financial identifiers](../managing-your-data/creating-and-managing-views/joining-on-core-data.md). This allows you to enrich your dataset by joining it to IEX Cloud core equities data or any other dataset that is also opted in. Furthermore, you can ingest data into and query for data in this dataset using IEX Cloud's supported financial identifiers.

    ```{seealso}
    You can learn more about dataset schemas by reading [Understanding Dataset Schemas](../managing-your-data/defining-schemas/data-model-concepts.md).
    ```

    IEX Cloud correctly identified the *symbol* property as containing financial identifiers and therefore opted the dataset in to IEX Cloud's metadata graph.
    
    Since this schema defines our dataset the way we want, click **Create Dataset Now**. The product builds and stores your dataset and your dataset overview appears.
# Early Access Program Info Hub

We are excited that you are participating in the new data infrastructure product Early Access Program and we want to make your experience frictionless and rewarding. To that end, we update this page regularly with the latest information on the following topics:

- Newly added features
- Bug fixes
- Known issues
- Known limitations

## Newly Added Features

Please see the console home page's IEX Cloud Early Access **Ideas Table** and the [Changelog](../reference/changelog.md).

- AWS S3: You can remove an [AWS Integration](../migrating-and-importing-data/accessing-s3-via-storage-integration.md) (credential) and configure a new one.

## Recently Fixed Bugs

These notable bugs were recently fixed. 

- AWS S3: You can now create a dataset from AWS S3 data using any supported credential type: AWS Integration or an Access key + secret access key. 

## Known Issues

Stear clear of the following bugs and unfinished features. When we resolve them, we'll update the appropriate sections above.

- Scheduling: Schedule entry summary error count does not update; a manual page refresh is required to see the updated last time run timestamps and records added counts.

## Known Limitations

You can learn about the product's basic features and functionality in our documentation here on this site. However, much of the documentation is still in progress. Limitations of features not yet documented are listed here:

- **Maximum records per ingestion (during Early Access):** A data ingestion must not exceed 20,000,000 records.

- Dataset queries can only join or select on properties mapped as *Primary index*, *Secondary index* (Subkey), or *Date index*

- Dataset query does not currently support Common Table Expressions (CTEs)

- `CUBE` and `ROLLUP` are the only functions supported in `GROUP BY` clauses. 

---
[Go to Docs Home](https://github.com/iexcloud/docs/blob/main/README.md)

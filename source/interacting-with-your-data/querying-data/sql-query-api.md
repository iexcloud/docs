# SQL Query API

Query

```sql
SELECT * FROM SAMPLE_AAPL_DATASET_AZWDTSJWS 
WHERE (date >= "2021-10-01" AND date <= "2021-10-08")
ORDER BY date ASC
```

Encoded URL

```
https://my.iex.cloud/v1/sql-query/MY?sqlQuery=SELECT%20*%20FROM%20SAMPLE_AAPL_DATASET_AZWDTSJWS%20\%20WHERE%20(date%20%3E=%20%222021-10-01%22%20AND%20date%20%3C=%20%222021-10-08%22)%20\%20ORDER%20BY%20date%20ASC&token=sk_TOKEN
```

Results:

```javascript
[
    {
        "close": 142.65,
        "date": "2021-10-01",
        "high": 142.92,
        "low": 139.1101,
        "open": 141.9,
        "symbol": "AAPL",
        "volume": 94639581
    },
    {
        "close": 139.14,
        "date": "2021-10-04",
        "high": 142.21,
        "low": 138.27,
        "open": 141.76,
        "symbol": "AAPL",
        "volume": 98322008
    },
    {
        "close": 141.11,
        "date": "2021-10-05",
        "high": 142.24,
        "low": 139.36,
        "open": 139.49,
        "symbol": "AAPL",
        "volume": 80861062
    },
    {
        "close": 142,
        "date": "2021-10-06",
        "high": 142.15,
        "low": 138.37,
        "open": 139.47,
        "symbol": "AAPL",
        "volume": 83221119
    },
    {
        "close": 143.29,
        "date": "2021-10-07",
        "high": 144.215,
        "low": 142.72,
        "open": 143.06,
        "symbol": "AAPL",
        "volume": 61732656
    },
    {
        "close": 142.9,
        "date": "2021-10-08",
        "high": 144.1781,
        "low": 142.56,
        "open": 144.03,
        "symbol": "AAPL",
        "volume": 58773155
    }
]
```
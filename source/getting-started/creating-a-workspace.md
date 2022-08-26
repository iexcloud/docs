# Creating a Workspace

A *workspace* is your unique domain for writing data and querying it, and delivering data to a apps. Your workspace name appears in your API URLs and is used in Apperate API calls, such as `GET /data/:workspace`.

**Base URL:**

```
https://WORKSPACE.iex.cloud/v1
```

**Example Workspace URL:**

```
https://mycompany.iex.cloud/v1
```

In the URL above, the workspace name `mycompany` is the subdomain of `iex.cloud`.

It's time to create a workspace.

**Prerequisites:**

- **IEX Cloud Apperate account** - Create one [here](https://iexcloud.io/cloud-login#/register).
- **Apperate workspace** - See [Creating a Workspace](../getting-started/creating-a-workspace.md). 

## Steps

Here's how to create a workspace:

1. Click on the link in your invitation email. The welcome page appears and prompts you to create your workspace.

    ![](./getting-started-with-apperate/create-a-workspace.png)

1. Name your workspace.

    > **Important:** The workspace name is permanent, so make sure to name it exactly how you want it.

    Workspace names have the following requirements.

    **Name requirements:**

    - Starts with a letter
    - Ends with a letter or number
    - Uses only lowercase alphanumeric characters and dashes
    - Is between 2-63 characters long
    - DOES NOT consist of ALL numeric values

1. After agreeing to the terms, click **Submit**. The **Create a dataset** page appears.

    ![](./getting-started-with-apperate/create-a-dataset.png)

Your workspace is created and ready for delivering data to your apps!

## What's Next

If you want to use IEX Cloud Core Data in your apps, please see [Using IEX Cloud Core Financial Data](../using-core-data.md).

If you need to store application data, learn how at [Writing and Fetching a Data Record](../getting-started/writing-and-fetching-a-record.md).

If you have data that you'd like to use with your apps, pull it into Apperate as demonstrated in [Migrating and Importing Data](../migrating-and-importing-data.md).


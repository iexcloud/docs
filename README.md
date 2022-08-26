# IEX Cloud Apperate Documentation 

The Apperate documentation is published to <https://iexcloud.io/documentation/>.

We write Markdown files that use an expansion syntax called MyST. Here are some helpful Markdown MyST articles.

- [CommonMark](https://myst-parser.readthedocs.io/en/latest/syntax/syntax.html) basic syntax.
- [Articles](https://pradyunsg.me/furo/reference/) that contain additional examples that include extensions we use via the Euro theme. Make sure to view examples via the Markdown (MyST) tabs.

All of the articles are nested in the `source/` folder. The article/section hierarchy follows the `source/` folder's nested hierarchy of Markdown files (`.md`) and folders. 

Here is a representative sampling of repository files:

| File | Description |
| --- | --- |
| `source/administration/managing-users.md` | A regular article. |
| `source/administration/access-and-security/` | Folder containing the article’s image files. |
| `source/migrating-and-importing-data.md` | A section intro article (i.e., a parent article). It lists the section articles and can also contain Markdown text. |
| `source/migrating-and-importing-data/` | This folder…<br> - Contains the parent article’s image files<br>- Contains the child articles and their image file folders |

## Related Topics

[Build instructions](./BUILD_INSTRUCTIONS.md)
# Elastic-Jekyll

Full-text search for your Jekyll blog with ElasticSearch.

## Features

 - Parses the html from your Jekyll `_site` directory using BeautifulSoup to get more accurate content instead of using the raw Markdown.
 - Automates the process of updating your ElasticSearch index to store the post title, url and body, ready for querying from your site.
 - Searching on the generated ElasticSearch index which can be hosted on a server and then called by Javascript on your Jekyll blog to retrieve results.

## Example Usage

### Indexing:

 - Make sure you have an ElasticSearch server running. If not local, change the config in `indexer.py` to reflect your location.
 - Run the command `python main.py <path_to_blog>`, running without an argument will assume your compiled blog is located at `~/blog/_site`.
 - If the library cannot find your content correctly, modify `indexer.py` to point to the correct HTML elements for title, post content etc (assuming you have unique CSS classes for these).

### Searching:

 - See sample query on the ElasticSearch index in the  `searcher.py` script.
 - Results include the url to the post, the post title and a highlight of the relevant text that can be shown to the user.

 ### When to run

 Due the fact that the library relies on the generated output within the `_site` directory, you will need to re-run the indexer *after* you have re-built your blog when making changes. This unfortunately means that we cannot use something like Git webhooks to further automate the process, however it is still easy when put inside a script to execute after your site is built.




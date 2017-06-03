from elasticsearch import Elasticsearch
import os
import re

index_name = "blog"
doc_type = "post"

def connect_elastic(host="localhost", port=9200):
    return Elasticsearch([{'host': 'localhost', 'port': 9200}])

def refresh_index(es):
    if es.indices.exists(index=index_name):
        es.indices.delete(index=index_name)
    es.indices.create(index=index_name)

def index_posts(es, posts):
    for post in posts:
        doc = {
            "title": post.title,
            "url": post.url,
            "body": post.body
        }

        es.index(index=index_name, doc_type=doc_type, id=post.id, body=doc)
        print("Created doc for " + post.url)


# POST /blog/post/_search
# {
#     "query": {
#       "multi_match": {
#         "query": "python",
#         "type": "best_fields",
#         "fuzziness": "AUTO",
#         "tie_breaker": 0.3,
#         "fields": ["title^3", "body"]
#       }
#     },
#     "highlight": {
#         "fields" : {
#             "body" : {}
#         }
#     },
#     "_source": ["title", "url"]
# }

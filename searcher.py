from elasticsearch import Elasticsearch

es =  Elasticsearch([{'host': 'localhost', 'port': 9200}])

user_query = "python"

query = {
    "query": {
      "multi_match": {
        "query": user_query,
        "type": "best_fields",
        "fuzziness": "AUTO",
        "tie_breaker": 0.3,
        "fields": ["title^3", "body"]
      }
    },
    "highlight": {
        "fields" : {
            "body" : {}
        }
    },
    "_source": ["title", "url"]
}

res = es.search(index="blog", body=query)
print("Found %d Hits:" % res['hits']['total'])

for hit in res['hits']['hits']:
    print(hit["_source"])

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

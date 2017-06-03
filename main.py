import sys
from find_posts import create_posts
import indexer

base_dir = "~/blog/_site"

if __name__ == "__main__":
    # provide blog base directory as arg
    if len(sys.argv) > 0:
        base_dir = str(sys.argv[1])

    print("Finding posts in %s" % base_dir)

    posts = create_posts(base_dir)
    print("Posts created")

    es = indexer.connect_elastic()
    print("ElasticSearch connection established")

    indexer.refresh_index(es)
    print("Current blog index removed")

    indexer.index_posts(es, posts)
    print("Finished indexing posts")

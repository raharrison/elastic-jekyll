import glob
from bs4 import BeautifulSoup
from post import Post

def find_post_paths(base_dir):
    files = glob.glob(base_dir + "/20*/*/*/*.html")
    files = [f.replace("\\", "/") for f in files]
    return files

def parse_post(path):
    with open(path, encoding="utf8") as f:
        contents = f.read()

        soup = BeautifulSoup(contents, 'html.parser')
        title = soup.find('h1', { "class" : "post-title" }).text.strip()
        
        post_elem = soup.find("div", {"class": "post"})
        post_elem.find(attrs={"class": "post-title"}).decompose()
        post_elem.find(attrs={"class": "post-date"}).decompose()

        paras = post_elem.find_all(text=True)

        body = " ".join(p.strip() for p in paras).replace("  ", " ").strip()
        # remove special characters

        return (title, body)

    raise "Could not read file: " + path


def create_posts(base_dir):
    paths = find_post_paths(base_dir)
    for path in paths:
        url = path.replace(base_dir, "")
        (title, body) = parse_post(path)
        yield Post(title, url, body)

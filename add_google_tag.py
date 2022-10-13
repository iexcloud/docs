import os
from pathlib import Path

google_tag = """

    <!-- Google tag (gtag.js) -->
    <script async src="https://www.googletagmanager.com/gtag/js?id=G-M0MJ9E8ZP5"></script>
    <script>
        window.dataLayer = window.dataLayer || [];
        function gtag(){dataLayer.push(arguments);}
        gtag('js', new Date());
        gtag('config', 'G-M0MJ9E8ZP5');
    </script>

  """

target_tag = "</head>"

def addTag(fname):
    file = open(fname, "rt")
    str = file.read()
    file.close()

    head_split = str.split(target_tag, 1)
    new_str = head_split[0] + google_tag + target_tag + head_split[1]
    file = open(fname, "wt")
    file.write(new_str)
    file.close()

def main():
    paths = sorted(Path("build").rglob("*.html"))
    for path in paths:
        addTag(os.fspath(path))

if __name__ == "__main__":
    main()
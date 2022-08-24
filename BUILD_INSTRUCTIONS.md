# Building Instructions

The site uses the [Sphinx](https://www.sphinx-doc.org/en/master/index.html) static site generator (SSG). The articles are written in Markdown and then converted to static HTML files using Sphinx and the [MyST parser](https://myst-parser.readthedocs.io/en/latest/). This site uses [ReStructured Text](https://docutils.sourceforge.io/docs/user/rst/quickref.html) (RST) text in the index.rst file and in section Markdown files to specify the site tree.

Building the docs site requires Python and several external plugins for Sphinx. Running the build generates HTML files to the `build/html` folder. Any web server can serve up the site by pointing to the `index.html` file.

### Requirements

Note: You can install the following software packages using Pip, [MiniConda](https://docs.conda.io/en/latest/miniconda.html) (includes Python), or a similar software installer. ([MiniConda3 for Linux 64-bit](https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh)).

> **Note:** The [.github/workflows/main.yml] file demonstrates installing all of the software.

Required software:

- [Python](https://www.python.org/downloads/): Sphinx is written in Python and requires Python 3.6+.

- [Sphinx](https://www.sphinx-doc.org/en/master/usage/installation.html): Provides the static site generator and infrastructure. 

    ```bash
    sudo yum install python-sphinx
    ```

- [Furo Theme](https://github.com/pradyunsg/furo): Furo is a rich, responsive theme that includes key features such as a local table of contents (TOC) for each article. Please refer to the [Furo documentation](https://pradyunsg.me/furo/) site which explains using the Furo theme and of course uses it).

    ```bash
    conda install -c conda-forge furo
    ```

- Sphinx extensions

    - MyST Parser enables writing articles in Markdown and structuring the file tree using RST-like declarations. The parser converts the Markdown files to HTML.
    - [Sphinx Rediraffe extenstion](https://pypi.org/project/sphinxext-rediraffe/) enables redirecting HTTP requests for an removed/replaced article with to a replacement article.
    - Other extensions below provide authoring features to use in our documentation.

    ```bash
    conda install -c conda-forge myst-parser
    conda install -c conda-forge sphinx-copybutton
    conda install -c conda-forge sphinx-design
    conda install -c conda-forge sphinx-inline-tabs
    ```

    ```bash
    sudo pip install sphinxext-rediraffe==v0.2.7
    ```

### Building the Site

```bash
cd docs
```

```bash
make html
```

The static HTML files are written to `docs/build/html`.

### Serving the Site

Any web server can host the site by pointing to `docs/build/html/index.html`.

#### Previewing the Site

If you want to build the site locally to preview it, you can use a web server such as Python's SimpleHTTPServer. Here are commands for running it:

```bash
cd docs/build/html
```

```bash
python3 -m http.server 8000
```

The site is available locally at port `8000`: <http://0.0.0.0:8000/>

#### Running on a Remote Machine

If you are running the site from a remote machine dev box, forward the port on your laptop by running this command on your laptop, making sure to replace `username` (laptop user), username (e.g., `firstname.lastname`), and dev box IP address `10.101.0.30` with your values.

```bash
ssh -F /Users/username/.ssh/config -i /Users/username/.ssh/id_rsa -L 8000:127.0.0.1:8000 -C -N firstname.lastname@10.101.0.30 &
```

The site is available here: <http://0.0.0.0:8000/>

## Contributing Fixes

You can contribute documentation fixes by editing the articles (`.md` files nested in the `source` folder) in a branch and sending your branch in a pull request to the `main` branch here on GitHub.
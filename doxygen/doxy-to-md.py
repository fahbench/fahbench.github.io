from xml.etree import ElementTree
from jinja2 import Template
import glob
import re
import os

# TODO: refactor template into file
# TODO: refactor index.md into file
# TODO: hide section when there's no attributes/functions
# TODO: order pages


template = Template(
"""---
title: {{klass.name}}
layout: api

---

### Public attributes

{: .table .table-striped .table-condensed}
| type   | name     |
|:-------|:---------|
{% for atr in klass.public_attr -%}
| {{atr.typ.text}} | {{atr.name}} |
{% endfor %}


### Public functions

{: .table .table-striped .table-condensed}
| type   | name     |
|:-------|:---------|
{% for atr in klass.public_func -%}
| {{atr.typ.text}} | {{atr.name}} |
{% endfor %}

"""
)


class Possibly_ref:
    def __init__(self, e):

        desc = e.find("ref")
        if desc is not None:
            self.text = "[{}]({})".format(desc.text, "{{site.url}}/")
        else:
            self.text = e.text

class Memberdef:
    def __init__(self, e):
        self.typ = Possibly_ref(e.find("type"))
        self.name = e.find("name").text

        if e.find("argsstring") is not None:
            self.name += e.findtext("argsstring", 'uh oh!')


INDIR = 'xml'
OUTDIR = '../_api'

class Klass:
    def __init__(self, e):
        self.name = e.findtext("compoundname")
        self.url = "{{{{site.url}}}}/{}/{}.html".format(OUTDIR, self.name)

        public_attr_node = e.find("sectiondef[@kind='public-attrib']")
        if public_attr_node is not None:
            self.public_attr = [Memberdef(x)
                                for x in public_attr_node.findall("memberdef")]
        else:
            self.public_attr = []

        public_func_node = e.find("sectiondef[@kind='public-func']")
        if public_func_node is not None:
            self.public_func = [Memberdef(x)
                                for x in public_func_node.findall("memberdef")]
        else:
            self.public_func = []

def do_class(name):
    tree = ElementTree.parse('{}/class{}.xml'.format(INDIR, name))
    root = tree.getroot()
    k = Klass(root.find("compounddef"))

    ret = template.render(klass=k)
    print(ret)

    with open("{}/{}.md".format(OUTDIR, name), 'w') as f:
        f.write(ret)

    return k


def main():
    os.makedirs(OUTDIR, exist_ok=True)
    for fn in glob.glob("xml/class*.xml"):
        name = re.search(r"class(\w+)\.xml", fn).group(1)
        do_class(name)

    with open("{}/index.md".format(OUTDIR), 'w') as f:
        f.write("\n".join([
            "---",
            "title: API Index",
            "layout: api",
            "---",
            "",
            "Use the sidebar to view API documentation",
            ""]))


main()

#!/usr/bin/env python3

import re
import yaml
import pprint
import frontmatter
import logging

fm = frontmatter.Frontmatter()

log = logging.getLogger()
logging.basicConfig()

bodyreg = re.compile(
    r"(\n*### \[([^\n]*)\] *)\n(.*?)\n+(INLETS?: *\n+(.*?)\n)?(OUTLETS?: *\n+(.*?)\n)?(ARGUMENTS?: *\n+(.*?)\n)?(### Inlets . Outlets *\n+.*?\n)?(> see also (.*?)\n)?(> updated for Pd version (.*?)\.?)?\n*$",
    re.DOTALL,
)


def parse_iolets(ioletstr, multiple=True):
    def parse_iolet(iolet):
        result = {}
        for l in iolet.splitlines():
            l = l.strip()
            if not l:
                continue
            if l.startswith("-"):
                x = re.findall("^- (.*) - (.*)", l)
                if x:
                    msg, descr = x[0]
                    result[msg] = descr
            else:
                log.error("OOOOPSIE: %s" % (l,))
        return result

    ioletstr = ioletstr.strip()
    if "- NONE" == ioletstr:
        return None

    if not multiple:
        # single iolet
        return {"1st": parse_iolet(ioletstr)}

    # multiple iolets
    result = {}
    ioletdata = []
    ioletid = ""
    for l in ioletstr.splitlines():
        if l.startswith("-"):
            if ioletid and ioletdata:
                result[ioletid] = parse_iolet("\n".join(ioletdata))
            ioletdata = []
            ioletid = l.strip().lstrip("-").rstrip(":").strip()
            continue
        ioletdata.append(l.strip())
    if ioletid and ioletdata:
        result[ioletid] = parse_iolet("\n".join(ioletdata))
    return result


class ObjectFile:
    def __init__(self, filename):
        data = fm.read_file(filename)
        self.data = data["attributes"]
        # parse the body!
        # body typically starts with '### [<objectname>]'
        # followed by '\n\n<description>\n\n'
        # followed by some lines of descriptive text
        # finally there's the formal part:
        # 'INLET:' (or 'INLETS:')
        # followed by a list of inlet descriptions
        # 'OUTLET:' (or 'OUTLETS:')
        # followed by a list of outlet descriptions
        # 'ARGUMENT:' (or 'ARGUMENTS:')
        # followed by a list of argument descriptions
        # "> see also" (optional)
        # "> updated for Pd version <version>" (optional)

        # for line in data['body'].strip().splitlines():

        dataparsed = [_.strip() for _ in bodyreg.findall(data["body"] + "\n")[0]]
        try:
            (
                _,
                title,
                body,
                inlets_full,
                inlets,
                outlets_full,
                outlets,
                _,
                arguments,
                _,
                _,
                see_also,
                _,
                last_update,
            ) = dataparsed
        except IndexError as e:
            pprint.pprint(data["body"])
            pprint.pprint(dataparsed)
            raise e

        # check if the first line of the body just repeats the description
        # and if so drop that line
        bodylines = body.strip().splitlines()
        desc = bodylines[0].strip().rstrip(".").lower()
        if desc == self.data["description"].strip().rstrip(".").lower():
            body = "\n".join(bodylines[1:])

        body = body.strip()
        if body == "Does something.":
            body = ""

        self.body = body

        # the title and the heading should match...
        # (if they don't, we trust the title)
        if title != self.data["title"].strip().lstrip("[").rstrip("]"):
            log.warning("title mismatch: %s != %s" % (title, self.data["title"]))

        ## inlets/outlets/arguments are structured
        self.data["inlets"] = parse_iolets(inlets, "INLETS" in inlets_full)
        self.data["outlets"] = parse_iolets(outlets, "OUTLETS" in outlets_full)
        arguments = parse_iolets(arguments, False)
        if arguments:
            self.data["arguments"] = arguments.get("1st")

        # as is the "see also"
        self.data["see_also"] = see_also.strip()

        self.data["last_update"] = last_update.strip()

        self.data = {k: v for k, v in self.data.items() if v != "" and v != None}

    def __str__(self):
        return self.frontmatter() + "\n" + self.body

    def frontmatter(self):
        return "\n".join(["---", yaml.dump(self.data), "---"])


if __name__ == "__main__":
    import sys

    def printOF(of):
        x = str(of)
        # x = of.data.get("last_update")
        # x = of.data.get("inlets")
        # x = of.body
        if x:
            print(x)
            print("=============================================")

    for f in sys.argv[1:]:
        try:
            of = ObjectFile(f)
            printOF(of)
        except IndexError as e:
            log.exception("OOPSIE: %s" % (f,))

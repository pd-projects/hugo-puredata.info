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
                _,
                inlets,
                _,
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
        bodylines = body.strip().splitlines()
        desc = bodylines[0].strip().rstrip(".").lower()
        if desc == self.data["description"].strip().rstrip(".").lower():
            body = "\n".join(bodylines[1:]).strip()

        if title != self.data["title"].strip().lstrip("[").rstrip("]"):
            log.warning("title-mismatch: %s != %s" % (title, self.data["title"]))

        # self.data["title"] = title.strip()
        # self.data["body"] = body.strip()
        self.data["inlets"] = inlets.strip()
        self.data["outlets"] = outlets.strip()
        self.data["arguments"] = arguments.strip()
        self.data["see_also"] = see_also.strip()
        self.data["last_update"] = last_update.strip()

        self.data = {k: v for k, v in self.data.items() if v != ""}

        self.body = body

    def __str__(self):
        return self.frontmatter() + "\n" + self.body

    def frontmatter(self):
        return "\n".join(["---", yaml.dump(self.data), "---"])


if __name__ == "__main__":
    import sys

    def printOF(of):
        print(of)
        print("=============================================")

    for f in sys.argv[1:]:
        try:
            of = ObjectFile(f)
            printOF(of)
        except IndexError as e:
            log.exception("OOPSIE: %s" % (f,))

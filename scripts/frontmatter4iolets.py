#!/usr/bin/env python3

import re
import yaml
import pprint
import frontmatter
import logging
import collections

try:
    import json
except ImportError:
    json = None
try:
    import toml
except ImportError:
    toml = None

log = logging.getLogger()
logging.basicConfig()

# allow to export OrderedDicts as YAML
_mapping_tag = yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG


def dict_representer(dumper, data):
    return dumper.represent_mapping(_mapping_tag, data.items())


yaml.add_representer(collections.OrderedDict, dict_representer)

# read markdown with frontmatter
fm = frontmatter.Frontmatter()

bodyreg = re.compile(
    r"(\n*### \[([^\n]*)\] *)\n(.*?)\n+(INLETS?: *\n+(.*?)\n)?(OUTLETS?: *\n+(.*?)\n)?(ARGUMENTS?: *\n+(.*?)\n)?(### Inlets . Outlets *\n+.*?\n)?(> see also (.*?)\n)?(> updated for Pd version (.*?)\.?)?\n*$",
    re.DOTALL,
)


def dehtml(x):
    try:
        return x.replace("&lt;", "<").replace("&gt;", ">")
    except:
        return x


def dict2order(d, keys):
    d = dict(d)
    o = collections.OrderedDict()
    for k in keys:
        if k in d:
            o[k] = d[k]
            del d[k]
    o.update(d)
    return o


class ObjectFile:
    YAML = 0
    TOML = 1
    JSON = 2

    def __init__(self, filename):
        self.filename = filename
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
        if bodylines:
            desc = bodylines[0].strip().rstrip(".").lower()
            if desc == self.data["description"].strip().rstrip(".").lower():
                body = "\n".join(bodylines[1:])

        body = body.strip()
        if body == "Does something.":
            body = ""

        self.body = body

        # the title and the heading should match...
        # (if they don't, we trust the title)
        self.data["title"] = self.data["title"].strip().lstrip("[").rstrip("]")
        if title != self.data["title"]:
            log.warning("title mismatch: %s != %s" % (title, self.data["title"]))

        ## inlets/outlets/arguments are structured
        self.data["inlets"] = self.parse_iolets(inlets, "INLETS" in inlets_full)
        self.data["outlets"] = self.parse_iolets(outlets, "OUTLETS" in outlets_full)
        arguments = self.parse_iolets(arguments, False)
        if arguments:
            self.data["arguments"] = arguments.get("1st")

        # as is the "see also"
        self.data["see_also"] = re.findall(r"\[\[([^]]*)\]\]", see_also.strip())

        self.data["last_update"] = last_update.strip()

        self.data = dict2order(
            {k: v for k, v in self.data.items() if v == 0 or v},
            [
                "title",
                "description",
                "bref",
                "categories",
                "last_update",
                "see_also",
                "arguments",
                "inlets",
                "outlets",
            ],
        )

    def parse_iolets(self, ioletstr, multiple=True):
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
                        result[dehtml(msg)] = dehtml(descr)
                else:
                    log.error("OOOOPSIE[%s]: %s" % (self.filename, l))
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

    def __str__(self):
        return self.toString()

    def yaml(self):
        return "\n".join(["---", yaml.dump(self.data), "---"])

    def toml(self):
        return "\n".join(["+++", toml.dumps(self.data), "+++"])

    def json(self):
        return json.dumps(self.data, indent=2)

    def toString(self, format=YAML):
        if ObjectFile.YAML == format:
            return self.yaml() + "\n" + self.body.strip() + "\n"
        if ObjectFile.TOML == format:
            return self.toml() + "\n" + self.body.strip() + "\n"
        if ObjectFile.JSON == format:
            return self.json() + "\n\n" + self.body.strip() + "\n"


if __name__ == "__main__":
    import os

    def getConfig():
        import argparse

        formats = []
        if yaml:
            formats.append("yaml")
        if toml:
            formats.append("toml")
        if json:
            formats.append("json")

        if not formats:
            import sys

            log.fatal("no output format available")
            sys.exit(1)

        defaults = {
            "verbosity": 0,
            "format": formats[0],
        }

        parser = argparse.ArgumentParser()
        parser.set_defaults(**defaults)
        parser.add_argument(
            "-O",
            "--outdir",
            help="Output directory for converted files (default: overwrite input files)",
        )

        parser.add_argument(
            "--format",
            choices=formats,
            help="Write output frontmatter in the given format (DEFAULT: {format})".format(
                **defaults
            ),
        )

        parser.add_argument(
            "-q",
            "--quiet",
            action="count",
            default=0,
            help="lower verbosity",
        )
        parser.add_argument(
            "-v",
            "--verbose",
            action="count",
            default=0,
            help="raise verbosity",
        )

        parser.add_argument(
            "files",
            nargs="+",
            metavar="MDFILE",
            help="markdown file to convert",
        )

        args = parser.parse_args()
        verbosity = int(args.verbosity) + args.verbose - args.quiet
        del args.verbose
        del args.quiet

        if args.format == "toml":
            args.format = ObjectFile.TOML
        elif args.format == "json":
            args.format = ObjectFile.JSON
        else:
            args.format = ObjectFile.YAML

        return args

    def printOF(of):
        x = str(of)
        # x = of.data.get("last_update")
        # x = of.data.get("inlets")
        # x = of.body
        if x:
            print(x)
            print("=============================================")

    cfg = getConfig()
    logging.getLogger().setLevel(logging.WARNING - (10 * cfg.verbosity))

    for infile in cfg.files:
        try:
            parsed = ObjectFile(infile)
            # printOF(parsed)
            if cfg.outdir:
                outfile = os.path.join(cfg.outdir, os.path.basename(infile))
            else:
                outfile = infile
            with open(outfile, "w") as ofile:
                ofile.write(parsed.toString(cfg.format))

        except IndexError as e:
            log.exception("OOPSIE: %s" % (infile,))

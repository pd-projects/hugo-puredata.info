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


def dict2order(d, keys):
    d = dict(d)
    o = collections.OrderedDict()
    for k in keys:
        if k in d:
            o[k] = d[k]
            del d[k]
    o.update(d)
    return o


def map2list(d, key="type", value="description", other="remark"):
    result = []
    try:
        for k, v in d.items():
            od = collections.OrderedDict()
            od[key] = k
            od[value] = v
            result.append(od)
    except AttributeError:
        result = d
    return result


def iolet_map2list(d, key="type", value="description", other="remark"):
    result = collections.OrderedDict()
    for iolet in d:
        if d[iolet]:
            x = map2list(d[iolet], key, value, other)
            if x:
                result[iolet] = x
        else:
            result[other] = iolet
    return result


class ObjectFile:
    YAML = 0
    TOML = 1
    JSON = 2

    def __init__(self, filename):
        self.filename = filename
        data = fm.read_file(filename)
        self.data = data["attributes"]
        self.body = data["body"]

        def fix_iolets(name):
            if name not in self.data:
                return
            self.data[name] = iolet_map2list(self.data[name])

        def fix_args(name, key, value):
            if name not in self.data:
                return
            self.data[name] = map2list(self.data[name], key, value)

        fix_iolets("inlets")
        fix_iolets("outlets")
        fix_args("arguments", "type", "description")
        fix_args("flags", "flag", "description")
        fix_args("methods", "method", "description")

        self.data = dict2order(
            {k: v for k, v in self.data.items() if v == 0 or v},
            [
                "title",
                "description",
                "categories",
                "pdcategory",
                "last_update",
                "see_also",
                "arguments",
                "flags",
                "inlets",
                "outlets",
            ],
        )

    def __str__(self):
        return self.toString()

    def yaml(self):
        return "\n".join(["---", yaml.dump(self.data).strip(), "---"])

    def toml(self):
        return "\n".join(["+++", toml.dumps(self.data).strip(), "+++"])

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

        except Exception as e:
            log.exception("OOPSIE: %s" % (infile,))

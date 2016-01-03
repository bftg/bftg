#!/usr/bin/env python3

import argparse
import sys
import git_download as gd
import patch
import template
import os

supported_gcc_versions = ["5.3.0"]
supported_binutils_versions = ["2.24"]
supported_newlib_versions = ["1.18.0"]

default_version_index = -1
default_software_packages = [
  "binutils-" + supported_binutils_versions[default_version_index],
  "gcc-"      + supported_gcc_versions[     default_version_index],
  "newlib-"   + supported_newlib_versions[  default_version_index],
]

default_git_base_url  = "git@github.com:bftg/"

def parse_options():
  parser = argparse.ArgumentParser(
    description="The Big Fucking Toolchain Generator")

  parser.add_argument("-t", "--target", type=str,
                      help="target name")
  parser.add_argument("-s", "--os", type=str,
                      help="""OS name, specify if you want a toolchain for your
                      own operating system""")
  parser.add_argument("-p", "--prefix", type=str,
                      help="install prefix",
                      required=True)
  parser.add_argument("-o", "--output", type=str,
                     default="output",
                     help="output directoy for generated files")
  parser.add_argument("--gits", type=str,
                      default=default_git_base_url,
                      dest='git_loc')
  parser.add_argument("--software", type=str, nargs="+",
                      default=default_software_packages,
                      dest="software_packages")

  return parser.parse_args()

def mkdir(directory):
  if not os.path.isdir(directory):
    os.mkdir(directory)

def need_patch(args):
  return args.os != None

def get_software_loc(software, args):
  return args.output + "/" + software_name(software)

def get_software_git_loc(software, args):
  return get_software_loc(software, args) + "/" + software

def software_version(software):
  return software.split("-", 1)[1]

def software_name(software):
  return software.split("-", 1)[0]

def main():
  args = parse_options()

  if not gd.download_gits(args):
    print("Failed to download gits")
    return 1

  if need_patch(args):
    if not patch.patch_software_packages(args):
      print("Failed to patch software")
      return 1

  if not template.generate_makefiles(args):
    print("Failed to generate Makefile", file=sys.stderr)
    return 1

  return 0

if __name__ == "__main__":
  sys.exit(main())

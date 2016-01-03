from subprocess import call
import os
import sys
import shutil
import bftg

def get_git_url(software, args):
  return args.git_loc + software

def download_gits(args):
  if os.path.isdir(args.output):
    print("Deleting \"" + args.output + "\"")
    shutil.rmtree(args.output)
  bftg.mkdir(args.output)
  for sp in args.software_packages:
      if not download_git(sp, args):
        return False

  return True

def download_git(software, args):
  directory = bftg.get_software_git_loc(software, args)
  url = get_git_url(software, args)
  bftg.mkdir(bftg.get_software_loc(software, args))
  if os.path.isdir(directory):
    print("Deleting " + directory)
    shutil.rmtree(directory)

  print("Downloading " + software)
  res = call(["git", "clone", url, directory]) == 0
  if not res:
    print("Failed to download " + software)
  return res

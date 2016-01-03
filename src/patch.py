from subprocess import call
import bftg
import template

def patch_software_packages(args):
  for sp in args.software_packages:
    if not patch_software_package(sp, args):
      return False

  return True

def patch_software_package(software, args):
  patch = template.generate_patch(software, args)
  version = bftg.software_version(software)
  with open(patch, "r") as patch_file:
    print("Patching " + software)
    call(["patch", "-p1", "-d",
          bftg.get_software_git_loc(software, args)], stdin=patch_file)
  return True

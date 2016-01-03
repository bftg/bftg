from pyratemp import pyratemp
import os
import bftg

patch_tmp_dir = "tmp"

def get_makefile_template_loc(software):
  return ("templates/" + bftg.software_name(software) + "/" +
          bftg.software_version(software) + "/Makefile.tmpl")

def get_patch_template_loc(software, args):
  return ("templates/" + bftg.software_name(software) + "/" +
          bftg.software_version(software) + "/patch.tmpl")

def tmp_patch_file_name(software):
  return patch_tmp_dir + "/" + software + ".patch"

def generate_makefiles(args):
  for sp in args.software_packages:
    tmpl = pyratemp.Template(filename=get_makefile_template_loc(sp))
    result = tmpl(prefix=args.prefix, version=bftg.software_version(sp),
                  target=args.target, osname=args.os)
    with open(bftg.get_software_loc(sp, args) +"/Makefile", "w") as text_file:
      os.write(text_file.fileno(), result.encode("utf-8"))
  return True

def generate_patch(software, args):
  bftg.mkdir(patch_tmp_dir)

  tmpl = pyratemp.Template(filename=get_patch_template_loc(software, args))
  result = tmpl(osname=args.os, OSNAME=args.os.upper())
  filename = tmp_patch_file_name(software)
  with open(filename, "w") as patch_file:
    os.write(patch_file.fileno(), result.encode("utf-8"))
  return filename

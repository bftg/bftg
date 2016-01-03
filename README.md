# bftg
The Big F***ing Toolchain Generator

# Description

bftg generates a cross compiling toolchain, specifically for a custom operating
system.  It was created for a couple reasons:

1. Having worked on different OS projects I was sick of having to rip out the
   changes to binutils, gcc and newlib and rename things to work with the new
   project.

2. After upgrading the development environment OS the gcc on my machine would
   fail to build to toolchain.  Sometimes this would be because new warnings
   were added, so configuring one or more of the projects with
   `--disable-werror` would solve the problem, sometimes it was more
   complicated.

To meet these goals bftg was created.  Point (1) is addressed with the bftg
program.  It will download the git repos for the necessary software packages and
patch them appropriately.

Just as important is point (2) ensuring that the toolchains created will
continue to compile as the development environment is upgraded.  As previously
stated, upgrading the development environment can cause the older toolchain to
not build.  You are left with a few options, none of them perhaps unreasonable
but annoying nonetheless:

* Don't upgrade your development environment.  This might not be an option if
  you work at a university or company with system administrators that ultimately
  control your machine.

* Upgrade the toolchain being used.  If you want to do this great, bftg can help
  you generate a new toolchain.  However, sometimes causing the toolchain
  upgrade will cause some issues for your code that in the perfect world you
  would deal with right away but the world is not perfect.

* Kludge together your old development environment on your new machine: ugly

* Use a virtual machine for your development environment: slow, can start to eat
  up a lot of space if you need one VM per OS project and you have a lot of
  projects.

So to prevent this from happening the second component of bftg will be a set of
automated tests along with modified versions of the toolchain software packages.
The modified software packages will ensure that older versions will continue to
build with newer development environments.  The automated tests will of course
make sure that any change works not just on the tested development environment
but all the development environments that are supported.  You will note a
keyword in the first sentence of this paragraph: **will**.  That is because at
this time this is not done yet.

# Usage

As of right now the only way to use bftg is to specify everything via the
command line (configuration files will helpful being come soon).  A typical use
case is:

`./bftg -p /home/user/cross -s myos -t i586-pc-myos`

This will create a patched version of binutils, gcc and newlib in the folder
`output`.  Within `output` if you run the following you will have a complete
toolchain:

```
$make -C binutils
$make -C gcc
$make -C newlib
$make -C gcc stage2
```

That's it, you now have your cross compiling toolchain.

#/************************************************************************
#*   IRC - Internet Relay Chat, Makefile
#*   Copyright (C) 1990, Jarkko Oikarinen
#*
#*   This program is free software; you can redistribute it and/or modify
#*   it under the terms of the GNU General Public License as published by
#*   the Free Software Foundation; either version 1, or (at your option)
#*   any later version.
#*
#*   This program is distributed in the hope that it will be useful,
#*   but WITHOUT ANY WARRANTY; without even the implied warranty of
#*   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#*   GNU General Public License for more details.
#*
#*   You should have received a copy of the GNU General Public License
#*   along with this program; if not, write to the Free Software
#*   Foundation, Inc., 675 Mass Ave, Cambridge, MA 02139, USA.
#*  
#*   $Id$
#*/

CC=gcc
INCLUDEDIR=../include
NETWORKSDIR=
FROMDOS=/home/cmunk/bin/4dos

# [CHANGEME]
# Default flags:
# Change XCFLAGS if you don't like what Config puts there.  Same with
# IRCDLIBS.
#
# If you are configuring by hand, try "-O -g" for XCFLAGS, and leave
# IRCDLIBS blank.  If that fails, try recomendations below.
#

#XCFLAGS=-O -g -export-dynamic
IRCDLIBS=-lcrypt -lnsl  -lz -ldl /root/Unreal/extras/regexp/lib/libtre.a     -L../extras/c-ares/lib /root/Unreal/extras/c-ares/lib/libcares.a -lrt  
CRYPTOLIB=-lssl -lcrypto
OPENSSLINCLUDES=

XCFLAGS=-I/root/Unreal/extras/regexp/include -I/root/Unreal/extras/c-ares/include -pipe -g -O2 -funsigned-char -fno-strict-aliasing -Wno-pointer-sign -export-dynamic
#
# use the following on MIPS:
#CFLAGS= -systype bsd43 -DSYSTYPE_BSD43 -I$(INCLUDEDIR)
# For Irix 4.x (SGI), use the following:
#CFLAGS= -g -cckr -I$(INCLUDEDIR)
#
# on NEXT use:
#CFLAGS=-bsd -I$(INCLUDEDIR)
#on NeXT other than 2.0:
#IRCDLIBS=-lsys_s
#
# AIX 370 flags
#CFLAGS=-D_BSD -Hxa -I$(INCLUDEDIR)
#IRCDLIBS=-lbsd
#
# Dynix/ptx V2.0.x
#CFLAGS= -I$(INCLUDEDIR) -O -Xo
#IRCDLIBS= -lsocket -linet -lnsl -lseq
# 
# Dynix/ptx V1.x.x
#IRCDLIBS= -lsocket -linet -lnsl -lseq
#
#use the following on SUN OS without nameserver libraries inside libc
#IRCDLIBS=-lresolv
#
# Solaris 2
#IRCDLIBS=-lsocket -lnsl -lresolv -L/usr/ucblib -R/usr/ucblib -lgen
#
# ESIX
#CFLAGS=-O -I$(INCLUDEDIR) -I/usr/ucbinclude
#IRCDLIBS=-L/usr/ucblib -L/usr/lib -lsocket -lucb -lns -lnsl
#
# LDFLAGS - flags to send the loader (ld). SunOS users may want to add
# -Bstatic here.
#
#LDFLAGS=-Bstatic
#
#Dell SVR4
#CC=gcc
#CFLAGS= -I$(INCLUDEDIR) -O2
#IRCDLIBS=-lsocket -lnsl -lucb

# [CHANGEME]
# IRCDMODE is the mode you want the binary to be.
# The 4 at the front is important (allows for setuidness)
#
# WARNING: if you are making ircd SUID or SGID, check config.h to make sure
#          you are not defining CMDLINE_CONFIG 
IRCDMODE = 711

# [CHANGEME]
# IRCDDIR must be the same as DPATH in include/config.h
#
IRCDDIR=/root/Unreal


URL=

# [CHANGEME]
# If you get a link-time error dealing with strtoul, comment out
# this line.
# STRTOUL=	strtoul.o
STRTOUL=

# [CHANGEME]
# If you get crashes around a specific number of clients, and that
# client load comes close or a little over the system-defined value of
# FD_SETSIZE, override it here and see what happens. You may override
# the system FD_SETSIZE by setting the FD_SETSIZE Makefile variable to
# -DFD_SETSIZE=<some number>.
FD_SETSIZE=

# Where is your openssl binary
OPENSSLPATH=/usr/bin/openssl

CFLAGS=-I$(INCLUDEDIR) $(XCFLAGS)  $(FD_SETSIZE)

SHELL=/bin/sh
SUBDIRS=src
BINDIR=/root/Unreal/src/ircd
INSTALL=/usr/bin/install
RM=/bin/rm
CP=/bin/cp
TOUCH=/bin/touch
RES=
all:	build

MAKEARGS =	'CFLAGS=${CFLAGS}' 'CC=${CC}' 'IRCDLIBS=${IRCDLIBS}' \
		'LDFLAGS=${LDFLAGS}' 'IRCDMODE=${IRCDMODE}' \
		'RES=${RES}' 'BINDIR=${BINDIR}' 'INSTALL=${INSTALL}' \
		'INCLUDEDIR=${INCLUDEDIR}' 'IRCDDIR=${IRCDDIR}' \
		'RM=${RM}' 'CP=${CP}' 'TOUCH=${TOUCH}' \
		'SHELL=${SHELL}' 'STRTOUL=${STRTOUL}' \
		'CRYPTOLIB=${CRYPTOLIB}' \
		'CRYPTOINCLUDES=${CRYPTOINCLUDES}' \
		'URL=${URL}'

custommodule:
	@if test -z "${MODULEFILE}"; then echo "Please set MODULEFILE when calling \`\`make custommodule''. For example, \`\`make custommodule MODULEFILE=callerid''." >&2; exit 1; fi
	+cd src; ${MAKE} ${MAKEARGS} MODULEFILE=${MODULEFILE} 'EXLIBS=${EXLIBS}' custommodule

server: Makefile
build: Makefile
	-@if [ ! -f include/setup.h ] ; then \
		echo "Hmm...doesn't look like you've run Config..."; \
		echo "Doing so now."; \
		sh Config; \
	fi
	@+for i in $(SUBDIRS); do \
		echo "Building $$i";\
		( cd $$i; ${MAKE} ${MAKEARGS} build; ) \
	done
	@echo ' __________________________________________________ '
	@echo '| Compile is now complete.                         |'
	@echo '| You should now read the documentation and learn  |'
	@echo '| how to configure your IRCd.                      |'
	@echo '|                                                  |'
	@echo '| If you really like UnrealIRCd, and would like to |'
	@echo '| make a donation, please read the Donation file in|'
	@echo '| this archive. :)                                 |'
	@echo '|                                                  |'
	@echo '| Thanks for using Unreal IRCd! If you are in need |' 
	@echo '| for any kind of help regarding the IRCd please   |'
	@echo '| read the Unreal.nfo file.                        |' 
	@echo '|__________________________________________________|'

clean:
	$(RM) -f *~ \#* core *.orig include/*.orig
	@+for i in $(SUBDIRS); do \
		echo "Cleaning $$i";\
		( cd $$i; ${MAKE} ${MAKEARGS} clean; ) \
	done
	-@if [ -f include/setup.h ] ; then \
	  echo "To really restart installation, remove include/setup.h" ; \
	fi

cleandir: clean
	rm -rf include/setup.h Makefile Settings

makex:
	chmod +x Config newnet ircd ircdcron/ircdchk killircd
	chmod +x rehash ircdreg

fromdos: cleandir
	$(FROMDOS) -dv *
	$(FROMDOS) -dv src/*
	$(FROMDOS) -dv include/*
	$(FROMDOS) -dv doc/*
	$(FROMDOS) -dv crypt/*
	$(FROMDOS) -dv ircdcron/*
makedist: makex
	echo "Stamping.."

stamp: makedist
	echo "/* Auto created release stamping */" > include/stamp.h
	echo "#define RELEASEID2 \"`date +%s`\"" >> include/stamp.h
	echo "#define RELEASESTUFF \"`hostname`\"" >> include/stamp.h
	echo "" >> include/stamp.h

depend:
	@+for i in $(SUBDIRS); do \
		echo "Making dependencies in $$i";\
		( cd $$i; ${MAKE} ${MAKEARGS} depend; ) \
	done

install: all
	$(INSTALL) -m 0700 -d $(IRCDDIR)
	$(INSTALL) -m 0700 src/ircd $(BINDIR) 2>/dev/null || { $(INSTALL) -m 0700 -d "$$(dirname '$(BINDIR)')"; $(INSTALL) -m 0700 src/ircd $(BINDIR); }
	$(INSTALL) -m 0700 -d $(IRCDDIR)/doc
	$(INSTALL) -m 0600 doc/Authors doc/example.conf doc/coding-guidelines doc/tao.of.irc doc/unreal32docs.html $(IRCDDIR)/doc
	$(INSTALL) -m 0700 -d $(IRCDDIR)/aliases
	$(INSTALL) -m 0600 aliases/*.conf $(IRCDDIR)/aliases
	$(TOUCH) $(IRCDDIR)/unrealircd.conf
	chmod 0600 $(IRCDDIR)/unrealircd.conf
	$(INSTALL) -m 0600 spamfilter.conf dccallow.conf $(IRCDDIR)
	$(INSTALL) -m 0600 badwords.*.conf help.conf LICENSE Donation $(IRCDDIR)
	$(INSTALL) -m 0700 unreal $(IRCDDIR)
	$(INSTALL) -m 0700 -d $(IRCDDIR)/modules
	$(INSTALL) -m 0700 src/modules/*.so $(IRCDDIR)/modules
	$(INSTALL) -m 0700 -d $(IRCDDIR)/ircdcron
	$(INSTALL) -m 0600 ircdcron/ircd.cron $(IRCDDIR)/ircdcron
	$(INSTALL) -m 0700 ircdcron/ircdchk $(IRCDDIR)/ircdcron
	-@if [ ! -f "$(IRCDDIR)/curl-ca-bundle.crt" ] ; then \
		$(INSTALL) -m 0700 curl-ca-bundle.crt $(IRCDDIR) ; \
	fi
	-@if [ server.cert.pem -nt "$(IRCDDIR)/server.cert.pem" ] ; then \
		$(INSTALL) -m 0600 server.req.pem $(IRCDDIR) ; \
		$(INSTALL) -m 0600 server.key.pem $(IRCDDIR) ; \
		$(INSTALL) -m 0600 server.cert.pem $(IRCDDIR) ; \
	fi

pem:	src/ssl.cnf
	@echo "Generating certificate request .. "
	$(OPENSSLPATH) req -new \
              -config src/ssl.cnf -out server.req.pem \
              -keyout server.key.pem -nodes
	@echo "Generating self-signed certificate .. "
	$(OPENSSLPATH) req -x509 -days 365 -in server.req.pem \
               -key server.key.pem -out server.cert.pem
	@echo "Generating fingerprint .."
	$(OPENSSLPATH) x509 -subject -dates -fingerprint -noout \
		-in server.cert.pem
	@echo "Setting o-rwx & g-rwx for files... "
	chmod o-rwx server.req.pem server.key.pem server.cert.pem
	chmod g-rwx server.req.pem server.key.pem server.cert.pem
	@echo "Done!. If you want to encrypt the private key, run"
	@echo "make encpem"

encpem: server.key.pem
	@echo "Encrypting server key .."
	$(OPENSSLPATH) rsa -in server.key.pem -out server.key.c.pem -des3
	-@if [ -f server.key.c.pem ] ; then \
		echo "Replacing unencrypted with encrypted .." ; \
		cp server.key.c.pem server.key.pem ; \
		rm -f server.key.c.pem ; \
	fi

Makefile: config.status Makefile.in
	./config.status

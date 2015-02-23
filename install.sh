#! /bin/sh
# lizard Linux install script
# copies necessary files to proper directories

UsAGE="Lizard Linux Installer
Usage:

        install.sh [ install path ]

\opt by default"

if [ "$(id -u)" != "0" ]; then
  echo "Must run as root"
  echo ""
  echo "$USAGE"
  exit 1

fi

if [ $# != 1 ]; then
  INSTALLROOT="/opt"
else
  INSTALLROOT="$1"
fi

if [ ! -d "$INSTALLROOT" ]; then
  echo "Invalid Directory"
  echo ""
  echo "$USAGE"
  exit 1
fi

EXEPATH="/usr/local/bin/salmonlizard"
FRMWKBASE="$INSTALLROOT/salmonlizard"

echo "Copying files to: $FRMWKBASE"

if [ ! -d "$FRMWKBASE" ]; then
  mkdir $FRMWKBASE
fi
cp -r * $FRMWKBASE

echo "#!/bin/sh" > $EXEPATH
echo "FRMWKBASE=$INSTALLROOT/salmonlizard" >> $EXEPATH
echo "python -B \$FRMWKBASE/salmon.py \"\$@\"" >> $EXEPATH
chmod -x $EXEPATH

echo "Finished"

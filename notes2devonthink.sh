#!/bin/zsh
#
#

DATETIME=`date +%Y%m%d.%H%M`
PGMDIR=$(PWD)
DEST_DIR="$HOME/Library/Application Support/DEVONthink 3/Inbox/"
PGM=$PGMDIR/handwriting_ocr.py
OUTDIR=$PGMDIR/output

# In case the tmp directory gets deleted by some other process
if [ ! -d $OUTDIR ]; then  
    mkdir $OUTDIR
fi


exec > $PGMDIR/tmp/rocketbook.$DATETIME.log  2>&1

set -x

export GOOGLE_APPLICATION_CREDENTIALS=$HOME/.gcpdn/gcpdn.key
# convert the Rocketbook page scanned as PDF into an image
fname=$PGMDIR/tmp/rocketbook/tmp.$RANDOM
filename=$(basename "$1")

/usr/local/bin/pdfimages -j "$1" $fname

# pdfimages , creates a JPEG image for each image in the pdf file.

# send the image to Google Video Intelligence API for OCR

for jpeg_fname in $fname*jpg
do
# put the results into a file.txt
    $PGM $jpeg_fname | tee $jpeg_fname.txt
# create a blank pdf
    convert xc:none -page 388x591 $jpeg_fname.blank.pdf

#Create the metadata txt file
$PGMDIR/metadata.py $jpeg_fname.txt $jpeg_fname.metadata.txt

# Put the google OCR results into the blank pdf
gs -o $jpeg_fname-annotated.pdf -sDEVICE=pdfwrite -dPDFSETTINGS=/prepress $jpeg_fname.blank.pdf $jpeg_fname.metadata.txt

done

cur_date=$(date '+%m-%d-%Y_%H_%m_%S')
# Merge the Rockebook pdf + New pdf with OCR'ed content
#cpdf -merge "$1" $fname*-annotated.pdf  -o $OUTDIR/$filename
gs -q -dNOPAUSE -dBATCH -sDEVICE=pdfwrite -sOutputFile=$OUTDIR/$filename "$1" $fname*-annotated.pdf 

$PGMDIR/import_to_devonthink.py $OUTDIR/$filename

The scripts in this package rely on several Python3 packages. 
I use this on Mac OS Catalina (10.15.7)

You need homebrew installed. 
[The Missing Package Manager for macOS (or Linux) — Homebrew](https://brew.sh/)

once you have homebrew installed. Here are the instructions - 

```
$ brew install python3 
$ brew install pipenv
$ brew install poppler
$ brew install ghostscript
$ brew install imagemagick
$ pip3 install google-cloud-vision
```

For the interfacing with Google, you'll need the API keys. 
[Vision Client Libraries  |  Cloud Vision API  |  Google Cloud](https://cloud.google.com/vision/docs/libraries#client-libraries-install-python)

change the following to point to where you've stored your API key
export GOOGLE_APPLICATION_CREDENTIALS=$HOME/.gcpdn/gcpdn.key

To test whether you have everything installed, here is what you can try

```
$ pipenv install --three
$ pipenv shell
# cd to where you donwloaded the rockebook code
$ python3 handwriting_ocr.py images/sample_note-000.jpg
- This is
an
example
of handwriting
recognition and
to Devonthink
importing
- It uses
Google for the
handwriting recognition
```

If you get an output similar to the above, you have everything installed. 

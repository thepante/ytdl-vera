#!/bin/bash

PY2=${HOME}/.local/lib/python2.7/site-packages/youtube_dl/extractor
PY3=/usr/lib/python3/dist-packages/youtube_dl/extractor

if [ -d "$PY2" ]; then
  cp ./extractor/vera.py "$PY2/vera.py" && 
  echo 'from .vera import VeraIE' >> $PY2/extractors.py
fi

if [ -d "$PY3" ]; then
  sudo cp ./extractor/vera.py "$PY3/vera.py" && 
  echo 'from .vera import VeraIE' >> $PY3/extractors.py

fi

if [ -f $PY2/vera.py ]
then
    echo "Integrado a YT-DL Python2.7 ..."
fi

if [ -f $PY3/vera.py ]
then
  	echo "Integrado a YT-DL Python3 ..."
fi

cd ~/ && rm -rf ~/.temp/ytdl-vera &&
echo "Autodestrucción de este repo temporal..." &&
echo "[ ✓ ] Listo, probá youtube-dl."

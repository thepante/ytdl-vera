#!/bin/bash
sudo cp ./extractor/vera.py "~/.local/lib/python2.7/dist-packages/youtube_dl/extractor/vera.py" && 
echo "[1/5] Copiado a Python2.7..." &&
cp ./extractor/vera.py "/usr/lib/python3/dist-packages/youtube_dl/extractor/vera.py" && 
echo "[2/5] Copiado a Python3..." &&
echo 'from .vera import VeraIE' >> ~/.local/lib/python2.7/dist-packages/youtube_dl/extractor/extractors.py &&
echo "[3/5] Incluido en youtube_dl Python2.7 ..." &&
echo 'from .vera import VeraIE' >> /usr/lib/python3/dist-packages/youtube_dl/extractor/extractors.py &&
echo "[4/5] Incluido en youtube_dl Python3 ..." &&
cd .. && rm -rf ytdl-vera &&
echo "[5/5] Autodestrucción de este repo..." &&
echo "[ ✓ ] Listo, probá youtube-dl."

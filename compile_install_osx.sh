ls -1 CIRCUITPY/*.py | grep --invert-match code.py | xargs -n 1 ./mpy-cross-2.2.0-macos-high-sierra
rsync             --verbose --update CIRCUITPY/code.py  /Volumes/CIRCUITPY/
rsync --recursive --verbose --update CIRCUITPY/*.mpy    /Volumes/CIRCUITPY/
rsync --recursive --verbose --update CIRCUITPY/lib/     /Volumes/CIRCUITPY/lib

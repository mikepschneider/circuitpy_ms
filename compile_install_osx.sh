# Exit immediately on failure
set -e

ls -1 CIRCUITPY/*.py \
		| grep --invert-match code.py \
		| xargs -n 1 ./mpy-cross-2.2.0-macos-high-sierra

./install_osx.sh

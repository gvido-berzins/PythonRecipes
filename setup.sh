#!/bin/bash
PYTHON=python
PIP_OPTS="--no-python-version-warning --exists-action i -q"
ENVFILE=".env"

function showBanner() {
    echo "          ,KkdxddxxOK,        "
    echo "         ;o..ooooooo:         "
    echo "     dWWWX00000ooooo:cNNd     "
    echo "    Odoooooooooooooo: ...o.   "
    echo "   :ooooooooooooooo: l....;   "
    echo "   ;ooooo lkxxxxxxxx:.....'   "
    echo "    oooo;;................    "
    echo "     'oo:,...............     "
    echo "         ,.....ddddd;         "
    echo "         ........  ..         "
    echo ""
    echo "     Python Setup Script      "
    echo "     -------------------      "
}

function showHelp() {
    echo ""
    echo -e "Run the follwing command to activate the environment:\n"
    echo -e "$ source venv/bin/activate\n"
}

function setInterpreter() {
    MAJOR=`python -V | grep -oP "([0-9])(?=\.[0-9]{2}\..*)"`
    [[ $MAJOR -eq "2" ]] && PYTHON=python3
    $PYTHON -V >/dev/null || exit "Valid python version not found please install Python"
    checkPythonMinorVersion
}

function checkPythonMinorVersion() {
    MINOR=`$PYTHON -c 'import sys; print(sys.version_info[1])'`
    if (( $MINOR < 10 )); then
        PYTHON=python3.10
        $PYTHON -V >/dev/null || exit "Minimum version should be Python 3.10.x"
    fi
    echo "Using Python Launcher: $PYTHON"
}

function checkDotEnv() {
    if [[ ! -f $ENVFILE ]]; then
        echo "[*] No .env file. Creating a new one"
        echo -e "PYTHONPATH=$PWD\n" > $ENVFILE
    fi
}

function setupVenv() {
    echo -e "[*] Creating virtual env in $PWD/venv"
    $PYTHON -m venv venv
    source venv/bin/activate
}

function setupStyling() {
    echo "[*] Installing flake8 & black"
    pip install $PIP_OPTS flake8 black
}

function setupPreCommit() {
    echo "[*] Installing pre-commit & hooks"
    pip install $PIP_OPTS pre-commit
    pre-commit install
}

function installRequirements() {
    pip install $PIP_OPTS -r requirements.txt
}

showBanner
setInterpreter
checkDotEnv
setupVenv
setupStyling
setupPreCommit
installRequirements
showHelp

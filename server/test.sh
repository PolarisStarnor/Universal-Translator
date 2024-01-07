#!/usr/bin/env sh

if [ -d tests ]
then #!
    echo "Running Tests..."
    python3 -m unittest discover -s tests -v
    echo
    echo "Tests Completed"
fi

if [ ! -d tests ]
then
    echo "Failed to find test directory"
fi

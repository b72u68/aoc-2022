#!/bin/bash

DAY=$(TZ=America/New_York date '+%d')
DIRNAME="day${DAY}"
if [ -d "$DIRNAME" ]; then
    echo "$DIRNAME has already existed."
else
    mkdir $DIRNAME
    touch "$DIRNAME/test.txt" "$DIRNAME/data.txt" "$DIRNAME/$DIRNAME.py"
    cp "template.py" "$DIRNAME/$DIRNAME.py"
    echo "$DIRNAME created successfully."
fi

echo off

if [%1]==[] (
    echo Must provide an argument!
) else (
    python pyPORIS\poris2python.py models\%1.ods
    copy pyPORIS\PORIS\PORIS.py %1.user\PORIS.py
    copy %1\%1PORIS.py %1.user\%1PORIS.py
)


#!/bin/bash

CMD_WHITE="sassc -t compressed -I css/theme-white css/cses.scss cses.css"
CMD_DARK="sassc -t compressed -I css/theme-dark css/cses.scss cses-dark.css"
CMD="($CMD_WHITE) && ($CMD_DARK)"

if [ "$1" = "-l" ]
then
  while true
  do
    find css/ -not -path '*/\.*' | entr -d bash -c "$CMD"
  done
else
  bash -c "$CMD"
fi

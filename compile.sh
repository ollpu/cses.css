#!/bin/bash

CMD="sassc -t compressed css/cses.scss cses.css"

if [ "$1" == "-l" ]
then
  find css/ -not -path '*/\.*' | entr $CMD
else
  $CMD
fi

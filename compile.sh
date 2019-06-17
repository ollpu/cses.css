#!/bin/bash

find css/ -not -path '*/\.*' | entr sassc -t compressed css/cses.scss cses.css

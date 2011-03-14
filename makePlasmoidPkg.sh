#!/bin/bash
zip  -x ".git/*" -x "*/*.pyc" -x ".gitignore" -x "makePlasmoidPkg.sh"  -r ../qrencoder.plasmoid .

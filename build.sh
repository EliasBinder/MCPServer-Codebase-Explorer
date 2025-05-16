#!/bin/bash

suffix=$(rustc -Vv | grep host | cut -f2 -d' ')

pyinstaller --onefile server.py -n mcp-codebase-explorer-$suffix

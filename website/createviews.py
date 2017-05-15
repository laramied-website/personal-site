#!/bin/bash

import os

for filename in os.listdir('templates'):
	#print filename
	print("def {0}(request):").format(filename[:-5])
	print("    render (request, '{0}')\n").format(filename)

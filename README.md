# TorRotation2020
A repository for all files used during the rotation project with Prof. Roch Guerin, department of Computer Science, Washington University in St Louis
Author: Ashwin Kumar. PhD student, Department of Computer Science, Washington University in St Louis
Contact: ashwinkumar@wustl.edu
Usage:
1. Set up a relay with the given files.
2. Set up the cronjobs using the file in Relay files/
3. It should start creating .dumpstrips in the root folder. Run create_dump.py and send output to out.tsv. The output is formatted in a way that any tsv reader will be able to read tables for v2 and v3.
4. Copy arraydump.pkl to Processing/, and run Processing/json_dumper.py. Copy the created .json files to the Viz/ folder
5. Run an http server from within the Viz/ folder and navigate to index.html to see the visualization for the data.
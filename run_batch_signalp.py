import os
import shutil
import argparse
import urllib.request
import xml.etree.ElementTree as ET

parser = argparse.ArgumentParser()

parser.add_argument('file_path')

args = parser.parse_args()
fname = args.file_path

try:
    os.mkdir("inputs")
except:
    shutil.rmtree("inputs")
    os.mkdir("inputs")

def parse_xgmml(file_path):
    tree = ET.parse(file_path)
    root = tree.getroot()

    nodes = []
    
    # Find all node elements
    for node_element in root.findall('.//{http://www.cs.rpi.edu/XGMML}node'):
        nodes.append(node_element.attrib)


    # Call the parsing function
    parsed_nodes = nodes

    uniprot_ids = []

    # Print the nodes
    for node in parsed_nodes:
        uniprot_ids.append(node['label'])

    return uniprot_ids

uniprot_ids = parse_xgmml(fname)

def id2fasta(ID):
    url = f"https://rest.uniprot.org/uniprotkb/{ID}?format=fasta"

    # Make the GET request
    response = urllib.request.urlopen(url)

    # Read the response content
    data = response.read()

    # Decode the response content as a string
    content = data.decode("utf-8")

    text_file = open(f"inputs/{ID}.fasta", "w")
    text_file.write(content)
    text_file.close()

[id2fasta(i) for i in uniprot_ids] 

commands = [f"/home/ubuntu/.local/bin/signalp6 --fastafile inputs/{i} --organism other --output_dir out/{i.split('.')[0]} --format txt --mode fast \n" for i in os.listdir("inputs")]

file1 = open("signalP_commands.sh", "w")
file1.writelines(commands)
file1.close()

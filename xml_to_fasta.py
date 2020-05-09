#!/usr/bin/env python                                                                                                                                                                                                                         

########################################################################
# This is a python script to convert blast xml output to a fasta file 
#
# Created By Amit Singh on 08-05-2020
#
#
# Pay attention please install - biopython python module before using this
#
# ------------> pip install biopython
#
########################################################################


# Importing required module

import sys
from Bio.Blast import NCBIXML


# Looking for command line arguments

try:

        xml_in = sys.argv[1]                     # Path to input xml file

        out_file = sys.argv[2]                   # Path to output fasta file
except: 

        print("--------------Error--------------"* + "\nSee Correct Usages below\n")

        print("Usages: python xml_to_fasta.py {input_file.xml} {output_file.fasta}")

        raise SystemExit()


blast_records = NCBIXML.parse(open(xml_in, 'rU'))

fasta_out = open(out_file,'w')


for blast_record in blast_records:
    
    for alignment in blast_record.alignments:
    
        for hsp in alignment.hsps: 
       
            seq_out = '>'+alignment.hit_def+'\n'+hsp.sbjct+'\n'

            fasta_out.write(seq_out)

blast_records.close()
fasta_out.close()

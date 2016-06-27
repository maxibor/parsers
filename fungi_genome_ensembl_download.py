#!/usr/bin/env python

import subprocess


release = str("31")
genomes_dir = "path/to/directory" #path to directory that must already exist
ensembl_species_file = "species_EnsemblFungi.txt" #ensembl_species_file describing all availables genomes, in genomes_dir
fasta_file_root_directory = "ftp://ftp.ensemblgenomes.org/pub/fungi/release-31/fasta/" #path to ensemblgenomes fungi


with open(genomes_dir+ensembl_species_file,"r") as species_list_file :
    next(species_list_file)
    for line in species_list_file :
        line = line.rstrip()
        line = line.split("\t")
        specie_dir = line[1]
        specie_name = specie_dir.capitalize()
        if line[4].split(" ") > 0 :
            assembly_name = "_".join(line[4].split(" "))
        else :
            assembly_name = line[4]
        core_db = line[12]
        core_db = core_db.split("_")

        if core_db[0] == "fungi" : # in a phylum directory
            phylum_dir = "_".join(core_db[0:3])
            download_link = fasta_file_root_directory+phylum_dir+"/"+specie_dir+"/dna/"+specie_name+"."+assembly_name+"."+release+".dna.genome.fa.gz"
            print download_link
            try :
                cmd = "wget -P "+genomes_dir+" "+download_link
                subprocess.check_output(cmd, shell = True)
            except :
                print "Error in parsing link"
        elif core_db[0] != "fungi" : #directly in a specie directory
            download_link = fasta_file_root_directory+specie_dir+"/dna/"+specie_name+"."+assembly_name+"."+release+".dna.genome.fa.gz"
            print download_link
            try :
                cmd = "wget -P "+genomes_dir+" "+download_link
                subprocess.check_output(cmd, shell = True)
            except :
                print "Error in parsing link"

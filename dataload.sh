### DEPENDENCIES
# cutadapt 			-- pip install cutadapt
# hisat2 			-- https://bioconda.github.io/recipes/hisat2/README.html
# fastq-sample 		-- https://github.com/dcjones/fastq-tools
# samtools			-- http://genomic-identity.wikidot.com/install-samtools
# featurecounts 	-- http://bioinf.wehi.edu.au/subread-package/


### DOWNLOAD RNA-Seq DATA 

# Data: SRP268654 - RNA-seq analysis of developing rice seeds under combined heat and drought stress
# Three replicates each of RNA-seq data of heat/drought resistant strain of rice (Oryza sativa N22) 
# grown both under control conditions and heat/drought conditions


# Download compressed fastq files for 6 trials (3 replicates under both drought & control conditions)
curl -L ftp://ftp.sra.ebi.ac.uk/vol1/fastq/SRR120/057/SRR12073957/SRR12073957.fastq.gz -o HeatAndDrought_Rep1.fastq.gz
curl -L ftp://ftp.sra.ebi.ac.uk/vol1/fastq/SRR120/058/SRR12073958/SRR12073958.fastq.gz -o HeatAndDrought_Rep2.fastq.gz
curl -L ftp://ftp.sra.ebi.ac.uk/vol1/fastq/SRR120/059/SRR12073959/SRR12073959.fastq.gz -o HeatAndDrought_Rep3.fastq.gz
curl -L ftp://ftp.sra.ebi.ac.uk/vol1/fastq/SRR120/054/SRR12073954/SRR12073954.fastq.gz -o Control_Rep1.fastq.gz
curl -L ftp://ftp.sra.ebi.ac.uk/vol1/fastq/SRR120/055/SRR12073955/SRR12073955.fastq.gz -o Control_Rep2.fastq.gz
curl -L ftp://ftp.sra.ebi.ac.uk/vol1/fastq/SRR120/056/SRR12073956/SRR12073956.fastq.gz -o Control_Rep3.fastq.gz

### QUALITY CONTROL

# Uncompress files and quality control of RNA-seq data, removing reads that are too short (< 45 bp) 
# and removing ends and beginnings of reads that have poor confidence (quality score < 20)

gzip -d "HeatAndDrought_Rep1.fastq.gz"
cutadapt -o trimmed_Drought_Rep1.fastq HeatAndDrought_Rep1.fastq -q 20 --minimum-length 45
rm "HeatAndDrought_Rep1.fastq"

gzip -d "HeatAndDrought_Rep2.fastq.gz"
cutadapt -o trimmed_Drought_Rep2.fastq HeatAndDrought_Rep2.fastq -q 20 --minimum-length 45
rm "HeatAndDrought_Rep2.fastq"

gzip -d "HeatAndDrought_Rep3.fastq.gz"
cutadapt -o trimmed_Drought_Rep3.fastq HeatAndDrought_Rep3.fastq -q 20 --minimum-length 45
rm "HeatAndDrought_Rep3.fastq"

gzip -d "Control_Rep1.fastq.gz"
cutadapt -o trimmed_Control_Rep1.fastq Control_Rep1.fastq -q 20 --minimum-length 45
rm "Control_Rep1.fastq"

gzip -d "Control_Rep2.fastq.gz"
cutadapt -o trimmed_Control_Rep2.fastq Control_Rep2.fastq -q 20 --minimum-length 45
rm "Control_Rep2.fastq"

gzip -d "Control_Rep3.fastq.gz"
cutadapt -o trimmed_Control_Rep3.fastq Control_Rep3.fastq -q 20 --minimum-length 45
rm "Control_Rep3.fastq"

### ALIGN TO GENOME
# Genome data: https://datacommons.cyverse.org/browse/iplant/home/shared/commons_repo/curated/IOMAP_Genomes_Data_2017/MAKER_genome_annotations/Oryza_sativa_N22.cdna.fasta
# Modified from: https://bioinformatics-core-shared-training.github.io/RNAseq_September_2019/html/C_Alignment_with_HISAT2_practical.html

hisat2 -x genome_hisat2 -U HeatAndDrought_Rep1.fastq.gz -S drought_1.sam
samtools view -b drought_1.sam > drought_1.bam
samtools sort drought_1.bam > drought_1.sorted.bam
samtools index drought_1.sorted.bam

hisat2 -x genome_hisat2 -U HeatAndDrought_Rep2.fastq.gz -S drought_2.sam
samtools view -b drought_2.sam > drought_2.bam
samtools sort drought_2.bam > drought_2.sorted.bam
samtools index drought_2.sorted.bam

hisat2 -x rice_genome -U HeatAndDrought_Rep3.fastq.gz -S drought_3.sam

hisat2 -x genome_hisat2 -U HeatAndDrought_Rep3.fastq.gz -S drought_3.sam
samtools view -b drought_3.sam > drought_3.bam
samtools sort drought_3.bam > drought_3.sorted.bam
samtools index drought_3.sorted.bam

hisat2 -x genome_hisat2 -U Control_Rep1.fastq.gz -S control_1.sam
samtools view -b control_1.sam > control_1.bam
samtools sort control_1.bam > control_1.sorted.bam
samtools index control_1.sorted.bam

hisat2 -x genome_hisat2 -U Control_Rep2.fastq.gz -S control_2.sam
samtools view -b control_2.sam > control_2.bam
samtools sort control_2.bam > control_2.sorted.bam
samtools index control_2.sorted.bam

hisat2 -x rice_genome -U Control_Rep3.fastq.gz -S control_3.sam


hisat2 -x genome_hisat2 -U Control_Rep3.fastq.gz -S control_3.sam
samtools view -b control_3.sam > control_3.bam
samtools sort control_3.bam > control_3.sorted.bam
samtools index control_3.sorted.bam
import pandas as pd
import numpy as np

UTR_df=pd.read_csv("UTR2.tsv", sep="\t", names=["UTR_Start", "UTR_End", "GeneID"])
UTR_df=UTR_df.set_index('GeneID')

miRNA_df=pd.read_csv("miRNA.tsv", sep="\t", names=["miRNA", "GeneID", "Gene_Symbol", "Start", "End", "Binding_Probability"])
miRNA_df=miRNA_df.set_index('GeneID')

mutation_df=pd.read_csv("DNA_rep_genes.tsv", sep="\t")

print(mutation_df)
print(UTR_df.head())
print(miRNA_df.head())

bs_start_list=[]
bs_end_list=[]
position_list=[]
ref_list=[]
alt_list=[]
master_df=pd.DataFrame()

for i, row in mutation_df.iterrows():
    gene_id=mutation_df.at[i, "ID"]
    position=mutation_df.at[i, "Position"]

    UTR_ss=UTR_df.loc[gene_id]
    miRNA_ss=miRNA_df.loc[gene_id]

    #print(UTR_ss.head())
    #print(miRNA_ss.head())

    UTR_start= UTR_ss.loc["UTR_Start"]
    miRNA_target_start=list(miRNA_ss.at[gene_id, "Start"])
    miRNA_target_end=list(miRNA_ss.at[gene_id, "End"])

    for start, end in zip(miRNA_target_start, miRNA_target_end):
        bs_start=UTR_start + start
        bs_end=UTR_start + end
#       for pos in position:
        if position>bs_start and position<bs_end:
            bs_start_list.append(bs_start)
            bs_end_list.append(bs_end)
            position_list.append(position)
            ref_list.append(mutation_df.at[i, "Ref"])
            alt_list.append(mutation_df.at[i, "Alt"])
            to_append_df=miRNA_ss.loc[(miRNA_ss['Start'] == start) & (miRNA_ss['End']== end)]
            if to_append_df.shape[0] == 2:
                bs_start_list.append(bs_start)
                bs_end_list.append(bs_end)
                position_list.append(position)
                ref_list.append(mutation_df.at[i, "Ref"])
                alt_list.append(mutation_df.at[i, "Alt"])
            master_df=master_df.append(to_append_df)

master_df['Start']=bs_start_list
master_df['End']=bs_end_list
master_df.insert(4, "Mutation_Position", position_list, True)
master_df.insert(5, "Ref", ref_list, True)
master_df.insert(6, "Alt", alt_list, True)
master_df.drop_duplicates(subset=['Gene_Symbol', 'miRNA', 'Mutation_Position'], ignore_index=True, keep=False)

print(master_df.head())

master_df.to_csv("miRNA_leukemia.tsv", sep="\t")

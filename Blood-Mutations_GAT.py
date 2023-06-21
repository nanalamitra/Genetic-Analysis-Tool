import pandas as pd

# Load the data from a TSV file
filename = "abc12.txt"
data = pd.read_csv(filename, sep="\t", skiprows=20, names=["rsid", "chromosome", "position", "genotype"])

# Define the rsids for JAK2, CALR, and MPL mutations
jak2_rsid = "rs123456"
calr_rsid = "rs387907125"
mpl_rsid = "rs769493949"

# Check for JAK2 mutation
if jak2_rsid in data["rsid"].values:
    jak2_genotype = data.loc[data["rsid"] == jak2_rsid, "genotype"].values
    if len(jak2_genotype) > 0:
        jak2_genotype = jak2_genotype[0]
        print(f"JAK2 genotype: {jak2_genotype}")
    else:
        print("No genotype found for JAK2")
else:
    print("JAK2 rsid not present in data")

# Check for CALR mutation
if calr_rsid in data["rsid"].values:
    calr_genotype = data.loc[data["rsid"] == calr_rsid, "genotype"].values
    if len(calr_genotype) > 0:
        calr_genotype = calr_genotype[0]
        print(f"CALR genotype: {calr_genotype}")
    else:
        print("No genotype found for CALR")
else:
    print("CALR rsid not present in data")

# Check for MPL mutation
if mpl_rsid in data["rsid"].values:
    mpl_genotype = data.loc[data["rsid"] == mpl_rsid, "genotype"].values
    if len(mpl_genotype) > 0:
        mpl_genotype = mpl_genotype[0]
        print(f"MPL genotype: {mpl_genotype}")
    else:
        print("No genotype found for MPL")
else:
    print("MPL rsid not present in data")

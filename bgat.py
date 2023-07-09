# Import the pandas library
import pandas as pd

# Define a list of breast cancer-related variants (identified by rsIDs)
breast_cancer_vars = ['rs80357082', 'rs80357756', 'rs80358309', 'rs587782982']
Blood_type_vars = ['rs8176746', 'rs8176747', 'rs34557413', 'rs41302905']
while True:
    # Prompt the user to enter a filename containing the 23andMe data
    filename = input("Enter the filename of your 23andMe data (or type 'DONE' to exit): ")
    
    # If the user enters 'DONE', exit the loop
    if filename == 'DONE':
        break
    
    try:
        # Load the 23andMe data into a pandas DataFrame
        data = pd.read_csv(filename,
                            
                            sep='\t',
                            skiprows=20,
                            header=None,
                            names=['rsid', 'chromosome', 'position', 'genotype'],
                            dtype=
                            {
                                'rsid': str, 
                                'chromosome': str, 
                                'position': int, 
                                'genotype': str
                            }
                        )

        # Rename the columns to 'rsid', 'chromosome', 'position', and 'genotype'
        data.columns = ['rsid', 'chromosome', 'position', 'genotype']

        # Filter out any non-SNP variants (e.g. insertions, deletions)
        data = data[data['rsid'].str.startswith('rs')]

        # Filter the data for breast cancer-related variants
        breast_cancer_data = data[data['rsid'].isin(breast_cancer_vars)]
        # Filter the data for blood type-related variants
        blood_type_data = data[data['rsid'].isin(Blood_type_vars)]

        # Print the data
        if (breast_cancer_data.empty):
            print(breast_cancer_data)
        else:
            print("No Breast cancer data found in genome")
        
    

        
        
    except FileNotFoundError:
        # If the file is not found, print an error message
        print("File not found. Please enter a valid filename or type 'DONE' to exit.")
        
    except Exception as e:
        # If there is any other error, print the error message
        print(e + "This is an error message")

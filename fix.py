import nbformat

# Path to your notebook
notebook_path = r"C:\Users\bikra\PovertyEmbedding\ml_mini_project_129_132 .ipynb"
fixed_path = r"C:\Users\bikra\PovertyEmbedding\ml_mini_project_129_132_fixed.ipynb"

# Load the notebook
nb = nbformat.read(notebook_path, as_version=4)

# Remove broken widgets metadata if it exists
if "widgets" in nb.metadata:
    del nb.metadata["widgets"]

# Save the fixed notebook
nbformat.write(nb, fixed_path)

print("Notebook fixed and saved as:", fixed_path)

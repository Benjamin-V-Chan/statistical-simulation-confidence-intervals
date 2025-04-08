"""
# 1. Import necessary libraries: pandas, matplotlib.pyplot, argparse, os.
# 2. Define the main() function:
#    a. Parse command-line arguments for the input simulation results CSV file and the output image file name.
#    b. Read the simulation results CSV into a pandas DataFrame.
#    c. Calculate the overall coverage probability (mean of the coverage boolean).
#    d. Create a histogram of the sample means.
#    e. Overlay a vertical dashed line for the overall mean of sample means.
#    f. Add a title including the computed coverage probability.
#    g. Ensure the outputs/ directory exists.
#    h. Save the plot image to the outputs/ folder.
# 3. Execute main() when the script is run.
"""
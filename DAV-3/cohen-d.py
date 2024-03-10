'''For a quality control analysis, a factory assesses the tensile strength of a 
sample of steel rods.

The sample exhibits a mean tensile strength of 750 MPa with a sample standard 
deviation of 50 MPa, while the known population mean is 800 MPa.

Calculate Cohen's d for this quality control study.'''

# For a one-sample test comparing a sample mean to a known population mean, the effect size can be calculated using:

# d = (Sample Mean - Population Mean) / Sample Standard Deviation
d = (750 - 800) / 50
print(d)
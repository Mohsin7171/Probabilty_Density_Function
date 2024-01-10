import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

def plot_salary_distribution(file_path):
    # Read the Data
    data = pd.read_csv(file_path, header=None, names=['salary'])

    mu, std = norm.fit(data['salary'])

    print(f"Mean Salary: {mu:.2f} Euros")

    plt.figure(figsize=(10, 5))

    num_bins = 10

    plt.hist(data['salary'], bins=num_bins, density=True, alpha=0.6, color='b', label='Actual Data')

    # Plot the PDF
    xmin, xmax = plt.xlim()
    x = np.linspace(xmin, xmax, 100)
    pdf = norm.pdf(x, mu, std)
    plt.plot(x, pdf, 'r', linewidth=2, label='Fit Results (PDF)')

    # Calculate the mean annual salary using the obtained PDF
    mean_salary = np.trapz(x * pdf, x)
    print("Mean Salary Through PDF")
    print(mean_salary)
    
    # Calculate the value of X for 5% of people above X
    percentile_value = 95
    X = norm.ppf(percentile_value / 100, mu, std)

    # Add labels and title
    plt.title('Salary Distribution')
    plt.xlabel('Salary (Euros)')
    plt.ylabel('Probability')

    # Add a legend at the top right corner
    plt.legend(loc='upper right', bbox_to_anchor=(1, 1), fancybox=True, shadow=True)

    # Display the plot in a separate window

    # Create a separate box to display values of W and X below the actual data box with colors
    box_text_w = f'Mean Salary (\u0303W): {mean_salary:.2f} Euros'
    box_text_x = f'Value of X ({5}% above): {X:.2f} Euros'

    plt.text(0.98, 0.80, box_text_w, transform=plt.gca().transAxes,
             color='blue', verticalalignment='top', horizontalalignment='right', bbox=dict(boxstyle='square', facecolor='white', alpha=0.8))

    plt.text(0.98, 0.70, box_text_x, transform=plt.gca().transAxes,
             color='green', verticalalignment='top', horizontalalignment='right', bbox=dict(boxstyle='square', facecolor='white', alpha=0.8))

    # Display the plot in a separate window
    plt.show()

# Call the function with your file path
plot_salary_distribution('data2-1.csv')

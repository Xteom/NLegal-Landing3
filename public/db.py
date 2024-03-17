import pandas as pd

# Load the Excel file
excel_path = 'extracted_data.csv'  # Update this to the path of your Excel file
df = pd.read_csv(excel_path)

# Convert the DataFrame to HTML
html_content = df.to_html()
# Save the HTML content to a file
# Save the HTML to a file (optional)
html_file_path = 'output.html'  # Specify the desired output HTML file path
with open(html_file_path, 'w') as f:
    f.write(html_content)

print(f"HTML content displaying the cell content has been generated and saved to: {html_file_path}")

# ################
# import pandas as pd

# # Load the Excel file
# excel_path = 'extracted_data.csv'   # Update this to the path of your Excel file
# df = pd.read_csv(excel_path)

# cell_content = df.iloc[1, 2] 
# html_content = f"<html><body><p>The content of the 3rd column, 2nd row is: {cell_content}</p></body></html>"

# # Convert the DataFrame to HTML
# #html_content = html_content.to_html()

# # Save the HTML to a file (optional)
# html_file_path = 'output.html'  # Specify the desired output HTML file path
# with open(html_file_path, 'w') as f:
#     f.write(html_content)

# print("HTML content has been generated and saved to:", html_file_path)



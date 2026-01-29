import zipfile
import os

def zip_project(source_dir, output_filename):
    with zipfile.ZipFile(output_filename, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for root, dirs, files in os.walk(source_dir):
            # Exclude directories
            dirs[:] = [d for d in dirs if d not in ['node_modules', '.git', '__pycache__', '.venv', 'env', '.idea', '.vscode']]
            
            for file in files:
                if file == output_filename or file.endswith('.zip') or file.endswith('.pyc'):
                    continue
                    
                file_path = os.path.join(root, file)
                arcname = os.path.relpath(file_path, source_dir)
                zipf.write(file_path, arcname)
                
    print(f"Project zipped successfully to: {output_filename}")

if __name__ == "__main__":
    source = r"C:\Users\mukil\.gemini\antigravity\scratch\insurance-claim-risk-classification"
    custom_name = "Insurance_Claim_Project_Submission.zip"
    output = os.path.join(source, custom_name)
    zip_project(source, output)

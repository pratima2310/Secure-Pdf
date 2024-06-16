import pikepdf
from pikepdf import Pdf, Permissions, Encryption

def secure_pdf(input_path: str, output_path: str, user_password: str, owner_password: str):
    try:
        # Open the existing PDF
        old_pdf = Pdf.open(input_path)
        
        # Define permissions (disallow text and graphics extraction)
        permissions = Permissions(extract=False)
        
        # Save the new PDF with encryption and specified permissions
        old_pdf.save(
            output_path,
            encryption=Encryption(user=user_password, owner=owner_password, allow=permissions)
        )
        print(f"PDF '{input_path}' has been secured and saved as '{output_path}'")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    # Example usage
    secure_pdf("example.pdf", "new_example.pdf", user_password="whatever", owner_password="pratima")

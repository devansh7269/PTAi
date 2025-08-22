import subprocess
import os
from rembg import remove
from PIL import Image

# Enhance image with Real-ESRGAN
def enhance_image(input_path, output_path):
    exe_path = r"C:\Users\HP\Downloads\RealESRGAN-ncnn-vulkan-20220424-windows\realesrgan-ncnn-vulkan.exe"

    if not os.path.exists(exe_path):
        print("❌ Real-ESRGAN executable not found! Check exe_path.")
        return

    try:
        subprocess.run([exe_path, "-i", input_path, "-o", output_path])
        print(f"✅ Enhanced image saved at {output_path}")
    except Exception as e:
        print(f"⚠️ Error while enhancing image: {e}")


# Remove background
def remove_bg(input_path, output_path):
    try:
        with open(input_path, "rb") as inp_file:
            input_data = inp_file.read()
            output_data = remove(input_data)

        with open(output_path, "wb") as out_file:
            out_file.write(output_data)

        print(f"✅ Background removed image saved at {output_path}")
    except Exception as e:
        print(f"⚠️ Error while removing background: {e}")


# Menu loop
def main():
    while True:
        print("\n=== Photo AI Menu ===")
        print("1. Enhance Image")
        print("2. Remove Background")
        print("3. Exit")

        choice = input("Enter your choice (1/2/3): ").strip()

        if choice == "1":
            input_path = input("Enter input image path: ").strip()
            output_path = input("Enter output image path (with .jpg or .png): ").strip()
            enhance_image(input_path, output_path)

        elif choice == "2":
            input_path = input("Enter input image path: ").strip()
            output_path = input("Enter output image path (with .png recommended): ").strip()
            remove_bg(input_path, output_path)

        elif choice == "3":
            print("👋 Exiting... Bye!")
            break

        else:
            print("❌ Invalid choice. Please enter 1, 2, or 3.")


if __name__ == "__main__":
    main()

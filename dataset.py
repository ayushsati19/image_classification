import os
import random
from PIL import Image, ImageDraw

def generate_image_data(output_dir: str, num_classes: int = 5, images_per_class: int = 100):
    """
    Generate synthetic image data for training an image classification model.

    Args:
        output_dir (str): Directory to save the generated images.
        num_classes (int): Number of classes to create.
        images_per_class (int): Number of images per class.
    """
    # Ensure the output directory exists
    os.makedirs(output_dir, exist_ok=True)

    for class_idx in range(num_classes):
        class_dir = os.path.join(output_dir, f"class_{class_idx}")
        os.makedirs(class_dir, exist_ok=True)
        
        for img_idx in range(images_per_class):
            # Create a blank image
            img = Image.new('RGB', (64, 64), (255, 255, 255))
            draw = ImageDraw.Draw(img)
            
            # Add random shapes to the image
            for _ in range(random.randint(5, 15)):
                shape_type = random.choice(["rectangle", "ellipse"])
                x1, y1 = random.randint(0, 50), random.randint(0, 50)
                x2, y2 = x1 + random.randint(5, 20), y1 + random.randint(5, 20)
                color = tuple(random.randint(0, 255) for _ in range(3))
                
                if shape_type == "rectangle":
                    draw.rectangle([x1, y1, x2, y2], fill=color, outline=None)
                elif shape_type == "ellipse":
                    draw.ellipse([x1, y1, x2, y2], fill=color, outline=None)
            
            # Save the image
            img_path = os.path.join(class_dir, f"image_{img_idx}.png")
            img.save(img_path)

    print(f"Generated synthetic image data in '{output_dir}'")

if __name__ == "__main__":
    # Generate 5 classes with 100 images each
    generate_image_data("data/images", num_classes=5, images_per_class=100)

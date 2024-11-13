from diffusers import StableDiffusionPipeline
import torch
from PIL import Image
import cv2
import random

def check_gpu():
    if torch.cuda.is_available():
        gpu_name = torch.cuda.get_device_name(0)
        print(f"GPU detected: {gpu_name}")
        return True
    else:
        raise RuntimeError("No GPU detected! This script is designed to run only on GPU.")

def load_model():
    print("Loading Stable Diffusion model on GPU only...")
    check_gpu()
    pipe = StableDiffusionPipeline.from_pretrained("CompVis/stable-diffusion-v1-4").to("cuda")
    print("Model loaded on GPU.")
    
    return pipe


def generate_image(pipe, prompt, output_file="generated_image.png", height=512, width=512, guidance_scale=20, num_inference_steps=999, use_half_precision=True):
   
    if use_half_precision:
        pipe = pipe.to(torch.float16)
    
    print(f"Generating image for prompt: {prompt} at resolution {height}x{width} with guidance scale {guidance_scale} and steps {num_inference_steps}")
    
    image = pipe(prompt, height=height, width=width, guidance_scale=guidance_scale, num_inference_steps=num_inference_steps).images[0]

    image.save(output_file)
    print(f"Image saved as {output_file}")
    
    return output_file 


def resize_image(input_file, output_file, new_width=3840, new_height=2160):

    img = Image.open(input_file)

    img_resized = img.resize((new_width, new_height), Image.LANCZOS)

    img_resized.save(output_file)
    print(f"Image resized to {new_width}x{new_height} and saved as {output_file}")

def upscale_image_opencv(input_file, output_file, scale=2, new_width=3840, new_height=2160):
    img = cv2.imread(input_file)
    
    upscaled_img = cv2.resize(img, (new_width, new_height), interpolation=cv2.INTER_CUBIC)
    
    cv2.imwrite(output_file, upscaled_img)
    print(f"Image upscaled by {scale}x and saved as {output_file}")

pipe = load_model()
prompt = ""
generated_image_file =generate_image(pipe, prompt, output_file=f"generated_image\{random.randrange(0,99999999)}.png")
resize_image(generated_image_file, f"generated_image\{random.randrange(0,99999999)}.png", new_width=3840, new_height=2160)
img_number = random.randrange(0,99999999)
upscale_image_opencv(generated_image_file,f"generated_image\{img_number}.png", scale=4)
import torch

# Check if CUDA is available
cuda_available = torch.cuda.is_available()

if cuda_available:
    # Get the CUDA device count
    cuda_device_count = torch.cuda.device_count()
    print(f"CUDA is available with {cuda_device_count} devices.")
else:
    print("CUDA is not available on this system.")

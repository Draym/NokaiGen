import torch
from aegan import Generator as G
import torchvision.utils as vutils

genexateXImages = 100
device = torch.device('cpu')
netG = G()
netG.load_state_dict(torch.load('trained_generator_weights.pt', map_location=device))
vec = torch.randn((genexateXImages, 16))
with torch.no_grad():
    fake = netG(vec)

for i in range(genexateXImages):
    vutils.save_image(fake.data[i], f'generated/img.{i:02d}.png', normalize=True)
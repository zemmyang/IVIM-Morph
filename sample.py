from ivim_morph.infer import load_case, infer_from_data
import os
import torch 

path = '//tcmldrive/NogaK/fetal_lung_case'
device = 'cuda' if torch.cuda.is_available() else 'cpu'

data_path = os.path.join(path, 'Case709_data.pt')
seg_path = os.path.join(path, 'Case709_seg.pt')
signal, seg = load_case(data_path, seg_path, device=device)

bvalues = [0, 50, 100, 200, 400, 600]

Dp, D, f = infer_from_data(signal, seg, bvalues, device=device)

print(Dp, D, f)

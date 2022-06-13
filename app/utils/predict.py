from PIL import Image
import torch
import torch.nn as nn
import timm
from torchvision import transforms
import pandas as pd
import warnings
warnings.filterwarnings('ignore')


class Model(nn.Module):
    def __init__(self, name, num_classes):
        super(Model, self).__init__()
        self.model = timm.create_model(name, pretrained=True, in_chans=3)
        self.model.reset_classifier(num_classes=0)
        in_features = self.model.num_features
        self.fc = nn.Linear(in_features, num_classes)

    def forward(self, x):
        x = self.model(x)
        x = self.fc(x)
        return x


class BirdsSongsDatasetOnce(torch.utils.data.Dataset):

    def __init__(self, audio_samples):
        self.audio_samples = audio_samples

    def __len__(self):
        return len(self.audio_samples)

    def __getitem__(self, index):
        image = Image.open(self.audio_samples)
        transform = transforms.Compose([transforms.ToTensor()])
        image = transform(image)

        return image


def create_data_loader_once_record(audio_paths, batch_size):
    ds = BirdsSongsDatasetOnce(
        audio_samples=audio_paths
    )
    data_loader = torch.utils.data.DataLoader(ds, batch_size=batch_size, num_workers=0)

    return data_loader


def load_model(path, device=torch.device('cpu'), name='resnest50d', num_classes=26):
    model = Model(name, num_classes)
    model.load_state_dict(torch.load(path, map_location=device))

    return model


def create_result(record_path, model_path="data/model/model.pt"):
    device = torch.device("cuda") if torch.cuda.is_available() else torch.device("cpu")
    nn_model = load_model(model_path)
    data_loader = create_data_loader_once_record(record_path, 1)
    nn_model.eval().to(device)
    result = None
    for data in data_loader:
        device_data = data.to(device)
        result = nn_model(device_data)

    return result


def get_argmax_elem_name(tensor, filepath="data/model/bird.csv"):
    index_max = torch.argmax(tensor)
    index_str = str(index_max.tolist()[0])
    bird_index_df = pd.read_csv(filepath)
    bird_name = bird_index_df.loc[bird_index_df.class_label == index_str].bird.unique()[0]
    return bird_name

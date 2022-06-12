import os.path
import librosa
import numpy as np
from PIL import Image
from sklearn import preprocessing


def get_sample(filename, class_name, output_folder):
    wave_data, wave_rate = librosa.load(filename)
    wave_data, _ = librosa.effects.trim(wave_data)
    song_sample = []
    sample_length = 5 * wave_rate
    samples_from_file = []
    n_mels = 216
    for idx in range(0, len(wave_data), sample_length):
        song_sample = wave_data[idx: idx + sample_length]
        if len(song_sample) >= sample_length:
            mel = librosa.feature.melspectrogram(song_sample, n_mels=n_mels)
            db = librosa.power_to_db(mel)
            normalised_db = preprocessing.minmax_scale(db)
            filename = class_name + ".tif"
            db_array = (np.asarray(normalised_db) * 255).astype(np.uint8)
            db_image = Image.fromarray(np.array([db_array, db_array, db_array]).T)
            db_image.save(os.path.join(output_folder, filename))

            samples_from_file.append({"song_sample": "{}{}".format(output_folder, filename),
                                      "bird": class_name})
    return samples_from_file

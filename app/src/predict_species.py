import numpy as np

from classifier import classifier


def predict_species_from(sample):
    """
    :param sample: Dict[float, float, float, float]. Represents the features of
    a single iris species to be classified.
    :return:
    """
    sampled_data = [
        sample["sepal_length_in_cm"],
        sample["sepal_width_in_cm"],
        sample["petal_length_in_cm"],
        sample["petal_width_in_cm"],
    ]
    np_array = np.array(sampled_data)
    reshaped_data_for_single_sample = np_array.reshape(1, -1)
    prediction = classifier.predict(reshaped_data_for_single_sample)
    predicted_species = prediction[0]
    return predicted_species

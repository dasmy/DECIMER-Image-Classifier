# -*- coding: utf-8 -*-

"""
decimer_image_classifier Python Package.

DECIMER Image Classifier is a classifier based on EfficientNetB0 that tells
images of chemical structures and other types of images apart.
"""

import os

# Use Keras 2 instead of 3, see
# https://blog.tensorflow.org/2024/03/whats-new-in-tensorflow-216.html
os.environ["TF_USE_LEGACY_KERAS"] = "1"
del os

__version__ = "1.0.0"

__all__ = [
    "decimer_image_classifier",
]


from .decimer_image_classifier import DecimerImageClassifier

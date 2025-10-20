# Machine Learning Paradigms

!!! quote "Sources"
    - [Mastering the Basics: Understanding Supervised and Unsupervised Learning Algorithms - Tech & Tales](https://techntales.medium.com/mastering-the-basics-understanding-supervised-and-unsupervised-learning-algorithms-0db403af7557)
    - [What is Semi-Supervised Learning? - IBM Technology](https://www.youtube.com/watch?v=C3Lr6Waw66g)

## What is Machine Learning?

The ultimate goal of machine learning (ML) is to train algorithms to accurately classify events as a function of known data about those events. For example, a model may be trained to predict tomorrow's weather based on time series of different atmospheric measurements.

How does a machine learn, and how can we assess how successfully they do so? The learning process is necessarly split into two variations: supervised and unsupervised learning. Yet both variations require the chosen ML algorithm to be fed example data, reflecting the data to be inputted to the final, trained algorithm when making its predictions.

Using more training data improves the achievable accuracy of an ML model (to first order) as it offers more evidence of underlying trends which should be learned. Models will overfit to the limited sample available in a small dataset. Training data provided must be representative of the true population data to guarantee generalisability, but it must also be _clean_; adding noisy data may actually decrease prediction accuracy because the model begins to fit to noise!

The example data for ML training is decomposed into two sets: the training and testing data. The former is used to incrementally optimise an algorithm's parameters towards making successful classifications, and the latter is then fed into the tuned model to evaluate to what extent the training process generalises to unseen data. A common train/test split proportion is 80/20.

## Supervised vs Unsupervised Learning

For this training data, if each data entry is labelled with its correct classification, training can directly optimise prediction accuracy through comparison with the labels provided—this defines supervised learning. Instead, if the the true classifications are not included within the training/testing data, the model itself must identify patterns within the data facilitating the prediction of outcomes, or instead patterns which motivate the splitting of the dataset into insightful subgroups. This second scenario requires unsupervised ML algorithms, and given that the true labels are unknown, an accuracy metric cannot be used to quantify their implementation success. Below is a table of common supervised/unsupervised learning techniques[^1].

| Supervised | Unsupervised |
|-----------|-----------|
| Linear regression    | K-means clustering    |
| Decision trees    | Hierarchical clustering    |
| Neural nets    | PCA    |

!!! Note "Practicality of Labelling"
    Manually labelling datasets can be time-consuming, hence why unsupervised learning can be desirable.

### Semi-supervised Learning

There is in fact a third paradigm: semi-supervised learning. Given the difficulty of performing lots of data annotation (so as to build a sufficiently large dataset), a dataset with labelled data can be padded with unlabelled data. This added context helps tackle overfitting when the number of labelled data entries would otherwise be smaller than ideal.

The wrapper method involves using a base model, which was trained on labelled data, to predict the labels for any unlabelled data[^2]. These generated labels are deemed "pseudolabels" and are assgined a probability of being correct. Sufficiently confident predictions are added to the labelled training data and then training can be repeated, now with a larger, labelled dataset. The wrapper method can be applied iteratively, using an increasingly well-trained model to predict labels, growing the dataset, and re-training on even more data to improve generalisability.

Alternatively, a clustering method (like K-means) could be applied and, within a cluster, the labelled elements inform the appropriate labels for its unlabelled elements[^2]. After which, an AI model can be trained through supervised learning, using all available labels.

Both of these can be combined with a process known as active learning. Pseudolabels assigned with low confidence could be passed onto a human to manually label. Crucially, combining human labelling with semi-supervised learning vastly reduces the human labour required.

## How is data labelled?

Suppose we wanted to train an algorithm to recognise the species of animals within an image. The data informing predictions would be the RGB values of each pixel (numerical quanties) and the label it is trying to predict would be a string of the animal species' name. Importantly, non-numerical labels must be encoded numerically,

One approach to this is one-hot encoding, in which unit vectors (of 0s and 1s) are used, with dimensions matching the number of classification types. 0s are said to be cold, whereas 1s are said to be hot. For a given class type, only one component is hot, whilst all the others are cold. Think of each species as a basis vector within a vector space of animal species.

An alternative encoding method is label-coding. For example, `"dog"=0`, `"cat"=1`, `"bird"=2`, etc.

For more complicated images, image segmentation labels are used to point to where exactly the label applies within the image, e.g. which pixel region contains an animal of a given species.


<!-- ## Feature Engineering

https://www.ibm.com/think/topics/feature-engineering

IBM article reference -->


[^1]: Mastering the Basics: Understanding Supervised and Unsupervised Learning Algorithms - Tech & Tales, 2023, [Link](https://techntales.medium.com/mastering-the-basics-understanding-supervised-and-unsupervised-learning-algorithms-0db403af7557))
[^2]: What is Semi-Supervised Learning? - IBM Technology, 2025, [Link](https://www.youtube.com/watch?v=C3Lr6Waw66g)


"""
This is the digitrecognition module.
"""

class DigitRecognizer:
    """
    A class used to represent a digit recognizer.

    ...

    Attributes
    ----------
    model : object
        the machine learning model used for digit recognition
    """

    def __init__(self, model):
        """
        Parameters
        ----------
        model : object
            The machine learning model to use for digit recognition
        """
        self.model = model

    def recognize(self, image):
        """
        Recognize the digit in the given image.

        Parameters
        ----------
        image : array-like
            The image of the digit to recognize

        Returns
        -------
        int
            The recognized digit
        """
        # Method implementation here
        pass

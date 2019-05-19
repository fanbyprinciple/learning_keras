# importin

from keras.models import Sequential
from keras.layers.noramlization import BatchNormalization
from keras.layers.convolutional import Conv2D
from keras.layers.core import Activation, Flatten, Dropout, Dense

from keras import backend as K 

print("imported !")

class StrideNet:
    @staticmethod
    def build(width, height, depth, classes, reg, init="he_normal"):
        # he build  method accepts six parameters:

        # width : Image width in pixels.
        # height : The image height in pixels.
        # depth : The number of channels for the image.
        # classes : The number of classes the model needs to predict.
        # reg : Regularization method.
        # init : The kernel initializer.
        model = Sequential()
        inputShape = (height, width, depth) # defining input shape 
        chanDim = -1 # used to indicate if channel_first is used

        # if we are using "channels first", update the input shape
		# and channels dimension
		if K.image_data_format() == "channels_first":
			inputShape = (depth, height, width)
			chanDim = 1

        # first layer - 16 filters, each of 7*7 , stride of 2*2
        # Conv2D
        # keras.layers.Conv2D(filters, kernel_size, strides=(1, 1), padding='valid', data_format=None, dilation_rate=(1, 1), 
        # activation=None, use_bias=True, kernel_initializer='glorot_uniform', bias_initializer='zeros', kernel_regularizer=None, 
        # bias_regularizer=None, activity_regularizer=None, kernel_constraint=None, bias_constraint=None)
        
        # strides 2*2 as a replacement of matrix pooling
        # padding valid will ensure that the kernal doesn't go out bounds of the input
        # kernal initialiser is used to classify conolutional layers prior to training the network
        # kernal regulariser helps us to regularise the model to prevent overfitting
        model.add(Conv2D(16, (7,7), strides=(2,2), padding="valid", kernel_initializer=init,kernal_regularizer=reg, input_shape=inputShape))

        # stacking two more convolutoinal filters
        # both 32, 3*3
        # reference for filters - https://www.saama.com/blog/different-kinds-convolutional-filters/
        model.add(Conv2D(32,(3,3), padding='same', kernal_initializer=init, kernal_regularizer=reg))
        
        model.add(Activation('relu'))
        model.add(BatchNormalization(axis=chanDim))
        model.add


import keras
model = keras.models.load_model('handwritten_digits.model.keras')
model.summary()

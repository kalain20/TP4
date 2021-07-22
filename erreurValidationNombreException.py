class ErreurValidationNombreException(Exception):

    def __init__(self, nombre, message):
        super().__init__()
        self.nombre = nombre

        if nombre < 0:
            raise ErreurValidationNombreException(message)

from usuario import usuario

class cliente():

    def __init__(self, cedula, nombre, apellido, telefono, fecha_nacimiento, email, tipo_usuario, estado, password, contacto_emergencia, limitaciones_fisicas, especificacion_limitacion):
        super().__init__( cedula, nombre, apellido, telefono, fecha_nacimiento, email, tipo_usuario, estado, password)
        self.__contacto_emergencia = contacto_emergencia
        self.__limitaciones_fisicas = limitaciones_fisicas
        self.__especificacion_limitacion = especificacion_limitacion
        
        
    
    # metodos get
    def get_contacto_emergencia(self):
        return self.__contacto_emergencia
    def get_limitaciones_fisicas(self):
        return self.__limitaciones_fisicas
    def get_especificacion_limitacion(self):
        return self.__especificacion_limitacion
    
    
    
    #metodos set
    def set_contacto_emergencia(self, contacto_emergencia):
        self.__contacto_emergencia = contacto_emergencia
    def set_limitaciones_fisicas(self, limitaciones_fisicas):
        self.__contacto_emergencia = limitaciones_fisicas
    def set_especificacion_limitacion(self, especificacion_limitacion):
        self.__contacto_emergencia = especificacion_limitacion
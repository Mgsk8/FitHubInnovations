class usuario():

    def __init__(self, cedula, nombre, apellido, telefono, fecha_nacimiento, email, tipo_usuario, estado, password):
        self.__cedula_usuario = cedula
        self.__nombre = nombre
        self.__apellido = apellido
        self.__telefono = telefono
        self.__fecha_nacimiento = fecha_nacimiento
        self.__email = email
        self.__tipo_usuario = tipo_usuario
        self.__estado = estado
        self.__password = password
    
    # metodos get
    def get_cedula(self):
        return self.__cedula_usuario
    def get_nombre(self):
        return self.__nombre
    def get_apellido(self):
        return self.__apellido
    def get_telefono(self):
        return self.__telefono
    def get_fecha_nacimiento(self):
        return self.__fecha_nacimiento
    def get_email(self):
        return self.__email
    def get_tipo_usuario(self):
        return self.__tipo_usuario
    def get_estado(self):
        return self.__estado
    def get_password(self):
        return self.__password
    
    #metodos set
    def set_cedula(self, cedula):
        self.__cedula_usuario = cedula
    def set_nombre(self, nombre):
        self.__nombre = nombre
    def set_apellido(self, apellido):
        self.__apellido = apellido
    def set_telefono(self, telefono):
        self.__telefono = telefono
    def set_fecha_nacimiento(self,fecha_nacimiento):
        self.__fecha_nacimiento = fecha_nacimiento
    def set_email(self, email):
        self.__email = email
    def set_tipo_usuario(self, tipo_usuario):
        self.__tipo_usuario = tipo_usuario
    def set_estado(self, estado):
        self.__estado = estado
    def set_password(self, password):
        self.__password = password
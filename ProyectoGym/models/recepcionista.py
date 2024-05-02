from usuario import usuario

class recepcionista():

    def __init__(self, cedula, nombre, apellido, telefono, fecha_nacimiento, email, tipo_usuario, estado, password, salario, direccion, id_horario_predefinido):
        super().__init__( cedula, nombre, apellido, telefono, fecha_nacimiento, email, tipo_usuario, estado, password)
        self.__salario = salario
        self.__direccion = direccion
        self.__id_horario_predefinido = id_horario_predefinido
        
    
    # metodos get
    def get_salario(self):
        return self.__salario
    def get_direccion(self):
        return self.__direccion
    def get_id_horario_predefinido(self):
        return self.__id_horario_predefinido
    
    
    #metodos set
    def set_nombre(self, salario):
        self.__salario = salario
    def set_direccion(self, direccion):
        self.__direccion = direccion
    def set_id_horario_predefinido(self, id_horario_predefinido):
        self.__id_horario_predefinido = id_horario_predefinido
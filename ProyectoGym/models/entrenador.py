from usuario import usuario

class entrenador():

    def __init__(self,  cedula, nombre, apellido, telefono, fecha_nacimiento, email, tipo_usuario, estado, password, salario, especialidad, direccion):
        super().__init__( cedula, nombre, apellido, telefono, fecha_nacimiento, email, tipo_usuario, estado, password)
        self.__salario = salario
        self.__especialidad = especialidad
        self.__direccion = direccion
        
        
    
    # metodos get
    def get_salario(self):
        return self.__salario
    def get_especialidad(self):
        return self.__especialidad
    def get_direccion(self):
        return self.__direccion
    
    
    
    #metodos set
    def set_nombre(self, salario):
        self.__salario = salario
    def set_especialidad(self, especialidad):
        self.__especialidad = especialidad
    def set_direccion(self, direccion):
        self.__direccion = direccion
    
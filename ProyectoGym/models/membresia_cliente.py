class membresia_cliente():

    def __init__(self, id_membresia, fecha_inicio, fecha_fin, tipo_membresia, id_cliente, estado):
            
        self.__id_membresia = id_membresia
        self.__fecha_inicio = fecha_inicio
        self.__fecha_fin = fecha_fin
        self.__tipo_membresia = tipo_membresia
        self.__id_cliente = id_cliente
        self.__estado = estado
        
    
    # metodos get
    def get_id_membresia(self):
        return self.__id_membresia
    
    def get_fecha_inicio(self):
        return self.__fecha_inicio

    def get_fecha_fin(self):
        return self.__fecha_fin
    
    def get_tipo_membresia(self):
        return self.__tipo_membresia
    
    def get_id_cliente(self):
        return self.__id_cliente
    
    def get_estado(self):
        return self.__estado
    
    #metodos set
    def set_id_membresia(self, id_membresia):
        self.__id_membresia = id_membresia
    
    def set_fecha_inicio(self, fecha_inicio):
        self.__fecha_inicio = fecha_inicio

    def set_fecha_fin(self, fecha_fin):
       self.__fecha_fin = fecha_fin
    
    def set_tipo_membresia(self, tipo_membresia):
        self.__tipo_membresia = tipo_membresia
    
    def set_id_cliente(self, id_cliente):
        self.__id_cliente = id_cliente
    
    def set_estado(self, estado):
        self.__estado = estado
class horario_dinamico():

    def __init__(self, id_horario_dinamico, dia, hora_entrada, hora_salida, id_entrenador):
        self.__id_horario_dinamico = id_horario_dinamico
        self.__dia = dia
        self.__hora_entrada = hora_entrada
        self.__hora_salida = hora_salida
        self.__id_entrenador = id_entrenador
        
        
    
    # metodos get
    def get_id_horario_dinamico(self):
        return self.__id_horario_dinamico
    def get_dia(self):
        return self.__dia
    def get_hora_entrada(self):
        return self.__hora_entrada
    def get_hora_salida(self):
        return self.__hora_salida
    def get_id_entrenador(self):
        return self.__id_entrenador
    
    
    #metodos set
    def set_id_horario_dinamico(self, horario_dinamico):
        self.__id_horario_dinamico = horario_dinamico
    def set_dia(self, dia):
        self.__dia = dia
    def set_hora_entrada(self, hora_entrada):
        self.__hora_entrada = hora_entrada
    def set_hora_salida(self, hora_salida):
        self.__hora_salida = hora_salida
    def set_id_entrenador(self, id_entrenador):
        self.__id_entrenador = id_entrenador
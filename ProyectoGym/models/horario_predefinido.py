class horario_predefinido():

    def __init__(self, id_horario_predefinido, dia, turno):
        self.__id_horario_predefinido = id_horario_predefinido
        self.__dia = dia
        self.__turno = turno
        
    
    # metodos get
    def get_id_horario_predefinido(self):
        return self.__id_horario_predefinido
    def get_dia(self):
        return self.__dia
    def get_hora_turno(self):
        return self.__turno
    

    #metodos set
    def set_id_horario_predefinido(self, horario_predefinido):
        self.__id_horario_predefinido = horario_predefinido
    def set_dia(self, dia):
        self.__dia = dia
    def set_turno(self, turno):
        self.__turno = turno
    
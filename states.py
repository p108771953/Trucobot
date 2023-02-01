from collections import namedtuple

class RoundState(namedtuple('_RoundState', ['turno', 'envido', 'pips', 'stacks', 'hands', 'deck', 'previous_state'])):
    '''
        *Resultado del envido (o si no se ha cantado, y si se puede cantar)
        *Valor actual del truco (1, 2, 3, ó 4)
        *cartas que se han jugado
        *active (bool : si es o no tu turno)
        *
    '''
    pass

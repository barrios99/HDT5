#Albeño, Fátima - 18060
#De León, Diana - 18607

import simpy
import random

contador_ins = 0
intervalo = 10
cant_procesos = random.expovariate(1.0/intervalo)

def proceso(cant_m,cant_p, extra ,env):
    memoria = cant_m
    # yield pidomemoria memoria.put cant_m
    # pedir procesador
    yield env.timeout(1)
    #seguir
    
def prueba(env):
    m_ram = simpy.Container(env, init=100)
    cpu = simpy.Resource(env, capacity = 1)
    p = env.process(proceso(m_ram,cant_procesos,cpu,env))
    yield p

env = simpy.Environment()
env.process(prueba(env))   
env.run()

#Asigna espacio entre 1 y 10 de RAM al proceso
random.seed(25)
espacio = random.randint(1,10)

#Crear la memoria RAM, capacidad maxima 100

#Albeño, Fátima - 18060
#De León, Diana - 18607

import simpy
import random

contador_ins = 0
intervalo = 10
cant_procesos = random.expovariate(1.0/intervalo)

def proceso(cant_m,cant_p, extra ,env):
    memoria = cant_m
    yield env.timeout(cant_p)
    
def prueba(env):
    #Crear la memoria RAM, capacidad maxima 100
    m_ram = simpy.Container(env, init=100)
    cpu = simpy.Resource(env, capacity = 1)
    p = env.process(proceso(m_ram,cant_procesos,cpu,env))
    yield p

#Asigna espacio entre 1 y 10 de RAM al proceso
random.seed(25)
espacio = random.randint(1,10)

env = simpy.Environment()
print (env.process(prueba(env)) )  
env.run()




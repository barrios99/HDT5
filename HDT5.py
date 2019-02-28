#Albeño, Fátima - 18060
#De León, Diana - 18607

import simpy
import random
import statistics as stats

v_p=2 #velocidad del procesador
contador_ins = 0
intervalo = 10

def proceso(m_ram, cant_p, espacio, env):
    global tiempo_procesos
    inicio=env.now
    random.seed(25)
    yield m_ram.put(espacio)
    with cpu.request() as turno:
        yield turno
        yield env.timeout(cant_p/v_p)
        yield m_ram.get(espacio)
    print('Pasando el proceso que usa '+ str(espacio) +' de RAM con '+ str(cant_p)+' de instrucciones en %d segundos'%env.now)
    tiempo_trans=env.now-inicio
    print ('se tardo %f para el proceso' % (tiempo_trans))
    tiempo_procesos.append(tiempo_trans)


def create(m_ram, cant_p, space, env):
    yield env.timeout(random.expovariate(1.0 / 10))
    env.process(proceso(m_ram, cant_p, space, env))



env = simpy.Environment()
#Crear la memoria RAM, capacidad maxima 100
m_ram = simpy.Container(env, init=0, capacity=100)
cpu = simpy.Resource(env, capacity = 1)
tiempo_procesos=[]
for i in range(25):
    env.process(create(m_ram, int(random.expovariate(1.0/intervalo)),random.randint(1,10),env))  
env.run()
print ("tiempo promedio por proceso es: ", stats.mean(tiempo_procesos))
print ("la desviacion estandar es: ", stats.pstdev(tiempo_procesos))



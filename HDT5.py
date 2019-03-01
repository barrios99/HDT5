#Albeño, Fátima - 18060
#De León, Diana - 18607

#importar librerias
import collections
import simpy
import random
import statistics as stats


def proceso(numero, m_ram, cant_p, espacio, env):
    ciclo=0
    global tiempo_procesos
    if ciclo==0:
        ciclo=1
        inicio=env.now
        print('Entrando el proceso %s que usa '%(numero)+ str(espacio) +' de RAM con '+ str(cant_p)+' de instrucciones en el %d segundos'%(env.now))
        yield m_ram.put(espacio)
        yield env.timeout(1)
    if ciclo>0:
        print('El proceso %s esta solicitando acceso  en el %d segundos'%(numero,env.now))
        yield env.timeout(0.1)
        with cpu.request() as req:
            yield req
            print('El proceso %s acceso en el %d segundos'%(numero,env.now))
            yield env.timeout(0.1)
            ciclo=2
            while cant_p>0:   
                if cant_p<=3:
                    cant_p=0
                    yield env.timeout(1)
                    yield m_ram.get(espacio)
                    ciclo=4
                elif cant_p>3:
                    cant_p-=3
                    yield env.timeout(1)
                    espera=random.randint(1,2)
                    ciclo=3
                    if espera==1:
                        tiempo_esp=random.randint(1,5) #tiempo de operaciones de entrada y salida
                        yield env.timeout(tiempo_esp)
                        ciclo=3
                
    if ciclo==4:
        print ('Proceso %s terminado en el %d segundos' %(numero,env.now))
        tiempo_trans=env.now-inicio
        print ('El proceso %s tardo %f segundos'%(numero,tiempo_trans))
        tiempo_procesos.append(tiempo_trans)


def create(numero, m_ram, cant_p, space, env):
    yield env.timeout(random.expovariate(1.0 / 10))
    env.process(proceso(numero, m_ram, cant_p, space, env))

#crea el ambiente de simpy
env = simpy.Environment()
#Crear la memoria RAM, capacidad maxima 100
m_ram = simpy.Container(env, init=0, capacity=100)
#Crear el CPU, la capacity es la velocidad del cpu
cpu = simpy.Resource(env, capacity = 1)
#guarda el tiempo que le toma a cada proceso realizar sus instrucciones 
tiempo_procesos=[]
random.seed(800)
#genera la cantidad de procesos que se quieran simular 
for i in range(25):
    env.process(create('%s'%i, m_ram,random.randint(1,10),random.randint(1,10),env))  
env.run()
#Calcula el promedio y desviacion estandar del tiempo usando la libreria de estadisticas 
print ("Tiempo promedio por proceso es: ", stats.mean(tiempo_procesos))
print ("La desviacion estandar es: ", stats.pstdev(tiempo_procesos))



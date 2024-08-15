import grpc
import calculadora_pb2
import calculadora_pb2_grpc
import sys

def ejecutar(operacion, numero1, numero2):
    # Crea un canal de comunicación con el servidor gRPC
    with grpc.insecure_channel('10.195.40.26:50051') as canal:
        # Crea un stub (cliente) a partir del canal
        stub = calculadora_pb2_grpc.CalculadoraStub(canal)

        if operacion == 'sumar':
            # Llama al método Sumar en el servidor con los números proporcionados
            respuesta = stub.Sumar(calculadora_pb2.OperacionSolicitud(numero1=numero1, numero2=numero2))
            # Imprime el resultado de la suma
            print(f'Resultado de sumar {numero1} y {numero2}: {respuesta.resultado}')
        
        elif operacion == 'restar':
            # Llama al método Restar en el servidor con los números proporcionados
            respuesta = stub.Restar(calculadora_pb2.OperacionSolicitud(numero1=numero1, numero2=numero2))
            # Imprime el resultado de la resta
            print(f'Resultado de restar {numero1} y {numero2}: {respuesta.resultado}')
        
        else:
            print("Operación no válida. Use 'sumar' o 'restar'.")

if __name__ == '__main__':
    if len(sys.argv) != 4:
        print("Uso: python cliente.py <operacion> <numero1> <numero2>")
        print("Ejemplo: python cliente.py sumar 10 5")
    else:
        operacion = sys.argv[1]  # 'sumar' o 'restar'
        numero1 = float(sys.argv[2])  # Primer número
        numero2 = float(sys.argv[3])  # Segundo número
        ejecutar(operacion, numero1, numero2)

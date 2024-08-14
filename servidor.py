from concurrent import futures
import grpc
import calculadora_pb2
import calculadora_pb2_grpc

# Implementación del servicio Calculadora
class CalculadoraServicer(calculadora_pb2_grpc.CalculadoraServicer):
    # Implementación del método Sumar
    def Sumar(self, request, context):
        # Suma los dos números recibidos en la solicitud
        resultado = request.numero1 + request.numero2
        # Devuelve la respuesta con el resultado de la suma
        return calculadora_pb2.OperacionRespuesta(resultado=resultado)

    # Implementación del método Restar
    def Restar(self, request, context):
        # Resta los dos números recibidos en la solicitud
        resultado = request.numero1 - request.numero2
        # Devuelve la respuesta con el resultado de la resta
        return calculadora_pb2.OperacionRespuesta(resultado=resultado)

# Función para iniciar el servidor gRPC
def servir():
    # Crea un servidor gRPC con un pool de threads
    servidor = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    # Registra el servicio Calculadora en el servidor
    calculadora_pb2_grpc.add_CalculadoraServicer_to_server(CalculadoraServicer(), servidor)
    # Especifica el puerto donde el servidor estará escuchando
    servidor.add_insecure_port('[::]:50051')
    # Inicia el servidor
    servidor.start()
    # Mantiene el servidor en ejecución
    servidor.wait_for_termination()

# Punto de entrada del servidor
if __name__ == '__main__':
    servir()

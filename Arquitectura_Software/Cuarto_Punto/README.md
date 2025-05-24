Ejercicio de sistema serverles

- recibe comentarios mediante una API HTTP y los almacena sin servidor usando AWS.

Componentes
- AWS API Gateway: Endpoint público
- AWS lambda: Código para manejar la lógica
- dynamoDB: Base de datos sin servidor

--Estructura del comentario--
```json
{
  "id": "abc123",
  "cliente": "Juan Pérez",
  "mensaje": "Excelente servicio"
}

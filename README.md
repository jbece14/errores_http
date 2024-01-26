# Respuestas estandar de errores HTTP comunes en APIs
Este repositorio contiene unas respuestas estandar sobre los errores HTTP mas comunes en el desarrollo de APIs, esto con el fin de tener mas claridad a la hora de ver una respuesta en los logs, saber el porque y como arreglarlo

Los errores que se manejan en este desarrollo son los siguientes
* 400 Bad Request
* 401 Unauthorized
* 403 Forbidden
* 404 Not Found
* 405 Method Not Allowed
* 408 Request Timeout
* 429 Too Many Requests
* 500 Internal Server Error

De igual modo tambien podremos encontrar las respuestas correctas que puede retornar el API
* 200 Ok
* 201 Created

En cada funcion es posible enviar un mensaje personalizado, aparte del ya generado de manera estandar, esto es mas que todo para desarrollos especificos donde se requieran mandar IDs, payloads o demas datos clave que se puedan necesitar en el JSON resultante

Por otro lado podemos encontrar los test de cada metodo, con el fin de que cuando sean usados puedan pasar por el checkeo de Sonar Cloud

# SIGA - Revisión de un pull request

Laboratorio de Seguridad de Software II

## Contexto

SIGA es una API de ejemplo para consultar pedidos.

La rama principal comienza con una funcionalidad mínima: una ruta de salud que permite comprobar si la API responde.

Un próximo pull request propondrá agregar inicio de sesión y consulta de pedidos. El equipo deberá revisar sus cambios antes de decidir si pueden integrarse.

## Objetivo de la actividad

Revisar código y resultados de herramientas de seguridad, identificar riesgos y justificar las correcciones necesarias.

La revisión conectará los siguientes conceptos:

- STRIDE: Clasificación de amenazas.
- OWASP ASVS: Requisitos de verificación de seguridad.
- ADR: Registro de una decisión de arquitectura.
- CI/CD: Integración y entrega continua.
- SAST: Análisis estático de seguridad del código.
- SCA: Análisis de dependencias y vulnerabilidad conocidad
- Detección de secretos
- Revisión de la configuración de contenedores.

## Estado inicial

Archivo de la aplicación: app.py.

Ruta disponible:

GET / salud

Respuesta esperada:

{"estado": "ok"}

En esta versión no hay usuarios, contraseñas, tokens, consultas a bases de datos ni endpoints de pedidos.

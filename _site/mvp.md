# MVP - Sistema Integrado de Gestión Configurable

**Versión:** 2.0 - Con módulo opcional de transporte  
**Fecha:** Agosto 2025  
**Aplicación Web Multitenant | Multi-rol por Tenant**

## Resumen Ejecutivo

Sistema web genérico y configurable para la gestión integrada de normas **ISO 9001** (Calidad), **ISO 14001** (Ambiental), **ISO 45001** (Seguridad y Salud en el Trabajo), **Decreto 1072** (SST Colombia) y opcionalmente **Decreto 1079 de 2015** (Sector Transporte Colombia) según el tipo de empresa cliente.

**Arquitectura:** 70% genérico configurable + 30% específico por norma + **módulo sectorial opcional para transporte**.

---

## Configuración por Tipo de Cliente

### Clientes Generales (Manufactura, Servicios, Construcción, etc.)
**Normas base disponibles:**
- ISO 9001 (Calidad)
- ISO 14001 (Ambiental) 
- ISO 45001 (SST)
- Decreto 1072 (SST Colombia)

### Clientes del Sector Transporte
**Normas base + módulo sectorial:**
- ISO 9001, ISO 14001, ISO 45001, Decreto 1072
- **+ Decreto 1079 de 2015** (Módulo activado automáticamente)
- **+ Funcionalidades especializadas** de transporte

### Aclaración sobre Construcción
Las **empresas de construcción** usan las **mismas normas base** que otros sectores:
- **ISO 9001, 14001, 45001, Decreto 1072**
- **NO requieren módulo especial** para gestión empresarial
- Las normas técnicas (NSR-10, Ley 400) son para diseño, no para SIG

### Futuros Sectores (Roadmap)
- **Sector Salud**: + Habilitación sanitaria
- **Sector Financiero**: + Superintendencia Financiera  
- **Sector Minero**: + Títulos mineros y ambientales

---

## Core Genérico (70% del Sistema)

### 1. Motor Universal de Eventos
**Un solo formulario que se adapta según configuración**

#### Campos base (siempre presentes):
- Fecha/hora del evento
- Área donde ocurrió
- Descripción del evento
- Persona que reporta
- Evidencias (fotos/documentos)

#### Configuración por norma:
- **Tipos de eventos ISO 9001**: No conformidad, Queja de cliente, Producto defectuoso, Falla de proceso
- **Tipos de eventos ISO 14001**: Derrame, Emisión no controlada, Mal manejo de residuos, Consumo excesivo de recursos
- **Tipos de eventos ISO 45001**: Accidente de trabajo, Incidente peligroso, Casi accidente, Acto inseguro, Condición insegura
- **Tipos de eventos Decreto 1072**: Accidente de trabajo reportable, Enfermedad laboral, Incidente de alto potencial
- **Campos adicionales**: Se agregan o quitan según el tipo seleccionado
- **Flujo de estados**: Configurable por tipo de evento
- **Responsables**: Asignación automática según reglas configuradas por la empresa

#### Estados universales:
```
Reportado → En análisis → Acciones en curso → Verificación → Cerrado
```

### 2. Dashboard Universal Configurable
**Widgets genéricos que se personalizan por norma/rol**

#### Widgets base:
- Contador de eventos (por estado, por norma)
- Semáforo general del sistema
- Mis pendientes (eventos asignados)
- Próximos vencimientos (alertas)
- Gráfico de tendencias mensual

#### Configuración:
- Cada rol ve solo sus widgets relevantes
- Filtros automáticos por norma asignada
- Personalización de métricas por empresa

### 3. Motor de Requisitos Legales
**Sistema genérico de seguimiento de obligaciones**

#### Estructura base:
- Nombre del requisito
- Norma que lo exige
- Frecuencia (anual, mensual, por evento)
- Responsable
- Fecha de vencimiento
- Estado (Vigente/Por vencer/Vencido)

#### Configuración por norma:
- Lista de requisitos específicos
- Plantillas de documentos
- Reglas de escalamiento
- Destinatarios de alertas

### 4. Sistema de Auditorías Universal
**Mismo flujo para todas las normas**

#### Fases genéricas:
1. **Planificación** (fechas, alcance, equipo auditor)
2. **Ejecución** (listas de verificación configurables)
3. **Hallazgos** (formato estándar)
4. **Plan de acción** (seguimiento automático)
5. **Cierre** (verificación de eficacia)

#### Configuración:
- Plantillas de listas por norma
- Frecuencias de auditoría
- Equipos auditores por competencia

### 5. Gestor Documental Universal
**Control unificado con etiquetado por norma**

#### Funciones base:
- Subir/descargar documentos
- Control de versiones automático
- Flujo de aprobación configurable
- Búsqueda por etiquetas/metadatos
- Alertas de revisión automáticas

#### Configuración:
- Tipos de documentos por norma
- Flujos de aprobación por tipo
- Plantillas predefinidas
- Responsables por categoría

---

## Módulo Específico - Transporte (20% del Sistema)

### **Decreto 1079 de 2015 - Sector Transporte (Activación Opcional)**

#### Gestión de Habilitaciones
- **Registro de empresas**: NIT, representante legal, objeto social
- **Tipos de servicio**: Público, especial, particular, carga
- **Radio de acción**: Municipal, departamental, nacional
- **Seguimiento de vigencias**: Habilitación empresarial, permisos operación

#### Control de Vinculación Vehicular
- **Contratos de vinculación**: Propietario, empresa, vehículo
- **Tarjetas de operación**: Número, vigencia, ruta autorizada
- **Modificaciones**: Cambios de empresa, propietario, servicio
- **Desvinculaciones**: Causas, procedimientos, reportes

#### Reportes Obligatorios Superintendencia
- **Reporte mensual de flota**: Vehículos operativos, rutas atendidas
- **Accidentes reportables**: Formato oficial, plazos de reporte
- **Cambios empresariales**: Representante legal, domicilio, capital
- **Sanciones recibidas**: Multas, suspensiones, revocatorias

#### Control de Seguros Obligatorios
- **SOAT por vehículo**: Vigencia, beneficiarios, reclamaciones
- **RCC (Responsabilidad Civil Contractual)**: Valores, vigencias
- **RCE (Responsabilidad Civil Extracontractual)**: Coberturas específicas
- **Seguros adicionales**: Vehículo, mercancía, pasajeros

#### Eventos Específicos Transporte
- **Vehículo sin documentos**: SOAT, revisión técnica, tarjeta operación
- **Conductor sin licencia**: Categoría incorrecta, vencida, suspendida
- **Exceso de velocidad**: Reportes de autoridades, GPS
- **Incumplimiento de ruta**: Desvíos no autorizados, horarios
- **Falla mecánica**: Que afecte la operación o seguridad

---

## Pantallas del MVP

### 1. Configuración Inicial por Sector (Solo Admin Tenant)
**Wizard que se adapta al tipo de empresa**

#### Configuración Base (Todos los clientes):
- **Seleccionar normas activas** (ISO 9001, 14001, 45001, 1072)
- **Definir áreas y responsables** por norma
- **Configurar tipos de eventos** personalizados
- **Registrar usuarios y roles** del sistema
- **Personalizar dashboard** según necesidades

#### Configuración Adicional Transporte (Solo si aplica):
- **Activar módulo Decreto 1079** automáticamente
- **Configurar tipo de empresa**: Pasajeros, carga, especial, mixto
- **Registrar flota**: Tipos de vehículos, capacidades, rutas
- **Importar conductores**: Licencias, categorías, especialidades
- **Configurar control GPS**: Integración con sistemas de rastreo
- **Definir rutas autorizadas**: Permisos, horarios, frecuencias

### 2. Dashboard Universal Adaptable
**Vista que se personaliza según el sector del cliente**

#### Dashboard Base (Todos los clientes):
- **Estado general del SIG**: Semáforo por norma activa
- **Eventos pendientes**: Por responsable y prioridad  
- **Próximos vencimientos**: Documentos, auditorías, capacitaciones
- **Indicadores clave**: Configurables por tipo de empresa
- **Acceso rápido**: Reportar evento, consultar documentos

#### Dashboard Transporte (Solo clientes del sector):
- **+ Estado de flota**: Vehículos operativos vs fuera de servicio
- **+ Mapa de rutas**: Ubicación de vehículos en tiempo real  
- **+ Control de conductores**: Habilitados, en ruta, disponibles
- **+ Alertas críticas**: Documentos vehiculares por vencer
- **+ Performance operativa**: Puntualidad, quejas, eficiencia

### 3. Reportar Evento Universal
**Formulario inteligente que se adapta**
- Selector de norma/tipo de evento
- Campos dinámicos según selección
- Validaciones configurables
- Asignación automática de responsable
- Generación de ticket único

### 4. Gestión de Recursos (Adaptable por Sector)
**Control de activos según tipo de empresa**

#### Para Clientes Generales:
- **Lista de equipos/áreas**: Maquinaria, instalaciones, procesos
- **Estado de recursos**: Operativo, mantenimiento, fuera de servicio
- **Documentación**: Manuales, certificaciones, garantías
- **Mantenimientos**: Preventivos, correctivos, próximos servicios
- **Historial operativo**: Uso, eventos, performance general

#### Para Clientes de Transporte (Funcionalidad extendida):
- **+ Control de flota**: Vehículos con documentación especializada
- **+ Gestión de conductores**: Licencias, capacitaciones, turnos
- **+ Seguimiento GPS**: Ubicación, rutas, cumplimiento horarios
- **+ Control combustible**: Consumos, eficiencia, costos
- **+ Mantenimientos vehiculares**: Según kilometraje y tiempo

### 5. Gestión de Personal (Base + Especializada)
**Control integral del personal según sector**

#### Para Todos los Clientes (Base):
- **Lista de empleados**: Por área, cargo, competencias
- **Capacitaciones**: Programadas, ejecutadas, certificaciones
- **Evaluaciones**: Desempeño, competencias, médicas
- **Documentación**: Contratos, certificados, permisos
- **Historial laboral**: Eventos, capacitaciones, evaluaciones

#### Para Transporte (Funcionalidad extendida):
- **+ Control de conductores**: Licencias por categoría y vigencia
- **+ Turnos y descansos**: Jornadas, tiempo de conducción máximo
- **+ Rutas asignadas**: Autorizaciones, performance por ruta
- **+ Exámenes específicos**: Visiometría, audiometría, coordinación
- **+ Cursos obligatorios**: Transporte público, manejo defensivo

### 6. Matriz de Requisitos Legales
**Control especializado de obligaciones**

#### Para todos los clientes:
- **ISO 14001**: Permisos ambientales, licencias, reportes a autoridades
- **Decreto 1072**: Reportes a ARL, comité de convivencia, COPASST, capacitaciones obligatorias
- Estados: Vigente / Por vencer (30 días) / Vencido
- Alertas automáticas por vencimiento

#### Adicional para transporte:
- **+ Decreto 1079**: Habilitaciones, tarjetas de operación, seguros obligatorios
- **+ Reportes Superintendencia**: Mensuales, accidentes, cambios empresariales

### 7. Calendario Integrado
**Vista mensual de todas las actividades**
- **Auditorías** internas por norma
- **Inspecciones** programadas
- **Vencimientos** de documentos y permisos
- **Reportes** obligatorios a entidades
- **Capacitaciones** programadas

### 8. Reportes y Analytics
**Inteligencia de negocio básica**
- Dashboards por norma
- Tendencias de eventos
- Cumplimiento de objetivos
- Reportes ejecutivos automáticos
- Exportación a PDF/Excel

---

## Roles Universales (Configurables)

### Super Admin (Multitenant)
- Crear/gestionar tenants
- Configuración global del sistema
- Monitoreo de uso y performance

### Admin Tenant
- Configurar sistema para su empresa
- Gestionar usuarios y permisos
- Personalizar flujos y formularios
- Acceso a todos los reportes

### Responsable SIG
- Vista consolidada de todas las normas
- Coordinación entre diferentes sistemas
- Reportes ejecutivos integrados

### Especialista por Norma
- Acceso solo a su norma específica
- Gestión de eventos de su especialidad
- Configuración de requisitos específicos

### **Roles Adicionales para Transporte:**

#### Gerente de Operaciones
- Vista consolidada de operación de transporte
- Control de flota y conductores
- Reportes ejecutivos de performance

#### Jefe de Flota
- Gestión completa de vehículos
- Control de mantenimientos y documentación
- Asignación de vehículos a rutas

#### Coordinador de Conductores
- Gestión de personal de conducción
- Control de turnos y descansos
- Seguimiento de capacitaciones

### Supervisor de Área
- Ver solo eventos de su área
- Reportar eventos
- Seguimiento de personal a cargo

### Usuario Operativo
- Reportar eventos
- Ver sus eventos reportados
- Consultar documentos públicos
- Ver calendario general

---

## Configuración Clave del Sistema

### Por Tenant (Empresa)
- Normas activas
- Estructura organizacional (áreas)
- Tipos de eventos personalizados
- Responsables por defecto
- Plantillas de documentos
- Frecuencias de auditoría

### Por Norma
- Tipos de eventos específicos
- Campos obligatorios/opcionales
- Estados del flujo
- Plantillas de reportes
- Requisitos legales aplicables

### Por Usuario
- Normas asignadas
- Áreas de responsabilidad
- Widgets visibles en dashboard
- Notificaciones activas

---

## Criterios de Éxito del MVP (3 meses)

### Adopción General del Sistema
- **10+ empresas piloto activas** (de diferentes sectores)
- **80% de eventos gestionados** en sistema vs métodos manuales
- **15+ usuarios activos** por empresa cliente
- **90% satisfacción** vs método anterior

### Eficiencia Operativa Universal
- **50% reducción en tiempo** de gestión de eventos
- **30% menos tiempo** en auditorías por documentación digital
- **40% reducción en costos** de multas y sanciones
- **100% trazabilidad** de procesos críticos

### Cumplimiento Legal (Todos los sectores)
- **100% de reportes obligatorios** en tiempo y forma
- **0 multas por reportes tardíos** (ARL, autoridades)
- **95% de requisitos legales** al día
- **24/7 disponibilidad** de información para auditorías

### Indicadores Específicos por Sector

#### Clientes Generales:
- **90% de documentos** controlados digitalmente
- **100% de NC** con seguimiento completo
- **Reducción 60% tiempo** en preparación de auditorías

#### Clientes de Transporte:
- **100% de vehículos** con documentación digital
- **0 vehículos operando** sin documentación vigente
- **95% puntualidad** en renovación de documentos críticos
- **Integración GPS** operativa al 100%

---

## Estrategia de Activación por Sector

### Detección Automática del Sector
Durante el registro del tenant, el sistema detecta automáticamente el sector basado en:
- **Actividad económica CIIU** declarada
- **Tipo de empresa** seleccionada en el wizard
- **Palabras clave** en razón social (transporte, logística, etc.)
- **Configuración manual** por el admin si es ambiguo

### Activación Progresiva de Módulos
1. **Fase 1**: Normas base (ISO 9001, 14001, 45001, 1072)
2. **Fase 2**: Detección del sector y propuesta de módulos adicionales
3. **Fase 3**: Activación automática de funcionalidades sectoriales (solo transporte)
4. **Fase 4**: Configuración específica y personalización

### Escalabilidad Sectorial
- **Módulo actual**: Transporte (Decreto 1079)
- **Próximos módulos**: Salud, Financiero, Minería (con normativas específicas de gestión)
- **Arquitectura preparada**: Para agregar nuevos sectores sin afectar existentes
- **Construcción**: Usa normas base, no requiere módulo especial

---

## Diferenciadores Competitivos

1. **Enfoque genérico configurable** - Un solo desarrollo sirve para múltiples sectores
2. **Especialización real para transporte** - Cumplimiento Decreto 1079 automatizado
3. **Integración real** - Eventos que afectan múltiples normas se gestionan una sola vez
4. **Configuración rápida** - Setup completo en menos de 2 horas por empresa
5. **Multitenant nativo** - Escalabilidad para múltiples empresas desde el diseño
6. **Módulos opcionales** - Solo se activan cuando el cliente los necesita
7. **Base sólida universal** - Sirve para cualquier tipo de empresa

---

## Configuración por Tipo de Empresa

### Empresas Generales (Manufactura, Servicios, Comercio, Construcción)
- **Normas**: ISO 9001, ISO 14001, ISO 45001, Decreto 1072
- **Eventos típicos**: No conformidades, incidentes ambientales, accidentes laborales
- **Documentos críticos**: Procedimientos, licencias ambientales, certificaciones SST
- **Indicadores**: Satisfacción cliente, cumplimiento ambiental, accidentalidad

### Empresas de Transporte (Activación Automática Módulo)
- **Normas**: Base + Decreto 1079
- **Eventos típicos**: Fallas vehiculares, problemas de conductores, incumplimientos operativos
- **Documentos críticos**: Habilitaciones, tarjetas de operación, seguros obligatorios
- **Indicadores**: Disponibilidad de flota, cumplimiento de rutas, satisfacción usuarios

---

**Documento final del MVP - Sistema Integrado de Gestión**  
**Sistema universal con módulo especializado para transporte**  
**Listo para desarrollo e implementación**
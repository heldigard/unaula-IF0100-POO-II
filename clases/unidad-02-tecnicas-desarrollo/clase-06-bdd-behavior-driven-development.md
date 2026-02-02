---
marp: true
theme: default
paginate: true
header: 'IF0100 - Lenguaje de Programación OO II | Unidad 2'
footer: 'UNAULA - Ingeniería Informática - 2026-I'
style: |
  section {
    font-size: 22px;
  }
  h1 {
    color: #1e40af;
    font-size: 2em;
  }
  h2 {
    color: #1e3a8a;
    font-size: 1.5em;
  }
  h3 {
    color: #3b82f6;
    font-size: 1.2em;
  }
  table {
    font-size: 0.85em;
  }
  code {
    font-size: 0.8em;
  }
  pre {
    font-size: 0.7em;
  }
---

<!-- _class: lead -->

# BDD - Behavior-Driven Development

**IF0100 - Lenguaje de Programación OO II**
*4° Semestre - Ingeniería Informática*

**Duración:** 90 minutos | **Unidad 2 - Clase 6**

---

## Objetivos de la Clase

Al finalizar esta clase, el estudiante será capaz de:

| # | Objetivo |
|---|-----------|
| 1 | **Distinguir** entre TDD y BDD |
| 2 | **Escribir** escenarios en lenguaje Gherkin |
| 3 | **Implementar** pruebas de comportamiento con SpecFlow |
| 4 | **Aplicar** el formato Given-When-Then |
| 5 | **Comunicar** requisitos de forma comprensible para todos |

---

## Agenda (90 min)

| Tiempo | Tema |
|--------|------|
| 15' | TDD vs BDD: ¿Cuál es la diferencia? |
| 15' | Gherkin: Lenguaje de especificación |
| 10' | SpecFlow para .NET |
| 20' | Escribiendo escenarios BDD |
| 20' | Implementación de Step Definitions |
| 10' | Buenas prácticas BDD |

---

## 1. TDD vs BDD

### 📊 Tabla Comparativa

| Aspecto | **TDD** | **BDD** |
|---------|---------|---------|
| **Enfoque** | TÉCNICO | NEGOCIO/COMPORTAMIENTO |
| **Audiencia** | Desarrolladores | TODOS (devs, QA, clientes) |
| **Lenguaje** | Código (C#) | Natural (español/inglés) |
| **Prueba** | Unidades pequeñas | Comportamiento del sistema |
| **Pregunta** | "¿Funciona?" | "¿Hace lo que el usuario espera?" |

### 💡 Ejemplo: Calculadora

| TDD | BDD |
|-----|-----|
| ```csharp<br>[Fact]<br>public void Sumar_RetornaResultado() {<br>&nbsp;&nbsp;Assert.Equal(5, calc.Sumar(2,3));<br>}<br>``` | ```gherkin<br>Dado que ingreso 2 y 3<br>Cuando solicito la suma<br>Entonces el resultado debe ser 5<br>``` |

---

## TDD vs BDD: Resumen Visual

```
┌─────────────────────────────────────────────────────────────┐
│                    TDD vs BDD                               │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│         TDD (Test Driven Development)                       │
│         ─────────────────────────────                       │
│                                                             │
│   • Enfoque: TÉCNICO                                       │
│   • Audiencia: DESARROLLADORES                             │
│   • Lenguaje: Código (C#, Java)                            │
│   • Prueba: Unidades pequeñas                              │
│   • Pregunta: "¿El código funciona?"                       │
│                                                             │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│         BDD (Behavior Driven Development)                   │
│         ─────────────────────────────────                   │
│                                                             │
│   • Enfoque: COMPORTAMIENTO/NEGOCIO                        │
│   • Audiencia: TODOS (devs, QA, clientes)                  │
│   • Lenguaje: Natural (español/inglés)                     │
│   • Prueba: Comportamiento del sistema                     │
│   • Pregunta: "¿El sistema hace lo que el usuario espera?" │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

---

## BDD: Concepto Fundamental

### 📖 Definición

> **BDD** es una metodología de desarrollo de software que fomenta la colaboración entre desarrolladores, QA y equipos de negocio, utilizando un lenguaje compartido y comprensible para todos.

### 🏛️ Principios Fundamentales BDD

| # | Principio |
|---|-----------|
| 1 | **LENGUAJE UBIQUO** - Un lenguaje compartido entre técnicos y negocio |
| 2 | **ESPECIFICACIÓN EJECUTABLE** - Los requisitos son pruebas automatizadas |
| 3 | **COMPORTAMIENTO ANTES QUE IMPLEMENTACIÓN** - "¿Qué debe hacer?" antes de "¿Cómo lo hace?" |
| 4 | **COLABORACIÓN** - Three Amigos: Dev + QA + Business |
| 5 | **DOCUMENTACIÓN VIVA** - Las especificaciones siempre están actualizadas |

---

## Los Tres Amigos

### 📊 Roles y Preguntas Clave

| Rol | Perspectiva | Pregunta clave |
|-----|-------------|------------------|
| **Negocio (PO)** | Valor | ¿Qué problema resolvemos? |
| **Desarrollador** | Solución | ¿Cómo lo construimos? |
| **Tester (QA)** | Calidad | ¿Qué podría fallar? |

### 💡 Valor de la Colaboración

| Beneficio | Descripción |
|-----------|-------------|
| Comprensión compartida | Todos entienden el requisito igual |
| Ejemplos concretos | Desde el inicio, no al final |
| Incertidumbre resuelta | Antes de codificar |
| Menos retrabajo | Menos reuniones de explicación |

> **Práctica:** Reunión de "Three Amigos" antes de cada historia

---

## Gherkin: Lenguaje de Especificación

### 📝 Vocabulario Básico

| Español | Inglés | Propósito |
|---------|--------|-----------|
| `Característica` | `Feature` | Agrupa escenarios relacionados |
| `Antecedentes` | `Background` | Pasos comunes a todos los escenarios |
| `Escenario` | `Scenario` | Caso de prueba específico |
| `Dado` | `Given` | Precondiciones/contexto inicial |
| `Cuando` | `When` | Acción/evento principal |
| `Entonces` | `Then` | Resultado esperado/verificación |
| `Y` | `And` | Continúa paso anterior |
| `Pero` | `But` | Excepción/alternativa |
| `Ejemplos` | `Examples` | Tabla de datos para esquemas |

---

## Formato Given-When-Then

### 🔄 Estructura Visual

```
┌─────────────────────────────────────────────────────────────┐
│                 GIVEN-WHEN-THEN                             │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│   GIVEN (Dado/Antecedentes)                                  │
│   • Precondiciones del escenario                            │
│   • Estado inicial del sistema                              │
│   • Contexto necesario                                    │
│                                                             │
│   WHEN (Cuando)                                              │
│   • Acción principal del usuario                            │
│   • Evento que dispara el comportamiento                   │
│                                                             │
│   THEN (Entonces)                                            │
│   • Resultado esperado                                    │
│   • Verificación del comportamiento                          │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

---

## Ejemplo Completo: Cajero Automático

```gherkin
# language: es
Característica: Retiro de dinero desde cajero automático
  Como cliente del banco
  Quiero retirar dinero desde un cajero
  Para tener efectivo disponible

  Escenario: Retiro exitoso con saldo suficiente
    Dado que tengo una cuenta con saldo de $1000
    Y mi tarjeta está activa
    Cuando intento retirar $200
    Entonces el cajero debe entregarme $200
    Y el saldo de mi cuenta debe ser $800
    Y debo recibir un recibo de la transacción

  Escenario: Retiro fallido por saldo insuficiente
    Dado que tengo una cuenta con saldo de $100
    Cuando intento retirar $200
    Entonces el cajero debe mostrar "Saldo insuficiente"
    Y no debe entregarme dinero
    Y el saldo de mi cuenta debe seguir siendo $100
```

---

## 2. SpecFlow para .NET

### 📦 Instalación

```bash
# Opción 1: Plantilla
dotnet new specflowproject -n MiApp.Specs --framework xunit

# Opción 2: Manual
dotnet new classlib -n MiApp.Specs
dotnet add package SpecFlow.xUnit
dotnet add package SpecFlow.Tools.MsBuild.Generation
dotnet add package FluentAssertions
dotnet add package xunit
dotnet add reference ../MiApp/MiApp.csproj
```

### 📋 Paquetes Clave

| Paquete | Versión | Propósito |
|---------|---------|-----------|
| SpecFlow.xUnit | 3.9.74 | Integración con xUnit |
| SpecFlow.Tools.MsBuild.Generation | 3.9.74 | Genera código C# desde .feature |
| FluentAssertions | 6.12.0 | Assertions fluidas y legibles |

### 📖 FluentAssertions

**FluentAssertions** es una librería que hace las aserciones más legibles con una sintaxis fluida "encadenada".

```csharp
// Sin FluentAssertions
Assert.Equal(5, resultado);                  // ✅ Poco legible
Assert.True(promedio >= 3.0);                // ❌ No dice cuál es el valor

// Con FluentAssertions
resultado.Should().Be(5);                     // ✅ "resultado should be 5"
promedio.Should().BeGreaterOrEqualTo(3.0);  // ✅ Mucho más claro
nombre.Should().NotBeNullOrEmpty();         // ✅ Self-documenting
```

> 💡 **Beneficio:** Las pruebas leen como oraciones en inglés.

---

## Estructura de Proyecto SpecFlow

```
MiApp.Specs/
├── Features/                    ← Archivos .feature (Gherkin)
│   ├── Calculadora.feature
│   └── RetiroCajero.feature
│
├── StepDefinitions/             ← C# que implementa pasos
│   ├── CalculadoraSteps.cs
│   └── RetiroCajeroSteps.cs
│
├── Hooks/                       ← Configuración global
│   └── Hooks.cs
│
├── Drivers/                     ← Helpers y utilidades
│   └── CalculadoraDriver.cs
│
└── MiApp.Specs.csproj
```

---

## 3. Escribiendo Escenarios BDD

### 📋 Ejemplo: Gestión de Calificaciones

```gherkin
# language: es
Característica: Gestión de calificaciones estudiantiles
  Como profesor
  Quiero registrar y consultar calificaciones
  Para llevar el control académico

  Antecedentes:
    Dado el estudiante con código "2024001"
    Y nombre "María López"

  Escenario: Registrar calificaciones exitosamente
    Dado que el estudiante está inscrito en "Matemáticas"
    Cuando registro las notas:
    | Parcial | Nota |
    | 1 | 4.5 |
    | 2 | 3.8 |
    | 3 | 4.2 |
    Entonces el promedio debe ser 4.17
    Y el estado debe ser "Aprobado"

  Escenario: Estudiante reprueba por promedio bajo
    Dado que el estudiante está inscrito en "Física"
    Cuando registro las notas:
    | Parcial | Nota |
    | 1 | 2.5 |
    | 2 | 2.8 |
    | 3 | 2.0 |
    Entonces el promedio debe ser 2.43
    Y el estado debe ser "Reprobado"
```

---

## Esquema de Escenario con Ejemplos

### 🔄 Parametrización en Gherkin

```gherkin
# language: es
Característica: Cálculo de descuento
  Como vendedor
  Quiero calcular descuentos automáticamente
  Para ofrecer precios competitivos

  Esquema del escenario: Aplicar descuento según categoría
    Dado un producto con precio <precio>
    Y el cliente es de categoría <categoria>
    Cuando calculo el precio final
    Entonces el descuento debe ser <descuento>%
    Y el precio final debe ser <precio_final>

    Ejemplos:
| precio | categoria | descuento | precio_final |
| 100 | "normal" | 0 | 100 |
| 100 | "frecuente" | 5 | 95 |
| 100 | "vip" | 10 | 90 |
| 200 | "vip" | 10 | 180 |
| 500 | "frecuente" | 5 | 475 |
```

> 💡 **Nota:** Un esquema equivale a 5 escenarios separados

---

## 4. Implementación de Step Definitions

### 🔧 Conectando Gherkin con C#

```csharp
// StepDefinitions/CalificacionesSteps.cs
using TechTalk.SpecFlow;
using FluentAssertions;
using MiApp;

namespace MiApp.Specs.StepDefinitions
{
    // [Binding]: Conecta pasos Gherkin con código C#
    // SpecFlow busca métodos con este atributo y los ejecuta
    [Binding]
    public class CalificacionesSteps
    {
        private readonly EscenarioContext _context;
        private Estudiante _estudiante;

        public CalificacionesSteps(EscenarioContext context)
        {
            _context = context;
        }

        [Given(@"el estudiante con código ""([^""]*)"",("")]
        public void DadoElEstudianteConCodigo(string codigo)
        {
            _estudiante = new Estudiante { Codigo = codigo };
        }

        [When(@"registro las notas:")]
        public void CuandoRegistroLasNotas(Table tabla)
        {
            foreach (var fila in tabla.Rows)
            {
                int parcial = int.Parse(fila["Parcial"]);
                double nota = double.Parse(fila["Nota"]);
                _estudiante.RegistrarNota(parcial, nota);
            }
            _promedio = _estudiante.CalcularPromedio();
        }

        [Then(@"el promedio debe ser (.*)")]
        public void EntoncesElPromedioDebeSer(double esperado)
        {
            _promedio.Should().BeApproximately(esperado, 0.01);
        }
    }
}
```

---

## 5. Buenas Prácticas BDD

### ✅ Escenarios Efectivos

| ✅ HACER | ❌ EVITAR |
|-----------|-------------|
| Ser específico y concreto | Ser demasiado técnico |
| Usar lenguaje del dominio | Usar nombres técnicos de campos |
| Un concepto por escenario | Mezclar múltiples conceptos |
| Datos realistas | Valores genéricos |

### 📋 Checklist BDD

| ✅ Nivel | Verificación |
|-----------|-------------|
| **Abstracción** | Pasos describen QUÉ, no CÓMO |
| **Independencia** | Cada escenario ejecuta solo |
| **Legibilidad** | Cualquiera del negocio lo entiende |
| **Especificidad** | Datos concretos, no genéricos |
| **Atomicidad** | Un escenario = un comportamiento |

---

## Documentación Viva

```
┌─────────────────────────────────────────────────────────────┐
│                 DOCUMENTACIÓN VIVA                          │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│   CÓDIGO (C#)          PRUEBAS (Gherkin)         REPORTE    │
│      ↓                      ↓                      ↓        │
│   ┌──────┐             ┌──────────┐           ┌────────┐   │
│   │Calcul│─────────────▶│*.feature │───────────▶│Pickles │   │
│   │adora│             │Escenarios│           └────────┘   │
│   └──────┘             └──────────┘           ┌────────┐   │
│                                                             │
│   Herramientas para generar documentación:                  │
│   • Pickles (genera HTML/PDF/Word desde .feature)          │
│   • SpecFlow+ LivingDoc (integrado con Azure DevOps)       │
│                                                             │
│   Resultado: Documentación siempre actualizada porque         │
│   los tests FALLAN si el comportamiento cambia             │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

---

## 🚀 Próxima Clase: DDD - Domain Driven Design

| Tema | Descripción |
|------|-------------|
| **DDD** | Dominio vs Infraestructura |
| **Entities** | Objetos con identidad |
| **Value Objects** | Objetos sin identidad |
| **Aggregates** | Agrupaciones de raíz |
| **Repositories** | Acceso a persistencia |
| **Services** | Lógica de dominio |

---

## Taller: BDD para Biblioteca

### 📚 Ejercicio Práctico

Crear escenarios BDD para sistema de préstamo de libros

**Contexto del dominio:**
- Usuarios pueden pedir libros prestados
- Cada libro tiene un plazo de devolución (14 días)
- Hay multas por retraso ($500/día)
- Límite de 5 libros simultáneos por usuario

**Tareas:**
1. ✅ Escribir feature "Préstamo de libros"
2. ✅ Crear 3 escenarios (éxito, fallo, multa)
3. ✅ Implementar Step Definitions
4. ✅ Ejecutar y verificar

---

# ¡Gracias!
## ¿Preguntas?

**"El software es comportamiento, no código"**

**UNAULA - Ingeniería Informática - 2026-I**

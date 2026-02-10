"""
Tests de filtros personalizados de Jinja2 - TaskFlow
Unidad: 4.1 - Introducción a Jinja2

Este módulo contiene pruebas unitarias para todos los filtros
personalizados definidos en src/taskflow/templates_utils/filters.py
"""

import pytest
from datetime import datetime, timezone, timedelta

from src.taskflow.templates_utils.filters import (
    prioridad_badge_color,
    estado_badge_color,
    prioridad_icon,
    estado_icon,
    formatear_fecha,
    truncate_words,
    formatear_relativo,
    inicial_nombre,
)


class TestPrioridadBadgeColor:
    """
    Tests para el filtro prioridad_badge_color.

    Verifica que retorna la clase de color correcta
    para cada valor de prioridad.
    """

    def test_prioridad_baja_retorna_secondary(self):
        """
        Test prioridad baja retorna secondary.

        GIVEN: Prioridad 'baja'
        WHEN: Se llama a prioridad_badge_color
        THEN: Retorna 'secondary'
        """
        assert prioridad_badge_color('baja') == 'secondary'

    def test_prioridad_media_retorna_info(self):
        """
        Test prioridad media retorna info.

        GIVEN: Prioridad 'media'
        WHEN: Se llama a prioridad_badge_color
        THEN: Retorna 'info'
        """
        assert prioridad_badge_color('media') == 'info'

    def test_prioridad_alta_retorna_warning(self):
        """
        Test prioridad alta retorna warning.

        GIVEN: Prioridad 'alta'
        WHEN: Se llama a prioridad_badge_color
        THEN: Retorna 'warning text-dark'
        """
        assert prioridad_badge_color('alta') == 'warning text-dark'

    def test_prioridad_urgente_retorna_danger(self):
        """
        Test prioridad urgente retorna danger.

        GIVEN: Prioridad 'urgente'
        WHEN: Se llama a prioridad_badge_color
        THEN: Retorna 'danger'
        """
        assert prioridad_badge_color('urgente') == 'danger'

    def test_prioridad_desconocida_retorna_secondary(self):
        """
        Test prioridad desconocida retorna secondary por defecto.

        GIVEN: Prioridad no reconocida
        WHEN: Se llama a prioridad_badge_color
        THEN: Retorna 'secondary' (valor por defecto)
        """
        assert prioridad_badge_color('inexistente') == 'secondary'


class TestEstadoBadgeColor:
    """
    Tests para el filtro estado_badge_color.

    Verifica que retorna la clase de color correcta
    para cada valor de estado.
    """

    def test_estado_pendiente_retorna_secondary(self):
        """
        Test estado pendiente retorna secondary.

        GIVEN: Estado 'pendiente'
        WHEN: Se llama a estado_badge_color
        THEN: Retorna 'secondary'
        """
        assert estado_badge_color('pendiente') == 'secondary'

    def test_estado_en_progreso_retorna_info(self):
        """
        Test estado en_progreso retorna info.

        GIVEN: Estado 'en_progreso'
        WHEN: Se llama a estado_badge_color
        THEN: Retorna 'info'
        """
        assert estado_badge_color('en_progreso') == 'info'

    def test_estado_completada_retorna_success(self):
        """
        Test estado completada retorna success.

        GIVEN: Estado 'completada'
        WHEN: Se llama a estado_badge_color
        THEN: Retorna 'success'
        """
        assert estado_badge_color('completada') == 'success'

    def test_estado_cancelada_retorna_dark(self):
        """
        Test estado cancelada retorna dark.

        GIVEN: Estado 'cancelada'
        WHEN: Se llama a estado_badge_color
        THEN: Retorna 'dark'
        """
        assert estado_badge_color('cancelada') == 'dark'

    def test_estado_desconocido_retorna_secondary(self):
        """
        Test estado desconocido retorna secondary por defecto.

        GIVEN: Estado no reconocido
        WHEN: Se llama a estado_badge_color
        THEN: Retorna 'secondary' (valor por defecto)
        """
        assert estado_badge_color('inexistente') == 'secondary'


class TestPrioridadIcon:
    """
    Tests para el filtro prioridad_icon.

    Verifica que retorna el icono correcto
    para cada valor de prioridad.
    """

    def test_icono_prioridad_baja(self):
        """Test icono para prioridad baja."""
        assert prioridad_icon('baja') == 'arrow-down'

    def test_icono_prioridad_media(self):
        """Test icono para prioridad media."""
        assert prioridad_icon('media') == 'dash'

    def test_icono_prioridad_alta(self):
        """Test icono para prioridad alta."""
        assert prioridad_icon('alta') == 'arrow-up'

    def test_icono_prioridad_urgente(self):
        """Test icono para prioridad urgente."""
        assert prioridad_icon('urgente') == 'exclamation-triangle'

    def test_icono_prioridad_desconocida(self):
        """Test icono para prioridad desconocida."""
        assert prioridad_icon('inexistente') == 'circle'


class TestEstadoIcon:
    """
    Tests para el filtro estado_icon.

    Verifica que retorna el icono correcto
    para cada valor de estado.
    """

    def test_icono_estado_pendiente(self):
        """Test icono para estado pendiente."""
        assert estado_icon('pendiente') == 'clock'

    def test_icono_estado_en_progreso(self):
        """Test icono para estado en_progreso."""
        assert estado_icon('en_progreso') == 'hourglass-split'

    def test_icono_estado_completada(self):
        """Test icono para estado completada."""
        assert estado_icon('completada') == 'check-all'

    def test_icono_estado_cancelada(self):
        """Test icono para estado cancelada."""
        assert estado_icon('cancelada') == 'x-circle'

    def test_icono_estado_desconocido(self):
        """Test icono para estado desconocido."""
        assert estado_icon('inexistente') == 'question'


class TestFormatearFecha:
    """
    Tests para el filtro formatear_fecha.

    Verifica el formateo correcto de fechas en distintos formatos.
    """

    def test_fecha_iso_formateada_correctamente(self):
        """
        Test formatear fecha ISO estándar.

        GIVEN: Una fecha en formato ISO
        WHEN: Se llama a formatear_fecha
        THEN: Retorna la fecha en formato DD/MM/YYYY
        """
        fecha = "2026-02-07"
        resultado = formatear_fecha(fecha)
        assert resultado == "07/02/2026"

    def test_fecha_iso_con_hora_formateada(self):
        """
        Test formatear fecha ISO con hora.

        GIVEN: Una fecha ISO con hora y Z
        WHEN: Se llama a formatear_fecha
        THEN: Retorna la fecha formateada correctamente
        """
        fecha = "2026-02-07T10:30:00Z"
        resultado = formatear_fecha(fecha)
        assert resultado == "07/02/2026"

    def test_fecha_none_retorna_vacio(self):
        """
        Test fecha None retorna string vacío.

        GIVEN: Fecha es None
        WHEN: Se llama a formatear_fecha
        THEN: Retorna string vacío
        """
        assert formatear_fecha(None) == ""

    def test_fecha_vacia_retorna_vacio(self):
        """
        Test fecha vacía retorna string vacío.

        GIVEN: Fecha es string vacío
        WHEN: Se llama a formatear_fecha
        THEN: Retorna string vacío
        """
        assert formatear_fecha("") == ""

    def test_fecha_con_formato_personalizado(self):
        """
        Test formatear fecha con formato personalizado.

        GIVEN: Una fecha y formato personalizado
        WHEN: Se llama a formatear_fecha con formato
        THEN: Retorna la fecha en el formato especificado
        """
        fecha = "2026-02-07"
        resultado = formatear_fecha(fecha, formato="%Y-%m-%d")
        assert resultado == "2026-02-07"


class TestTruncateWords:
    """
    Tests para el filtro truncate_words.

    Verifica el truncado correcto de textos largos.
    """

    def test_truncar_texto_mas_largo_que_limite(self):
        """
        Test truncar texto más largo que el límite.

        GIVEN: Un texto más largo que el límite
        WHEN: Se llama a truncate_words
        THEN: Retorna el texto truncado con puntos suspensivos
        """
        texto = "Este es un texto muy largo que debe ser truncado"
        resultado = truncate_words(texto, 5)
        assert resultado == "Este es un texto muy..."

    def test_truncar_texto_mas_corto_que_limite(self):
        """
        Test truncar texto más corto que el límite.

        GIVEN: Un texto más corto que el límite
        WHEN: Se llama a truncate_words
        THEN: Retorna el texto original sin cambios
        """
        texto = "Texto corto"
        resultado = truncate_words(texto, 10)
        assert resultado == "Texto corto"

    def test_truncar_texto_exacto_al_limite(self):
        """
        Test truncar texto con longitud exacta al límite.

        GIVEN: Un texto con exactamente el número de palabras del límite
        WHEN: Se llama a truncate_words
        THEN: Retorna el texto original sin puntos suspensivos
        """
        texto = "Uno dos tres cuatro cinco"
        resultado = truncate_words(texto, 5)
        assert resultado == texto

    def test_truncar_texto_vacio(self):
        """
        Test truncar texto vacío.

        GIVEN: Un texto vacío
        WHEN: Se llama a truncate_words
        THEN: Retorna string vacío
        """
        assert truncate_words("") == ""

    def test_truncar_texto_none(self):
        """
        Test truncar texto None.

        GIVEN: Texto es None
        WHEN: Se llama a truncate_words
        THEN: Retorna string vacío
        """
        assert truncate_words(None) == ""


class TestFormatearRelativo:
    """
    Tests para el filtro formatear_relativo.

    Verifica el formateo correcto de fechas como tiempo relativo.
    """

    def test_fecha_ahora_mismo(self):
        """
        Test fecha hace pocos segundos.

        GIVEN: Una fecha hace menos de 60 segundos
        WHEN: Se llama a formatear_relativo
        THEN: Retorna "ahora mismo"
        """
        ahora = datetime.now(timezone.utc).isoformat()
        resultado = formatear_relativo(ahora)
        assert resultado == "ahora mismo"

    def test_fecha_hace_minutos(self):
        """
        Test fecha hace minutos.

        GIVEN: Una fecha hace 5 minutos
        WHEN: Se llama a formatear_relativo
        THEN: Retorna "hace 5 minutos"
        """
        hace_5_min = (datetime.now(timezone.utc) - timedelta(minutes=5)).isoformat()
        resultado = formatear_relativo(hace_5_min)
        assert "minuto" in resultado
        assert "5" in resultado

    def test_fecha_hace_horas(self):
        """
        Test fecha hace horas.

        GIVEN: Una fecha hace 3 horas
        WHEN: Se llama a formatear_relativo
        THEN: Retorna "hace 3 horas"
        """
        hace_3_horas = (datetime.now(timezone.utc) - timedelta(hours=3)).isoformat()
        resultado = formatear_relativo(hace_3_horas)
        assert "hora" in resultado
        assert "3" in resultado

    def test_fecha_hace_dias(self):
        """
        Test fecha hace días.

        GIVEN: Una fecha hace 5 días
        WHEN: Se llama a formatear_relativo
        THEN: Retorna "hace 5 días"
        """
        hace_5_dias = (datetime.now(timezone.utc) - timedelta(days=5)).isoformat()
        resultado = formatear_relativo(hace_5_dias)
        assert "día" in resultado
        assert "5" in resultado

    def test_fecha_muy_antigua_retorna_fecha_formateada(self):
        """
        Test fecha muy antigua retorna fecha formateada.

        GIVEN: Una fecha hace más de una semana
        WHEN: Se llama a formatear_relativo
        THEN: Retorna la fecha formateada como DD/MM/YYYY
        """
        hace_10_dias = (datetime.now(timezone.utc) - timedelta(days=10)).isoformat()
        resultado = formatear_relativo(hace_10_dias)
        assert "/" in resultado  # Debe tener formato de fecha

    def test_fecha_none_retorna_vacio(self):
        """
        Test fecha None retorna string vacío.

        GIVEN: Fecha es None
        WHEN: Se llama a formatear_relativo
        THEN: Retorna string vacío
        """
        assert formatear_relativo(None) == ""


class TestInicialNombre:
    """
    Tests para el filtro inicial_nombre.

    Verifica la extracción correcta de la inicial del nombre.
    """

    def test_inicial_nombre_simple(self):
        """
        Test inicial de nombre simple.

        GIVEN: Un nombre "Juan"
        WHEN: Se llama a inicial_nombre
        THEN: Retorna "J"
        """
        assert inicial_nombre("Juan") == "J"

    def test_inicial_nombre_completo(self):
        """
        Test inicial de nombre completo.

        GIVEN: Un nombre "Juan Pérez"
        WHEN: Se llama a inicial_nombre
        THEN: Retorna "J" (primera letra del nombre)
        """
        assert inicial_nombre("Juan Pérez") == "J"

    def test_inicial_nombre_minuscula(self):
        """
        Test inicial de nombre en minúscula.

        GIVEN: Un nombre "maría"
        WHEN: Se llama a inicial_nombre
        THEN: Retorna "M" (convertida a mayúscula)
        """
        assert inicial_nombre("maría") == "M"

    def test_inicial_nombre_none_retorna_interrogacion(self):
        """
        Test inicial de nombre None.

        GIVEN: Nombre es None
        WHEN: Se llama a inicial_nombre
        THEN: Retorna "?"
        """
        assert inicial_nombre(None) == "?"

    def test_inicial_nombre_vacio_retorna_interrogacion(self):
        """
        Test inicial de nombre vacío.

        GIVEN: Nombre es string vacío
        WHEN: Se llama a inicial_nombre
        THEN: Retorna "?"
        """
        assert inicial_nombre("") == "?"

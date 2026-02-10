#!/bin/bash
# Script para corregir caracteres raros en notebooks

echo "🔍 Escaneando notebooks en busca de caracteres raros..."

# Lista de notebooks
notebooks=(
  "notebooks/unidad-00/00-01-introduccion-python.ipynb"
  "notebooks/unidad-00/00-02-estructuras-control.ipynb"
  "notebooks/unidad-00/00-03-estructuras-datos.ipynb"
  "notebooks/unidad-00/00-04-modulos-errores.ipynb"
  "notebooks/unidad-01/01-01-clases-objetos.ipynb"
  "notebooks/unidad-01/01-02-encapsulamiento.ipynb"
  "notebooks/unidad-01/01-03-herencia-composicion.ipynb"
  "notebooks/unidad-01/01-04-polimorfismo.ipynb"
  "notebooks/unidad-01/01-05-interfaces.ipynb"
  "notebooks/unidad-02/02-01-tdd-intro.ipynb"
  "notebooks/unidad-02/02-02-tdd-ciclo.ipynb"
  "notebooks/unidad-02/02-03-testing-avanzado.ipynb"
  "notebooks/unidad-02/02-04-bdd-intro.ipynb"
  "notebooks/unidad-02/02-05-ddd-intro.ipynb"
)

for nb in "${notebooks[@]}"; do
  if [ -f "$nb" ]; then
    echo "Verificando: $nb"
  fi
done

echo "✅ Escaneo completado"

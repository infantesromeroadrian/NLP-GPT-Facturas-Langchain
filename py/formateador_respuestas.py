import json
import logging

class FormateadorRespuestas:
    def __init__(self, respuestas):
        self.respuestas = respuestas

    def obtener_formato_salida(self):
        """Transforma las respuestas en el formato de salida deseado."""
        return {
            "nombre_cliente": self.respuestas.get("¿Cuál es el nombre del cliente?", "").strip(),
            "dni_cliente": self.respuestas.get("¿Cuál es el DNI del cliente?", "").strip(),
            "calle_cliente": self.respuestas.get("¿Cuál es la calle del cliente?", "").strip(),
            "cp_cliente": self.respuestas.get("¿Cuál es el código postal del cliente?", "").strip(),
            "población_cliente": self.respuestas.get("¿Cuál es la población del cliente?", "").strip(),
            "provincia_cliente": self.respuestas.get("¿Cuál es la provincia del cliente?", "").strip(),
            "nombre_comercializadora": self.respuestas.get("¿Cuál es el nombre de la empresa comercializadora?", "").strip(),
            "cif_comercializadora": self.respuestas.get("¿Cuál es el CIF de la comercializadora?", "").strip(),
            "dirección_comercializadora": self.respuestas.get("¿Cuál es la dirección de la comercializadora?", "").strip(),
            "cp_comercializadora": self.respuestas.get("¿Cuál es el código postal de la comercializadora?", "").strip(),
            "población_comercializadora": self.respuestas.get("¿Cuál es la población de la comercializadora?", "").strip(),
            "provincia_comercializadora": self.respuestas.get("¿Cuál es la provincia de la comercializadora?", "").strip(),
            "número_factura": self.respuestas.get("¿Cuál es el número de factura?", "").strip(),
            "inicio_periodo": self.respuestas.get("¿Cuál es el inicio del periodo de facturación?", "").strip(),
            "fin_periodo": self.respuestas.get("¿Cuál es el fin del periodo de facturación?", "").strip(),
            "importe_factura": self.respuestas.get("¿Cuál es el importe de la factura?", "").strip(),
            "fecha_cargo": self.respuestas.get("¿Cuál es la fecha del cargo?", "").strip(),
            "consumo_periodo": self.respuestas.get("¿Cuál es el consumo en el periodo?", "").strip(),
            "potencia_contratada": self.respuestas.get("¿Cuál es la potencia contratada?", "").strip()
        }

    def guardar_en_archivo(self, archivo_destino):
        """Saves the output format in a JSON file."""
        formato_salida = self.obtener_formato_salida()
        with open(archivo_destino, "w", encoding="utf-8") as f:
            json.dump(formato_salida, f, ensure_ascii=False, indent=4)
        logging.info(f"Output format saved in '{archivo_destino}'.")
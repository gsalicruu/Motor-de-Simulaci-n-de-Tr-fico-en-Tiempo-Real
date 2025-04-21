
import asyncio
from comunicacion.mensajeria import recibir_vehiculos

vehiculos_en_simulacion = []

async def recibir_callback(vehiculo_dict):
    print(f"[Zona Sur] Recibido vehículo: {vehiculo_dict['id']}")
    vehiculos_en_simulacion.append(vehiculo_dict)

async def main():
    print("[Zona Sur] Escuchando vehículos entrantes...")
    await recibir_vehiculos("zona_sur", recibir_callback)

if __name__ == "__main__":
    asyncio.run(main())

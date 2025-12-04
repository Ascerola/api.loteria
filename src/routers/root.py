from fastapi import APIRouter, status
from fastapi.responses import JSONResponse
from sqlalchemy import text

from db.conn import get_session

router = APIRouter()


@router.get("/")
async def root():
    try:
        with get_session() as session:
            session.execute(text("SELECT 1"))
        return {"message": "DB connection successful"}
    except Exception as exc:  # noqa: BLE001
        return JSONResponse(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            content={"message": "DB connection failed", "detail": str(exc)},
        )


@router.get("/dashboard/mock")
async def dashboard_mock():
    return {
        "fecha": "2025-06-20",
        "usuario": "Administrador",
        "kpis": {
            "ingresos_hoy": 1_245_000,
            "pagos_hoy": 890_000,
            "ganancia_neta": 355_000,
            "puntos_activos": {"activos": 3, "total": 3},
        },
        "sorteos_del_dia": [
            {
                "id": "la-primera-10am",
                "nombre": "La Primera",
                "hora": "10:00",
                "estado": "COMPLETADO",
                "reportes": {"recibidos": 3, "esperados": 3},
                "ganador": 47,
                "vendido": 180_000,
                "ganancia": 55_000,
                "acciones": ["ver_detalle", "reporte"],
            },
            {
                "id": "nica-hondurena-11am",
                "nombre": "La Nica/Hondureña",
                "hora": "11:00",
                "estado": "EN_PROCESO",
                "reportes": {"recibidos": 2, "esperados": 3},
                "ganador": 23,
                "vendido": 95_000,
                "ganancia": 0,
                "acciones": ["procesar", "ver_detalle"],
            },
            {
                "id": "la-tica-1pm",
                "nombre": "La Tica",
                "hora": "13:00",
                "estado": "PENDIENTE",
                "reportes": {"recibidos": 0, "esperados": 3},
                "ganador": None,
                "vendido": 0,
                "ganancia": 0,
                "acciones": ["esperando_datos"],
            },
            {
                "id": "nica-hondurena-3pm",
                "nombre": "La Nica/Hondureña",
                "hora": "15:00",
                "estado": "NO_INICIADO",
                "reportes": {"recibidos": 0, "esperados": 3},
                "ganador": None,
                "vendido": 0,
                "ganancia": 0,
                "acciones": ["programado"],
            },
        ],
        "puntos_de_venta": [
            {
                "nombre": "Punto Centro",
                "neto": 45_000,
                "reportes": {"recibidos": 3, "esperados": 3},
            },
            {
                "nombre": "Punto Norte",
                "neto": 32_000,
                "reportes": {"recibidos": 2, "esperados": 3},
            },
            {
                "nombre": "Punto Sur",
                "neto": -12_000,
                "reportes": {"recibidos": 2, "esperados": 3},
            },
        ],
        "numeros_mas_vendidos": [
            {"numero": 25, "tickets": 41},
            {"numero": 47, "tickets": 38},
            {"numero": 73, "tickets": 34},
            {"numero": 12, "tickets": 29},
            {"numero": 89, "tickets": 27},
        ],
        "ultima_actualizacion": "2025-06-20T10:15:00-06:00",
    }

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field
from dotenv import load_dotenv
import os
import mercadopago

# === Carrega variáveis do .env ===
load_dotenv()
mp_access_token = os.getenv("MP_ACCESS_TOKEN")

if not mp_access_token:
    raise Exception("MP_ACCESS_TOKEN não está definido no .env")

# === SDK do Mercado Pago ===
sdk = mercadopago.SDK(mp_access_token)

# === Inicializa o app FastAPI ===
app = FastAPI(
    title="API de Doações com Pix - Mercado Pago",
    description="API que gera QR Code de pagamento via PIX usando Mercado Pago",
    version="1.0.0"
)

# === Configuração de CORS (liberado para qualquer origem durante desenvolvimento) ===
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Substituir por domínios confiáveis em produção
    allow_methods=["*"],
    allow_headers=["*"],
    allow_credentials=True
)

# === Modelo de dados para a doação ===
class DoacaoRequest(BaseModel):
    valor: float = Field(..., gt=0, description="Valor da doação em reais")
    email: str = Field(..., description="Email do doador")
    descricao: str = Field(default="Doação via site", description="Descrição da cobrança")

# === ROTA PARA CRIAR COBRANÇA PIX ===
@app.post("/doar")
def criar_pagamento(dados: DoacaoRequest):
    try:
        payment_data = {
            "transaction_amount": dados.valor,
            "description": dados.descricao,
            "payment_method_id": "pix",
            "payer": {
                "email": dados.email
            }
        }

        pagamento = sdk.payment().create(payment_data)
        print("Resposta Mercado Pago:", pagamento)  # <<< Log para debug

        if pagamento["status"] != 201:
            raise HTTPException(status_code=pagamento["status"], detail=pagamento.get("message", "Erro ao criar pagamento"))

        data = pagamento["response"]

        qr_code = data.get("point_of_interaction", {}).get("transaction_data", {}).get("qr_code")
        qr_image = data.get("point_of_interaction", {}).get("transaction_data", {}).get("qr_code_base64")

        if not qr_code or not qr_image:
            raise HTTPException(status_code=500, detail="QR Code não gerado pelo Mercado Pago.")

        return {
            "qr_code": qr_code,
            "qr_image_base64": qr_image,
            "payment_id": data.get("id"),
            "status": data.get("status")
        }

    except Exception as e:
        print("Erro na criação do pagamento:", e)  # <<< Log para debug
        raise HTTPException(status_code=500, detail=str(e))

from fastapi import APIRouter , Depends , HTTPException
from models import servicos
from sqlalchemy.orm import Session
from dependecias import pegar_sessao , verificar_token_clientes
from schemas import servicos_schemas
from uuid import UUID

order = APIRouter(prefix = "/servicos", tags=['servicos'])

@order.post("/Criar_servico")
async def criar_server(
    ServicosSchemas: servicos_schemas,
    session: Session = Depends(pegar_sessao),
    current_cliente = Depends(verificar_token_clientes)
):
    servico = servicos(
        clientes=ServicosSchemas.clientes,
        nome=ServicosSchemas.nome,
        descricao=ServicosSchemas.descricao,
        preco=ServicosSchemas.preco,
        duracao_min=ServicosSchemas.duracao_min,
        ativo=ServicosSchemas.ativo,
        novo_horario=ServicosSchemas.novo_horario
    )
    session.add(servico)
    session.commit()
    return {"mensagem": f"Serviço criado com sucesso {servico.id}"}


@order.delete("/servicos/deletar/{id_servico}")
async def deletar(id_servico: UUID , session: Session = Depends(pegar_sessao)):
    servico = session.query(servicos).filter(servicos.id == id_servico).first()
    if not servico:
        raise HTTPException(status_code = 400 , detail="Serviço Indisponivel")
    session.delete(servico)
    session.commit()

    return {"mensagem":"Pedido deletado com sucesso"}